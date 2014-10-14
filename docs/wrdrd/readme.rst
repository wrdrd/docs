
wrdrd
=======

A Python package with a collection of scripts for web consulting.

Installation
~~~~~~~~~~~~

At the command line::

    pip install -e git+https://github.com/wrdrd/docs#egg=wrdrd


Usage
~~~~~~~~

:py:mod:`wrdrd.tools` contains a number of command line utilities

.. contents::
   :local:

domaintool
~~~~~~~~~~~
::

    # Retrieve DNS and Whois information for a domain
    domaintool wrdrd.com

    # Print usage
    domaintool --help


crawl
~~~~~~
::

    # Install requirements
    pip install -r requirements.txt

    # Download NLTK libraries
    python -m nltk.downloader all

    # Crawl a website
    crawl -c http://www.wrdrd.com/

    # Print HTML to stdout
    crawl --html http://www.wrdrd.com/

    # Print text to stdout
    crawl --text http://www.wrdrd.com/

    # Print usage
    crawl --help


stripsinglehtml
~~~~~~~~~~~~~~~~
::

    # Strip Sphinx (single) HTML markup
    stripsinglehtml ./_build/singlehtml/index.html > __index.html

    # Print usage
    stripsinglehtml --help
