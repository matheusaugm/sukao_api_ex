from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model import Base


# Modelo para a tabela "ingredientes"
class Ingredientes(Base):
    __tablename__ = 'ingredientes'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

# Tabela de associação para a relação muitos-para-muitos entre "produto" e "ingredientes"
ingredientes_produto = Table('ingredientes_produto', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('id_produto', Integer, ForeignKey('produto.id')),
    Column('id_ingrediente', Integer, ForeignKey('ingredientes.id'))
)
