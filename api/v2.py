from fastapi import APIRouter, Depends
from api import Inquiry

api_router = APIRouter()

api_router.include_router(Inquiry.router)

