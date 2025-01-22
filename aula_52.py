# Introdução ao desempacotamento + tuples (tuplas)
# lista = ['Lasanha', 'Aparmediana', 'Nhoque']
# comida1, comida2, comida3 = ['Lasanha', 'Aparmediana', 'Nhoque']
comida1, *_ = ['Lasanha', 'Aparmediana', 'Nhoque']
print(comida1, _)
