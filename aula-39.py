# Calculadora com while
while True:
    numero_1 = input('Insira um número: ')
    numero_2 = input('Insira outro (ou o mesmo) número: ')
    operador = input('Insira um operador (+ - * /): ')
    num_valido = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        num_valido = True
        print('Realizarei sua operação a seguir:')
        if operador == '+':
            print(num_1_float + num_2_float)

        if operador == '-':
            print(num_1_float - num_2_float)

        if operador == '*':
            print(num_1_float * num_2_float)

        if operador == '/':
            print(num_1_float / num_2_float)
    except:
        num_valido = None

    if num_valido is None:
        print('Um ou ambos os números são inválidos, tente novamente.')
        continue

    operadores_validos = '+-*/'
    if operador not in operadores_validos:
        print('Operador inválido, tente novamente.')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador.')
        continue

    sair = input('Quer sair? [s] sim [n] não: ').lower().startswith('s')
    if sair:
        print('[SAINDO...]')
        contador = 0
        while contador < 3:
            contador += 1
            print(contador)
        break

print('Você saiu')
