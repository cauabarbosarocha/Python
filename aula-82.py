# Função lambda em Python
# A função lambda é uma funçõa como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Cauã', 'sobrenome': 'Barbosa'},
    {'nome': 'Heloisa', 'sobrenome': 'Martins'},
    {'nome': 'Agatha', 'sobrenome': 'Barbosa'},
    {'nome': 'Hugo', 'sobrenome': 'Barbosa'},
    {'nome': 'Fenrir', 'sobrenome': 'Fenrisulfr'},
    {'nome': 'Ray', 'sobrenome': 'Holt'}
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
