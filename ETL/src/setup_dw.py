from sqlalchemy import text
from config import dw_engine

def configurar_dw():
    print("Configurando o Data Warehouse...")

    # Criação das tabelas no Data Warehouse
    with dw_engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS bronze"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS silver"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS gold"))

print("Schemas do DW criados.")
