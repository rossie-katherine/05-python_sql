import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Configurações para o ERP
erp_engine = create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('ERP_USUARIO')}:{os.getenv('ERP_SENHA')}"
    f"@{os.getenv('ERP_HOST')}:{os.getenv('ERP_PORT')}"
    f"/{os.getenv('ERP_DATABASE')}"
)

# Configurações para o DW → do jeito que o python deu pronto
dw_engine = create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('DW_USUARIO')}:{os.getenv('DW_SENHA')}"
    f"@{os.getenv('DW_HOST')}:{os.getenv('DW_PORT')}"
    f"/{os.getenv('DW_DATABASE')}"
)

