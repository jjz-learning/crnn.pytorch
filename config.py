# -*- coding: utf-8 -*-
"""
 @File    : config.py
 @Time    : 2019-12-24 11:49
 @Author  : yizuotian
 @Description    : 配置类
"""
from data.words import Word


class Config(object):
    # dataset
    chinese_word = True
    alphabet = True
    digit = True
    punctuation = True
    currency = True

    def __init__(self):
        self.word = Word(self.chinese_word, self.alphabet, self.digit, self.punctuation, self.currency)


class TestConfig(Config):
    chinese_word = False


# cfg = TestConfig()
cfg = Config()
