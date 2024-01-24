"""
Iterável = str, range, etc...
Iterador = quem sabe entregar um valor por vez
next = me entregue o próximo valor
iter = me entregue seu iterador
"""
text = 'Cauã' # iterável
# iterador = iter(text) # iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break
for letra in text:
    print(letra)
