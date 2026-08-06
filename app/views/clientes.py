from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QCheckBox,
    QMessageBox,
    QHeaderView
)

from app.controllers.cliente_controller import ClienteController


class TelaClientes(QWidget):

    def __init__(self):
        super().__init__()

        self.id_cliente = None

        self.setWindowTitle("Clientes")

        layout = QVBoxLayout()

        titulo = QLabel("👤 Cadastro de Clientes")
        titulo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:10px;
        """)

        layout.addWidget(titulo)

        formulario = QGridLayout()

        # ==========================
        # LINHA 1
        # ==========================

        formulario.addWidget(QLabel("Nome"),0,0)

        self.nome = QLineEdit()
        formulario.addWidget(self.nome,0,1)

        formulario.addWidget(QLabel("CPF"),0,2)

        self.cpf = QLineEdit()
        formulario.addWidget(self.cpf,0,3)

        # ==========================

        formulario.addWidget(QLabel("Telefone"),1,0)

        self.telefone = QLineEdit()
        formulario.addWidget(self.telefone,1,1)

        formulario.addWidget(QLabel("WhatsApp"),1,2)

        self.whatsapp = QLineEdit()
        formulario.addWidget(self.whatsapp,1,3)

        # ==========================

        formulario.addWidget(QLabel("E-mail"),2,0)

        self.email = QLineEdit()
        formulario.addWidget(self.email,2,1)

        formulario.addWidget(QLabel("Nascimento"),2,2)

        self.data_nascimento = QLineEdit()
        self.data_nascimento.setPlaceholderText("dd/mm/aaaa")

        formulario.addWidget(self.data_nascimento,2,3)

        # ==========================

        formulario.addWidget(QLabel("Cidade"),3,0)

        self.cidade = QLineEdit()
        formulario.addWidget(self.cidade,3,1)

        formulario.addWidget(QLabel("CEP"),3,2)

        self.cep = QLineEdit()
        formulario.addWidget(self.cep,3,3)

        # ==========================

        formulario.addWidget(QLabel("Endereço"),4,0)

        self.endereco = QLineEdit()

        formulario.addWidget(
            self.endereco,
            4,
            1,
            1,
            3
        )

        layout.addLayout(formulario)

        self.aceita_promocoes = QCheckBox(
            "Aceita receber promoções"
        )

        self.aceita_promocoes.setChecked(True)

        layout.addWidget(
            self.aceita_promocoes
        )

        layout.addWidget(
            QLabel("Observações")
        )

        self.observacoes = QTextEdit()

        self.observacoes.setFixedHeight(80)

        layout.addWidget(
            self.observacoes
        )

        botoes = QHBoxLayout()

        self.btn_salvar = QPushButton("💾 Salvar")
        self.btn_editar = QPushButton("✏️ Editar")
        self.btn_excluir = QPushButton("🗑️ Excluir")
        self.btn_limpar = QPushButton("🧹 Limpar")

        botoes.addWidget(self.btn_salvar)
        botoes.addWidget(self.btn_editar)
        botoes.addWidget(self.btn_excluir)
        botoes.addWidget(self.btn_limpar)

        layout.addLayout(botoes)
                # ==========================
        # TABELA
        # ==========================

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(6)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Nome",
            "WhatsApp",
            "Cidade",
            "Nascimento",
            "Telefone"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(self.tabela)

        self.setLayout(layout)

        # ==========================
        # EVENTOS
        # ==========================

        self.btn_salvar.clicked.connect(self.salvar_cliente)

        self.btn_editar.clicked.connect(self.editar_cliente)

        self.btn_excluir.clicked.connect(self.excluir_cliente)

        self.btn_limpar.clicked.connect(self.limpar_campos)

        self.tabela.cellClicked.connect(
            self.selecionar_cliente
        )

        self.carregar_clientes()

    # ==========================
    # CARREGAR CLIENTES
    # ==========================

    def carregar_clientes(self):

        dados = ClienteController.listar()

        self.tabela.setRowCount(len(dados))

        for linha, cliente in enumerate(dados):

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(str(cliente[0]))
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(cliente[1] or "")
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(cliente[3] or "")
            )

            self.tabela.setItem(
                linha,
                3,
                QTableWidgetItem(cliente[8] or "")
            )

            self.tabela.setItem(
                linha,
                4,
                QTableWidgetItem(cliente[6] or "")
            )

            self.tabela.setItem(
                linha,
                5,
                QTableWidgetItem(cliente[2] or "")
            )

    # ==========================
    # SELECIONAR
    # ==========================

    def selecionar_cliente(self, linha, coluna):

        self.id_cliente = int(
            self.tabela.item(linha,0).text()
        )

        cliente = ClienteController.buscar(
            self.id_cliente
        )

        if not cliente:
            return

        self.nome.setText(cliente[1] or "")
        self.telefone.setText(cliente[2] or "")
        self.whatsapp.setText(cliente[3] or "")
        self.cpf.setText(cliente[4] or "")
        self.email.setText(cliente[5] or "")
        self.data_nascimento.setText(cliente[6] or "")
        self.endereco.setText(cliente[7] or "")
        self.cidade.setText(cliente[8] or "")
        self.cep.setText(cliente[9] or "")

        self.aceita_promocoes.setChecked(
            bool(cliente[10])
        )

        self.observacoes.setPlainText(
            cliente[11] or ""
        )
            # ==========================
    # SALVAR
    # ==========================

    def salvar_cliente(self):

        sucesso = ClienteController.adicionar(
            self.nome.text(),
            self.telefone.text(),
            self.whatsapp.text(),
            self.cpf.text(),
            self.email.text(),
            self.data_nascimento.text(),
            self.endereco.text(),
            self.cidade.text(),
            self.cep.text(),
            1 if self.aceita_promocoes.isChecked() else 0,
            self.observacoes.toPlainText()
        )

        if sucesso:

            QMessageBox.information(
                self,
                "Sucesso",
                "Cliente cadastrado."
            )

            self.limpar_campos()

            self.carregar_clientes()

        else:

            QMessageBox.warning(
                self,
                "Erro",
                "CPF ou E-mail já cadastrado."
            )

    # ==========================
    # EDITAR
    # ==========================

    def editar_cliente(self):

        if self.id_cliente is None:

            QMessageBox.warning(
                self,
                "Aviso",
                "Selecione um cliente."
            )

            return

        ClienteController.atualizar(
            self.id_cliente,
            self.nome.text(),
            self.telefone.text(),
            self.whatsapp.text(),
            self.cpf.text(),
            self.email.text(),
            self.data_nascimento.text(),
            self.endereco.text(),
            self.cidade.text(),
            self.cep.text(),
            1 if self.aceita_promocoes.isChecked() else 0,
            self.observacoes.toPlainText()
        )

        QMessageBox.information(
            self,
            "Sucesso",
            "Cliente atualizado."
        )

        self.limpar_campos()

        self.carregar_clientes()

    # ==========================
    # EXCLUIR
    # ==========================

    def excluir_cliente(self):

        if self.id_cliente is None:

            QMessageBox.warning(
                self,
                "Aviso",
                "Selecione um cliente."
            )

            return

        resposta = QMessageBox.question(
            self,
            "Excluir",
            "Deseja realmente excluir este cliente?"
        )

        if resposta == QMessageBox.Yes:

            ClienteController.excluir(
                self.id_cliente
            )

            QMessageBox.information(
                self,
                "Sucesso",
                "Cliente excluído."
            )

            self.limpar_campos()

            self.carregar_clientes()

    # ==========================
    # LIMPAR
    # ==========================

    def limpar_campos(self):

        self.id_cliente = None

        self.nome.clear()
        self.telefone.clear()
        self.whatsapp.clear()
        self.cpf.clear()
        self.email.clear()
        self.data_nascimento.clear()
        self.endereco.clear()
        self.cidade.clear()
        self.cep.clear()

        self.observacoes.clear()

        self.aceita_promocoes.setChecked(True)

        self.nome.setFocus()