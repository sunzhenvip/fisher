"""
    帮助函数
"""

__author__ = 'sz'


def is_isbn_or_key(word):
    """
        函数
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    # print(isbn_or_key)
    return isbn_or_key
