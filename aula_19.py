primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'{primeiro_valor} é menor que {segundo_valor}')
else:
    print('Números iquais')