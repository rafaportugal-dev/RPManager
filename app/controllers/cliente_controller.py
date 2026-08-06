from app.services import cliente_service


class ClienteController:

    @staticmethod
    def adicionar(
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
        return cliente_service.adicionar_cliente(
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

    @staticmethod
    def listar():
        return cliente_service.listar_clientes()

    @staticmethod
    def buscar(id_cliente):
        return cliente_service.buscar_cliente(id_cliente)

    @staticmethod
    def atualizar(
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
        cliente_service.atualizar_cliente(
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

    @staticmethod
    def excluir(id_cliente):
        cliente_service.excluir_cliente(id_cliente)