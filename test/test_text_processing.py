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
        ("我".decode('utf-8'), True),
        ("a", False),
        (",", False)
    ]
)
def test_is_zh(input, expected):
    assert is_zh(input) == expected

#test split_zh_en
@pytest.mark.parametrize(
    "input, expected", [
        ("需要注意的是,", ["需要注意的是"]),
        ("虽然对str调用encode()方法是错误的", ["虽然对", "调用", "方法是错误的"]),
        ("strufnskgc",[])
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
    e = AnalyzedWord(u"虽然", u'c')
    f = AnalyzedWord(u"调用", u'vn')
    texts = ['需要注意的是，虽然str调用']
    expected = [a, b, c, d, e, f]
    for text in texts:
        result = cut(text)
        for obj, obj_expected in six.moves.zip(result, expected):
            assert obj.word == obj_expected.word
            assert obj.pinyin == obj_expected.pinyin
            assert obj.nature == obj_expected.nature