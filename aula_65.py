'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado rebebe apenas o argumetno (valor)
'''
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', x + y + z)
    
soma(1, 3, 4)
soma(y=3, x=1, z=4)
soma(1, 3, z=4)
