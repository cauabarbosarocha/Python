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
# hora = input('Que horas são? ')
# try:
#     horario = int(hora)
#     bom_dia = horario >= 6 and horario < 12
#     boa_tarde = horario >= 12 and horario <= 17
#     boa_noite = horario >= 18 and horario <= 23
#     boa_madrugada = horario >= 0 and horario <= 5

#     if bom_dia:
#         print('Bom dia, tenha um ótimo dia')

#     if boa_tarde:
#         print('Boa tarde, tenha uma ótima tarde')

#     if boa_noite:
#         print('Boa noite, tenha uma ótima noite')

#     if boa_madrugada:
#         print('Boa madrugada, tenha uma ótima noitada')
#     else:
#         print('Não conheço este horário')
# except:
#     print('Por favor, digite seu horário')
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""
nome = input('Por favor digite seu primeiro nome: ')
tamanho_nome = len(nome)

# Minha lógica tava certa, menos meu código
# if tamanho_nome > 1:
#     nome_curto = tamanho_nome <= 4
#     nome_normal = tamanho_nome = 5 or tamanho_nome <= 6
#     nome_longo = tamanho_nome >= 7

#     if nome_curto:
#             print("Seu nome é curto")

#     if nome_normal:
#             print("Seu nome é normal")

#     if nome_longo:
#             print("Seu nome é muito grande")
# else:
#         print("Por favor, digite mais letras")

# Mesma lógica que a minha, porem o código funcinou
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Por favor, digite mais de uma letra')
    