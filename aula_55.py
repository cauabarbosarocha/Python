"""
Faça uma lista de compras
O usuário  deve ter a possibilidade de
inserir, aapgar, e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
# import os

lista = []

# while True:
#     entrada = input('Selecione uma opção: \n [i]nserir  [a]pagar  [l]istar:    ')
#     lista_enumerada = enumerate(lista)
#     apagar = entrada == 'a' and lista == []
#     listar = entrada == 'l' and lista == []

#     if entrada == 'i':
#         valor = input('Item: ')
#         lista.append(valor)
#         continue

#     if apagar:
#         indice = input('Escolha um índice: ')
#     # item_apagado = float(indice)

#     if listar:
#         print(next(lista_enumerada))
#         continue
#     else:
#         print('Não à nada para listar.')
#         continue
while True:
    opcao = input('Selecione uma opção \n   [i]nserir  [a]pagar  [l]istar: ')
    if opcao == 'i':
        # os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice = input('Escolha um índice para ser apagado: ')
        try:
            indice = int(indice)
            del lista[indice]
        except ValueError:
            print('Por favor digite um valor int.')
        except IndexError:
            print('índice não existente')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
