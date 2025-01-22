"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Cauã'
preco = 1000.987654321
variavel = '%s, o valor deu R$ %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %X' % (7, 15762))
