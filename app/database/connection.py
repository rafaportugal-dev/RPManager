import sqlite3
import os

# ==========================
# CAMINHO DO BANCO
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_NAME = os.path.join(BASE_DIR, "rpmanager.db")


def conectar():
    print(f"Banco utilizado: {DB_NAME}")
    return sqlite3.connect(DB_NAME)


# ==========================
# CLIENTES
# ==========================

def criar_tabela_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        whatsapp TEXT,
        cpf TEXT UNIQUE,
        email TEXT UNIQUE,
        data_nascimento TEXT,
        endereco TEXT,
        cidade TEXT,
        cep TEXT,
        aceita_promocoes INTEGER DEFAULT 1,
        observacoes TEXT,
        data_cadastro TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# PRODUTOS
# ==========================

def criar_tabela_produtos():
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


# ==========================
# CATEGORIAS
# ==========================

def criar_tabela_categorias():
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