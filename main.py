from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


app = FastAPI()

classifier = pipeline("sentiment-analysis")


class Item(BaseModel):
    text: str

@app.get("/")
def root() -> dict:
    return {"message": "FastApi service started!"}

@app.get("/{text}")
def get_params(text: str) -> dict:
    return classifier(text)

@app.post("/predict/")
def predict(item: Item) -> dict:
    return classifier(item.text)
