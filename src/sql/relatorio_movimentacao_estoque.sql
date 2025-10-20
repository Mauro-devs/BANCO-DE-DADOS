SELECT  me.data_movimentacao,
        me.tipo_movimentacao,
        p.nome AS nome_produto,
        me.quantidade,
        fo.cnpj,
        fu.nome AS nome_funcionario
FROM 
	MOVIMENTACAO_ESTOQUE me
JOIN 
	FUNCIONARIOS fu ON me.cpf_funcionario = fu.cpf
JOIN 
	PRODUTOS_FORNECEDORES pf ON me.id_produto_fornecedor = pf.id_produto_fornecedor
JOIN 
	FORNECEDORES fo ON pf.cnpj_fornecedor = fo.cnpj
JOIN 
	PRODUTOS p ON pf.id_produto = p.id_produto
ORDER BY
    me.TIPO_MOVIMENTACAO, me.DATA_MOVIMENTACAO;