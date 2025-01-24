from sys import path

import aula_100_package.modulo
# from aula_100_package.modulo import soma_modulo
from aula_100_package import modulo
from aula_100_package.modulo import * # má prática

# print(*path, sep="\n")

print(soma_modulo(2, 2))
print(aula_100_package.modulo.soma_modulo(2, 2))
print(modulo.soma_modulo(2, 2))
print(variavel)
