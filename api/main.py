from flask import Flask, request, jsonify
from use_cases.efetuar_pedido import efetuar_pedido
from use_cases.cancelar_pedido import cancelar_pedido
from use_cases.listar_pedidos import listar_pedidos
from domain.exceptions import *

app = Flask(__name__)

@app.post("/pedidos")
def criar_pedido():
    data = request.json
    try:
        pedido = efetuar_pedido(data["descricao"], data["quantidade"])
        return jsonify(pedido.__dict__), 201
    except (ProdutoNaoExiste, EstoqueInsuficiente) as e:
        return jsonify({"erro": str(e)}), 400

@app.delete("/pedidos/<pedido_id>")
def deletar_pedido(pedido_id):
    try:
        pedido = cancelar_pedido(pedido_id)
        return jsonify(pedido), 200
    except PedidoNaoEncontrado as e:
        return jsonify({"erro": str(e)}), 404

@app.get("/pedidos")
def listar():
    return jsonify(listar_pedidos()), 200

if __name__ == "__main__":
    app.run(debug=True)