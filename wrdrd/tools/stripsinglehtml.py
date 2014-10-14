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

# GOOGLE_SITES_TABLE_OF_CONTENTS = ("""<div><img src="https://www.google.com/chart?chc=sites&amp;cht=d&amp;chdp=sites&amp;chl=%5B%5BTable+of+contents'%3D20'f%5Cv'a%5C%3D0'10'%3D249'0'dim'%5Cbox1'b%5CF6F6F6'fC%5CF6F6F6'eC%5C0'sk'%5C%5B'%5D'a%5CV%5C%3D12'f%5C%5DV%5Cta%5C%3D10'%3D0'%3D250'%3D297'dim'%5C%3D10'%3D10'%3D250'%3D297'vdim'%5Cbox1'b%5Cva%5CF6F6F6'fC%5CC8C8C8'eC%5C'a%5C%5Do%5CLauto'f%5C&amp;sig=TzxATGSyGo59uvdEcnpk0pMmCmI" data-type="toc" data-props="align:left;maxDepth:6;width:250;" width="250" height="300" style="display:block;text-align:left;margin-right:auto;"></div>""")

# def format_for_google_sites(bs, strip_h1=True):
    # bs = bs.find('div', {'class': 'body'})
    # h1 = bs.find('h1')
    # h1.insert_after(bs4.BeautifulSoup().new_tag("div", thespot="???"))
    # if strip_h1:
        # h1.extract()
        # TODO: replace with comment
    # p = bs.find('p')
    # if p.text == u'Contents:':
        # p.extract()
    # else:
        # raise Exception("???")  # TODO
    # return unicode(bs).replace(
        # '''<div thespot="???"></div>''',
        # GOOGLE_SITES_TABLE_OF_CONTENTS)


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

    # prs.add_option('-g', '--google-sites',
                   # dest='google_sites',
                   # action='store_true')

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

    # if opts.google_sites:
        #bs = format_for_google_sites(bs)

    print(unicode(bs))

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
