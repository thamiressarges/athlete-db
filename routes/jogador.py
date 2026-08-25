from fastapi import APIRouter
from config.database import connection
from models.jogador import Jogador
from schemas.jogador import jogaodrEntidade, listaJogadoresEntidade

router = APIRouter()

@router.get('/')
async def inicio():
    return "Bem vindo ao Athlete DB"

@router.get('/jogadores')
async def lista_jogadores():
    return listaJogadoresEntidade(connection.local.jogador.find())

@router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    connection.local.jogador.insert_one(dict(jogador))
    return listaJogadoresEntidade(connection.local.jogadores.find())
