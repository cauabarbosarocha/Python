# Módulo padrão do Python (import, from, as e *
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys

# platform = 'ESSE É MEU SISTEMA'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, pbjeto2
# Vantagens: nomes pequenos
# Desvantagens: sem o namespace do módulo

# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido

# import sys as s

# sys = 'sei lá'
# print(sys)
# print(s.platform)

# alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reseravr nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

from sys import platform as plat, exit as ex

print(plat)
print(ex)

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

# from sys import *

# print(platform)
# exit()