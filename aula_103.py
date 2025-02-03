# Variáveis livres + nonlocal

# print(globals())
# def fora(x):
#     a = x # Variável livre
    
#     def dentro():
#         print(locals())
#         print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(89)
# dentro2 = fora(7986)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_concatenar):
        nonlocal valor_final
        valor_final += valor_concatenar
        return valor_final
    return interna

c = concatenar('b')
print(c('g'))
print(c('e'))
