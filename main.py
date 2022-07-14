from typing import Union
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randint


app = FastAPI()

banco_de_dados = []

class Produto(BaseModel):
    titulo: str
    descricao: Union[str, None] = None
    link: Union[str, None] = None
    foto: Union[str, None] = None
    recebido_como: Union[str, None] = None

@app.get("/")
def read_root():
    return "lista de desejo"

@app.post("/produto")
def adiciona_produto(produto: Produto = Body(embed=True)):
    if len(banco_de_dados) != 0:
        ultimo_produto = banco_de_dados[-1]
        ultimo_id = ultimo_produto["id"]
        ultimo_id = ultimo_id + 1
        produto = dict(produto)
        produto["id"] = ultimo_id
        banco_de_dados.append(produto)
        return banco_de_dados
    
    if len(banco_de_dados) == 0:
        produto = dict(produto)
        produto["id"] = 0
        banco_de_dados.append(produto)
        return banco_de_dados


@app.get ("/produto")
def pega_produto_aleatorio():
    tamanho_da_lista = len(banco_de_dados)
    posicao = randint(0, tamanho_da_lista - 1)
    return banco_de_dados[posicao]


@app.get("/produtos")
def pega_todos_os_produtos():
    return banco_de_dados
