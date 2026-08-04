from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QComboBox
)
from PySide6.QtCore import Qt


class TelaVendas(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vendas")
        self.resize(900, 600)

        layout = QVBoxLayout()

        titulo = QLabel("🛒 Nova Venda")
        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(titulo)

        # Código de barras
        codigo_layout = QHBoxLayout()

        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código de barras")

        self.btn_bipar = QPushButton("📷 Bipar")

        codigo_layout.addWidget(self.codigo)
        codigo_layout.addWidget(self.btn_bipar)

        layout.addLayout(codigo_layout)

        # Buscar produto
        self.buscar = QLineEdit()
        self.buscar.setPlaceholderText("Buscar produto")

        layout.addWidget(self.buscar)

        # Tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)

        self.tabela.setHorizontalHeaderLabels([
            "Produto",
            "Quantidade",
            "Valor",
            "Total"
        ])

        layout.addWidget(self.tabela)

        # Total
        self.total = QLabel("Total: R$ 0,00")

        self.total.setAlignment(Qt.AlignRight)

        self.total.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:#00d084;
        """)

        layout.addWidget(self.total)

        # Pagamento
        pagamento = QHBoxLayout()

        pagamento.addWidget(QLabel("Pagamento"))

        self.forma = QComboBox()

        self.forma.addItems([
            "PIX",
            "Dinheiro",
            "Cartão Débito",
            "Cartão Crédito"
        ])

        pagamento.addWidget(self.forma)

        layout.addLayout(pagamento)

        # Botões
        botoes = QHBoxLayout()

        self.finalizar = QPushButton("Finalizar Venda")
        self.cancelar = QPushButton("Cancelar")

        botoes.addWidget(self.finalizar)
        botoes.addWidget(self.cancelar)

        layout.addLayout(botoes)

        self.setLayout(layout)