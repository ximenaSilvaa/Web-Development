from fastapi import FastAPI, Form
from typing import Annotated
from  pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class Item(BaseModel):
    primero: str
    segundo: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/suma")
def suma(primero: str = Form(...), segundo: str = Form(...)):
    x = int(primero)
    y = int(segundo)
    resultado = x + y
    return {"resultado": resultado}

