import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'SSD', 'preco': 230.00},
    {'nome': 'Fonte', 'preco': 559.99},
    {'nome': 'Memória RAM', 'preco': 250.00},
    {'nome': 'Processador', 'preco': 1050.00},
    {'nome': 'Placa de Vídeo', 'preco': 5200.00},
]

novos_produtos_e_precos = [
    {**preco_novo, 'preco': preco_novo['preco'] * 1.1}
    for preco_novo in produtos
]

print(*novos_produtos_e_precos, sep="\n")

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)



# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
