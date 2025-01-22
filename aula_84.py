# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Heloisa',
    'sobrenome': 'Martins'
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.58
}

pessoas_completas = {**pessoa, **dados_pessoa}
# print(pessoas_completas)

# args e kwargs
# args (já vi)
# kwargs - keyword arguments (argumentos nomeados)

def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMWADOS:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostra_argumentos_nomeados(nome='Cauã', qlqr=123)

# mostra_argumentos_nomeados(**pessoas_completas)

confgs = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4,
}

mostra_argumentos_nomeados(**confgs)
