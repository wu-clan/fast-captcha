#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import BytesIO

from PIL import Image

from fast_captcha import img_captcha


def test_img_file():
    img, text = img_captcha(img_byte='file')
    assert isinstance(img, Image.Image)
    assert isinstance(text, str)
    assert len(text) == 4

    img, text = img_captcha(img_byte='file', code_num=6)
    assert isinstance(img, Image.Image)
    assert isinstance(text, str)
    assert len(text) == 6


def test_img_bytesio():
    img, text = img_captcha(img_byte='bytesio')
    assert isinstance(img, BytesIO)
    assert isinstance(text, str)
    assert len(text) == 4

    img, text = img_captcha(img_byte='bytesio', code_num=6)
    assert isinstance(img, BytesIO)
    assert isinstance(text, str)


def test_img_base64():
    img, text = img_captcha(img_byte='base64')
    assert isinstance(img, str)
    assert isinstance(text, str)
    assert len(text) == 4

    img, text = img_captcha(img_byte='base64', code_num=6)
    assert isinstance(img, str)
    assert isinstance(text, str)
    assert len(text) == 6
