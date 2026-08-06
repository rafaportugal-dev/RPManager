from PySide6.QtWidgets import (
    QFrame,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QGridLayout
)


class PainelPagamento(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("painelPagamento")

        self.setStyleSheet("""
        #painelPagamento{
            background:#2b2d31;
            border:1px solid #3f4147;
            border-radius:12px;
            padding:10px;
        }

        QPushButton{
            min-height:55px;
            font-size:15px;
            font-weight:bold;
            border-radius:10px;
        }

        QPushButton:hover{
            background:#40444b;
        }

        QLabel{
            color:white;
            font-size:18px;
            font-weight:bold;
        }
        """)

        layout = QVBoxLayout(self)

        titulo = QLabel("💳 Pagamento")

        layout.addWidget(titulo)

        grid = QGridLayout()

        self.btn_pix = QPushButton("💚 PIX")
        self.btn_dinheiro = QPushButton("💵 Dinheiro")
        self.btn_debito = QPushButton("💳 Débito")
        self.btn_credito = QPushButton("💳 Crédito")
        self.btn_misto = QPushButton("🔀 Misto")
        self.btn_finalizar = QPushButton("✅ Finalizar Venda")

        grid.addWidget(self.btn_pix,0,0)
        grid.addWidget(self.btn_dinheiro,0,1)

        grid.addWidget(self.btn_debito,1,0)
        grid.addWidget(self.btn_credito,1,1)

        grid.addWidget(self.btn_misto,2,0,1,2)

        grid.addWidget(self.btn_finalizar,3,0,1,2)

        layout.addLayout(grid)