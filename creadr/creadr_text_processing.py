# -*- coding=UTF-8 -*-
#import split_zh_en
from pypinyin import pinyin
import jieba.posseg as pseg


def cut(text):
    """demo one way to encapsulate the text with metadata, also display"""
    result = []
   # text = split_zh_en.split_zh_en(text)
    for token in pseg.cut(text):
        text_obj = {}
        word, nature = token
        pins = pinyin(word)
        text_obj['word'] = word
        text_obj['nature'] = nature
        text_obj['pinyins'] = pins
        result.append(text_obj)
    return result

texts = [
        u'某君昆仲，今隐其名，皆余昔日在中学时良友；分隔多年，消息渐阙。日前偶闻其一大病；适归故乡，迂道往访，则仅晤一人，言病者其弟也。劳君远道来视，然已早愈，赴某地候补⑵矣。因大笑，出示日记二册，谓可见当日病状，不妨献诸旧友。持归阅一过，知所患盖“迫害狂”之类。语颇错杂无伦次，又多荒唐之言；亦不著月日，惟墨色字体不一，知非一时所书。间亦有略具联络者，今撮录一篇，以供医家研究。记中语误，一字不易；惟人名虽皆村人，不为世间所知，无关大体，然亦悉易去。至于书名，则本人愈后所题，不复改也。七年四月二日识。'
]
for text in texts:
    obj = cut(text)
    print()
    print (obj)
    print ('\n\n')