# Exercício - Adiando Execução de função
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def cria_funcao(funcao, *args):
    return funcao

soma_cinco = cria_funcao(soma, 5)
multiplica_dex = cria_funcao(multiplica, 10)
