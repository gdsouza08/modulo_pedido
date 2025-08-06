import unittest
from use_cases.efetuar_pedido import efetuar_pedido
from domain.exceptions import *

class TestEfetuarPedido(unittest.TestCase):
    def test_produto_inexistente(self):
        with self.assertRaises(ProdutoNaoExiste):
            efetuar_pedido("Produto Fantasma", 1)

    def test_estoque_insuficiente(self):
        with self.assertRaises(EstoqueInsuficiente):
            efetuar_pedido("Notebook", 999)

    def test_pedido_valido(self):
        pedido = efetuar_pedido("Notebook", 1)
        self.assertEqual(pedido.descricao, "Notebook")
        