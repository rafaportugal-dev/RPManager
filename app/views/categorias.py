from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QHeaderView
)

from app.controllers.categoria_controller import CategoriaController


class TelaCategorias(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Categorias")

        layout = QVBoxLayout()

        # ==========================
        # TÍTULO
        # ==========================

        titulo = QLabel("📂 Cadastro de Categorias")

        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(titulo)

        # ==========================
        # CAMPO
        # ==========================

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome da categoria")

        layout.addWidget(self.nome)

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

        self.tabela.setColumnCount(2)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Categoria"
        ])

        header = self.tabela.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.Stretch
        )

        layout.addWidget(self.tabela)

        self.setLayout(layout)

        # ==========================
        # CONTROLLER
        # ==========================

        self.controller = CategoriaController(self)