# fast_captcha

fast to use captcha

# install

```shell
pip install fast-captcha
```

## text_captcha

```python
from fast_captcha import text_captcha

print(text_captcha())  # BnZU
```

## img_captcha

```python
from fast_captcha import img_captcha

img, text = img_captcha()

print(img)  # <_io.BytesIO object at 0x000002366AB93DB0>
print(text)  # 2z22
```

# FastAPI

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from fast_captcha import img_captcha

app = FastAPI()

@app.get('/captcha', summary='captcha', name='captcha')
def get_captcha():
    img, text = img_captcha()
    return StreamingResponse(content=img, media_type='image/jpeg')
```

# Django-Ninja

```python
from ninja import NinjaAPI
from django.http import StreamingHttpResponse

from fast_captcha import img_captcha

app = NinjaAPI()

@app.get('/captcha', summary='captcha', url_name='captcha')
def get_captcha(request):
    img, text = img_captcha()
    return StreamingHttpResponse(streaming_content=img, content_type='image/jpeg')
```

# License
MIT License

Copyright (c) 2022 xiaowu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.