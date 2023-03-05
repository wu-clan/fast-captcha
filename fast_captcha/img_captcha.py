#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from fast_captcha import text_captcha


def use_rgb() -> tuple:
    """
    random colors for captcha text and distractions

    :return:
    """
    return tuple((random.randint(0, 255) for _ in range(3)))


def ttf() -> list:
    """
    get all *.ttf file

    :return:
    """
    fp = Path(__file__).parent.joinpath('fonts')
    ft = [str(t) for t in fp.glob('*.ttf')]
    return ft


def img_captcha(
        *,
        code_num=4,
        width=120,
        height=40,
        font_type=random.choice(ttf()),
        font_size=32,
        draw_lines=True,
        lines_num=4,
        draw_points=False,
        points_density=4,
        img_type='jpeg',
        img_byte=True) -> tuple:
    """
    img captcha

    :param code_num: number of codes
    :param width: picture width, default 120
    :param height: picture height, default 40
    :param font_size: font display size, default 32
    :param font_type: captcha font default random
    :param draw_lines: whether to draw lines
    :param lines_num: number of lines drawn
    :param draw_points: whether to draw points
    :param points_density: draw point's density, the higher the value the higher the density
    :param img_type: image type, for-example: jpeg, png ...
    :param img_byte: convert image to bytes, if you use byte stream
    :return:
    """
    # create img
    img = Image.new('RGB', (width, height), (255, 255, 255))
    # create draw lines
    draw = ImageDraw.Draw(img)
    # set font type and size
    font = ImageFont.truetype(font_type, font_size)
    # random text code
    text = text_captcha(code_num)
    # draw text
    for i, t in enumerate(text):
        draw.text(xy=(i * width // code_num + random.randint((random.randint(i, code_num)), code_num), code_num / 2),
                  text=t,
                  font=font,
                  fill=use_rgb())
    # draw lines
    if draw_lines:
        for i in range(lines_num):
            draw.line(xy=[random.randint(0, width), random.randint(0, height),
                          random.randint(0, width), random.randint(0, height)],
                      fill=use_rgb())
    # draw points
    if draw_points:
        chance = min(100, max(0, int(points_density)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=use_rgb())
    # img type
    if img_byte:
        io = BytesIO()
        img.save(io, img_type)
        io.seek(0)
        img = io
    else:
        img = img
    return img, text
