from transformers import pipeline
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse, FileResponse
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

classifier = pipeline("sentiment-analysis")

class Request(BaseModel):
    text: str

class RequestItems(BaseModel):
    items: list[str]

class Response(BaseModel):
    response: str

@app.get("/", response_model=Response)
async def root():
    try:
        return JSONResponse(content="FastApi service started!", media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error " + str(e))

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join("static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})

@app.post("/predict/", response_model=Response)
async def predict(request: Request):
    try:
        return JSONResponse(content=classifier(request.text), media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error " + str(e))

@app.post("/batch_predict/", response_model=Response)
async def batch_predict(requestItems: RequestItems):
    try:
        results = []
        for item in requestItems.items:
            results.append(classifier(item))
        return JSONResponse(content=results, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error " + str(e))

# Create documentation for the API endpoints
app.openapi_schema = get_openapi(
    title="Sentiment Analysis API",
    version="1.0.0",
    description="API for sentiment analysis",
    routes=app.routes,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)