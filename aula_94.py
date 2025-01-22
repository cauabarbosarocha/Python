# Try, except, else e finelly

try:
    numero_1 = 90
    numero_2 = 0
    # print('Linha 1'[1000])
    divisao = numero_1 / numero_2
    print('Linha 2')
except ZeroDivisionError:
    print('[ERROR] Impossível dividir por 0.')
except (TypeError, IndexError) as error:
    print('TypeError ou IndexError.')
    print('[ERROR]', error)
    print('[CLASS]', error.__class__.__name__)
# except NameError:
#     print('[ERROR] Variável não definida.')
except Exception:
    print('[ERROR] Desconhecido.')

print('CONTINUA...')
