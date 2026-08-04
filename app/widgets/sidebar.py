from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        titulo = QLabel("RP Manager")
        titulo.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            padding:15px;
        """)

        self.layout.addWidget(titulo)

        self.botoes = []

    def adicionar_botao(self, texto):

        botao = QPushButton(texto)

        botao.setMinimumHeight(45)

        self.layout.addWidget(botao)

        self.botoes.append(botao)

        return botao

    def finalizar(self):

        self.layout.addStretch()

        versao = QLabel("Versão 0.4")
        self.layout.addWidget(versao)