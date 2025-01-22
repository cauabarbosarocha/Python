# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Preta',
    'preco': 3.5,
    'categoria': 'Escritório'
}

dicionario =  {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    # if chave == 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c')
]

dicionario = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)}
print(s1)
