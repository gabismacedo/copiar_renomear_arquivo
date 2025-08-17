# Mover e Renomear Arquivo CSV

Este projeto é um pequeno utilitário Python para automatizar a cópia e o renomeio de um arquivo localizado em um diretório. 
O script verifica a data de modificação do arquivo, copia-o para uma pasta de destino caso o arquivo seja do dia atual e renomeia o arquivo com a data do processamento.
Todas as operações são registradas em um arquivo de log para facilitar o acompanhamento de ações e possíveis erros.

## Como funciona

- O arquivo principal (`main.py`) apenas importa e executa a função `moverArquivo` definida em `mover_arquivo.py`.
- O script busca por um arquivo chamado `nome_arquivo.csv` na pasta `C:\documentos`.
- Se o arquivo foi modificado na data corrente, ele é copiado para `C:\Área de Trabalho\arquivo`.
- Após a cópia, o arquivo é renomeado para incluir a data de hoje no formato `nome_arquivo_DDMMAAAA.csv`.
- Todas as ações, incluindo erros e avisos, são registradas em um log localizado em `log/arquivo_log.log`.

## Bibliotecas Utilizadas

O projeto utiliza apenas bibliotecas padrão do Python, não havendo necessidade de instalar pacotes externos:

- [`datetime`](https://docs.python.org/pt-br/3/library/datetime.html): utilizada para manipular datas e horários.
- [`os`](https://docs.python.org/pt-br/3/library/os.html): usada para operações com arquivos e diretórios.
- [`shutil`](https://docs.python.org/pt-br/3/library/shutil.html): utilizada para copiar arquivos.
- [`logging`](https://docs.python.org/pt-br/3/library/logging.html): utilizada para registrar logs das operações realizadas.

## Estrutura dos Arquivos

- `main.py`: ponto de entrada do projeto, responsável por iniciar o processo.
- `mover_arquivo.py`: contém a função `moverArquivo` que realiza toda a lógica de verificação, cópia, renomeio e logging.
- `log/arquivo_log.log`: arquivo de log gerado automaticamente pelo script.

## Observações

- Os caminhos para os arquivos e diretórios estão definidos para o ambiente Windows e podem ser alterados conforme a necessidade.
- Certifique-se de que os diretórios de origem e destino existem e que o script possui permissão para leitura e escrita nesses locais.
- O diretório `log` deve existir antes da execução do script.

## Exemplo de execução

Basta executar o arquivo principal:

```bash
python main.py
```

Todo o processo será registrado no arquivo de log.

---
