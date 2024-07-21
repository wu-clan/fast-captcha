#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import random

from io import BytesIO
from pathlib import Path
from typing import List, Literal, Tuple

from PIL import Image, ImageDraw, ImageFont

from fast_captcha.text_captcha import text_captcha


def use_rgb() -> Tuple[int, ...]:
    """
    random colors for captcha text and distractions

    :return:
    """
    return tuple((random.randint(0, 255) for _ in range(3)))


def get_ttf() -> List[str]:
    """
    get all *.ttf file

    :return:
    """
    file_path = Path(__file__).parent.joinpath('fonts')
    ttf = [str(f) for f in file_path.glob('*.ttf')]
    return ttf


def img_captcha(
    *,
    code_num: int = 4,
    width: int = 120,
    height: int = 40,
    font_type: str = random.choice(get_ttf()),
    font_size: int = 32,
    draw_lines: bool = True,
    lines_num: int = 4,
    draw_points: bool = False,
    points_density: int = 4,
    img_type: str = 'jpeg',
    img_byte: Literal['file', 'bytesio', 'base64'] = 'bytesio',
) -> Tuple[Image.Image | BytesIO | bytes, str]:
    """
    img captcha

    :param code_num: number of codes.
    :param width: picture width, default 120.
    :param height: picture height, default 40.
    :param font_size: font display size, default 32.
    :param font_type: captcha font default random.
    :param draw_lines: whether to draw lines.
    :param lines_num: number of lines drawn.
    :param draw_points: whether to draw points.
    :param points_density: draw point's density, the higher the value the higher the density.
    :param img_type: image type, for-example: jpeg, png ...
    :param img_byte: convert image to bytes, if you are using byte stream.
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
        draw.text(
            xy=(i * width // code_num + random.randint((random.randint(i, code_num)), code_num), code_num / 2),
            text=t,
            font=font,
            fill=use_rgb(),
        )
    # draw lines
    if draw_lines:
        for i in range(lines_num):
            draw.line(
                xy=[
                    random.randint(0, width),
                    random.randint(0, height),
                    random.randint(0, width),
                    random.randint(0, height),
                ],
                fill=use_rgb(),
            )
    # draw points
    if draw_points:
        chance = min(100, max(0, int(points_density)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=use_rgb())
    # img save
    io = BytesIO()
    img.save(io, img_type)
    io.seek(0)
    if img_byte == 'file':
        img = img
    elif img_byte == 'bytesio':
        img = io
    elif img_byte == 'base64':
        import base64

        img = base64.b64encode(io.getvalue()).decode('utf-8')
    else:
        raise ValueError('img_byte must be one of file, bytesio, base64')
    return img, text
