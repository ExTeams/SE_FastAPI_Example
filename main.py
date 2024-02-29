from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi.testclient import TestClient

class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/")
def root():
    return "FastApi service started!"


@app.get("/{text}")
def get_params(text: str):
    return classifier(text)


@app.post("/predict/")
def predict(item: Item):
    print(item)
    return classifier(item.text)


@app.post("/analyze_texts/")
def analyze_texts(items):
    results = []
    for item in items:
        result = {"text": item.text, "sentiment": classifier(item.text)}
        results.append(result)
    return results

