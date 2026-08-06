print("PDVController carregado")
from app.views.selecionar_cliente import SelecionarCliente
from app.controllers.produto_controller import ProdutoController


class PDVController:

    def __init__(self, view):

        self.view = view

        self.subtotal = 0.0
        self.desconto = 0.0
        self.cashback = 0.0
        self.total = 0.0

        # Eventos
        self.view.painel_busca.btn_adicionar.clicked.connect(
            self.adicionar_produto
        )

        self.view.painel_busca.txt_codigo.returnPressed.connect(
            self.adicionar_produto
        )
        self.view.painel_cliente.btn_buscar.clicked.connect(
             self.selecionar_cliente
        )

    # ======================================

    def adicionar_produto(self):

        codigo = self.view.painel_busca.txt_codigo.text().strip()

        if not codigo:
            return

        produto = ProdutoController.buscar_por_codigo(codigo)

        if produto is None:

            self.view.painel_busca.lbl_status.setText(
                "❌ Produto não encontrado."
            )

            return

        (
            id_produto,
            codigo,
            nome,
            categoria,
            fornecedor,
            preco_custo,
            preco_venda,
            estoque,
            estoque_minimo
        ) = produto

        self.view.painel_carrinho.adicionar_item(
            codigo,
            nome,
            1,
            preco_venda,
            0,
            preco_venda
        )

        # Atualiza painel do produto

        self.view.painel_produto.lbl_nome.setText(nome)

        self.view.painel_produto.lbl_codigo.setText(
            f"Código: {codigo}"
        )

        self.view.painel_produto.lbl_categoria.setText(
            f"Categoria: {categoria}"
        )

        self.view.painel_produto.lbl_fornecedor.setText(
            f"Fornecedor: {fornecedor}"
        )

        self.view.painel_produto.lbl_estoque.setText(
            f"Estoque: {estoque}"
        )

        self.view.painel_produto.lbl_custo.setText(
            f"Custo: R$ {preco_custo:.2f}"
        )

        self.view.painel_produto.lbl_preco.setText(
            f"Venda: R$ {preco_venda:.2f}"
        )

        lucro = preco_venda - preco_custo

        self.view.painel_produto.lbl_lucro.setText(
            f"Lucro: R$ {lucro:.2f}"
        )

        # Totais

        self.subtotal += preco_venda

        self.total = self.subtotal - self.desconto

        self.view.painel_total.lbl_subtotal.setText(
            f"R$ {self.subtotal:.2f}"
        )

        self.view.painel_total.lbl_total.setText(
            f"R$ {self.total:.2f}"
        )

        self.view.painel_busca.txt_codigo.clear()

        self.view.painel_busca.txt_codigo.setFocus()

        self.view.painel_busca.lbl_status.setText(
            f"✔ {nome} adicionado."
        )
    # ======================================

    def selecionar_cliente(self):

        janela = SelecionarCliente()

        if janela.exec():

            cliente = janela.cliente_selecionado

            self.view.painel_cliente.txt_cliente.setText(
                cliente["nome"]
            )

            self.view.painel_cliente.lbl_info.setText(
                f"📞 {cliente['telefone']} | 📱 {cliente['whatsapp']} | 🏙 {cliente['cidade']}"
            )