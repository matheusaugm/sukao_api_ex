from pydantic import BaseModel
from typing import List
from model.produto import Produto


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    codigo: int = 10
    produto: str = "Natural Atum"
    valor: float = 24.00
    ingredientes: str = "(atum, cenoura, maionese, alface e tomate)"


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no nome do produto.
    """
    produto: str = "Teste"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "codigo": produto.codigo,
            "produto": produto.produto,
            "valor": produto.valor,
            "ingredientes": produto.ingredientes
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado
    """
    id: int = 1
    codigo: int = 10
    produto: str = "Natural Atum"
    valor: float = 24.00
    ingredientes: str = "(atum, cenoura, maionese, alface e tomate)"


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    produto: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "codigo": produto.codigo,
        "produto": produto.produto,
        "valor": produto.valor,
        "ingredientes": len(produto.ingredientes)
    }
