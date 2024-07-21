#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .img_captcha import get_ttf as get_ttf
from .img_captcha import img_captcha as img_captcha
from .text_captcha import text_captcha as text_captcha

__version__ = '0.3.2'

__all__ = ['text_captcha', 'get_ttf', 'img_captcha']
