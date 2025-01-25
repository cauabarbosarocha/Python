
import copy

from aula_101_exercicio import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos_e_precos = [
    {**preco_novo, 'preco': round(preco_novo['preco'] * 1.1, 2)}
    for preco_novo in produtos
]
# print('Aumento de 10%')
# print(*produtos, sep='\n')
# print()
# print(*novos_produtos_e_precos, sep="\n")

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_por_nome = sorted(
    copy.deepcopy(novos_produtos_e_precos),
    key=lambda produto: produto['nome'],
    reverse=True
)

# print()
# print('Ordenado por nome')
# print(*novos_produtos_e_precos, sep='\n')
# print()
# print(*produtos_por_nome, sep="\n")

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_por_preco = sorted(
    copy.deepcopy(novos_produtos_e_precos),
    key=lambda produto: produto['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos_e_precos, sep='\n')
print()
print(*produtos_por_nome, sep='\n')
print()
print(*produtos_por_preco, sep='\n')