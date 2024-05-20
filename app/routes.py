from flask import render_template, redirect, url_for, request, make_response
from app import app, db
from app.models import Cliente, ItemCardapio, Pedido, PedidoItem, Estoque

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para visualizar os clientes
@app.route('/clientes')
def clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

# Rota para adicionar um novo cliente
@app.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('clientes'))
    return render_template('add_cliente.html')

# Rota para visualizar o cardápio
@app.route('/cardapio')
def cardapio():
    itens = ItemCardapio.query.all()
    return render_template('cardapio.html', itens=itens)

# Rota para adicionar um novo item ao cardápio
@app.route('/add_item_cardapio', methods=['GET', 'POST'])
def add_item_cardapio():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        ingredientes = request.form['ingredientes']
        foto = request.form['foto']
        informacoes_nutricionais = request.form['informacoes_nutricionais']
        novo_item = ItemCardapio(nome=nome, descricao=descricao, preco=preco, ingredientes=ingredientes, foto=foto, informacoes_nutricionais=informacoes_nutricionais)
        db.session.add(novo_item)
        db.session.commit()
        return redirect(url_for('cardapio'))
    return render_template('add_item_cardapio.html')

# Rota para fazer um pedido
@app.route('/fazer_pedido', methods=['GET', 'POST'])
def fazer_pedido():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        itens = request.form.getlist('itens')
        quantidades = request.form.getlist('quantidades')
        metodo_pagamento = request.form['metodo_pagamento']
        
        novo_pedido = Pedido(cliente_id=cliente_id, metodo_pagamento=metodo_pagamento)
        db.session.add(novo_pedido)
        db.session.commit()
        
        for item_id, quantidade in zip(itens, quantidades):
            pedido_item = PedidoItem(pedido_id=novo_pedido.id, item_id=item_id, quantidade=quantidade)
            db.session.add(pedido_item)
            
            # Atualizar estoque
            estoque_item = Estoque.query.filter_by(item_id=item_id).first()
            if estoque_item:
                estoque_item.quantidade -= int(quantidade)
        
        db.session.commit()
        return redirect(url_for('pedidos'))
    clientes = Cliente.query.all()
    itens = ItemCardapio.query.all()
    return render_template('fazer_pedido.html', clientes=clientes, itens=itens)

# Rota para visualizar os pedidos
@app.route('/pedidos')
def pedidos():
    pedidos = Pedido.query.all()
    return render_template('pedidos.html', pedidos=pedidos)

# Rota para visualizar os estoques
@app.route('/estoque')
def estoque():
    estoque = Estoque.query.all()
    return render_template('estoque.html', estoque=estoque)

# Relatorio em FPDF
from fpdf import FPDF


# Rotas para relatórios
@app.route('/relatorio_clientes')
def relatorio_clientes():
    clientes = Cliente.query.all()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adiciona título ao relatório
    pdf.cell(200, 10, txt="Relatório de Clientes", ln=True, align='C')

    # Adiciona cabeçalho com os nomes das colunas
    pdf.cell(50, 10, txt="Nome", border=1, ln=True, align='C')
    pdf.cell(50, 10, txt="Email", border=1, ln=True, align='C')
    pdf.cell(50, 10, txt="Telefone", border=1, ln=True, align='C')

    # Adiciona os dados de cada cliente
    for cliente in clientes:
        pdf.cell(50, 10, txt=cliente.nome, border=1, ln=True, align='C')
        pdf.cell(50, 10, txt=cliente.email, border=1, ln=True, align='C')
        pdf.cell(50, 10, txt=cliente.telefone, border=1, ln=True, align='C')
        
    # Salva o relatório em PDF
    pdf_file = "relatorio_clientes.pdf"
    pdf.output(pdf_file)

    # Abre o arquivo PDF e o envia como resposta para o navegador
    with open(pdf_file, "rb") as file:
        response = make_response(file.read())
        response.headers['Content-Disposition'] = 'inline; filename=relatorio_clientes.pdf'
        response.headers['Content-type'] = 'application/pdf'

    return response

@app.route('/relatorio_vendas')
def relatorio_vendas():
    pedidos = Pedido.query.all()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adiciona título ao relatório
    pdf.cell(200, 10, txt="Relatório de Vendas", ln=True, align='C')

    # Adiciona cabeçalho com os nomes das colunas
    pdf.cell(50, 10, txt="ID do Pedido", border=1, ln=True, align='C')
    pdf.cell(50, 10, txt="ID do Cliente", border=1, ln=True, align='C')
    pdf.cell(50, 10, txt="Método de Pagamento", border=1, ln=True, align='C')

    # Adiciona os dados de cada pedido
    for pedido in pedidos:
        pdf.cell(50, 10, txt=str(pedido.id), border=1, ln=True, align='C')
        pdf.cell(50, 10, txt=str(pedido.cliente_id), border=1, ln=True, align='C')
        pdf.cell(50, 10, txt=pedido.metodo_pagamento, border=1, ln=True, align='C')

    # Salva o relatório em PDF
    pdf_file = "relatorio_vendas.pdf"
    pdf.output(pdf_file)

    # Abre o arquivo PDF e o envia como resposta para o navegador
    with open(pdf_file, "rb") as file:
        response = make_response(file.read())
        response.headers['Content-Disposition'] = 'inline; filename=relatorio_vendas.pdf'
        response.headers['Content-type'] = 'application/pdf'

    return response

