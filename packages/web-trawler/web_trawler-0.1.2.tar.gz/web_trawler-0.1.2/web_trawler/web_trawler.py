#!python3

"""
Trawl web pages for files to download
"""

import lxml.html
import urllib.request
import urllib.parse
import urllib.error
import contextlib
import collections
import argparse
import logging
import os.path
import multiprocessing
import multiprocessing.pool
import fnmatch


# This namedtuple has to be defined outside of functions to be picklable for multiprocessing
Link = collections.namedtuple("Link", "href title mb type")


def _parse_args():
    """
    Parses command line arguments and returns named tuple with argument values
    """
    parser = argparse.ArgumentParser(
        description=("batch downloads files linked to from webpages"),
        prog="web_trawler"
    )
    parser.add_argument("url")
    parser.add_argument("--target", "-t", default="download")
    parser.add_argument("--include_links_from_linked_pages", "-i", action="store_true")
    parser.add_argument("--quiet", "-q", action="store_true")
    parser.add_argument("--processes", "-p", type=int, default=None)
    parser.add_argument("--whitelist", "-w", type=str, default=None)
    parser.add_argument("--blacklist", "-b", type=str, default=None)
    parser.add_argument("--no_of_files_limit", "-n", type=int, default=None)
    parser.add_argument("--mb_per_file_limit", "-m", type=float, default=None)
    args = parser.parse_args()
    return args


def _compose_link_info_tuple(href_and_title):
    """
    For parallel processing of http requests for headers.

    Parameters
    ----------
    href_and_title : tuple

    Returns
    -------
    namedtuple with
        href : string
        title : string
            From a tag content
        mb : string
            File size in MB calculated from content-length from http header
        type : string
            Unaltered from "content-type" field from http header
    """

    def get_from_header(href):
        """
        HTTP requests header, which is used to fill out the link information

        Parameters
        ----------
        href : str

        Returns
        -------
        mb : str
            File size in MB calculated from content-length from http header
        content_type : str
            Unaltered from "content-type" field from http header
        """

        mb = content_type = "?"
        try:
            with contextlib.closing(urllib.request.urlopen(href)) as response:
                header = response.info()
        except urllib.error.HTTPError as e:
            logging.warning("HTTPError requesting header for %s: %s" % (href, e))
            return False
        else:
            try:
                mb = "{0:.3f}".format(int(header["content-length"]) / 1000000)
            except TypeError as e:
                logging.debug("HTTP header did not contain content-length: %s" % e)
            content_type = header["content-type"]

        return (mb, content_type)

    returned = get_from_header(href_and_title[0])
    if returned:
        mb = returned[0]
        content_type = returned[1]
    else:
        return None

    logging.info("Adding link: %s MB: %s" % (mb, href_and_title[0]))
    return Link(href=href_and_title[0], title=href_and_title[1], mb=mb, type=content_type)


def _get_max_no_of_processes(user_input):
    """
    If user hasn't specified a number of processors to use, use all except one (unless there is only one)
    """
    if user_input is None:
        all_but_one = multiprocessing.cpu_count() - 1
        no_of_processors = all_but_one if all_but_one > 0 else 1
    elif user_input >= 1:
        no_of_processors = user_input
    else:
        raise ValueError("There has to be at least one process")
    return no_of_processors


def _download_file(link_info_tuple):
    """
    For parallel downloading of files.
    """
    logging.info("Downloading %s (%s MB)" % (link_info_tuple[0], link_info_tuple[2]))
    urllib.request.urlretrieve(link_info_tuple[0], link_info_tuple[1])


def _delegate_downloads_to_threads(link_info_tuples):
    """
    Helper function to spawn up to 10 simultaneous threads for each process for downloads
    """
    with multiprocessing.pool.ThreadPool(10) as thread_pool:
        thread_pool.map(_download_file, link_info_tuples)


