from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class PainelBusca(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("painelBusca")

        self.setStyleSheet("""
        #painelBusca{
            background:#2b2d31;
            border:1px solid #3f4147;
            border-radius:12px;
            padding:10px;
        }

        QLabel{
            color:white;
            font-size:15px;
            font-weight:bold;
        }

        QLineEdit{
            min-height:50px;
            font-size:24px;
            border-radius:10px;
            padding-left:15px;
            font-weight:bold;
        }

        QPushButton{
            min-height:50px;
            min-width:150px;
            border-radius:10px;
            font-size:16px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#3d4046;
        }
        """)

        layout = QVBoxLayout(self)

        titulo = QLabel("📦 Leitura do Produto")
        layout.addWidget(titulo)

        linha = QHBoxLayout()

        self.txt_codigo = QLineEdit()
        self.txt_codigo.setPlaceholderText(
            "Bipe ou digite o código de barras"
        )

        self.btn_adicionar = QPushButton("➕ Adicionar")

        linha.addWidget(self.txt_codigo)
        linha.addWidget(self.btn_adicionar)

        layout.addLayout(linha)

        self.lbl_status = QLabel(
            "Aguardando leitura..."
        )

        self.lbl_status.setAlignment(Qt.AlignLeft)

        self.lbl_status.setStyleSheet("""
            color:#00d084;
            font-size:13px;
        """)

        layout.addWidget(self.lbl_status)

        self.txt_codigo.setFocus()