#!/usr/bin/env python

import itertools
import socket
import subprocess
import sys
from collections import Counter
from pathlib import Path

import bs4
import requests
import pytest
from xprocess import ProcessStarter

from wrdrd.tools.crawl import (
    crawl_url,
    wrdcrawler,
    expand_link,
    same_netloc,
    strip_fragment,
    extract_links,
    build_networkx_graph,
    write_nxgraph_to_dot,
    write_nxgraph_to_json,
    sum_counters,
    tokenize,
    iteritems,
    StringIO,
    word_frequencies,
)


# @pytest.fixture(scope="session")
# def find_free_port():
#     with socket.socket() as s:
#         s.bind(("localhost", 0))
#         port = s.getsockname()[1]
#     return port


@pytest.fixture(scope="session")
def myserver(xprocess):
    dirname = Path(__file__).parent.parent / "docs" / "_build" / "html"
    port = 40025  # find_free_port

    class Starter(ProcessStarter):
        pattern = "^Serving HTTP on"
        args = [
            sys.executable,
            "-m",
            "http.server",
            "--directory",
            dirname,
            "-b",
            "localhost",
            port,
        ]

    url = f"http://localhost:{port}/"
    print(("setup", dirname, port, url))
    logfile = xprocess.ensure("myserver", Starter)
    yield logfile, url
    process = xprocess.getinfo("myserver")
    process.kill()
    subprocess.call(["kill", "-s SIGQUIT", str(process.pid)])
    print(("teardown", dirname, port, url))


def test_tokenize():
    input_ = "d'yer mak'er is a great song, don't you think?"
    expected_output = [
        "d'yer",
        "mak'er",
        "is",
        "a",
        "great",
        "song",
        ",",
        "do",
        "n't",
        "you",
        "think",
        "?",
    ]
    output = list(tokenize(input_))
    assert output == expected_output  # (input_, output, expected_output)


def test_word_frequencies():
    url = "./"
    keywords = ["cat", "dog", "mouse", "mouse", "whale", "dog"]
    output = word_frequencies(url, keywords)
    assert output.url == url
    assert output.frequencies == Counter(
        {"dog": 2, "mouse": 2, "cat": 1, "whale": 1}
    )


def test_crawl_url(myserver):
    START_URL = myserver[1]
    output = StringIO.StringIO()
    crawled = crawl_url(START_URL, output=output)
    assert crawled


def test_wrdcrawler(myserver):
    START_URL = myserver[1]
    output = StringIO.StringIO()
    output = wrdcrawler(START_URL, output=output)
    output.seek(0)
    print(output.read())
    assert output

    # print(pformat(keyword_counts))


def test_expand_link():
    test_data = (
        (
            ("http://localhost/index.html", "About.html"),
            "http://localhost/About.html",
        ),
        (
            ("http://localhost:8080#Test", "About.html"),
            "http://localhost:8080/About.html",
        ),
        (
            ("http://localhost?query", "About.html#Test"),
            "http://localhost/About.html#Test",
        ),
    )
    for input_, expected_output in test_data:
        output = expand_link(*input_)
        assert output == expected_output


def test_strip_fragment():
    test_data = (
        ("http://localhost/#test", "http://localhost/"),
        ("http://localhost:8080?query#Test", "http://localhost:8080?query",),
        ("http://localhost?query", "http://localhost?query"),
    )
    for input_, expected_output in test_data:
        output = strip_fragment(input_)
        assert output == expected_output


def test_same_netloc():
    test_data = (
        (("http://localhost/index.html", "http://localhost/"), True),
        (("http://localhost:8080#Test", "http://localhost/"), False),
        (("http://localhost:8080#Test", "http://localhost"), False),
    )
    for input_, expected_output in test_data:
        output = same_netloc(*input_)
        try:
            assert output == expected_output
        except Exception:
            print(input_)
            raise


def test_sum_counters():
    c1 = {"a": 2, "b": 1, "c": 3}
    c2 = {"a": 1, "b": 2, "d": 3}
    csum = sum_counters([c1, c2])
    for k, v in iteritems(csum):
        assert v == 3  # k


def test_other(myserver):
    url = myserver[1]
    resp = requests.get(url)
    bs = bs4.BeautifulSoup(resp.content)
    links = list(extract_links(url, bs))
    for key, links in itertools.groupby(links, lambda x: x.parent_id):
        print("## %s" % key)
        print(list(links))


def test_build_networkx_graph(myserver, tmpdir):
    url = myserver[1]
    output = sys.stdout
    resp = requests.get(url)
    bs = bs4.BeautifulSoup(resp.content)
    links = list(extract_links(url, bs))
    g = build_networkx_graph(url, links)  # , output=output)
    assert len(g)

    output = StringIO.StringIO()
    write_nxgraph_to_dot(g, output)
    output.seek(0)
    print(output.read())
    output.seek(0)
    assert output.read()
    output.seek(0)
    dotpath = tmpdir / "nxgraph_dot.dot"
    with open(dotpath, "w") as f:
        f.write(output.read())
    dotcontent = dotpath.read_text(encoding="utf8")
    assert dotcontent
    assert dotcontent.startswith("strict digraph")

    output = StringIO.StringIO()
    write_nxgraph_to_json(g, output)
    output.seek(0)
    print(output.read())
    output.seek(0)
    assert output.read()
    output.seek(0)
    forcejsonpath = tmpdir / "nxgraph_force.json"
    with open(forcejsonpath, "w") as f:
        f.write(output.read())

    import matplotlib.pyplot as plt
    import networkx

    networkx.draw_circular(g)
    svgpath = tmpdir / "nxgraph_draw_circular.svg"
    plt.savefig(svgpath)
    svgcontents = svgpath.read_text(encoding="utf8")
    assert svgcontents
    assert "<svg" in svgcontents
    # plt.show()
