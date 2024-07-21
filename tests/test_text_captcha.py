#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fast_captcha.text_captcha import text_captcha


def test_text():
    text = text_captcha()
    assert isinstance(text, str)
    assert len(text) == 4

    text = text_captcha(num=6)
    assert isinstance(text, str)
    assert len(text) == 6
