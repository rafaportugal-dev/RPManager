from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class PainelProduto(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("painelProduto")

        self.setStyleSheet("""
        #painelProduto{
            background:#2b2d31;
            border:1px solid #3f4147;
            border-radius:12px;
            padding:10px;
        }

        QLabel{
            color:white;
        }
        """)

        layout = QVBoxLayout(self)

        titulo = QLabel("📦 Produto")

        titulo.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(titulo)

        self.lbl_foto = QLabel("SEM FOTO")

        self.lbl_foto.setAlignment(Qt.AlignCenter)

        self.lbl_foto.setFixedHeight(220)

        self.lbl_foto.setStyleSheet("""
            border:2px dashed gray;
            font-size:18px;
            color:gray;
        """)

        layout.addWidget(self.lbl_foto)

        self.lbl_nome = QLabel("Produto")

        self.lbl_nome.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        layout.addWidget(self.lbl_nome)

        self.lbl_codigo = QLabel("Código:")
        layout.addWidget(self.lbl_codigo)

        self.lbl_categoria = QLabel("Categoria:")
        layout.addWidget(self.lbl_categoria)

        self.lbl_fornecedor = QLabel("Fornecedor:")
        layout.addWidget(self.lbl_fornecedor)

        self.lbl_estoque = QLabel("Estoque:")
        layout.addWidget(self.lbl_estoque)

        self.lbl_custo = QLabel("Custo:")
        layout.addWidget(self.lbl_custo)

        self.lbl_preco = QLabel("Venda:")
        layout.addWidget(self.lbl_preco)

        self.lbl_lucro = QLabel("Lucro:")
        layout.addWidget(self.lbl_lucro)

        layout.addStretch()