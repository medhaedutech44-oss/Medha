from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get('/')
def home():
    return {"message":"Hello World"}