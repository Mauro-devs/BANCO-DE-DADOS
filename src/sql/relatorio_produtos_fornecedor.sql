SELECT f.cnpj, 
    f.nome_fantasia, 
    COUNT(pf.id_produto) AS total_produtos
FROM 
    PRODUTOS_FORNECEDORES pf
JOIN FORNECEDORES f 
    ON pf.cnpj_fornecedor = f.cnpj
GROUP BY f.nome_fantasia, 
        f.cnpj
ORDER BY 
    total_produtos DESC;