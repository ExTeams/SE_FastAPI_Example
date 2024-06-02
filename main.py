from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi

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

# Create documentation for the API endpoints
app.openapi_schema = get_openapi(
    title="Sentiment Analysis API",
    version="1.0.0",
    description="API for sentiment analysis",
    routes=app.routes,
)
