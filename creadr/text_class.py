#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pypinyin import pinyin

class AnalyzedWord(object):
    """Summary of class here.
    Encapsulate word, pinyin, nature in class

    Attributes:
        word: Chinese words
        nature: the word's nature
        pinyin: the word's pinyin
    """
    def __init__(self, word, nature):
        self.word = word
        self.nature = nature
        self.pinyin = self.get_pinyin(word)

    def get_pinyin(self, word):
        """use pypinyin to get pinyin of word"""
        pins = pinyin(word)
        result = []
        for pin in pins:
            result.append(pin[0])
        return result

    def to_json(self):
        """demo one way to display word, pinyin and nature in json"""
        return {
            'word': self.word,
            'pinyin': self.pinyin,
            'nature': self.nature
        }
