from app.database import categoria_db


def adicionar_categoria(nome):
    categoria_db.adicionar(nome)


def listar_categorias():
    return categoria_db.listar()


def atualizar_categoria(id_categoria, nome):
    categoria_db.atualizar(id_categoria, nome)


def excluir_categoria(id_categoria):
    categoria_db.excluir(id_categoria)