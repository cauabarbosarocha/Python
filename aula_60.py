"""
Desempacotamento em chamadas
de métodos e funções
"""
string = 'ABCD'
lista = ['Aparmediana', 'Nhoque', 1, 2, 3, 'Lasanha']
tupla = 'Arroz', 'Feijão', 'Bife'
salas = [
    # 0          1
    ['Gabriel', 'Roger'], # 0
    # 0
    ['Leticia'], # 1
    # 0          1        2
    ['Vitória', 'Erika', 'Mayara',] #(0, 1, 2, 3)] # 2
]

# a, b, *_, c, d = lista
# print(a, c)

# for comida in lista:
#     print(comida, end=' ')

print('Aparmediana', 'Nhoque', 1, 2, 3, 'Lasanha')
print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')
