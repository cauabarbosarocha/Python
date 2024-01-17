"""
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
while True:
    nome = input('Digite seu nome ou "sair": ')
    
    if nome == 'sair':
        print('Saindo')
        break
    else:
        print(f'Seu nome é {nome}')

print('Você saiu')
