# Análise de Vendas de Produtos de Supermecado

## Descrição do Projeto

Dado um arquivo CSV contendo dados de vendas de produtos de um supermecado, a tarefa consiste em ler os dados, processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.

## Tecnologias Utilizadas

- Python
- Pandas
- OpenPyXL
- NumPy
- CSV


## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/rafaelporfiriobarros/etl_produtos_vendas_entregas.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python etl.py
   ```

## Estrutura do Script

O script realiza as seguintes etapas:

1. **Leitura do CSV**: Lê um arquivo `produtos_supermercado.csv` contendo informações sobre produtos, categorias, quantidade e preço de venda.
2. **Processamento dos dados**: Agrupa os produtos por categoria.
3. **Cálculo de vendas**: Calcula o total de vendas por categoria.
4. **Gera um novo CSV**: Salva os resultados no arquivo `total_vendas_por_categoria.csv`.

