Web Trawler
===========

Given the url of an html web page, this Python package asynchronously downloads all non-web 
files linked to from that web page, e.g. audio files, Excel documents, etc. Optionally, all 
web pages linked to from the original web page can be trawled for files as well.

Installation
------------

`Python 3`_ must be installed and in your system PATH. That is, it must be a recognised command
for the command line interface. Enter :code:`python --version` in your command line to see whether
you have Python 3 installed. 

The Python package manager :code:`pip` is also required. Check that you have it by running :code:`pip --version`. 
It is automatically installed with recent versions of Python, but it can also be installed manually. 
See `the official installation instructions`_

.. _`Python 3`: https://www.python.org/downloads/
.. _`the official installation instructions`: https://pip.pypa.io/en/stable/installing/

Installing the web_trawler package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the following code in your command line interface (excluding the $, which is just a prompt icon): 

.. code-block:: bash

    $ pip install web_trawler

The package has no external dependencies. For testing, pytest_ is required.

.. _pytest: https://docs.pytest.org/en/latest/contents.html

The source code for web_trawler is available on gitlab.com_.

.. _gitlab.com: https://gitlab.com/dlab-indecol/web_trawler

Usage
-----

Command line
^^^^^^^^^^^^

Once installed, web_trawler can be used like this:

.. code-block:: bash

    $ web_trawler google.com

Run this command to see how web_trawler finds links
and inspects their http headers for more information. A bunch of logging events will be output to console. 
There are ordinarily no files linked to from google.com,
but if there are, they will be downloaded to the directory :code:`download/` relative to where you ran the command.

The url argument is required. In addition, the following optional arguments are supported:

    --target TARGET                     Give a path for where you would like the files to be downloaded. The default
                                        path is "download".
    --include_links_from_linked_pages   Set web_trawler to find download links from all web pages
                                        linked to from the original web page as well (only goes one step,
                                        and only for links within the domain of the original web page)
    --quiet                             Suppresses output information about which links are being processed
                                        and which files are being downloaded.
    --processes PROCESSES               Manually set how many processes will be spawned. The default is to spawn
                                        one less than the number of processors detected (so as not to stall the
                                        system). For each process, up to 10 threads are spawned.
    --whitelist WHITELIST               Space-separated file endings to whitelist. Allows use of wildcards, e.g.
                                        "xls*" to capture all the Excel file extension variants, like xlsx, xlsb,
                                        xlsm and xls. A given blacklist takes precedence over the whitelist.
    --blacklist BLACKLIST               Space-separated file endings to blacklist. Works just whitelist, only it
                                        excludes files of the given file endings.
    --no_of_files_limit LIMIT           Set a maximum number of files you are willing to download, in case
                                        web_trawler finds more than expected.
    --mb_per_file_limit LIMIT           Set a maximum file size you are willing to download. Warnings are logged to
                                        console for each file excluded.

Each argument has a shorthand consisting of their first letters, e.g. :code:`-t`, :code:`-i`, :code:`-q`, etc.

A realistic example of use
""""""""""""""""""""""""""

If we'd like to download, say, all zip and Excel files up to 100 MB from
`a web page on the World Input-Output Database site`_, into a local directory called "data",
we'd need to use the arguments :code:`-t` (for target), :code:`-w` (for whitelist) and :code:`-m` 
(for mb_per_file_limit):

.. _a web page on the World Input-Output Database site: http://www.wiod.org/database/wiots16

.. code-block:: bash

    $ web_trawler http://www.wiod.org/database/wiots16 -t "data" -w "zip xls*" -m 100

Notice the use of a wildcard in the whitelist. The web page specified links to two different Excel associated
file endings. The wildcard ensures that both are captured.

If you test this command, downloads of a bunch of large files will start. Press :code:`ctrl-c` or :code:`ctrl-z` to
interrupt or force quit the process, respectively.

Make sure to clean up any downloaded files you don't want. They should be in a folder relative to where you ran the
command. If you didn't specify a target, they are downloaded to a directory called "download".

Including links from linked pages
"""""""""""""""""""""""""""""""""

To see how the :code:`-i` argument works without starting a million downloads, run the following command, where
:code:`-m 0` ensures that all files are skipped:

.. code-block:: bash

    $ web_trawler http://www.wiod.org/database/wiots16 -i -m 0

Note that this will still create the target directory if it doesn't exist already.

Use within Python
^^^^^^^^^^^^^^^^^

The following code does the exact same thing as the last example for the command line usage:

.. code-block::

    import web_trawler

    web_trawler.trawl("http://www.wiod.org/database/wiots16", 
                      include_links_from_linked_pages=True, mb_per_file_limit=0)

The function :code:`trawl` does the same thing as web_trawler as run from the command line, but with the arguments
passed to it directly in Python.

Several of the intermediary functions used in web_trawler can also be accessed through Python, i.e. to get a
list with information about all links on a webpage, or just the links to files, filtered with a blacklist
or whitelist. Here's a brief description of each of them:

    :get_links:         Takes only one argument, a url, and returns a list of Link namedtuples, described below.
                        This list is unfiltered. All http links that return a http request are included.
    :get_file_links:    Runs get_links and returns a filtered list of Link namedtuples for files only,
                        with whitelist and/or blacklist applied if specified. Arguments have self-explanatory names.
                        The whitelist and blacklist can be provided as a space-separated string or as a list.

Both :code:`get_links` and :code:`get_file_links` return lists of namedtuples with the following fields:

    :href:    the link url
    :title:   the content of the :code:`<a>` tag containing the link
    :mb:      calculated from the http header :code:`content-length`
    :type:    the http header :code:`content-type`, unmodified

Use in Matlab
^^^^^^^^^^^^^

In Matlab, functions of pip installed Python packages can be called using the :code:`py` script, where optional
arguments are specified using the pyargs function:

.. code-block:: matlab

    >> py.web_trawler.get_file_links('http://www.wiod.org/database/wiots16', pyargs('whitelist', 'xls*'))

Stdout isn't displayed, that's why the :code:`get_file_links` function was chosen, as it returns something.
To use the full functionality of web_trawler, you could run the function :code:`trawl` instead. As long as
there are no errors, nothing will show up in the Command Window. Files will nevertheless be downloaded,
relative to your Current Folder in Matlab.
