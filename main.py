import sys

from PySide6.QtWidgets import QApplication

from app.views.dashboard import Dashboard
from app.styles.dark_theme import DARK_THEME
from app.database.connection import (
    criar_tabelas,
    criar_tabela_produtos
)


def main():
    # Cria as tabelas do banco de dados
    criar_tabelas()
    criar_tabela_produtos()

    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME)

    janela = Dashboard()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()