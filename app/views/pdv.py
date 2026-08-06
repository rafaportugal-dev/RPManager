from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from app.widgets.pdv.painel_cliente import PainelCliente
from app.widgets.pdv.painel_busca import PainelBusca
from app.widgets.pdv.painel_carrinho import PainelCarrinho
from app.widgets.pdv.painel_produto import PainelProduto
from app.widgets.pdv.painel_total import PainelTotal
from app.widgets.pdv.painel_pagamento import PainelPagamento
from app.controllers.pdv_controller import PDVController

class TelaPDV(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RP Manager PDV")

        layout_principal = QVBoxLayout(self)

        # ===============================
        # Cliente
        # ===============================

        self.painel_cliente = PainelCliente()
        layout_principal.addWidget(self.painel_cliente)

        # ===============================
        # Busca
        # ===============================

        self.painel_busca = PainelBusca()
        layout_principal.addWidget(self.painel_busca)

        # ===============================
        # Centro
        # ===============================

        centro = QHBoxLayout()

        self.painel_carrinho = PainelCarrinho()
        centro.addWidget(self.painel_carrinho, 4)

        direita = QVBoxLayout()

        self.painel_produto = PainelProduto()
        direita.addWidget(self.painel_produto)

        self.painel_total = PainelTotal()
        direita.addWidget(self.painel_total)

        self.painel_pagamento = PainelPagamento()
        direita.addWidget(self.painel_pagamento)

        centro.addLayout(direita, 2)

        layout_principal.addLayout(centro)
        self.controller = PDVController(self)