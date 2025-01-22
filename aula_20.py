# Operadores Lógidcos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você á viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E] Entrar [S] Sair:  ')
# senha_digitada = input('Digite sua senha:  ')
# senha_permitida = '1234'
# if entrada == 'E' or entrada == 'e' and senha_permitida == senha_digitada:
#     print('Entrar')
# elif entrada == 'S' or entrada == 's' and senha_permitida == senha_digitada:
#     print('Sair')
# else:
#     print('Acesso negado')    
print(True and False and True)
print(True and 0 and True)
