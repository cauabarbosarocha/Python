#  arquivo main

import importlib

import aula_99_m

print(aula_99_m.nome)

for i in range(5):
    importlib.reload(aula_99_m)

print('Fim')
