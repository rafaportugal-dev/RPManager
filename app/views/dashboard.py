from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from app.views.clientes import Clientes


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RP Manager")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        principal = QHBoxLayout()
        central.setLayout(principal)

        # Menu lateral
        menu = QVBoxLayout()

        titulo = QLabel("RP Manager")
        menu.addWidget(titulo)

        btn_dashboard = QPushButton("🏠 Dashboard")
        btn_clientes = QPushButton("👤 Clientes")
        btn_aparelhos = QPushButton("📱 Aparelhos")
        btn_os = QPushButton("📄 Ordem de Serviço")
        btn_estoque = QPushButton("📦 Estoque")
        btn_financeiro = QPushButton("💰 Financeiro")
        btn_relatorios = QPushButton("📊 Relatórios")

        btn_clientes.clicked.connect(self.abrir_clientes)

        menu.addWidget(btn_dashboard)
        menu.addWidget(btn_clientes)
        menu.addWidget(btn_aparelhos)
        menu.addWidget(btn_os)
        menu.addWidget(btn_estoque)
        menu.addWidget(btn_financeiro)
        menu.addWidget(btn_relatorios)

        menu.addStretch()

        # Área principal
        conteudo = QVBoxLayout()

        self.area = QLabel("Bem-vindo ao RP Manager")
        conteudo.addWidget(self.area)

        conteudo.addWidget(QLabel("Sistema para Assistência Técnica"))

        principal.addLayout(menu, 1)
        principal.addLayout(conteudo, 4)

    def abrir_clientes(self):
        self.janela_clientes = Clientes()
        self.janela_clientes.show()