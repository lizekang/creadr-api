# -*- coding=UTF-8 -*-
import split_zh_en
from pypinyin import pinyin
import jieba.posseg as pseg


def cut(text):
    """demo one way to encapsulate the text with metadata, also display"""
    result = []
    text1 = split_zh_en.split_zh_en(text)
    for txt in text1:
        for token in pseg.cut(txt):
            text_obj = {}
            word, nature = token
            if nature != "x":
                pins = pinyin(word)
                text_obj['word'] = word
                text_obj['nature'] = nature
                text_obj['pinyins'] = pins
                result.append(text_obj)
    return result

texts = [
u'需要注意的是，虽然对str调用encode()方法是错误的，但实际上Python不会抛出异常，而是返回另外一个相同内容但不同id的str；对unicode调用decode()方法也是这样。很不理解为什么不把encode()和decode()分别放在unicode和str中而是都放在basestring中，但既然已经这样了，我们就小心避免犯错吧。'
]
for text in texts:
    obj = cut(text)
    print()
    print(obj)
    print()