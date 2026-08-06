from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem,
    QHBoxLayout
)


class PainelCarrinho(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("painelCarrinho")

        self.setStyleSheet("""
        #painelCarrinho{
            background:#2b2d31;
            border:1px solid #3f4147;
            border-radius:12px;
            padding:10px;
        }

        QLabel{
            color:white;
            font-size:16px;
            font-weight:bold;
        }

        QTableWidget{
            background:#202225;
            border:none;
            gridline-color:#3f4147;
            font-size:14px;
        }

        QHeaderView::section{
            background:#36393f;
            color:white;
            padding:8px;
            border:none;
            font-weight:bold;
        }
        """)

        layout = QVBoxLayout(self)

        titulo = QLabel("🛒 Carrinho")
        layout.addWidget(titulo)

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(6)

        self.tabela.setHorizontalHeaderLabels([
            "Código",
            "Produto",
            "Qtd",
            "Unitário",
            "Desc.",
            "Total"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.tabela.verticalHeader().setVisible(False)

        self.tabela.setAlternatingRowColors(True)

        layout.addWidget(self.tabela)

        rodape = QHBoxLayout()

        self.lbl_itens = QLabel("Itens: 0")
        self.lbl_quantidade = QLabel("Quantidade: 0")
        self.lbl_lucro = QLabel("Lucro: R$ 0,00")
        self.lbl_subtotal = QLabel("Subtotal: R$ 0,00")

        rodape.addWidget(self.lbl_itens)
        rodape.addSpacing(20)
        rodape.addWidget(self.lbl_quantidade)
        rodape.addStretch()
        rodape.addWidget(self.lbl_lucro)
        rodape.addSpacing(20)
        rodape.addWidget(self.lbl_subtotal)

        layout.addLayout(rodape)

    # =========================================================

    def adicionar_item(
        self,
        codigo,
        produto,
        quantidade,
        valor,
        desconto,
        total
    ):

        # Verifica se o produto já existe

        for linha in range(self.tabela.rowCount()):

            codigo_existente = self.tabela.item(linha, 0).text()

            if codigo_existente == str(codigo):

                qtd = int(self.tabela.item(linha, 2).text())

                qtd += quantidade

                novo_total = qtd * valor - desconto

                self.tabela.item(linha, 2).setText(str(qtd))

                self.tabela.item(
                    linha,
                    5
                ).setText(f"R$ {novo_total:.2f}")

                self.atualizar_resumo()

                return

        # Produto novo

        linha = self.tabela.rowCount()

        self.tabela.insertRow(linha)

        self.tabela.setItem(
            linha,
            0,
            QTableWidgetItem(str(codigo))
        )

        self.tabela.setItem(
            linha,
            1,
            QTableWidgetItem(produto)
        )

        self.tabela.setItem(
            linha,
            2,
            QTableWidgetItem(str(quantidade))
        )

        self.tabela.setItem(
            linha,
            3,
            QTableWidgetItem(f"R$ {valor:.2f}")
        )

        self.tabela.setItem(
            linha,
            4,
            QTableWidgetItem(f"R$ {desconto:.2f}")
        )

        self.tabela.setItem(
            linha,
            5,
            QTableWidgetItem(f"R$ {total:.2f}")
        )

        self.atualizar_resumo()

    # =========================================================

    def atualizar_resumo(self):

        itens = self.tabela.rowCount()

        quantidade = 0

        subtotal = 0

        for linha in range(itens):

            quantidade += int(
                self.tabela.item(linha, 2).text()
            )

            valor = (
                self.tabela.item(linha, 5)
                .text()
                .replace("R$", "")
                .strip()
            )

            subtotal += float(valor)

        self.lbl_itens.setText(
            f"Itens: {itens}"
        )

        self.lbl_quantidade.setText(
            f"Quantidade: {quantidade}"
        )

        self.lbl_subtotal.setText(
            f"Subtotal: R$ {subtotal:.2f}"
        )