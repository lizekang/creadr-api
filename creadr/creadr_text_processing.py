#!/usr/bin/env python
# -*- coding: utf-8 -*-
import text_class
import jieba.posseg as pseg
from split_zh_en import split_zh_en

def cut(text):
    """demo one way to encapsulate the text with metadata, also display
    Args:
        text: user request str

    Returns:
        An array contains every word's instance, contains word, pinyin, nature
    """

    result = []
    text1 = split_zh_en(text)
    for txt in text1:
        if txt[0] == 1:
            for token in pseg.cut(txt[1]):
                word, nature = token
                word_obj = text_class.AnalyzedWord(word, nature)
                result.append(word_obj.to_json())
        else:
            word_obj = text_class.AnalyzedWord(txt[1], 'en')
            result.append(word_obj.to_json())
    return result
