import sqlite3

# Nome do banco de dados
DB_NAME = "rpmanager.db"


def conectar():
    """Cria uma conexão com o banco de dados."""
    return sqlite3.connect(DB_NAME)


def criar_tabelas():
    """Cria a tabela de clientes caso ela não exista."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        cpf TEXT UNIQUE,
        email TEXT UNIQUE,
        endereco TEXT,
        data_cadastro TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def adicionar_cliente(nome, cpf, telefone, endereco, email):
    """Adiciona um cliente ao banco."""
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO clientes
        (nome, cpf, telefone, endereco, email)
        VALUES (?, ?, ?, ?, ?)
        """, (nome, cpf, telefone, endereco, email))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        print("Erro: CPF ou e-mail já cadastrado.")
        return False

    finally:
        conn.close()


def listar_clientes():
    """Lista todos os clientes."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, nome, telefone, cpf, email, endereco, data_cadastro
    FROM clientes
    ORDER BY nome
    """)

    clientes = cursor.fetchall()

    conn.close()

    return clientes


def buscar_cliente(cpf):
    """Busca um cliente pelo CPF."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM clientes
    WHERE cpf = ?
    """, (cpf,))

    cliente = cursor.fetchone()

    conn.close()

    return cliente


def atualizar_cliente(id_cliente, nome, cpf, telefone, endereco, email):
    """Atualiza os dados de um cliente."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE clientes
    SET nome = ?,
        cpf = ?,
        telefone = ?,
        endereco = ?,
        email = ?
    WHERE id = ?
    """, (nome, cpf, telefone, endereco, email, id_cliente))

    conn.commit()
    conn.close()


def excluir_cliente(id_cliente):
    """Exclui um cliente."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM clientes
    WHERE id = ?
    """, (id_cliente,))

    conn.commit()
    conn.close()

def criar_tabela_produtos():
    """Cria a tabela de produtos."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE,
        nome TEXT NOT NULL,
        categoria TEXT,
        fornecedor TEXT,
        preco_custo REAL,
        preco_venda REAL,
        estoque INTEGER DEFAULT 0,
        estoque_minimo INTEGER DEFAULT 0,
        data_cadastro TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()