from model import model_pipeline

from typing import Union

from fastapi import FastAPI, UploadFile

import io

from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    
    image = Image(io.BytesIO(content))
    
    result = model_pipeline(text, image)
    return {"answer": result}