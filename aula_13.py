nome = 'Cauã Barbosa'
altura = 1.70
peso = 53
imc = peso / (altura ** 2)

# print(nome, "tem", altura, "de altura,")
# print("pesa", peso, "quilos e seu IMC é")
# print(imc)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
