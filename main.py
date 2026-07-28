import sys

from PySide6.QtWidgets import QApplication
from app.views.dashboard import Dashboard
from app.styles.dark_theme import DARK_THEME
app = QApplication(sys.argv)
app.setStyleSheet(DARK_THEME)
janela = Dashboard()
janela.show()

sys.exit(app.exec())
