import sys

from PySide6.QtWidgets import QApplication

from app.views.dashboard import Dashboard
from app.styles.dark_theme import DARK_THEME
from app.database.connection import criar_tabelas

# Cria o banco de dados e as tabelas (caso ainda não existam)
criar_tabelas()

app = QApplication(sys.argv)
app.setStyleSheet(DARK_THEME)

janela = Dashboard()
janela.show()

sys.exit(app.exec())