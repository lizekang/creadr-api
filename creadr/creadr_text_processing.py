# -*- coding=UTF-8 -*-
from creadr.split_zh_en import split_zh_en
from creadr.text_class import AnalyzedWord
from pypinyin import pinyin
import jieba.posseg as pseg


def cut(text):
    """demo one way to encapsulate the text with metadata, also display"""
    result = []
    text1 = split_zh_en(text)
    for txt in text1:
        for token in pseg.cut(txt):
            word, nature = token
            if nature != "x":
                word_obj = AnalyzedWord(word, nature)
                result.append(word_obj)
    return result

texts = [
u'需要注意的是，虽然对str调用encode()方法是错误的，但实际上Python不会抛出异常，而是返回另外一个相同内容但不同id的str；对unicode调用decode()方法也是这样。很不理解为什么不把encode()和decode()分别放在unicode和str中而是都放在basestring中，但既然已经这样了，我们就小心避免犯错吧。'
]
for text in texts:
    objs = cut(text)
    result = []
    for obj in objs:
        result.append(obj.to_json())
    print(result)
