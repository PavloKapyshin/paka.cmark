# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest


class ToHTMLTest(unittest.TestCase):
    SAMPLE = (
        "Проверяем *CommonMark*.\n\nВставляем `код`.\nИ другие штуки.\n\n"
        "<p>Test of <em>HTML</em>.</p>")

    def setUp(self):
        from paka.cmark import LineBreaks, to_html

        self.func = to_html
        self.line_breaks = LineBreaks

    def check(self, source, expected, **kwargs):
        self.assertEqual(self.func(source, **kwargs), expected)

    def test_empty(self):
        self.check("", "")

    def test_ascii(self):
        self.check("Hello, Noob!", "<p>Hello, Noob!</p>\n")

    def test_no_breaks(self):
        expected = (
            "<p>Проверяем <em>CommonMark</em>.</p>\n"
            "<p>Вставляем <code>код</code>. И другие штуки.</p>\n"
            "<p>Test of <em>HTML</em>.</p>\n")
        self.check(self.SAMPLE, expected)
        self.check(self.SAMPLE, expected, breaks=False)

    def test_soft_breaks(self):
        expected = (
            "<p>Проверяем <em>CommonMark</em>.</p>\n"
            "<p>Вставляем <code>код</code>.\nИ другие штуки.</p>\n"
            "<p>Test of <em>HTML</em>.</p>\n")
        self.check(self.SAMPLE, expected, breaks=True)
        self.check(self.SAMPLE, expected, breaks=self.line_breaks.soft)
        self.check(self.SAMPLE, expected, breaks="soft")

    def test_hard_breaks(self):
        expected = (
            "<p>Проверяем <em>CommonMark</em>.</p>\n"
            "<p>Вставляем <code>код</code>.<br />\nИ другие штуки.</p>\n"
            "<p>Test of <em>HTML</em>.</p>\n")
        self.check(self.SAMPLE, expected, breaks=self.line_breaks.hard)
        self.check(self.SAMPLE, expected, breaks="hard")

    def test_no_breaks_and_safe(self):
        expected = (
            "<p>Проверяем <em>CommonMark</em>.</p>\n"
            "<p>Вставляем <code>код</code>. И другие штуки.</p>\n"
            "<!-- raw HTML omitted -->\n")
        self.check(self.SAMPLE, expected, safe=True)
        self.check(self.SAMPLE, expected, breaks=False, safe=True)

    def test_soft_breaks_and_safe(self):
        expected = (
            "<p>Проверяем <em>CommonMark</em>.</p>\n"
            "<p>Вставляем <code>код</code>.\nИ другие штуки.</p>\n"
            "<!-- raw HTML omitted -->\n")
        self.check(self.SAMPLE, expected, breaks=True, safe=True)
        self.check(
            self.SAMPLE, expected, breaks=self.line_breaks.soft, safe=True)
        self.check(self.SAMPLE, expected, breaks="soft", safe=True)

    def test_hard_breaks_and_safe(self):
        expected = (
            "<p>Проверяем <em>CommonMark</em>.</p>\n"
            "<p>Вставляем <code>код</code>.<br />\nИ другие штуки.</p>\n"
            "<!-- raw HTML omitted -->\n")
        self.check(
            self.SAMPLE, expected, breaks=self.line_breaks.hard, safe=True)
        self.check(self.SAMPLE, expected, breaks="hard", safe=True)
