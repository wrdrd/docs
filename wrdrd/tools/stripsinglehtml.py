#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
wrdrd.tools.stripsinglehtml
"""
import codecs
import bs4


def stripsinglehtml(path='index.html'):
    """
    strip markup from sphinx singlehtml files
    (rather than writing a sphinx [...]-er)

    Args:
        path (str): path to a Sphinx singlehtml file
    Returns:
        bs4.BeautifulSoup: stripped HTML file
    """
    contents = None
    with codecs.open(path, 'r', encoding='utf8') as f:
        contents = f.read()

    bs = bs4.BeautifulSoup(contents)
    bs.find('body')
    bs = bs.find('body')
    [x.extract() for x in bs.find_all('a', {'class': 'headerlink'})]
    elem = bs.find('div', {'class': 'sphinxsidebar'})
    elem and elem.extract()
    elem = bs.find('div', {'id': 'indices-and-tables'})
    elem and elem.extract()
    [x.extract() for x in bs.find_all('div', {'class': 'related'})]

    return bs


import unittest


class Test_stripsinglehtml(unittest.TestCase):

    def test_stripsinglehtml(self):
        filename = './test/data/singlehtml.html'
        output = stripsinglehtml(filename)
        self.assertTrue(output)


def main(*args):
    """
    :py:mod:`wrdrd.tools.stripsinglehtml` main method: print unicode
    stripsinglehtml output to ``stdout``.

    Args:
        args (list): list of commandline arguments
    Returns:
        int: zero
    """
    import logging
    import optparse
    import sys

    prs = optparse.OptionParser(
        usage="%prog <path>",
        description="Strip markup from a Sphinx singlehtml HTML page")

    prs.add_option('-v', '--verbose',
                   dest='verbose',
                   action='store_true',)
    prs.add_option('-q', '--quiet',
                   dest='quiet',
                   action='store_true',)
    prs.add_option('-t', '--test',
                   dest='run_tests',
                   action='store_true',)

    args = args and list(args) or sys.argv[1:]
    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        sys.argv = [sys.argv[0]] + args
        import unittest
        sys.exit(unittest.main())

    if len(args) != 1:
        raise Exception("Must specify a file path")
    path = args[0]

    sys.stdout = codecs.getwriter('utf-8')(sys.stdout, errors='replace')
    bs = stripsinglehtml(path)
    print(unicode(bs))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
