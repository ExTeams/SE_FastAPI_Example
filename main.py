from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from transformers import pipeline
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader

class Item(BaseModel):
    text: str

app = FastAPI()

sentiment_classifier = pipeline("sentiment-analysis")
text_gen = pipeline("text2text-generation")

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('result.html')

@app.get("/")
def root():
    return {"message": "FastAPI service started!"}


@app.get("/sentiment/{text}")
def get_sentiment(text: str):
    return sentiment_classifier(text)

@app.get("/{text}", response_class=HTMLResponse)
def get_params(request: Request, text: str):
    prediction_result = classifier(text)
    rendered_template = template.render(result=prediction_result)
    return HTMLResponse(content=rendered_template)

@app.get("/ner/{text}")
def get_named_entities(text: str):
    return text_gen(text)


@app.post("/predict/")
def predict_sentiment(item: Item):
    return sentiment_classifier(item.text)
