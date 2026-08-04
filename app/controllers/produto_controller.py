from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from app.services.produto_service import (
    adicionar_produto,
    listar_produtos,
    atualizar_produto,
    excluir_produto
)


class ProdutoController:

    def __init__(self, view):

        self.view = view
        self.id_produto = None

        self.view.salvar.clicked.connect(self.salvar)
        self.view.editar.clicked.connect(self.editar)
        self.view.excluir.clicked.connect(self.excluir)

        self.view.tabela.cellClicked.connect(self.selecionar)

        self.carregar()

    # =====================================

    def carregar(self):

        produtos = listar_produtos()

        self.view.tabela.setRowCount(len(produtos))

        for linha, produto in enumerate(produtos):

            for coluna, valor in enumerate(produto):

                if coluna == 4:
                    texto = f"R$ {float(valor):,.2f}"
                    texto = texto.replace(",", "X")
                    texto = texto.replace(".", ",")
                    texto = texto.replace("X", ".")
                else:
                    texto = str(valor)

                self.view.tabela.setItem(
                    linha,
                    coluna,
                    QTableWidgetItem(texto)
                )

    # =====================================

    def salvar(self):

        try:

            adicionar_produto(
                self.view.codigo.text(),
                self.view.nome.text(),
                self.view.categoria.currentText(),
                "",
                0,
                float(self.view.preco.text().replace(",", ".")),
                0,
                0
            )

            QMessageBox.information(
                self.view,
                "Sucesso",
                "Produto cadastrado."
            )

            self.limpar()

            self.carregar()

        except Exception as erro:

            QMessageBox.critical(
                self.view,
                "Erro",
                str(erro)
            )

    # =====================================

    def selecionar(self, linha, coluna):

        self.id_produto = int(
            self.view.tabela.item(linha, 0).text()
        )

        self.view.codigo.setText(
            self.view.tabela.item(linha, 1).text()
        )

        self.view.nome.setText(
            self.view.tabela.item(linha, 2).text()
        )

        categoria = self.view.tabela.item(linha, 3).text()

        indice = self.view.categoria.findText(categoria)

        if indice >= 0:
            self.view.categoria.setCurrentIndex(indice)

        preco = self.view.tabela.item(linha, 4).text()

        preco = (
            preco.replace("R$", "")
                 .replace(".", "")
                 .replace(",", ".")
                 .strip()
        )

        self.view.preco.setText(preco)

    # =====================================

    def editar(self):

        if self.id_produto is None:
            return

        atualizar_produto(
            self.id_produto,
            self.view.codigo.text(),
            self.view.nome.text(),
            self.view.categoria.currentText(),
            float(self.view.preco.text().replace(",", "."))
        )

        QMessageBox.information(
            self.view,
            "Sucesso",
            "Produto atualizado."
        )

        self.limpar()

        self.carregar()

    # =====================================

    def excluir(self):

        if self.id_produto is None:
            return

        resposta = QMessageBox.question(
            self.view,
            "Excluir",
            "Deseja excluir este produto?"
        )

        if resposta == QMessageBox.Yes:

            excluir_produto(self.id_produto)

            QMessageBox.information(
                self.view,
                "Sucesso",
                "Produto excluído."
            )

            self.limpar()

            self.carregar()

    # =====================================

    def limpar(self):

        self.id_produto = None

        self.view.codigo.clear()
        self.view.nome.clear()
        self.view.preco.clear()

        self.view.categoria.setCurrentIndex(0)

        self.view.codigo.setFocus()