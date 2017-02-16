from pypinyin import pinyin

class AnalyzedWord(object):
    def __init__(self, word, nature):
        self.word = word
        self.nature = nature
        self.pinyin = self.get_pinyin(word)

    def get_pinyin(self, word):
        pins = pinyin(word)
        return pins

    def to_json(self):
        return {
            'word': self.word,
            'pinyin': self.pinyin,
            'nature': self.nature
        }
