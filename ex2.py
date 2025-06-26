# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for compra in range(n):
    compra = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    ultimo_adicionado = compra.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = compra[:ultimo_adicionado]
    preco = float(compra[ultimo_adicionado + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra


for item, preco in carrinho:
  print(f"{item}: R${preco:.2f}")
  
print(f"Total: R${total:.2f}")  