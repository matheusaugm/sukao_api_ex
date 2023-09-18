from sqlalchemy import Column, String, Integer, Float

from model import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, unique=True)
    produto = Column(String(255), unique=True)
    valor = Column(Float)
    ingredientes = Column(String(255))

    def __init__(self, codigo:int, produto:str, valor:float,
                 ingredientes:str):
        """
        Cria um Produto

        Arguments:
            codigo: codigo do produto
            produto: nome do produto
            valor: valor do produto
            ingredientes: ingredientes da composição do produto
        """
        self.codigo = codigo
        self.produto = produto
        self.valor = valor
        self.ingredientes = ingredientes
