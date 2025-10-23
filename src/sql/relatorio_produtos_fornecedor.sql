SELECT 
    f.cnpj, 
    f.nome, 
    COUNT(pf.id_produto) AS total_produtos
FROM 
    PRODUTOS_FORNECEDORES pf
JOIN FORNECEDORES f 
    ON pf.cnpj_fornecedor = f.cnpj
GROUP BY f.nome, 
        f.cnpj
ORDER BY 
    total_produtos DESC