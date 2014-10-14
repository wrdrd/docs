#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
wrdcrawler
============
Given a starting page link,
crawl pages (up to a specified depth).

pip install requests beautifulsoup4

"""

import StringIO
import datetime
import functools
import itertools
import logging
import sys
import urlparse
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

import bs4
import requests
import urlobject

import networkx

try:
    import nltk
    import textblob
except ImportError as e:
    nltk = None
    textblob = None

def get_unicode_stdout(stdout=None, errors='replace', **kwargs):
    import codecs
    stdout = stdout or sys.stdout
    return codecs.getwriter('utf-8')(stdout, errors=errors, **kwargs)
sys._stdout = sys.stdout
sys.stdout = get_unicode_stdout(sys.stdout)

log = logging.getLogger()
urllib3log = logging.getLogger('requests.packages.urllib3.connectionpool')
urllib3log.setLevel(logging.ERROR)


Link = namedtuple('Link', ('loc', 'href', 'name', 'target', 'text', 'parent_id'))

def extract_links(url, bs):
    links = bs.findAll('a')
    for l in links:
        elem = l.find_parent(attrs={'id': lambda x: bool(x)})
        nearest_parent = elem.get('id') if elem else None
        yield Link(
            url,
            l.get('href'),
            l.get('name'),
            l.get('target'),
            l.text.strip(),
            nearest_parent)


Image = namedtuple('Image', ('loc', 'src', 'alt', 'height', 'width', 'text'))

def extract_images(url, bs):
    images = bs.findAll('img')
    for i in images:
        yield Image(
            url,
            i.get('src'),
            i.get('alt'),
            i.get('height'),
            i.get('width'),
            i.get('text'))


CSS = namedtuple('CSS', ('loc', 'src'))

def extract_css(url, bs):
    csses = bs.findAll('link', {'rel':'stylesheet'})
    for c in csses:
        yield CSS(
            url,
            c.get('href'))


JS = namedtuple('JS', ('loc', 'src'))

def extract_js(url, bs):
    jses = bs.findAll('script')
    for j in jses:
        type_ = j.get('type')
        if type_ not in (None, 'text/javascript'):
            log.info("Strange script type: %r" % type_)
            continue
        yield JS(
            url,
            j.get('src'))


def tokenize(text):
    return textblob.tokenizers.word_tokenize(text)


STOP_WORDS = None
def get_stop_words():
    global STOP_WORDS
    if STOP_WORDS is None:
        STOP_WORDS = dict.fromkeys(nltk.corpus.stopwords.words('english'), 1)
        STOP_WORDS.update({'pm':1, 'am':1})
        STOP_WORDS.pop('about')
#get_stop_words()


def get_text_from_bs(bs):
    return u' '.join(x.replace('\n',' ') for x in bs.strings)


def strip_script_styles_from_bs(bs):
    #bs = bs.copy()
    for tag in ('script', 'style'):
        for elem in bs.find_all(tag):
            elem.extract()
    return bs


def extract_words_from_bs(bs):
    body = bs.find('body')
    if not body:
        raise Exception(body)
    body = strip_script_styles_from_bs(body)
    return get_text_from_bs(body)


KeywordFrequency = namedtuple('KeywordFrequency', ('url', 'frequencies'))

def word_frequencies(url, keywords):
    words = (x.lower() for x in keywords)
    return KeywordFrequency(
        url,
        Counter(w for w in words if len(w) > 1 and w not in STOP_WORDS))


def extract_keywords(url, bs):
    return word_frequencies(url, tokenize(extract_words_from_bs(bs)))


def current_datetime():
    return datetime.datetime.now().isoformat()


CrawlRequest = namedtuple('CrawlRequest', ('src', 'url', 'datetime'))

class URLCrawlQueue(object):
    NEW = 0
    OUT = 1
    DONE = 2
    ERROR = 3
    def __init__(self):
        self.already = OrderedDict()
        self.q = []

    def __iter__(self):
        return self.q.__iter__()

    def pop(self):
        item = self.q.pop(0)
        self.already[item.url] = URLCrawlQueue.OUT
        return item

    def push(self, item):
        if item.url not in self.already:  # one shot
            self.already[item.url] = URLCrawlQueue.NEW
            self.q.append(item)
        #else:
        #    log.debug("Skipping already enqueued: %s" % str(item))

    def done(self, item):
        self.already[item.url] = URLCrawlQueue.DONE

    def error(self, item):
        self.already[item.url] = URLCrawlQueue.ERROR

    def count(self):
        return len(self.q)


class ResultStore(object):
    def __init__(self):
        self.db = OrderedDict()

    def __contains__(self, k):
        return k in self.db

    def __iter__(self):
        return self.db.__iter__()

    def __setitem__(self, k, v):
        return self.db.__setitem__(k, v)

    def itervalues(self):
        return self.db.itervalues()


def expand_link(_src, _url):
    src = urlobject.URLObject(_src)
    url = urlobject.URLObject(_url)

    if url.scheme.startswith('http'):
        return _url

    return unicode(
        src
        .with_path(url.path)
        .with_query(url.query)
        .with_fragment(url.fragment))


def strip_fragment(url):
    url = urlobject.URLObject(url)
    _url = url.without_fragment()
    if not(unicode(_url)):
        return u'/'
    else:
        return unicode(_url)


def same_netloc(_url, _domain):
    url = urlparse.urlsplit(_url)
    dom = urlparse.urlsplit(_domain)
    return url.netloc == dom.netloc


def crawl_url(start_url, output=sys.stdout):
    queue = URLCrawlQueue()

    queue.push(
        CrawlRequest(start_url, start_url, current_datetime()))

    crawled = ResultStore()

    while queue.count():  # TODO
        crawl_req = queue.pop()
        url = crawl_req.url
        log.info("Fetching URL: %s" % str(crawl_req))
        crawl_status = {
            'crawl_req': crawl_req,
        }

        try:
            resp = requests.get(url)
        except Exception as e:
            log.info("Crawl ERROR: %r (%r)" % (crawl_req, str(e)))
            queue.error(crawl_req)
            crawl_status.update(
                {'status': 'ERROR',
                 'error': str(e)})
            crawled[url] = crawl_status
            continue

        crawl_status.update({
            'status_date': current_datetime(),
            'status_code': resp.status_code,
            'status_reason': resp.reason
        })

        if resp.status_code != 200:
            crawled[url] = crawl_status
            continue

        bs = bs4.BeautifulSoup(resp.content)

        _links = extract_links(url, bs)
        _links = list(_links)

        for link in _links:
            _link = strip_fragment(expand_link(url, link.href))
            if same_netloc(_link, start_url):
                queue.push(CrawlRequest(url, _link, current_datetime()))
            #else:
            #    log.debug("Skipping %r" % _link)

        _images = extract_images(url, bs)
        _css = extract_css(url, bs)
        _js = extract_js(url, bs)
        _keywords = extract_keywords(url, bs)

        crawl_status.update({
            'links': _links,
            'images': _images,
            'css': _css,
            'js': _js,
            'keywords': _keywords})

        crawled[url] = crawl_status
        queue.done(crawl_req)

    return crawled


def sum_counters(iterable):
    totals = defaultdict(lambda: 0)
    for counts in iterable:
        for key,value in counts.iteritems():
            totals[key] += value
    return totals


def frequency_table(counterdict, sort_by='count'):
    total = float(sum(counterdict.itervalues()))
    keyfunc = lambda x: x
    reverse = None

    if sort_by == 'count':
        keyfunc = lambda x: (x[1], x[0])
        reverse = True
    elif sort_by == 'name':
        keyfunc = lambda x: (x[0], x[1])
        reverse = False

    keyword_counts = sorted(
        counterdict.iteritems(),
        key=keyfunc,
        reverse=reverse)

    for word, count in keyword_counts:
        pct = count / total
        _tuple = (pct, count, word)
        yield _tuple


def print_frequency_table(frequencies, output=sys.stdout):
    write = functools.partial(print, file=output)
    hdrfmt = "    %5s %6s  %s"
    rowfmt = u"    {:.2%} {:-6}  {}"
    write(hdrfmt % ("pct", "count", "word"))
    write("   %s" % ('-'*42))
    for row in frequencies:
        if len(row) != 3:
            raise Exception(row)
        write(rowfmt.format(*row))


def to_a_search_engine(url):
    content = requests.get(url).content
    bs = bs4.BeautifulSoup(content)
    bs = strip_script_styles_from_bs(bs)
    lines = (x.strip() for x in bs.strings if x.strip())
    return (x.strip() for x in
            itertools.chain(*(x.split('\n') for x in lines)))


def build_networkx_graph(url, links, label=None, output=sys.stdout):
    #write = functools.partial(print, file=output)
    import cgi
    def escape(var):
        return '"%s"' % cgi.escape(var, quote=True)

    label = label or url
    g = networkx.DiGraph(label=label, ratio='compress')
    for link in links:
        a = escape(link.loc)
        a_url = expand_link(url, link.loc)
        b = escape(link.href)
        b_url = expand_link(url, link.href)

        if same_netloc(a_url, b_url):
            _url = strip_fragment(link.href)
            b = escape(_url)
            b_url = expand_link(url, _url)

        g.add_node(a, URL=a_url)
        g.add_node(b, URL=b_url)

        g.add_edge(a, b, label=link.text)

    return g


def write_nxgraph_to_dot(g, output):
    return networkx.drawing.write_dot(g, output)


def write_nxgraph_to_json(g, output):
    import json
    from networkx.readwrite import json_graph
    jsond = json_graph.node_link_data(g)
    return json.dump(jsond, output)


def wrdcrawler(url, output=sys.stdout):
    write = functools.partial(print, file=output)

    crawled = crawl_url(url)

    keywords = (page.get('keywords') for page in crawled.itervalues())
    word_frequencies = sum_counters(k.frequencies for k in keywords if k)

    write("Crawled pages")
    write("=============")
    write("")
    for crawled_url in crawled:
        write(u" * %s" % crawled_url)
    write("\n")


    if 0:
        links = (page.get('links') for page in crawled.itervalues())
        links = (l for l in links if l)
        write("Page Graph")
        write("==========")
        g = build_networkx_graph(url, links, label=url, output=output)
        write_nxgraph_to_dot(g, output)
        write("\n")

    write("To a search engine")
    write("==================")
    write("::\n")
    for line in to_a_search_engine(url):
        write(u"    %s" % line)
    write("\n")

    write("Word Frequencies by count")
    write("=========================")
    write("::\n")
    print_frequency_table(
        frequency_table(word_frequencies, sort_by='count'),
        output=output)
    write('\n')

    write("Word Frequencies by name")
    write("========================")
    write("::\n")
    print_frequency_table(
        frequency_table(word_frequencies, sort_by='name'),
        output=output)
    write('\n')

    return output




import unittest
class Test_wrdcrawler(unittest.TestCase):
    def test_crawl_url(self):
        START_URL = "http://localhost:1000/"
        output = StringIO.StringIO()
        crawled = crawl_url(START_URL, output=output)
        self.assertTrue(crawled)

    def test_wrdcrawler(self):
        START_URL="http://localhost:10000/"
        output = StringIO.StringIO()
        output = wrdcrawler(START_URL, output=output)
        output.seek(0)
        print(output.read())
        self.assertTrue(output)

        #print(pformat(keyword_counts))

    def test_expand_link(self):
        test_data = (
            (("http://localhost/index.html", "About.html"),
             "http://localhost/About.html"),
            (("http://localhost:8080#Test", "About.html"),
             "http://localhost:8080/About.html"),
            (("http://localhost?query", "About.html#Test"),
             "http://localhost/About.html#Test"),
        )
        for input_, expected_output in test_data:
            output = expand_link(*input_)
            self.assertEqual(output, expected_output)

    def test_strip_fragment(self):
        test_data = (
            ("http://localhost/#test",
             "http://localhost/"),
            ("http://localhost:8080?query#Test",
             "http://localhost:8080?query"),
            ("http://localhost?query",
             "http://localhost?query"),
        )
        for input_, expected_output in test_data:
            output = strip_fragment(input_)
            self.assertEqual(output, expected_output)

    def test_same_netloc(self):
        test_data = (
            (("http://localhost/index.html", "http://localhost/"),
             True),
            (("http://localhost:8080#Test", "http://localhost/"),
             False),
            (("http://localhost:8080#Test", "http://localhost"),
             False),
        )
        for input_, expected_output in test_data:
            output = same_netloc(*input_)
            try:
                self.assertEqual(output, expected_output)
            except:
                print(input_)
                raise

    def test_sum_counters(self):
        c1 = {'a': 2, 'b': 1, 'c': 3}
        c2 = {'a': 1, 'b': 2,         'd': 3}
        csum = sum_counters([c1, c2])
        for k,v in csum.iteritems():
            self.assertEqual(v, 3, k)

    def test_tokenize(self):
        input_ = "d'yer mak'er is a great song, don't you think?"
        expected_output = [
            "d'yer", "mak'er", "is", "a", "great", "song", ",",
            "do",
            "n't", "you", "think", "?"]
        output = list(tokenize(input_))
        self.assertEqual(output, expected_output,
                         (input_, output, expected_output))

    def test_other(self): # TODO
        import requests, bs4, itertools
        url = 'http://localhost:8181'
        bs = bs4.BeautifulSoup(requests.get(url).content)
        links = list(extract_links(url, bs))
        for key, links in itertools.groupby(links, lambda x: x.parent_id):
            print("## %s" % key)
            print(list(links))

    def test_build_networkx_graph(self):
        url = 'http://localhost:8181/'
        output = sys.stdout
        bs = bs4.BeautifulSoup(requests.get(url).content)
        links = list(extract_links(url, bs))
        g = build_networkx_graph(url, links, output=output)
        self.assertTrue(g)

        output = StringIO.StringIO()
        write_nxgraph_to_dot(g, output)
        output.seek(0)
        print(output.read())
        output.seek(0)
        self.assertTrue(output.read())

        output = StringIO.StringIO()
        write_nxgraph_to_json(g, output)
        output.seek(0)
        print(output.read())
        output.seek(0)
        self.assertTrue(output.read())
        output.seek(0)
        with open('./force/force.json','w') as f:
            f.write(output.read())

        import matplotlib.pyplot as plt
        networkx.draw_circular(g)
        plt.savefig("awesome.svg")
        #plt.show()


def main(*args):
    import logging
    import optparse
    import sys

    prs = optparse.OptionParser(
        usage="%prog [-c|-t] <url>",
        description="Recursively crawl and parse a page or set of pages")

    prs.add_option('-c', '--crawl',
                    dest='crawl',
                    action='store_true',
                    help=('Crawl from the specified URL'
                         ' and write a few reports to stdout'))

    prs.add_option('-H', '--html',
                    dest='html',
                    action='store_true',
                    help=('Print the raw HTML of the specified URL'))

    prs.add_option('-s', '--text',
                    dest='text',
                    action='store_true',
                    help=('Parse the text out of the specified URL'))

    prs.add_option('-l', '--links', # TODO
                    dest='links',
                    action='store_true',
                    help=('Extract links from the specified URL'))

    prs.add_option('-d', '--dotgraph',
                    dest='dotgraph',
                    action='store_true',
                    help=('Draw DOT graph from links within the page at '
                          'the specified URL'))

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

    get_stop_words()

    if opts.run_tests:
        sys.argv = [sys.argv[0]] + args
        import unittest
        sys.exit(unittest.main())


    if not any((opts.crawl, opts.html, opts.text, opts.links, opts.dotgraph)):
        prs.print_help()
        sys.exit(1)

    if len(args) != 1:
        prs.print_help()
        raise Exception("Must specify a URL")
    url = args[0]

    if opts.crawl:
        print(wrdcrawler(url))
        sys.exit(0)


    resp = requests.get(url)
    bs = bs4.BeautifulSoup(resp.content)
    if opts.html:
        sys._stdout.write(resp.content)

    if opts.text:
        for line in to_a_search_engine(url):
            print(line)

    if opts.links:
        for link in extract_links(url, bs):
            print(link)

    if opts.dotgraph:
        # TODO
        #build_dot_graph(url, [extract_links(url, bs), ], label=url)
        pass


if __name__ == "__main__":
    sys.exit(main())
