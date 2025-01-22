"""
Operação ternária (condição de uma linha)
<valos> if <condição> else <outro valor>
"""
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)
digito = 9
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito >= 9 else digito
print(novo_digito)
print('Valor' if True else 'Outro valor' if True else 'Fim') # não recomendado
