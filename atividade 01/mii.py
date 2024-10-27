# Inicializamos variáveis importantes
total_gasto = 0  # Para somar o valor total da compra
produtos_acima_1000 = 0  # Para contar quantos produtos custam mais de R$1000
produto_mais_barato = ""  # Nome do produto mais barato
preco_mais_barato = None  # Preço do produto mais barato, começando como 'None' pois ainda não temos valores

# Laço para inserir produtos até que o usuário decida parar
while True:
    # Entrada de dados do produto
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$"))

    # Atualizar o total gasto
    total_gasto += preco_produto

    # Verificar se o produto custa mais de R$1000
    if preco_produto > 1000:
        produtos_acima_1000 += 1

    # Encontrar o produto mais barato
    if preco_mais_barato is None or preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto

    # Perguntar ao usuário se deseja continuar
    continuar = input("Deseja adicionar mais um produto? (S/N): ").strip().upper()
    if continuar == 'N':
        break  # Interrompe o laço se o usuário não quiser mais adicionar produtos

# Exibir o resumo da compra
print("\nResumo da compra:")
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Quantidade de produtos que custam mais de R$1000: {produtos_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato} que custa R${preco_mais_barato:.2f}")
