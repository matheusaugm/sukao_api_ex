from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from model import Base
from ingredientes import ingredientes_produto

# Relacionamento entre "produto" e "ingredientes" usando a tabela de associação
class ProdutoIngredientes(Base):
    __table__ = ingredientes_produto
    produto = relationship("Produto", back_populates="ingredientes")
    ingrediente = relationship("Ingredientes", back_populates="produtos")