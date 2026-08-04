from app.database.connection import conectar


def criar_tabela():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def adicionar(nome):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO categorias(nome)
        VALUES(?)
    """, (nome,))

    conn.commit()
    conn.close()


def listar():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome
        FROM categorias
        ORDER BY nome
    """)

    dados = cursor.fetchall()

    conn.close()

    return dados


def atualizar(id_categoria, nome):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE categorias
        SET nome=?
        WHERE id=?
    """, (
        nome,
        id_categoria
    ))

    conn.commit()
    conn.close()


def excluir(id_categoria):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM categorias
        WHERE id=?
    """, (id_categoria,))

    conn.commit()
    conn.close()