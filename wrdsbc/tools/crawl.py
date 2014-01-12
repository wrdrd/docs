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

import datetime
import itertools
import logging
import sys
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
from pprint import pformat

import bs4
import nltk
import requests
import textblob
import urlobject


def get_unicode_stdout(stdout=None, errors='replace', **kwargs):
    import codecs
    stdout = stdout or sys.stdout
    return codecs.getwriter('utf-8')(stdout, errors=errors, **kwargs)
sys.stdout = get_unicode_stdout(sys.stdout)

log = logging.getLogger()
urllib3log = logging.getLogger('requests.packages.urllib3.connectionpool')
urllib3log.setLevel(logging.ERROR)


Link = namedtuple('Link', ('loc', 'href', 'name', 'target', 'text'))

def extract_links(url, bs):
    links = bs.findAll('a')
    for l in links:
        yield Link(
            url,
            l.get('href'),
            l.get('name'),
            l.get('target'),
            l.text)


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
get_stop_words()


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
    return unicode(url.without_fragment())


def filter_link(url, domain):
    if url.startswith(domain):
        return True
    return False


def crawl_url(start_url):
    queue = URLCrawlQueue()

    queue.push(
        CrawlRequest(start_url, start_url, current_datetime()))

    crawled = ResultStore()
    links = list()
    images = list()
    csses = list()
    jses = list()
    keywords = list()

    while queue.count():  # TODO
        crawl_req = queue.pop()
        log.info("Fetching URL: %s" % str(crawl_req))
        crawl_status = {
            'crawl_req': crawl_req,
            'status': 'pending',
        }

        try:
            resp = requests.get(crawl_req.url)
        except Exception as e:
            log.info("Crawl ERROR: %r (%r)" % (crawl_req, str(e)))
            queue.error(crawl_req)
            crawl_status.update(
                {'status': 'ERROR',
                 'error': str(e)})
            crawled[crawl_req.url] = crawl_status
            continue

        crawl_status.update({
            'status': 'fetched',
            'status_code': resp.status_code,
            'status_reason': resp.reason
        })

        if resp.status_code != 200:
            crawled[crawl_req.url] = crawl_status
            continue

        bs = bs4.BeautifulSoup(resp.content)

        url = crawl_req.url
        _links = extract_links(url, bs)
        _links = list(_links)

        crawled[crawl_req.url] = crawl_status

        for link in _links:
            _link = strip_fragment(expand_link(url, link.href))
            if filter_link(_link, start_url):
                queue.push(CrawlRequest(url, _link, current_datetime()))
            #else:
            #    log.debug("Skipping %r" % _link)

        _images = extract_images(url, bs)
        _css = extract_css(url, bs)
        _js = extract_js(url, bs)
        _keywords = extract_keywords(url, bs)

        links.extend(_links)
        images.extend(_images)
        csses.extend(_css)
        jses.extend(_js)
        keywords.append(_keywords)

        queue.done(crawl_req)

    return crawled, links, images, csses, jses, keywords


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


def print_frequency_table(frequencies):
    hdrfmt = "    %5s %6s  %s"
    rowfmt = "    {:.2%} {:-6}  {}"
    print(hdrfmt % ("pct", "count", "word"))
    print("   %s" % ('-'*42))
    for row in frequencies:
        #print(row)
        if len(row) != 3:
            raise Exception(row)
        print(rowfmt.format(*row))


def to_a_search_engine(url):
    content = requests.get(url).content
    bs = bs4.BeautifulSoup(content)
    bs = strip_script_styles_from_bs(bs)
    lines = (x.strip() for x in bs.strings if x.strip())
    return (x.strip() for x in
            itertools.chain(*(x.split('\n') for x in lines)))


def wrdcrawler(url):
    crawled, links, images, csses, jses, keywords = crawl_url(url)
    word_frequencies = sum_counters(k.frequencies for k in keywords)

    print("Crawled pages")
    print("=============")
    for crawled_url in crawled:
        print(u" * %s" % crawled_url)
    print("\n")


    print("To a search engine")
    print("==================")
    print("::\n")
    for line in to_a_search_engine(url):
        print(u"    %s" % line)

    print("\n")
    print("Word Frequencies by count")
    print("=========================")
    print("::\n")
    print_frequency_table(frequency_table(word_frequencies, sort_by='count'))

    print('\n')
    print("Word Frequencies by name")
    print("========================")
    print("::\n")
    print_frequency_table(frequency_table(word_frequencies, sort_by='name'))



import unittest
class Test_wrdcrawler(unittest.TestCase):
    def test_wrdcrawler(self):
        START_URL="http://localhost:10000/"
        crawled, links, images, csses, jses, keywords = wrdcrawler(START_URL)
        self.assertTrue(links)
        print(pformat(sorted(links)))
        print(pformat(sorted(images)))
        print(pformat(sorted(csses)))
        print(pformat(sorted(jses)))
        print(pformat(sorted(keywords)))

        keyword_counts = sorted(
            sum_counters(k.frequencies for k in keywords).iteritems(),
            key=lambda x: x[1],
            reverse=True)

        print(pformat(keyword_counts))


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

    prs.add_option('-s', '--text',
                    dest='text',
                    action='store_true',
                    help=('Parse the text out of the specified URL'))

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
        raise Exception("Must specify a URL")
    url = args[0]

    if opts.crawl:
        wrdcrawler(url)

    if opts.text:
        for line in to_a_search_engine(url):
            print(line)

if __name__ == "__main__":
    sys.exit(main())
