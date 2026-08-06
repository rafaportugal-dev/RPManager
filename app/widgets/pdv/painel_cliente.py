from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)


class PainelCliente(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("painelCliente")

        self.setStyleSheet("""
        #painelCliente{
            background-color:#2b2d31;
            border:1px solid #3f4147;
            border-radius:12px;
            padding:10px;
        }

        QLabel{
            font-size:15px;
            font-weight:bold;
            color:white;
        }

        QLineEdit{
            min-height:38px;
            border-radius:8px;
            padding-left:10px;
            font-size:14px;
        }

        QPushButton{
            min-height:38px;
            border-radius:8px;
            font-size:14px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#3a3d42;
        }
        """)

        layout = QVBoxLayout(self)

        titulo = QLabel("👤 Cliente")
        layout.addWidget(titulo)

        linha = QHBoxLayout()

        self.txt_cliente = QLineEdit()
        self.txt_cliente.setPlaceholderText("Pesquisar cliente pelo nome ou telefone")

        self.btn_buscar = QPushButton("🔍 Buscar")

        self.btn_novo = QPushButton("➕ Novo")

        linha.addWidget(self.txt_cliente, 5)
        linha.addWidget(self.btn_buscar)
        linha.addWidget(self.btn_novo)

        layout.addLayout(linha)

        self.lbl_info = QLabel(
            "Nenhum cliente selecionado"
        )

        self.lbl_info.setStyleSheet("""
            color:#00d084;
            font-size:13px;
            font-weight:normal;
        """)

        layout.addWidget(self.lbl_info)