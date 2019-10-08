from constant import ALPH, ALPH_REVERSE, PUNC, PUNC_REVERSE


def encode(forEncode):
    result = ""
    for i in forEncode.lower():
        if i in ALPH:
            result = result + ALPH_REVERSE[ALPH.index(i)]
        elif i in PUNC:
            result = result + PUNC_REVERSE[PUNC.index(i)]
        else:
            result = result + " "
    return result


def decode(forDecode):
    result = ""
    for i in forDecode.lower():
        if i in ALPH_REVERSE:
            result = result + ALPH[ALPH_REVERSE.index(i)]
        elif i in PUNC_REVERSE:
            result = result + PUNC[PUNC_REVERSE.index(i)]
        else:
            result = result + " "
    return result
