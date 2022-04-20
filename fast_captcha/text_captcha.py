#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import random


def text_captcha(num: int = 4) -> str:
    """
    text captcha
    :param num: number of codes
    :return:
    """
    return ''.join(
        (random.choice(string.ascii_letters + string.digits) for _ in range(num))
    )
