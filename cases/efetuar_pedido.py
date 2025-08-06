from domain.models import Pedido
from domain.exceptions import ProdutoNaoExiste, EstoqueInsuficiente
from infrastructure.repository import carregar_json, salvar_json

def efetuar_pedido(nome_produto, quantidade):
    produtos = carregar_json("produtos.json")
    pedidos = carregar_json("pedidos.json")

    produto = next((p for p in produtos if p["nome"] == nome_produto), None)
    if not produto:
        raise ProdutoNaoExiste("Produto não encontrado.")

    if produto["estoque"] < quantidade:
        raise EstoqueInsuficiente("Quantidade indisponível no estoque.")

    produto["estoque"] -= quantidade

    pedido = Pedido.criar(nome_produto, quantidade, produto["preco"])
    pedidos.append(pedido.__dict__)

    salvar_json("produtos.json", produtos)
    salvar_json("pedidos.json", pedidos)
    return pedido