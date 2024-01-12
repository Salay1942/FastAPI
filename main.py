from fastapi import FastAPI
from api.v2 import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")