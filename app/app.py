from fastapi import FastAPI, Request

from pydantic import BaseModel
import os
import json
import requests

app = FastAPI()
NOME_INSTANCIA = os.getenv("NOME_INSTANCIA", "app")
CAMINHO_ARQUIVO = f"/mensagens/{NOME_INSTANCIA}.json"

# Inicializa o arquivo de log da instância
os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
if not os.path.exists(CAMINHO_ARQUIVO):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump([], f)

class Mensagem(BaseModel):
    message: str

from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
import requests

app = FastAPI()
NOME_INSTANCIA = os.getenv("NOME_INSTANCIA", "app")
CAMINHO_ARQUIVO = f"/mensagens/{NOME_INSTANCIA}.json"

# Garante que o arquivo existe
os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
if not os.path.exists(CAMINHO_ARQUIVO):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump([], f)

class Mensagem(BaseModel):
    message: str

def gravar_mensagem_localmente(mensagem: dict):
    with open(CAMINHO_ARQUIVO, "r+") as f:
        mensagens = json.load(f)
        mensagens.append(mensagem)
        f.seek(0)
        json.dump(mensagens, f, indent=2)
        f.truncate()  # <- ESSENCIAL para remover o lixo do final do arquivo


def replicar_para_outros_containers(mensagem: dict):
    containers = ["app1", "app2", "app3"]
    containers.remove(NOME_INSTANCIA)
    for container in containers:
        try:
            requests.post(
                f"http://{container}:5000/send",
                json=mensagem,
                headers={"X-Replica": "true"},
                timeout=1
            )
        except Exception as e:
            print(f"Falha ao replicar para {container}: {e}")

@app.post("/send")
def receber_mensagem(mensagem: Mensagem, request: Request):
    # Ignora replicação circular
    if request.headers.get("X-Replica") == "true":
        gravar_mensagem_localmente(mensagem.dict())
        return {"status": "ok", "origem": "replicado"}

    # Mensagem original (não replicada ainda)
    dados = mensagem.dict()
    gravar_mensagem_localmente(dados)
    replicar_para_outros_containers(dados)
    return {"status": "ok", "mensagem": mensagem.message}

@app.get("/messages")
def listar_mensagens():
    with open(CAMINHO_ARQUIVO, "r") as f:
        return json.load(f)
