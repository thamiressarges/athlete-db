from fastapi import FastAPI
from routes.jogador import router
from fastapi.middleware.cors import CORSMiddleware

cliente_app = [
    "http://localhost:3000"
]

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cliente_app,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)