from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from app.services.categoria_service import (
    adicionar_categoria,
    listar_categorias,
    atualizar_categoria,
    excluir_categoria
)


class CategoriaController:

    def __init__(self, view):

        self.view = view
        self.id_categoria = None

        self.view.salvar.clicked.connect(self.salvar)
        self.view.editar.clicked.connect(self.editar)
        self.view.excluir.clicked.connect(self.excluir)

        self.view.tabela.cellClicked.connect(self.selecionar)

        self.carregar()

    # ==============================

    def carregar(self):

        categorias = listar_categorias()

        self.view.tabela.setRowCount(len(categorias))

        for linha, categoria in enumerate(categorias):

            self.view.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(str(categoria[0]))
            )

            self.view.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(categoria[1])
            )

    # ==============================

    def salvar(self):

        try:

            adicionar_categoria(
                self.view.nome.text()
            )

            QMessageBox.information(
                self.view,
                "Sucesso",
                "Categoria cadastrada."
            )

            self.view.nome.clear()

            self.carregar()

        except Exception as erro:

            QMessageBox.critical(
                self.view,
                "Erro",
                str(erro)
            )

    # ==============================

    def selecionar(self, linha, coluna):

        self.id_categoria = int(
            self.view.tabela.item(linha, 0).text()
        )

        self.view.nome.setText(
            self.view.tabela.item(linha, 1).text()
        )

    # ==============================

    def editar(self):

        if self.id_categoria is None:
            return

        atualizar_categoria(
            self.id_categoria,
            self.view.nome.text()
        )

        QMessageBox.information(
            self.view,
            "Sucesso",
            "Categoria atualizada."
        )

        self.view.nome.clear()

        self.carregar()

    # ==============================

    def excluir(self):

        if self.id_categoria is None:
            return

        resposta = QMessageBox.question(
            self.view,
            "Excluir",
            "Deseja excluir esta categoria?"
        )

        if resposta == QMessageBox.Yes:

            excluir_categoria(
                self.id_categoria
            )

            self.view.nome.clear()

            self.carregar()