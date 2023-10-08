# fast_captcha

fast to use captcha

# Install

```shell
pip install fast-captcha
```

# Use

## text

```python
from fast_captcha import text_captcha

print(text_captcha())  # BnZU
```

## img

```python
from fast_captcha import img_captcha

img, text = img_captcha()

print(img)  # <_io.BytesIO object at 0x000002366AB93DB0>
print(text)  # 2z22
```

# Integration

## FastAPI

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

## Django-Ninja

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
