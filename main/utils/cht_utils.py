import re


def strip_leading_ch_symbol(text: str) -> str:
    """remove leading chinese symbols"""
    ch_symbols = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰–—‘’‛“”„‟…‧﹏."
    text = re.sub(r'^[%s]+' % ch_symbols, "", text)
    return text


# 轉換全形英文字母為半形字
def convert_chin_english(text_line):
    output = text_line

    output = output.replace("Ａ", "A")
    output = output.replace("Ｂ", "B")
    output = output.replace("Ｃ", "C")
    output = output.replace("Ｄ", "D")
    output = output.replace("Ｅ", "E")
    output = output.replace("Ｆ", "F")
    output = output.replace("Ｇ", "G")
    output = output.replace("Ｈ", "H")
    output = output.replace("Ｉ", "I")
    output = output.replace("Ｊ", "J")
    output = output.replace("Ｋ", "K")
    output = output.replace("Ｌ", "L")
    output = output.replace("Ｍ", "M")
    output = output.replace("Ｎ", "N")
    output = output.replace("Ｏ", "O")
    output = output.replace("Ｐ", "P")
    output = output.replace("Ｑ", "Q")
    output = output.replace("Ｒ", "R")
    output = output.replace("Ｓ", "S")
    output = output.replace("Ｔ", "T")
    output = output.replace("Ｕ", "U")
    output = output.replace("Ｖ", "V")
    output = output.replace("Ｗ", "W")
    output = output.replace("Ｘ", "X")
    output = output.replace("Ｙ", "Y")
    output = output.replace("Ｚ", "Z")

    return output


# 轉換全形標點符號及四則運算為半形字
def convert_symbols(text_line):
    output = text_line

    output = output.replace("（", "(")
    output = output.replace("）", ")")

    output = output.replace("％", "%")
    output = output.replace("．", ".")

    output = output.replace("　", " ")
    output = output.replace("，", ",")
    output = output.replace("。", ".")

    output = output.replace("＋", "+")
    output = output.replace("－", "-")
    output = output.replace("＊", "*")
    output = output.replace("／", "/")

    output = output.replace("！", "!")
    output = output.replace("？", "?")
    output = output.replace("～", "~")

    return output
