from app.database.connection import conectar
import sqlite3


def adicionar_cliente(
    nome,
    telefone,
    whatsapp,
    cpf,
    email,
    data_nascimento,
    endereco,
    cidade,
    cep,
    aceita_promocoes,
    observacoes
):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO clientes (
                nome,
                telefone,
                whatsapp,
                cpf,
                email,
                data_nascimento,
                endereco,
                cidade,
                cep,
                aceita_promocoes,
                observacoes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            nome,
            telefone,
            whatsapp,
            cpf,
            email,
            data_nascimento,
            endereco,
            cidade,
            cep,
            aceita_promocoes,
            observacoes
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            telefone,
            whatsapp,
            cpf,
            email,
            data_nascimento,
            endereco,
            cidade,
            cep,
            aceita_promocoes,
            observacoes,
            data_cadastro
        FROM clientes
        ORDER BY nome
    """)

    dados = cursor.fetchall()

    conn.close()

    return dados


def buscar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM clientes
        WHERE id = ?
    """, (id_cliente,))

    cliente = cursor.fetchone()

    conn.close()

    return cliente


def atualizar_cliente(
    id_cliente,
    nome,
    telefone,
    whatsapp,
    cpf,
    email,
    data_nascimento,
    endereco,
    cidade,
    cep,
    aceita_promocoes,
    observacoes
):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE clientes
        SET
            nome=?,
            telefone=?,
            whatsapp=?,
            cpf=?,
            email=?,
            data_nascimento=?,
            endereco=?,
            cidade=?,
            cep=?,
            aceita_promocoes=?,
            observacoes=?
        WHERE id=?
    """, (
        nome,
        telefone,
        whatsapp,
        cpf,
        email,
        data_nascimento,
        endereco,
        cidade,
        cep,
        aceita_promocoes,
        observacoes,
        id_cliente
    ))

    conn.commit()
    conn.close()


def excluir_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM clientes
        WHERE id=?
    """, (id_cliente,))

    conn.commit()
    conn.close()