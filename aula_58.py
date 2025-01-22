# Listas dentro de listas e seus índice
salas = [
    # 0          1
    ['Gabriel', 'Roger'], # 0
    # 0
    ['Leticia'], # 1
    # 0          1        2
    ['Vitória', 'Erika', 'Mayara',] #(0, 1, 2, 3)] # 2
]

# print(sala[2][1])
# print(sala[0][1])
# print(sala[2][2])
# print(sala[2][3][2])

for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)
