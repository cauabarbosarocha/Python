# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Heloisa',
    'sobrenome': 'Martins'
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

# args e kwargs
# args (já vi)
# kwargs - keyword arguments (argumentos nomeados)