def get_links(url):
    """
    Find everything linked to from a web page.

    Parameters
    ----------
    url : str
        To be interpreted as a url (could be relative or absolute)

    Returns
    -------
    list
        of namedtuples with
            href : string
            title : string
                From a tag content
            mb : string
                File size in MB calculated from content-length from http header
            type : string
                Unaltered from "content-type" field from http header
    """

    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    try:
        with contextlib.closing(urllib.request.urlopen(url)) as response:
            doc = lxml.html.parse(response).getroot()
    except urllib.error.URLError:
        return []

    hrefs_and_titles = []
    for link in doc.cssselect("a"):
        href = urllib.parse.urljoin(url, link.get("href"))
        title = link.text_content() if link.text_content() != "" else "(no title)"
        if urllib.parse.urlparse(href).scheme in ["http", "https"]:
            hrefs_and_titles.append((href, title))

    with multiprocessing.pool.ThreadPool(10) as thread_pool:
        links = thread_pool.map(_compose_link_info_tuple, hrefs_and_titles)

    links = [link for link in links if link is not None]

    return links


def get_file_links(url, include_links_from_linked_pages=False, no_of_files_limit=None,
                   no_of_processes_specified_by_user=None, whitelist=None, blacklist=None):
    """
    Gets all links from a web page (and optionally the web pages linked to from it) and filters this list for
    links to files.

    Parameters
    ----------
    url : str
    include_links_from_linked_pages : bool
    no_of_files_limit : int
    whitelist : str or list
    blacklist : str or list

    Returns
    -------
    list
        A list of named tuples of the format described in the dosctring for get_links()
    """

    def check_count(count):
        """
        Checks if the list of files to be downloaded has gotten too long; raises exception if the case
        """

        if no_of_files_limit and count > int(no_of_files_limit):
            logging.critical("The user specified max limit on the number of files is set to %s, and there are at least"
                             "%s file links found. Aborting" % (no_of_files_limit, count))
            raise RuntimeError("There are more files to download than the limit specified!")

    def follow_link_check(link):
        """
        Checks if a given link is to a web page from the same domain as the url parameter from the outer function
        """
        same_domain = urllib.parse.urlparse(url).netloc == urllib.parse.urlparse(link.href).netloc
        return link.type.startswith("text/html") and same_domain

    def file_link_check(link, whitelist, blacklist):
        """
        Checks if a given link is to a file, and if so if the file ending is whitelisted or blacklisted
        """

        if link.type.startswith("application") or link.type.startswith("text/plain") \
               or link.type.startswith("image") or link.type.startswith("audio") \
               or link.type.startswith("video"):

            if blacklist:
                if type(blacklist) is str:
                    blacklist = blacklist.split()
                for item in blacklist:
                    if fnmatch.fnmatch(link.href, "*." + item):
                        return False

            if whitelist:
                if type(whitelist) is str:
                    whitelist = whitelist.split()
                match = False
                for item in whitelist:
                    if fnmatch.fnmatch(link.href, "*." + item):
                        match = True
                return match

            return True

        else:
            return False

    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    links = get_links(url)

    file_links = [link for link in links if file_link_check(link, whitelist, blacklist)]

    count = len(file_links)
    check_count(count)

    if include_links_from_linked_pages:
        html_links = [link for link in links if follow_link_check(link)]
        no_of_processes = _get_max_no_of_processes(no_of_processes_specified_by_user)
        logging.info("%s of %s processors will be used for further http requests (if as many are available)" % (
            no_of_processes, multiprocessing.cpu_count()))
        with multiprocessing.Pool(no_of_processes) as process_pool:
            nested_links = process_pool.map(get_links, [link.href for link in html_links])

        links_from_link = []
        for sublist in nested_links:
            for link in sublist:
                links_from_link.append(link)

        file_links_from_link = [link for link in links_from_link if file_link_check(link, whitelist, blacklist)]
        count = count + len(file_links_from_link)
        check_count(count)
        file_links.extend(file_links_from_link)

    return list(set(file_links))


