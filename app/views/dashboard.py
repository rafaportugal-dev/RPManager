from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLabel,
    QStackedWidget
)

from app.widgets.card import Card
from app.views.clientes import TelaClientes
from app.views.produtos import TelaProdutos
from app.views.vendas import TelaVendas
from app.views.categorias import TelaCategorias

class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RP Manager")
        self.resize(1300, 750)

        central = QWidget()
        self.setCentralWidget(central)

        layout_principal = QHBoxLayout(central)

        # ==========================
        # MENU LATERAL
        # ==========================

        menu = QVBoxLayout()

        titulo = QLabel("RP Manager")
        titulo.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            padding:15px;
        """)
        menu.addWidget(titulo)

        self.btn_dashboard = QPushButton("🏠 Dashboard")
        self.btn_clientes = QPushButton("👤 Clientes")
        self.btn_produtos = QPushButton("📦 Produtos")
        self.btn_vendas = QPushButton("🛒 Vendas")
        self.btn_aparelhos = QPushButton("📱 Aparelhos")
        self.btn_os = QPushButton("📄 Ordem de Serviço")
        self.btn_estoque = QPushButton("📚 Estoque")
        self.btn_financeiro = QPushButton("💰 Financeiro")
        self.btn_relatorios = QPushButton("📊 Relatórios")
        self.btn_config = QPushButton("⚙ Configurações")
        self.btn_categorias = QPushButton("📂 Categorias")
        botoes = [
            self.btn_dashboard,
            self.btn_clientes,
            self.btn_produtos,
            self.btn_vendas,
            self.btn_aparelhos,
            self.btn_os,
            self.btn_estoque,
            self.btn_financeiro,
            self.btn_categorias,
            self.btn_relatorios,
            self.btn_config,
        ]

        for botao in botoes:
            botao.setMinimumHeight(45)
            menu.addWidget(botao)

        menu.addStretch()
        menu.addWidget(QLabel("Versão 0.3"))

        # ==========================
        # ÁREA CENTRAL
        # ==========================

        self.paginas = QStackedWidget()
                # ==========================
        # DASHBOARD
        # ==========================

        pagina_dashboard = QWidget()

        dash_layout = QVBoxLayout()

        titulo_dash = QLabel("🏠 Dashboard")
        titulo_dash.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        dash_layout.addWidget(titulo_dash)
        dash_layout.addWidget(QLabel("Bem-vindo ao RP Manager"))

        dash_layout.addSpacing(20)

        cards = QGridLayout()

        cards.addWidget(Card("Clientes", 0, "👥"), 0, 0)
        cards.addWidget(Card("Produtos", 0, "📦"), 0, 1)
        cards.addWidget(Card("Ordens", 0, "🔧"), 1, 0)
        cards.addWidget(Card("Financeiro", "R$ 0,00", "💰"), 1, 1)

        dash_layout.addLayout(cards)
        dash_layout.addStretch()

        pagina_dashboard.setLayout(dash_layout)

        # ==========================
        # OUTRAS PÁGINAS
        # ==========================

        pagina_clientes = TelaClientes()
        pagina_produtos = TelaProdutos()
        pagina_vendas = TelaVendas()
        pagina_categorias = TelaCategorias()

        self.paginas.addWidget(pagina_dashboard)    # 0
        self.paginas.addWidget(pagina_clientes)     # 1
        self.paginas.addWidget(pagina_produtos)     # 2
        self.paginas.addWidget(pagina_categorias)   # 3
        self.paginas.addWidget(pagina_vendas)       # 4

        layout_principal.addLayout(menu, 1)
        layout_principal.addWidget(self.paginas, 5)
                # ==========================
        # EVENTOS
        # ==========================

        self.btn_dashboard.clicked.connect(self.mostrar_dashboard)
        self.btn_clientes.clicked.connect(self.mostrar_clientes)
        self.btn_produtos.clicked.connect(self.mostrar_produtos)
        self.btn_vendas.clicked.connect(self.mostrar_vendas)
        self.btn_categorias.clicked.connect(
        self.mostrar_categorias
)   
    # ==========================
    # MÉTODOS
    # ==========================

    def mostrar_dashboard(self):
        self.paginas.setCurrentIndex(0)

    def mostrar_clientes(self):
        self.paginas.setCurrentIndex(1)

    def mostrar_produtos(self):
        self.paginas.setCurrentIndex(2)

    def mostrar_categorias(self):
        self.paginas.setCurrentIndex(3)

    def mostrar_vendas(self):
        self.paginas.setCurrentIndex(4)