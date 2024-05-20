-- Create table for cliente
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

-- Create table for item_cardapio
CREATE TABLE item_cardapio (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    preco FLOAT NOT NULL,
    ingredientes VARCHAR(255) NOT NULL,
    foto VARCHAR(255),
    informacoes_nutricionais VARCHAR(255)
);

-- Create table for estoque
CREATE TABLE estoque (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL REFERENCES item_cardapio(id),
    quantidade INT NOT NULL
);

-- Create table for pedido
CREATE TABLE pedido (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL REFERENCES cliente(id),
    quantidade INT NOT NULL,
    metodo_pagamento VARCHAR(50) NOT NULL
);

-- Create table for pedido_item
CREATE TABLE pedido_item (
    pedido_id INT NOT NULL REFERENCES pedido(id),
    item_id INT NOT NULL REFERENCES item_cardapio(id),
    quantidade INT NOT NULL,
    PRIMARY KEY (pedido_id, item_id)
);

