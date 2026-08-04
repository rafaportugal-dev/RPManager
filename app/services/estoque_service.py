from app.database.connection import conectar


def listar_estoque():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            produtos.id,
            produtos.codigo,
            produtos.nome,
            produtos.categoria,
            produtos.estoque,
            produtos.estoque_minimo
        FROM produtos
        ORDER BY produtos.nome
    """)

    dados = cursor.fetchall()

    conn.close()

    return dados


def atualizar_estoque(
    id_produto,
    estoque,
    estoque_minimo
):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE produtos
        SET
            estoque=?,
            estoque_minimo=?
        WHERE id=?
    """, (
        estoque,
        estoque_minimo,
        id_produto
    ))

    conn.commit()
    conn.close()