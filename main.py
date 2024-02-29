from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from transformers import pipeline
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader

class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("sentiment-analysis")

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('result.html')

@app.get("/")
def root():
    return {"FastApi service started!"}

@app.get("/{text}", response_class=HTMLResponse)
def get_params(request: Request, text: str):
    prediction_result = classifier(text)
    rendered_template = template.render(result=prediction_result)
    return HTMLResponse(content=rendered_template)



@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)
