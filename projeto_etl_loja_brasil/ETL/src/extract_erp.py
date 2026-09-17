import pandas as pd
from config import erp_engine, dw_engine



sql_vendas = """
SELECT
    p.id_pedido,
    p.data_pedido,
    p.status AS status_pedido,
    c.id_cliente,
    c.nome AS cliente,
    c.cidade,
    c.estado,
    i.id_produto,
    pr.nome AS produto,
    cat.nome AS categoria,
    m.nome AS marca,
    i.quantidade,
    i.preco_unitario,
    i.desconto
FROM vendas.pedidos p
INNER JOIN cadastro.clientes c
    ON c.id_cliente = p.id_cliente
INNER JOIN vendas.itens_pedido i
    ON i.id_pedido = p.id_pedido
INNER JOIN cadastro.produtos pr
    ON pr.id_produto = i.id_produto
INNER JOIN cadastro.categorias cat
    ON cat.id_categoria = pr.id_categoria
INNER JOIN cadastro.marcas m
    ON m.id_marca = pr.id_marca;
"""

def extrair_erp():
    print("Extraindo dados do banco de dados Loja Brasil")
    df_vendas = pd.read_sql(sql_vendas, erp_engine)
    
    df_vendas.to_sql(
        "erp_vendas",
        dw_engine,
        schema="bronze",
        if_exists="replace",
        index=False
    )
print("Dados de vendas carregados para o DW (schema bronze).")
