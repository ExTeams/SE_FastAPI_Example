from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()

sentiment_classifier = pipeline("sentiment-analysis")
text_gen = pipeline("text2text-generation")


@app.get("/")
def root():
    return {"message": "FastAPI service started!"}


@app.get("/sentiment/{text}")
def get_sentiment(text: str):
    return sentiment_classifier(text)


@app.get("/ner/{text}")
def get_named_entities(text: str):
    return text_gen(text)


@app.post("/predict/")
def predict_sentiment(item: Item):
    return sentiment_classifier(item.text)
