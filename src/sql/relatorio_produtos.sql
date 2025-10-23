SELECT prd.id_produto ,
        prd.nome, 
        prd.preco_unitario, 
        prd.descricao,
        prd.categoria
FROM PRODUTOS prd
ORDER BY prd.categoria, prd.preco_unitario