
import pandas as pd
import requests
from config import dw_engine

url_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/42/municipios"


def extrair_ibge():
    print("Extraindo dados do IBGE")
            
    response = requests.get(url_ibge, timeout=30)
    response.raise_for_status()

    dados_ibge = response.json()

    df_ibge = pd.DataFrame([
        {
            "id_ibge": municipio["id"],
            "cidade": municipio["nome"],
            "estado": municipio["microrregiao"]["mesorregiao"]["UF"]["sigla"],
            "regiao": municipio["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"],
            "mesorregiao": municipio["microrregiao"]["mesorregiao"]["nome"],
            "microrregiao": municipio["microrregiao"]["nome"],
            "regiao_imediata": municipio["regiao-imediata"]["nome"],
            "regiao_intermediaria": municipio["regiao-imediata"]["regiao-intermediaria"]["nome"]
        }
        for municipio in dados_ibge
    ])

    df_ibge.to_sql(
        "ibge_municipios",
        dw_engine,
        schema="bronze",
        if_exists="replace",
        index=False
    )
    
    print("Dados do IBGE carregados para o DW (schema bronze).")
