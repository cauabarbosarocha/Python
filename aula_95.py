# try, except, else, fanaly
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try: # não pode rodar sozinho e sempre irá iniciar
    print('ABRINDO ARQUIVO')
    9/0
except ZeroDivisionError as error: # não pode estar sozinho e podemos ter quantos precisarmos
    # print(error.__class__.___name__)
    # print(error)
    print('[ERROR] Impossível dividir por 0.')
else: # não pode estar sozinho e sempre estará depois do except
    print('Não teve erro.')
finally: # não pode estar sozinho e sempre finalizara
    print('FECHANDO ARQUIVO')
