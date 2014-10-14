#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_wrdrd
----------------------------------

Tests for `wrdrd` module.
"""

import unittest

import wrdrd
import wrdrd.tools
import wrdrd.tools.domain
import wrdrd.tools.crawl
import wrdrd.tools.stripsinglehtml


class TestWrdrd(unittest.TestCase):

    def setUp(self):
        pass

    def test_imports(self):
        assert wrdrd
        assert wrdrd.tools
        assert wrdrd.tools.domain
        assert wrdrd.tools.crawl
        assert wrdrd.tools.stripsinglehtml

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
