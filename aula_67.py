"""
Escopo de funções em Python
Escopo significa o local on de aquele código pode atingir.
Existe o escopo global e o local.
    * O escopo global é o escopo onde todo o código é alcançavel;
    * O escopo local é o escopo onde apenas nomes do mesmo local
    podem ser alcançados.

"""
x = 1

def escopo():
    global x
    x = 7

    def outra_funcao():
        y = 20
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
