# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# set_1 = set('Cauã')

set_1 = set() # vazio
set_2 = {'Cauã',16, 6, 12} # com dados
print(set_1, type(set_1))
print(set_2, type(set_2))

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

lista_1 = [12, 16, 6, 12, 6, 6, 8, 8, 8, 8]
set_3 = set(lista_1)
lista_2 = set_3
print(lista_2)
print(8 in set_3)
print(4 not in set_3)
for numero in set_3:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

set_4 = set()
set_4.add('Cauã')
set_4.add(8)
set_4.update(('Opa, bão?', 1, 2, 3, 4, 5))
# set_4.clear() # Limpa o set
set_4.discard(8) # Precisa especificar o valor a ser descartado
set_4.discard('Cauã')
print(set_4)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

set_5 = {1, 2, 3}
set_6 = {2, 3, 4}
set_7 = set_5 | set_6
set_8 = set_5 & set_6
set_9 = set_5 - set_6 # set_6 - set_5 = 4
set_10 = set_5 ^ set_6
print(set_7)
print(set_8)
print(set_9)
print(set_10)
