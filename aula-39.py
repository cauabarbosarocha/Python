# Calculadora com while
while True:
    numero_1 = input('Insira um número: ')
    numero_2 = input('Insira outro (ou o mesmo) número: ')
    operador = input('Insira um operador (+, -, *, /): ')
    
    sair = input('Quer sair? [s] sim [n] não: ').lower().startswith('s')
    if sair:
        print('[SAINDO...]')
        contador = 0
        while contador < 3:
            contador += 1
            print(contador)
        break

print('Você saiu')
