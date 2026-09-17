# Pipeline em ETL - fluxo de execução 

from setup_dw import configurar_dw
from extract_erp import extrair_erp 
from extract_ibge import extrair_ibge
from extract_excel import extrair_excel
from silver import processar_silver 
from gold import processar_gold 

def main(): 
    # Configurar o Data Warehouse
    configurar_dw()

    # Extrair dados do ERP
    extrair_erp()

    # Extrair dados do IBGE
    extrair_ibge()

    # Extrair dados do Excel
    extrair_excel() 

    #Transformar dados
    processar_silver()

    #Carregar dados
    processar_gold()    

    print("Pipeline de ETL concluído com sucesso!")

if __name__ == "__main__":
    main()  

    