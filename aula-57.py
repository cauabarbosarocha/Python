"""
split e join com list e str
    -split | divide uma str
    -join | une uma str
"""
frase = '               Ée    ,                 Boa tarde??                   '
lista_frase_crua = frase.split(",")

lista_frase_formatada = []
for i, frase in enumerate(lista_frase_crua):
    lista_frase_formatada.append(lista_frase_crua[i].strip())

print(lista_frase_crua)
print(lista_frase_formatada)

frases_unidas = ' | '.join(lista_frase_formatada)
print(frases_unidas)
