from fastapi import APIRouter
from transformers import pipeline
from pydantic import BaseModel

router = APIRouter()
classifier = pipeline("sentiment-analysis")

class Item(BaseModel):
    text: str

@router.get("/")
async def root():
    return {"FastApi service started!"}

@router.get("/{text}")
async def get_params(text: str):
    return classifier(text)

@router.post("/predict/")
async def predict(item: Item):
    return classifier(item.text)
