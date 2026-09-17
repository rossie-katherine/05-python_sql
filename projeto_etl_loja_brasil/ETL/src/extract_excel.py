import openpyxl
import pandas as pd
from config import dw_engine

ARQUIVO = "dados/metas_vendas.xlsx"

def extrair_excel():
    print("Extraindo dados do arquivo Excel...")

    df_metas = pd.read_excel(ARQUIVO)
    df_metas.to_sql(
        "metas_vendas",
        dw_engine,
        schema="bronze",
        if_exists="replace",
        index=False
)

print("Dados extraídos e carregados na tabela bronze.metas_vendas." )
print("Extração concluída.")