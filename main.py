# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/9 9:37
"""
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from utils import get_img_src, get_sentence
import uvicorn

IMAGE_PATH = "./static/images"
FILE_PATH = "./static/files/sentences.xlsx"


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    sentence = get_sentence(FILE_PATH, True)
    return templates.TemplateResponse("index.html", context={"request": request, "sentence": sentence})


@app.post("/new")
def acquire_img(data: dict):
    if data["secret"] != "我爱肥肥子":
        return_data = {
            "status": 0,
            "msg": "暗号不正确"
        }
    else:
        img_src = get_img_src(IMAGE_PATH)
        sentence = get_sentence(FILE_PATH, False)
        return_data = {
            "status": 1,
            "img_src": img_src,
            "sentence": sentence
        }
    return return_data


if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
