from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
    QHeaderView
)

from app.controllers.cliente_controller import ClienteController


class SelecionarCliente(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecionar Cliente")
        self.resize(800, 500)

        self.cliente_selecionado = None

        layout = QVBoxLayout(self)

        titulo = QLabel("🔍 Selecionar Cliente")
        titulo.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            padding:10px;
        """)

        layout.addWidget(titulo)

        self.busca = QLineEdit()
        self.busca.setPlaceholderText(
            "Digite o nome, telefone ou WhatsApp..."
        )

        layout.addWidget(self.busca)

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(5)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Nome",
            "Telefone",
            "WhatsApp",
            "Cidade"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(self.tabela)

        botoes = QHBoxLayout()

        self.btn_selecionar = QPushButton("Selecionar")
        self.btn_cancelar = QPushButton("Cancelar")

        botoes.addStretch()
        botoes.addWidget(self.btn_selecionar)
        botoes.addWidget(self.btn_cancelar)

        layout.addLayout(botoes)

        self.carregar()

        self.busca.textChanged.connect(self.filtrar)

        self.btn_cancelar.clicked.connect(self.reject)

        self.btn_selecionar.clicked.connect(self.selecionar)

        self.tabela.doubleClicked.connect(self.selecionar)

    # ======================================

    def carregar(self):

        self.clientes = ClienteController.listar()

        self.preencher(self.clientes)

    # ======================================

    def preencher(self, dados):

        self.tabela.setRowCount(len(dados))

        for linha, cliente in enumerate(dados):

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(str(cliente[0]))
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(cliente[1] or "")
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
                QTableWidgetItem(cliente[8] or "")
            )

    # ======================================

    def filtrar(self):

        texto = self.busca.text().lower()

        filtrados = []

        for cliente in self.clientes:

            nome = (cliente[1] or "").lower()
            telefone = (cliente[2] or "").lower()
            whatsapp = (cliente[3] or "").lower()

            if (
                texto in nome
                or texto in telefone
                or texto in whatsapp
            ):
                filtrados.append(cliente)

        self.preencher(filtrados)

    # ======================================

    def selecionar(self):

        linha = self.tabela.currentRow()

        if linha < 0:
            return

        self.cliente_selecionado = {
            "id": self.tabela.item(linha, 0).text(),
            "nome": self.tabela.item(linha, 1).text(),
            "telefone": self.tabela.item(linha, 2).text(),
            "whatsapp": self.tabela.item(linha, 3).text(),
            "cidade": self.tabela.item(linha, 4).text(),
        }

        self.accept()