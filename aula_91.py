# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'Sou', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = {n for n in range(100)} # Salva todos os valores na memória
generator = (n for n in range(100)) # Não salva todos os valores na memória, apenas mostra um valor por vez
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
