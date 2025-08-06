from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime

@dataclass
class Pedido:
    id: str
    descricao: str
    quantidade: int
    preco_unitario: float
    status: str
    criado_em: str

    def total(self):
        return self.quantidade * self.preco_unitario

    @staticmethod
    def criar(descricao, quantidade, preco_unitario):
        return Pedido(
            id=str(uuid4()),
            descricao=descricao,
            quantidade=quantidade,
            preco_unitario=preco_unitario,
            status="ativo",
            criado_em=datetime.now().isoformat()
        )