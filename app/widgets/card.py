from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class Card(QFrame):

    def __init__(self, titulo, valor, emoji="📌"):
        super().__init__()

        self.setMinimumSize(220, 120)

        self.setStyleSheet("""
            QFrame {
                background-color: #2F3136;
                border: 1px solid #3f3f3f;
                border-radius: 12px;
            }

            QLabel {
                color: white;
                border: none;
                background: transparent;
            }
        """)

        layout = QVBoxLayout()

        self.lbl_titulo = QLabel(f"{emoji}  {titulo}")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        self.lbl_titulo.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
        """)

        self.lbl_valor = QLabel(str(valor))
        self.lbl_valor.setAlignment(Qt.AlignCenter)
        self.lbl_valor.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:#00d084;
        """)

        layout.addWidget(self.lbl_titulo)
        layout.addStretch()
        layout.addWidget(self.lbl_valor)

        self.setLayout(layout)