from fastapi import APIRouter
from config.database import connection
from models.jogador import Jogador
from schemas.jogador import jogadorEntidade, listaJogadoresEntidade
from bson import ObjectId

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
    return listaJogadoresEntidade(connection.local.jogador.find())

@router.get('/jogadores/{id}')
async def busca_jogador(id):
    return jogadorEntidade(connection.local.jogador.find_one(
        {"_id": ObjectId(id)}
    ))

@router.put('/jogadores/{id}')
async def atualiza_jogador(id, jogador: Jogador):
    connection.local.jogador.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            '$set': dict(jogador)
        }
    )
    return jogadorEntidade(connection.local.jogador.find_one(
        {
            "_id": ObjectId(id)
        }
    ))

@router.delete('/jogadores/{id}')
async def exclui_jogador(id):
    return jogadorEntidade(
        connection.local.jogador.find_one_and_delete(
            {
                "_id": ObjectId(id)
            }
        )
    )