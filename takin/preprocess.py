# -*- encoding: utf-8 -*-
'''
@File   :   preprocess.py
@Time   :   2021/04/12 18:28:06
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   The function set of text preprocess.
'''

import re


def lowercase(text: str) -> str:
    """
    All characters of text are converted into lowercase. 
    """
    return text.lower()


def capitalize(text: str) -> str:
    """
    The first character of text are converted into uppercase.
    """
    return text.capitalize()


def delete_escape_character(text: str) -> str:
    """
    Delete all escape characters (\r|\n|\t|\f|\v) of text.
    """
    return re.sub(r"[\r\n\t\f\v]", " ", text)


def delete_extra_whitespace(text: str) -> str:
    """
    Delete any extra white spaces of text.
    """
    return " ".join(text.split())


def delete_digit(text: str) -> str:
    """
    Delete all digits in text.
    """
    return re.sub(r"[0-9]", "", text)


def delete_punctuation(text: str) -> str:
    """
    Delete all punctuation in text.
    """
    return re.sub(r"[;:,.\"?!'·！？；，。：“”、‘’《》]", "", text)


def delete_letter_in_zh(text: str) -> str:
    """
    Delete English letters in Chinese text.
    """
    return re.sub(r"[A-Za-z]", "", text)


def delete_chinese_in_en(text: str) -> str:
    """
    Delete chinese characters in English text.
    """
    return re.sub(r"[\u4e00-\u9fa5]", "", text)


def delete_special_character(text: str) -> str:
    """
    Delete special characters in text.
    """
    return re.sub(r"[\╔\ˊ\〉\〈\–\η\●\®\·\•\-\~#/*&$|★▶><\\^@+[=\]()（）{%_}?\…]+", "", text)


def delete_bracket(text: str) -> str:
    """
    Delete the content in the brackets and the brackets themselves.
    Including <*>、(*)、（*）、【*】、[*]、{*}
    """
    text = re.sub(r"<[^<>]*>", "", text)
    text = re.sub(r"\([^()]*\)", "", text)
    text = re.sub(r"\（[^（）]*\）", "", text)
    text = re.sub(r"\【[^【】]*\】", "", text)
    text = re.sub(r"\[[^\[\]]*\]", "", text)
    text = re.sub(r"\{[^{}]*\}", "", text)
    return text


def delete_series_number(text: str) -> str:
    """
    Delete all series numbers in text.
    Including *.、(*).、*).
    """
    text = re.sub(r"\d+\.[^\d+]", "", text)
    text = re.sub(r"\(\d+\).", "", text)
    text = re.sub(r"\d+\).", "", text)
    text = re.sub(r"\d+\)", "", text)
    text = re.sub(r"\d+\)、", "", text)
    return text