import pandas as pd 
from config import dw_engine

def processar_silver():
    print("Iniciando processamento (transformação) da camada Silver...")

    df_vendas = pd.read_sql(
        "SELECT * FROM bronze.erp_vendas",
        dw_engine
    )

    df_ibge = pd.read_sql(
        "SELECT * FROM bronze.ibge_municipios",
        dw_engine
    )

    df_metas = pd.read_sql(
        "SELECT * FROM bronze.metas_vendas",
        dw_engine
    )

# Transformação e limpeza de dados 
#Conversão 
    df_vendas["data_pedido"] = pd.to_datetime(df_vendas["data_pedido"])
    df_vendas["ano"] = df_vendas["data_pedido"].dt.year
    df_vendas["mes"] = df_vendas["data_pedido"].dt.month

#Cálculos

    df_vendas["valor_item"] = (
        df_vendas["quantidade"]
        * df_vendas["preco_unitario"]
        * (1 - df_vendas["desconto"] / 100)
    ).round(2)

#Remover pedidos cancelados

    df_vendas = df_vendas[
        df_vendas["status_pedido"] != "Cancelado"
    ].copy()

# Padronização de nomes de cidades e estados para merge 

    df_vendas["cidade"] = df_vendas["cidade"].str.strip()
    df_ibge["cidade"] = df_ibge["cidade"].str.strip()

    df_vendas["estado"] = df_vendas["estado"].str.upper()
    df_ibge["estado"] = df_ibge["estado"].str.upper()

#União de DataFrames 

    df_vendas = df_vendas.merge(
        df_ibge,
        on=["cidade", "estado"],
        how="left"
    )


    df_vendas = df_vendas.merge(
        df_metas,
        on=["ano", "mes", "estado"],
        how="left"
    )

#Validações

    print("Sem correspondência IBGE:",
        df_vendas["id_ibge"].isna().sum())
    print("Sem correspondência de meta:",
        df_vendas["meta_vendas"].isna().sum())

#Gravando vendas tratadas na camada silver 

    df_vendas.to_sql(
        "vendas_tratadas",
        dw_engine,
        schema="silver",
        if_exists="replace",
        index=False
    )

#Gravando municipios na camada silver 

    df_ibge.to_sql(
        "municipios",
        dw_engine,
        schema="silver",
        if_exists="replace",
        index=False
    )

#Gravando metas vendas na camada silver 

    df_metas.to_sql(
        "metas_vendas",
        dw_engine,
        schema="silver",
        if_exists="replace",
        index=False
    )

    print("Silver carregada.")