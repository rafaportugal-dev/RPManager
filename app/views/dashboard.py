from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel
)

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RP Manager")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        principal = QHBoxLayout()
        central.setLayout(principal)

        menu = QVBoxLayout()

        titulo = QLabel("RP Manager")
        menu.addWidget(titulo)

        menu.addWidget(QPushButton("🏠 Dashboard"))
        menu.addWidget(QPushButton("👤 Clientes"))
        menu.addWidget(QPushButton("📱 Aparelhos"))
        menu.addWidget(QPushButton("📄 Ordem de Serviço"))
        menu.addWidget(QPushButton("📦 Estoque"))
        menu.addWidget(QPushButton("💰 Financeiro"))
        menu.addWidget(QPushButton("📊 Relatórios"))

        menu.addStretch()

        conteudo = QVBoxLayout()

        conteudo.addWidget(QLabel("Bem-vindo ao RP Manager"))
        conteudo.addWidget(QLabel("Sistema para Assistência Técnica"))

        principal.addLayout(menu, 1)
        principal.addLayout(conteudo, 4)