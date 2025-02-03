# Exercício - Adiando Execução de função
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def cria_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna 

soma_cinco = cria_funcao(soma, 5)
multiplica_dex = cria_funcao(multiplica, 10)
print(soma_cinco(90))
print(multiplica_dex(90))
