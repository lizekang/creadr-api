#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from creadr.split_zh_en import is_zh
from creadr.split_zh_en import split_zh_en
@pytest.mark.parametrize(
    "input, expected", [
        ("我".decode('utf-8'), True),
        ("a", False),
        (",", False)
    ]
)
def test_is_zh(input, expected):
    assert is_zh(input) == expected

@pytest.mark.parametrize(
    "input, expected", [
        ("需要注意的是,", ["需要注意的是"]),
        ("虽然对str调用encode()方法是错误的", ["虽然对", "调用", "方法是错误的"]),
        ("strufnskgc",[])
    ]
)
def test_split_zh_en(input, expected):
    assert split_zh_en(input) == expected

