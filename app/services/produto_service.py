from app.database import produto_db


def adicionar_produto(
    codigo,
    nome,
    categoria,
    fornecedor,
    preco_custo,
    preco_venda,
    estoque,
    estoque_minimo
):

    return produto_db.adicionar_produto(
        codigo,
        nome,
        categoria,
        fornecedor,
        preco_custo,
        preco_venda,
        estoque,
        estoque_minimo
    )


def listar_produtos():

    return produto_db.listar_produtos()


def buscar_produto_por_codigo(codigo):

    return produto_db.buscar_produto_por_codigo(codigo)


def atualizar_produto(
    id_produto,
    codigo,
    nome,
    categoria,
    preco
):

    return produto_db.atualizar_produto(
        id_produto,
        codigo,
        nome,
        categoria,
        preco
    )


def excluir_produto(id_produto):

    return produto_db.excluir_produto(id_produto)