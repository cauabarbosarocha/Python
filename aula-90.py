# dir, hasattr, e getattr e Python

string = 'Cauã'
metodo = 'upper69'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
