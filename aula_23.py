# Operadores in e not in
# Strings não iteráveis
#  0 1 2 3 
#  C a u ã
# -4-3-2-1

# nome = 'Cauã'
# print(nome[3])
# print('auã' in nome)
# print('um' in nome)
# print(10 * '-')
# print('Cau' not in nome)
# print('um' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontra: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
