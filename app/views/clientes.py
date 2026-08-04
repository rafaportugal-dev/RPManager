from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem
)

from app.database.connection import (
    adicionar_cliente,
    listar_clientes
)

class TelaClientes(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Clientes")
        self.resize(700, 600)

        layout = QVBoxLayout()

        # Nome
        layout.addWidget(QLabel("Nome"))
        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Digite o nome")
        layout.addWidget(self.nome)

        # CPF
        layout.addWidget(QLabel("CPF"))
        self.cpf = QLineEdit()
        self.cpf.setPlaceholderText("Digite o CPF")
        layout.addWidget(self.cpf)

        # Telefone
        layout.addWidget(QLabel("Telefone"))
        self.telefone = QLineEdit()
        self.telefone.setPlaceholderText("Digite o telefone")
        layout.addWidget(self.telefone)

        # E-mail
        layout.addWidget(QLabel("E-mail"))
        self.email = QLineEdit()
        self.email.setPlaceholderText("Digite o e-mail")
        layout.addWidget(self.email)

        # Endereço
        layout.addWidget(QLabel("Endereço"))
        self.endereco = QLineEdit()
        self.endereco.setPlaceholderText("Digite o endereço")
        layout.addWidget(self.endereco)

        # Botão Salvar
        self.botao = QPushButton("Salvar Cliente")
        self.botao.clicked.connect(self.salvar_cliente)
        layout.addWidget(self.botao)

        # -------------------------
        # TABELA DE CLIENTES
        # -------------------------

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(5)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Nome",
            "Telefone",
            "CPF",
            "E-mail"
        ])

        layout.addWidget(self.tabela)

        self.setLayout(layout)

        # Carrega os clientes cadastrados
        self.carregar_clientes()

    def carregar_clientes(self):

        clientes = listar_clientes()

        self.tabela.setRowCount(len(clientes))

        for linha, cliente in enumerate(clientes):

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(str(cliente[0]))
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(cliente[1])
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(cliente[2] or "")
            )

            self.tabela.setItem(
                linha,
                3,
                QTableWidgetItem(cliente[3] or "")
            )

            self.tabela.setItem(
                linha,
                4,
                QTableWidgetItem(cliente[4] or "")
            )

    def salvar_cliente(self):

        sucesso = adicionar_cliente(
            self.nome.text(),
            self.cpf.text(),
            self.telefone.text(),
            self.endereco.text(),
            self.email.text()
        )

        if sucesso:

            QMessageBox.information(
                self,
                "Sucesso",
                "Cliente cadastrado com sucesso!"
            )

            self.nome.clear()
            self.cpf.clear()
            self.telefone.clear()
            self.email.clear()
            self.endereco.clear()

            self.nome.setFocus()

            # Atualiza a tabela
            self.carregar_clientes()

        else:

            QMessageBox.warning(
                self,
                "Erro",
                "CPF ou e-mail já cadastrado."
            )