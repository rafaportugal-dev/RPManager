from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QComboBox,
    QHeaderView
)

from app.controllers.produto_controller import ProdutoController


class TelaProdutos(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Produtos")

        layout = QVBoxLayout()

        # ==========================
        # TÍTULO
        # ==========================

        titulo = QLabel("📦 Cadastro de Produtos")
        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(titulo)

        # ==========================
        # PESQUISA
        # ==========================

        pesquisa_layout = QHBoxLayout()

        pesquisa_layout.addWidget(QLabel("🔍 Pesquisar"))

        self.pesquisa = QLineEdit()
        self.pesquisa.setPlaceholderText("Nome ou código")

        pesquisa_layout.addWidget(self.pesquisa)

        layout.addLayout(pesquisa_layout)

        # ==========================
        # CAMPOS
        # ==========================

        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código de barras")

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome do produto")

        self.categoria = QComboBox()
        self.categoria.addItems([
            "Capinhas",
            "Películas",
            "Carregadores",
            "Cabos",
            "Perfumes",
            "Outros"
        ])

        self.preco = QLineEdit()
        self.preco.setPlaceholderText("Preço")

        layout.addWidget(self.codigo)
        layout.addWidget(self.nome)
        layout.addWidget(self.categoria)
        layout.addWidget(self.preco)

        # ==========================
        # BOTÕES
        # ==========================

        botoes = QHBoxLayout()

        self.salvar = QPushButton("💾 Salvar")
        self.editar = QPushButton("✏ Editar")
        self.excluir = QPushButton("🗑 Excluir")

        botoes.addWidget(self.salvar)
        botoes.addWidget(self.editar)
        botoes.addWidget(self.excluir)

        layout.addLayout(botoes)

        # ==========================
        # TABELA
        # ==========================

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(5)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Código",
            "Produto",
            "Categoria",
            "Preço"
        ])

        header = self.tabela.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.Stretch
        )

        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            4,
            QHeaderView.ResizeToContents
        )

        layout.addWidget(self.tabela)

        self.setLayout(layout)

        # ==========================
        # CONTROLLER
        # ==========================

        self.controller = ProdutoController(self)