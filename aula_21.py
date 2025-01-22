# Operador Lógico
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for coniderado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar em não valor 

# entrada = input('[E] Entrar [S] Sair:  ')
# senha_digitada = input('Digite sua senha:  ')
# senha_permitida = '1234'
# if (entrada == 'E' or entrada == 'e') and senha_permitida == senha_digitada:
#     print('Entrar')
# elif (entrada == 'S' or entrada == 's') and senha_permitida == senha_digitada:
#     print('Sair')
# else:
#     print('Acesso negado')

senha = input('Senha: ') or 'Sem senha'
print(senha)
