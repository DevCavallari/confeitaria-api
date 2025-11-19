from conexao import get_conexao
from psycopg2.extras import RealDictCursor
from flask import jsonify

def buscar_cardapio():
    conexao = get_conexao()
    cursor = conexao.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM cardapio")
    itens = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(cardapio)


def buscar_cardapio():
    itens = [
        {
            "id": 1,
            "nome": "Chocomoça",
            "descricao": " Bolo de chocolate com ninho ",
            "preco": 200.99,
            "foto": ""

        }
    ]
    return itens

def buscar_cardapio_id(item_id):
    return{
            "id": 1,
            "nome": "Chocomoça",
            "descricao": " Bolo de chocolate com ninho ",
            "preco": 150.99,
            "foto": ""
    }

