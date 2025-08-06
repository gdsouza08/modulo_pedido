import json
import os

BASE_PATH = "data"

def carregar_json(arquivo):
    caminho = os.path.join(BASE_PATH, arquivo)
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r") as f:
        return json.load(f)

def salvar_json(arquivo, dados):
    caminho = os.path.join(BASE_PATH, arquivo)
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)