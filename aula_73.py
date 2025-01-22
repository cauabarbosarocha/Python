# Exercício
# Crie funções que duplicam, triplicam, e quadruplicam
# o número recebido como parâmetro
def cria_multiplicador(multiplicador):
    def multiplicacao(numero):
        return numero * multiplicador
    return multiplicacao

for numeros in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    multiplicado = cria_multiplicador(numeros)
    print(multiplicado(4))
