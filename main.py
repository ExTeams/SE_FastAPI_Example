from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"FastApi service started!"}

@app.get("/timur")
def root():
    return {"Polikarpov"}

@app.get("/Oleg")
def root():
    return {"Savenko"}

@app.get("/Vladislav")
def root():
    return {"Sanduian"}

@app.get("/savenko")
def root():
    return {"Это сделал Олег Савенко!(EZ)"}

@app.get("/{text}")
def get_params(text: str):
    return classifier(text)


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)

