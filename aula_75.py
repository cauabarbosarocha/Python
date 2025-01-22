# Manipulando chaves e valores em dicionários
pessoa = {}

# #
# #

chave = 'nome'

pessoa[chave] = 'Cauã Barbosa'
pessoa['sobrenome'] = 'Rocha'

print(pessoa)
print(pessoa['nome'])
# print(pessoa['nome1'])

print(pessoa[chave])

pessoa[chave] = 'Jorge'

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print( 'NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
