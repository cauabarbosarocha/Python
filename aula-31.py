"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Escreva um número inteiro: ')

# try:
#     numero_int = int(numero)
#     numero_checado = numero_int % 2 == 0
#     if numero_checado:
#         print(f'O {numero} é par')
#     else:
#         print(f'O {numero} é ímpar')
# except:    
#     print('Por favor digite um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
decrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? ')
try:
    horario = int(hora)
    bom_dia = horario >= 6 and horario < 12
    boa_tarde = horario >= 12 and horario <= 17
    boa_noite = horario >= 18 and horario <= 23
    boa_madrugada = horario >= 0 and horario <= 5

    if bom_dia:
        print('Bom dia, tenha um ótimo dia')

    if boa_tarde:
        print('Boa tarde, tenha uma ótima tarde')

    if boa_noite:
        print('Boa noite, tenha uma ótima noite')

    if boa_madrugada:
        print('Boa madrugada, tenha uma ótima noitada')
except:
    print('Por favor, digite seu horário')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiverr 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""
