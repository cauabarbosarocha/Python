# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# set_1 = set('Cauã')

# set_1 = set() # vazio
# set_2 = {'Cauã',16, 6, 12} # com dados
# print(set_1, type(set_1))
# print(set_2, type(set_2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# lista_1 = [12, 16, 6, 12, 6, 6, 8, 8, 8, 8]
# set_3 = set(lista_1)
# lista_2 = set_3
# print(lista_2)
# print(8 in set_3)
# print(4 not in set_3)
# for numero in set_3:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard



# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos