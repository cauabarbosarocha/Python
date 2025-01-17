# Try, except, else e finelly

try:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite um segundo número: '))
    divisao = numero_1 / numero_2
except ZeroDivisionError:
    print('[ERROR] Impossível dividir por 0.')
except (ValueError, IndentationError):
    print('[ERROR] TypeError ou IndexError.')
# except NameError:
#     print('[ERROR] Variável não definida.')
except Exception:
    print('[ERROR] Desconhecido.')

print('CONTINUA...')
