#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import six
from creadr.split_zh_en import is_zh
from creadr.split_zh_en import split_zh_en
from creadr.text_class import AnalyzedWord
from creadr.creadr_text_processing import cut

#test is_zh()
@pytest.mark.parametrize(
    "input, expected", [
        (u"我", True),
        ("a", False),
        (",", False)
    ]
)
def test_is_zh(input, expected):
    assert is_zh(input) == expected

#test split_zh_en
@pytest.mark.parametrize(
    "input, expected", [
        ("需要注意的是", [[1, '需要注意的是']]),
        ("虽然对str调用encode()方法是错误的", [[1, '虽然对'], [0, 'str'], [1, '调用'], [0, 'encode()'], [1, '方法是错误的']]),
        ("strufnskgc",[[0, 'strufnskgc']])
    ]
)
def test_split_zh_en(input, expected):
    assert split_zh_en(input) == expected

#test creadr_text_processing.py
#test cut(text)
def test_cut():
    a = AnalyzedWord(u"需要", u'v')
    b = AnalyzedWord(u"注意", u'v')
    c = AnalyzedWord(u"的", u'uj')
    d = AnalyzedWord(u"是", u'v')
    h = AnalyzedWord(u"，", u'x')
    e = AnalyzedWord(u"虽然", u'c')
    f = AnalyzedWord(u"str", u'en')
    g = AnalyzedWord(u"调用", u'vn')
    texts = ['需要注意的是，虽然str调用']
    expected = [a, b, c, d, h, e, f, g]
    for text in texts:
        result = cut(text)
        for obj, obj_expected in six.moves.zip(result, expected):
            assert obj['nature'] == obj_expected.nature

# test class, mainly test to_json() function
def test_class():
    a = AnalyzedWord(u'需要', u'v')
    b = AnalyzedWord(u'xuyao', u'en')
    c = AnalyzedWord(u',', u'x')
    a_expected = {'nature': 'v', 'word_obj': [{'pinyin': u"x\u016b", 'word': u"需"}, {'pinyin': u"y\u00e0o", 'word': u"要"}]}
    b_expected = {'nature': 'en', 'word_obj': [{'pinyin': u"", 'word': u"xuyao"}]}
    c_expected = {'nature': 'x', 'word_obj': [{'pinyin': u"", 'word': u","}]}
    assert a.to_json() == a_expected
    assert b.to_json() == b_expected
    assert c.to_json() == c_expected