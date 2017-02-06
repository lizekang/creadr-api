# -*- coding=UTF-8 -*-
def split_zh_en(str):
    unicodeStr = str
    zh_group = []
    zh_gather = ""
    zh_status = False

    for c in unicodeStr:
        if not zh_status and is_zh(c):
            zh_status = True
        elif not is_zh(c) and zh_status:
            zh_status = False
            if zh_gather != "":
                zh_group.append( zh_gather)
        if zh_status:
            zh_gather += c
        else:
            zh_gather = ""


    if zh_gather != "":
        zh_group.append(zh_gather)

    return zh_group


def is_zh(c):
    x = ord(c)
    # Punct & Radicals
    if x >= 0x2e80 and x <= 0x33ff:
        return True

    # Fullwidth Latin Characters
    elif x >= 0xff00 and x <= 0xffef:
        return True

    # CJK Unified Ideographs &
    # CJK Unified Ideographs Extension A
    elif x >= 0x4e00 and x <= 0x9fbb:
        return True
    # CJK Compatibility Ideographs
    elif x >= 0xf900 and x <= 0xfad9:
        return True

    # CJK Unified Ideographs Extension B
    elif x >= 0x20000 and x <= 0x2a6d6:
        return True

    # CJK Compatibility Supplement
    elif x >= 0x2f800 and x <= 0x2fa1d:
        return True

    else:
        return False

text = u'需要注意的是，虽然对str调用encode()方法是错误的，但实际上Python不会抛出异常，而是返回另外一个相同内容但不同id的str；对unicode调用decode()方法也是这样。很不理解为什么不把encode()和decode()分别放在unicode和str中而是都放在basestring中，但既然已经这样了，我们就小心避免犯错吧。'
print(split_zh_en(text))
