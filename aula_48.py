"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - ídices e fatiamentos
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
# pirnt(bool()) # falsy
# print(lista, type(lista))

#        0   1      2              3    4  
#       -5  -4     -3             -2   -1
lista = [123, True, 'Cauã Barbosa', 1.2, []]
lista[2] = 'Robison'
print(lista[2].upper(), type(lista[2]))
