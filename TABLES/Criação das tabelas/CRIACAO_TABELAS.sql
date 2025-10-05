
DROP TABLE MOVIMENTACAO_ESTOQUE;
DROP TABLE ITEM_VENDA;
DROP TABLE PRODUTO;
DROP TABLE FORNECEDOR;
DROP TABLE CATEGORIA;
DROP TABLE VENDA;
DROP TABLE FUNCIONARIO;
DROP TABLE CLIENTE;
DROP TABLE PAGAMENTO;



CREATE TABLE CATEGORIA(
	id_categoria INT PRIMARY KEY,
	tipo VARCHAR2(20) NOT NULL,
	
	CONSTRAINT check_tipo CHECK (tipo IN ('MOUSE', 'TECLADO', 'MONITOR', 'HEADSET', 'MOUSE_PAD'))
);


CREATE TABLE FORNECEDOR(
	id_fornecedor INT PRIMARY KEY,
	nome VARCHAR2(50) NOT NULL,
	cnpj VARCHAR2(14) NOT NULL UNIQUE,
	telefone VARCHAR2(9)
	
);

CREATE TABLE PRODUTO(
	id_produto INT PRIMARY KEY,
	id_categoria INT NOT NULL,
	id_fornecedor INT NOT NULL,
	nome VARCHAR2(50) NOT NULL,
	descricao VARCHAR2(30) NOT NULL,
	preco_unitario DECIMAL(10,2) NOT NULL,
	quantidade_minima INT NOT NULL,
	
	CONSTRAINT fk_id_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES FORNECEDOR(id_fornecedor),
	CONSTRAINT fk_id_categoria FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria)	
);



CREATE TABLE FUNCIONARIO(

	id_funcionario INT PRIMARY KEY,
	nome VARCHAR2(50) NOT NULL,
	cpf VARCHAR2(11) NOT NULL UNIQUE,
	telefone VARCHAR2(9) NOT NULL
);

CREATE TABLE MOVIMENTACAO_ESTOQUE(
	id_movimentacao INT PRIMARY KEY,
	id_produto INT NOT NULL,
	id_funcionario INT NOT NULL,
	tipo VARCHAR2(10) NOT NULL,
	quantidade INT NOT NULL,
	data_movimentacao DATE NOT NULL,
	
	CONSTRAINT check_tipo_movimentacao CHECK (tipo IN ('ENTRADA', 'SAIDA', 'PERDA')),
	CONSTRAINT fk_id_produto FOREIGN KEY (id_produto) REFERENCES PRODUTO(id_produto),
	CONSTRAINT fk_id_funcionario FOREIGN KEY (id_funcionario) REFERENCES FUNCIONARIO(id_funcionario)
	
);

CREATE TABLE CLIENTE(
	id_cliente INT PRIMARY KEY,
	nome VARCHAR2(30) NOT NULL,
	cpf VARCHAR2(11) NOT NULL,
	telefone VARCHAR2(9) NOT NULL
);

CREATE TABLE PAGAMENTO(
	
	id_pagamento INT PRIMARY KEY,
	tipo VARCHAR2(10) NOT NULL,
	
	CONSTRAINT tipo_pagamento CHECK (tipo IN ('DEBITO', 'CREDITO', 'BOLETO', 'PIX'))
);



CREATE TABLE VENDA(
	id_venda INT PRIMARY KEY,
	id_cliente INT NOT NULL,
	id_funcionario INT NOT NULL,
	id_pagamento INT NOT NULL,
	data_venda DATE NOT NULL,
	valor_total DECIMAL(10,2) NOT NULL,
	tipo VARCHAR2(10) NOT NULL,

	-- Nome Corrigido: Indicando VENDA
	CONSTRAINT chk_venda_tipo CHECK (tipo IN ('COMPRA', 'VENDA', 'SAIDA')),
	
	CONSTRAINT fk_id_cliente_venda FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),
	CONSTRAINT fk_funcionario_venda FOREIGN KEY (id_funcionario) REFERENCES FUNCIONARIO(id_funcionario),
	CONSTRAINT fk_pagamento FOREIGN KEY (id_pagamento) REFERENCES PAGAMENTO(id_pagamento)
);

CREATE TABLE ITEM_VENDA(

	id_item INT PRIMARY KEY,
	id_venda INT NOT NULL,
	id_produto INT NOT NULL,
	quantidade INT NOT NULL,
	preco_unitario DECIMAL(10,2) NOT NULL,
	
	CONSTRAINT fk_id_venda_item_venda FOREIGN KEY (id_venda) REFERENCES VENDA(id_venda),
	CONSTRAINT fk_id_produto_item_venda FOREIGN KEY (id_produto) REFERENCES PRODUTO(id_produto)
);




