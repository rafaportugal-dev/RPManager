import sys

from PySide6.QtWidgets import QApplication

from app.views.dashboard import Dashboard
from app.styles.dark_theme import DARK_THEME

from app.database.connection import (
    criar_tabela_clientes,
    criar_tabela_produtos,
    criar_tabela_categorias
)


def main():
    # ==========================
    # CRIA AS TABELAS
    # ==========================

    criar_tabela_clientes()
    criar_tabela_produtos()
    criar_tabela_categorias()

    # ==========================
    # APLICAÇÃO
    # ==========================

    app = QApplication(sys.argv)

    app.setStyleSheet(DARK_THEME)

    janela = Dashboard()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()