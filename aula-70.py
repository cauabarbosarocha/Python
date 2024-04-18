# Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos
não nomeados recebidos.
Retorne o total para uma variável e mostre o valor
da valiável
"""

# numeros = input('Digite quantos números quiser: ')
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total 
    
numeros = 1, 3, 56, 100
print(multiplicacao(*numeros))

"""
Crie uma função que fale se um númemro é par ou impar.
Retorne se o número é par ou impar
"""
def par_impar(numero):
    par = numero % 2 == 0
    if par:
        return f'O número {numero} é Par'
    
    return f'O número {numero} é Impar'

print(par_impar(90))
