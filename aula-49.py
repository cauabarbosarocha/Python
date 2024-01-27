"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - ídices e fatiamentos
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, deletar = lista[i] (CRUD)
"""
lista = [10, 7, 4, 2]
print(lista)

lista[1] = 18 # Mudança de ídice
print(lista)

numero = lista[1] # Índicae em váriavel
print(numero)

del lista[1] # Deletando um índice (recomendado remover o ultimo item)
print(lista)

lista.append(90) # Adicionado coisas
print(lista)

lista.pop() # Remove o último item
print(lista)
