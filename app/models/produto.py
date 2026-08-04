from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem
)


class TelaProdutos(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Produtos")

        layout = QVBoxLayout()

        titulo = QLabel("📦 Cadastro de Produtos")
        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(titulo)

        # Pesquisa
        busca = QHBoxLayout()

        self.pesquisa = QLineEdit()
        self.pesquisa.setPlaceholderText("Pesquisar produto...")

        self.btn_buscar = QPushButton("🔍 Buscar")

        busca.addWidget(self.pesquisa)
        busca.addWidget(self.btn_buscar)

        layout.addLayout(busca)

        # Tabela
        self.tabela = QTableWidget()

        self.tabela.setColumnCount(6)

        self.tabela.setHorizontalHeaderLabels([
            "Código",
            "Produto",
            "Categoria",
            "Preço",
            "Estoque",
            "Fornecedor"
        ])

        layout.addWidget(self.tabela)

        # Botões
        botoes = QHBoxLayout()

        self.btn_novo = QPushButton("➕ Novo Produto")
        self.btn_editar = QPushButton("✏ Editar")
        self.btn_excluir = QPushButton("🗑 Excluir")

        botoes.addWidget(self.btn_novo)
        botoes.addWidget(self.btn_editar)
        botoes.addWidget(self.btn_excluir)

        layout.addLayout(botoes)

        self.setLayout(layout)