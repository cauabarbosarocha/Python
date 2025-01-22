"""
Formatação básica de strings
s - string
d - int
f - float
.<decimal do dígito>f
x ou X - Hexadecimal
(Caractere)(<>^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex. 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')
print(f'{1000.325:0>+10,.2f}')
print(f'O hexadecimal de 72 é {32:09x}')
print(f'{variavel!r}')
