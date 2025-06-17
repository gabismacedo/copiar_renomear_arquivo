from datetime import datetime
import os
import shutil
import logging

def moverArquivo():
    
    # formatação do arquivo log
    logging.basicConfig(filename=r'log\arquivo_log.log', 
                        encoding='utf-8', 
                        level=logging.DEBUG, 
                        format= '%(asctime)s - %(levelname)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    
    # caminho e nome do arquivo, o nome é sempre o mesmo
    arquivo = r'C:\documentos\CARRINHO_ABANDONADO.csv'
    # pasta de destino para onde o arquivo sera encaminhado
    pasta_destino = r'C:\Área de Trabalho\arquivo'
    data_arquivo = os.path.getmtime(arquivo) # pega a data do arquivo neste formato 17293847.0
    # formata a data para aaaa-mm-dd
    data_formatada = datetime.fromtimestamp(data_arquivo)
    logging.info(f'Data do arquivo {data_formatada}')
    data_hoje = datetime.now()

    # compara se a data de hoje é igual a data do arquivo
    if data_formatada.date() == data_hoje.date():
        shutil.copy(arquivo,pasta_destino) # faz a copia
        #renomeia o arquivo
        os.rename(r'C:\Área de Trabalho\arquivo\CARRINHO_ABANDONADO.csv', 
                fr'C:\Área de Trabalho\arquivo\CARRINHO_ABANDONADO_{data_hoje.strftime('%d%m%Y')}.csv')
        logging.info('Arquivo copiado e renomeado')
    else:
        logging.warning('Arquivo não incluido na pasta hoje')
    
