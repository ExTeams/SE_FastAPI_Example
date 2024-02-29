from fastapi import FastAPI
from router import root, get_params, predict

app = FastAPI()

app.include_router(root.router)
app.include_router(get_params.router)
app.include_router(predict.router)
