# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_pode_0(d):
    if d == 0:
        raise ZeroDivisionError('Você tentou dividir por zero.')    
    return True

def tipo_errado(n,d):
    tipo_n = type(n)
    tipo_d = type(d)
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int (1, 2, 3 ...) ou floar (0.9, 2 ...). '
                        f'"{tipo_n}" enviado.')

    if not isinstance(d, (float, int)):
        raise TypeError(f'{d} deve ser int (1, 2, 3 ...) ou floar (0.9, 2 ...). '
                        f'"{tipo_d}" enviado.')

def divide(n, d):
    tipo_errado(n, d)
    nao_pode_0(d)
    return n / d
    
print(divide(8, 'b'))