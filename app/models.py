# Objeto 'db' do pacote 'app', que é uma instância do SQLAlchemy
from app import db

class Cliente(db.Model):
    __tablename__ = 'cliente'  
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

class ItemCardapio(db.Model):
    __tablename__ = 'item_cardapio'  
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    ingredientes = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255))
    informacoes_nutricionais = db.Column(db.String(255))

class Estoque(db.Model):
    __tablename__ = 'estoque'  
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item_cardapio.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    item = db.relationship('ItemCardapio')

class Pedido(db.Model):
    __tablename__ = 'pedido' 
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    metodo_pagamento = db.Column(db.String(50), nullable=False)
    itens = db.relationship('PedidoItem', back_populates='pedido')

class PedidoItem(db.Model):
    __tablename__ = 'pedido_item'  
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item_cardapio.id'), primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    pedido = db.relationship('Pedido', back_populates='itens')
    item = db.relationship('ItemCardapio')
