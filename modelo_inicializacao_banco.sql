INSERT INTO cliente (nome, email, telefone) VALUES
    ('João', 'joao@example.com', '(11) 98765-4321'),
    ('Maria', 'maria@example.com', '(11) 12345-6789');

INSERT INTO item_cardapio (nome, descricao, preco, ingredientes, foto, informacoes_nutricionais) VALUES
    ('Hambúrguer', 'Hambúrguer artesanal', 15.99, 'Pão, carne, queijo, alface, tomate', 'hamburguer.jpg', 'Tabela nutricional disponível no rótulo'),
    ('Pizza', 'Pizza de pepperoni', 25.99, 'Massa, molho de tomate, queijo, pepperoni', 'pizza.jpg', 'Contém glúten e lactose');

INSERT INTO estoque (item_id, quantidade) VALUES
    (1, 50), -- Para o hambúrguer
    (2, 30); -- Para a pizza
    
INSERT INTO pedido (cliente_id, quantidade, metodo_pagamento) VALUES
    (1, 2, 'Cartão de crédito'),
    (2, 1, 'Dinheiro');

INSERT INTO pedido_item (pedido_id, item_id, quantidade) VALUES
    (1, 1, 2), 
    (2, 2, 1); 

