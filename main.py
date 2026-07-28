import sys

from PySide6.QtWidgets import QApplication
from app.views.dashboard import Dashboard

app = QApplication(sys.argv)

janela = Dashboard()
janela.show()

sys.exit(app.exec())
