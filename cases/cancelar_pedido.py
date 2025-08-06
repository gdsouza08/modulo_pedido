from infrastructure.repository import carregar_json, salvar_json
from domain.exceptions import PedidoNaoEncontrado

def cancelar_pedido(pedido_id):
    pedidos = carregar_json("pedidos.json")

    for pedido in pedidos:
        if pedido["id"] == pedido_id and pedido["status"] == "ativo":
            pedido["status"] = "cancelado"
            salvar_json("pedidos.json", pedidos)
            return pedido

    raise PedidoNaoEncontrado("Pedido não encontrado ou já cancelado.")