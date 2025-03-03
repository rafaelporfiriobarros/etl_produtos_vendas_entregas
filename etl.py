import csv

# Função para ler o arquivo CSV
def ler_csv(nome_arquivo):
    with open(nome_arquivo, mode="r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        return list(leitor)

# Função para processar os dados em um dicionário
def processar_dados(dados):
    categorias = {}
    for item in dados:
        categoria = item["Categoria"]
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

# Função para calcular o total de vendas por categoria
def calcular_vendas_categoria(dados):
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(float(item["Quantidade"]) * float(item["Venda"]) for item in itens)
        vendas_por_categoria[categoria] = round(total_vendas, 2)
    return vendas_por_categoria

# Função para salvar os dados em um novo CSV
def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode="w", encoding="utf-8-sig", newline="") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["Categoria", "Total de Vendas"])
        for categoria, total in dados.items():
            escritor.writerow([categoria, total])
    print(f"\nArquivo '{nome_arquivo}' criado com sucesso!")

# Função principal
def main():
    nome_arquivo = "produtos_supermercado.csv"
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)

    # Nome do arquivo de saída
    nome_saida = "total_vendas_por_categoria.csv"
    salvar_csv(nome_saida, vendas_categoria)

if __name__ == "__main__":
    main()
