from infrastructure.repository import carregar_json

def listar_pedidos():
    pedidos = carregar_json("pedidos.json")
    return [p for p in pedidos if p["status"] == "ativo"]