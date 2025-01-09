# Exemplo de uso dos sets

# "Jogo" de achar letra

set_letra = set()

while True:
    letra = input('Digite uma letra: ')
    set_letra.add(letra)

    if 'c' in set_letra:
        print('VOCÊ ME ACHOU!!')
        break

    print(set_letra)
