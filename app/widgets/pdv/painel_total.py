from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QGridLayout
)

from PySide6.QtCore import Qt


class PainelTotal(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("painelTotal")

        self.setStyleSheet("""
        #painelTotal{
            background:#202225;
            border:1px solid #3f4147;
            border-radius:12px;
            padding:15px;
        }

        QLabel{
            color:white;
        }
        """)

        layout = QVBoxLayout(self)

        titulo = QLabel("💰 Resumo da Venda")

        titulo.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        layout.addWidget(titulo)

        grid = QGridLayout()

        grid.addWidget(QLabel("Subtotal"),0,0)
        self.lbl_subtotal = QLabel("R$ 0,00")
        grid.addWidget(self.lbl_subtotal,0,1)

        grid.addWidget(QLabel("Desconto"),1,0)
        self.lbl_desconto = QLabel("R$ 0,00")
        grid.addWidget(self.lbl_desconto,1,1)

        grid.addWidget(QLabel("Cashback"),2,0)
        self.lbl_cashback = QLabel("R$ 0,00")
        grid.addWidget(self.lbl_cashback,2,1)

        layout.addLayout(grid)

        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        layout.addWidget(linha)

        total = QLabel("TOTAL")
        total.setAlignment(Qt.AlignCenter)

        total.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(total)

        self.lbl_total = QLabel("R$ 0,00")

        self.lbl_total.setAlignment(Qt.AlignCenter)

        self.lbl_total.setStyleSheet("""
            font-size:36px;
            font-weight:bold;
            color:#00d084;
        """)

        layout.addWidget(self.lbl_total)