"""
Introdução ás funções (def) em Python
Funções são trechos de código usads para replicar
determinada ação ap longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""
# def imprimir(a, b, c):
#     # print('Olá, Mundo')
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Cauã')
saudacao('Jorge')
saudacao()
