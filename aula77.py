# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uam chave
# pop - apaga uma item com a chave especifica (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro
# import copy

pessoa1 = {
    'nome': 'Cauã Barbosa',
    'sobrenome': 'Rocha',
    'idade': 18
}

# pessoa1.update({
#     'nome': 'Alanzoka',
#     'sobrenome': 'Nextage',
#     'profissao': 'Dar bala em newba'n
# })
pessoa1.update(nome="Alanzoka", sobrenome="Nextage", profissao="Dar bala em NEWBA")
print(pessoa1)

tupla = (('nome', 'Lucas'), ('sobrenome', 'Inutilismo'), ('idade', 28), ('profissao', 'Deus musical'))
lista = [['nome', 'Sabrina'], ['sobrenome', 'Carpenter'], ['idade', 25], ['profissao', 'Deusa musical']]
print(tupla)
print(lista)

# ultima_chave = pessoa1.popitem()
# print(ultima_chave)
# print(pessoa1)

# nome = pessoa1.pop('nome')
# print(nome)
# print(pessoa1)

# print(pessoa1['idade'])
# print(pessoa1.get('idade', 'Não existe mané'))

# pessoa2 = pessoa1.copy() # shallow copy

# pessoa2['nome'] = "Alanzoka"
# pessoa2['sobrenome'] = "Nextage"
# print(pessoa1)
# print(pessoa2)

# dicionario1 = {
#     'numero1': 1,
#     'numero2': [900, 69, 777]
# }
# dicionario2 = copy.deepcopy(dicionario1) # deep copy

# dicionario1['numero1'] = 15
# dicionario2['numero2'][2] = 5

# print(dicionario1)
# print(dicionario2)
