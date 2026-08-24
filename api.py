from fastapi import FastAPI
from routes.jogador import router

app = FastAPI()

app.include_router(router)