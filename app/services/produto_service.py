from app.database.connection import conectar


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

    conn = conectar()

    try:

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO produtos(
                codigo,
                nome,
                categoria,
                fornecedor,
                preco_custo,
                preco_venda,
                estoque,
                estoque_minimo
            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            codigo,
            nome,
            categoria,
            fornecedor,
            preco_custo,
            preco_venda,
            estoque,
            estoque_minimo
        ))

        conn.commit()

    finally:

        conn.close()


def listar_produtos():

    conn = conectar()

    try:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                codigo,
                nome,
                categoria,
                preco_venda
            FROM produtos
            ORDER BY nome
        """)

        return cursor.fetchall()

    finally:

        conn.close()


def atualizar_produto(
    id_produto,
    codigo,
    nome,
    categoria,
    preco
):

    conn = conectar()

    try:

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE produtos
            SET
                codigo=?,
                nome=?,
                categoria=?,
                preco_venda=?
            WHERE id=?
        """, (
            codigo,
            nome,
            categoria,
            preco,
            id_produto
        ))

        conn.commit()

    finally:

        conn.close()


def excluir_produto(id_produto):

    conn = conectar()

    try:

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM produtos WHERE id=?",
            (id_produto,)
        )

        conn.commit()

    finally:

        conn.close()