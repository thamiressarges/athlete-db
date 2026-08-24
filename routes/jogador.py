from fastapi import APIRouter
from config.database import connection
from models.jogador import Jogador

router = APIRouter()

@router.get("/")
async def inicio():
    return "Bem vindo ao Athlete DB"