def download(source, target="download", mb_per_file_limit=None, no_of_processes_specified_by_user=None):
    """
    Downloads files to local directory given url or list of urls.

    Parameters
    ----------
    source : str or namedtuple or list of str or namedtuple
        The namedtuples, if used, must have href and mb fields, with url in href
    target : str
        Path for which directory to download to
    mb_per_file_limit : float or None
        File size limit in MB (0 means no limit)
    no_of_processes_specified_by_user : int or None
        Used as a limit for number of simultaneously spawned processes
    """

    if type(source) is not list:
        source = [source]
    if source:
        if not target == "":
            os.makedirs(target, exist_ok=True)
            target = target.rstrip("/") + "/"

        if len(source) > 10:
            no_of_processes = _get_max_no_of_processes(no_of_processes_specified_by_user)
            logging.info("%s of %s processors will be used for downloading (if as many are available)" % (
                no_of_processes, multiprocessing.cpu_count()))
        else:
            no_of_processes = 1

        link_info_tuples = []
        for link in source:

            try:
                href = link.href
                mb = link.mb
            except AttributeError:
                if type(link) is str:
                    href = link
                    mb = "?"
                else:
                    raise ValueError("Invalid input: Use urls or namedtuples in the following format:"
                                     " 'href title mb type'")

            if not (href.startswith("http://") or href.startswith("https://")):
                href = "http://" + href

            if mb != "?" and mb_per_file_limit is not None and float(mb) > float(mb_per_file_limit):
                logging.warning("Skipping because file size %s MB > %s MB limit: %s" % (mb, mb_per_file_limit, href))
            else:
                target_path = target + href[href.rfind("/")+1:]
                link_info_tuples.append((href, target_path, mb))

        if len(link_info_tuples) > 10:
            link_info_tuples_portions = []
            portion_size = len(link_info_tuples) // no_of_processes + 1
            for i in range(0, len(link_info_tuples), portion_size):
                link_info_tuples_portions.append(link_info_tuples[i:i + portion_size])

            with multiprocessing.Pool(no_of_processes) as process_pool:
                process_pool.map(_delegate_downloads_to_threads, link_info_tuples_portions)

        else:
            _delegate_downloads_to_threads(link_info_tuples)


def trawl(url, include_links_from_linked_pages=False, no_of_files_limit=None, no_of_processes_specified_by_user=None,
          whitelist=None, blacklist=None, target="download", mb_per_file_limit=None, quiet=False):
    """
    Gets list of file links from get_file_links and passes it to download.

    Parameters
    ----------
    url : str
    include_links_from_linked_pages : bool
    no_of_files_limit : int or None
    no_of_processes_specified_by_user : int or None
    whitelist : str or list
    blacklist : str or list
    target : str
    mb_per_file_limit : float or None
    quiet : bool
    """

    logging.basicConfig(level=logging.CRITICAL if quiet else logging.INFO,
                        format="%(levelname)s (%(asctime)s): %(message)s", datefmt="%H:%M:%S")
    file_links = get_file_links(url, include_links_from_linked_pages=include_links_from_linked_pages,
                                no_of_files_limit=no_of_files_limit,
                                no_of_processes_specified_by_user=no_of_processes_specified_by_user,
                                whitelist=whitelist, blacklist=blacklist)
    logging.info("%s files to download in total" % (len(file_links)))
    download(file_links, target=target, mb_per_file_limit=mb_per_file_limit,
             no_of_processes_specified_by_user=no_of_processes_specified_by_user)


def main():
    """
    Entry point for command line users
    """

    args = _parse_args()

    trawl(args.url, include_links_from_linked_pages=args.include_links_from_linked_pages,
          no_of_files_limit=args.no_of_files_limit,
          no_of_processes_specified_by_user=args.processes, whitelist=args.whitelist, blacklist=args.blacklist,
          target=args.target, mb_per_file_limit=args.mb_per_file_limit, quiet=args.quiet)


if __name__ == "__main__":
    main()
