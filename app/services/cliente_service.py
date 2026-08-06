from app.database import cliente_db


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
    return cliente_db.adicionar_cliente(
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


def listar_clientes():
    return cliente_db.listar_clientes()


def buscar_cliente(id_cliente):
    return cliente_db.buscar_cliente(id_cliente)


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
    cliente_db.atualizar_cliente(
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
    )


def excluir_cliente(id_cliente):
    cliente_db.excluir_cliente(id_cliente)