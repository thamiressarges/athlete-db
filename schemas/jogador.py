def jogadorEntidade(db_item) -> dict:
    return {
        'id': str(db_item['_id']),
        'nome': db_item['nome'],
        'idade': db_item['idade'],
        'time': db_item['time']
    }

def listaJogadoresEntidade(db_item_lista) -> list:
    lista_jogadores = []
    for item in db_item_lista:
        lista_jogadores.append(jogaodrEntidade(item))
    return lista_jogadores

