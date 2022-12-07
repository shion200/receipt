from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title = 'FastAPIで作成する家計簿アプリ'
    description = 'Fastapiでレシートを画像認識させて家計簿アプリをつくる'
    version = '0.9 beta'
)

def index(request: Request):
    return {'Hello' : 'World'}