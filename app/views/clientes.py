from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
)


class Clientes(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Cadastro de Clientes"))

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome")

        self.telefone = QLineEdit()
        self.telefone.setPlaceholderText("Telefone")

        self.cpf = QLineEdit()
        self.cpf.setPlaceholderText("CPF")

        self.email = QLineEdit()
        self.email.setPlaceholderText("E-mail")

        botao = QPushButton("Salvar")

        layout.addWidget(self.nome)
        layout.addWidget(self.telefone)
        layout.addWidget(self.cpf)
        layout.addWidget(self.email)
        layout.addWidget(botao)

        self.setLayout(layout)