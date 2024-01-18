"""
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quandoum código não tem fim
"""
contador = 0

while contador < 10:
    contador += 1

    if contador == 7:
        continue

    print(contador)

    if contador == 8:
        break

print('Acabou')
