# Exercício - Sistema de perguntas e respostas

perguntas = [
    {
        'perguntas': 'Quem descobriu o Brasil?',
        'opções': ['Peter Parker', 'LVCAS', 'Dio Brando', 'Pedro Alvares Cabral'],
        'resposta': 'Pedro Alvares Cabral'
    },
    {
        'perguntas': 'Qual o valor de X (4x + 2 = 38)?',
        'opções': [9, 13, 5, 40],
        'resposta': 9
    },
    {
        'perguntas': 'Qual a forma correta do verbo "haver" no pretérito perfeito?',
        'opções': ['Houveram', 'Houve', 'Houver', 'Houverão'],
        'resposta': 'Houve' # Caso esteja errado, culpe o ChatGPT, não tive criatividade para elaborar uma terceira pergunta
    }
]

pergunta_1 = perguntas[0].get('perguntas')
opcoes_1 = perguntas[0].get('opções')
resposta_1 = perguntas[0].get( 'resposta')

print(pergunta_1)

alternativas_questao_1 = range(len(opcoes_1))
for alternativa_1 in alternativas_questao_1:
    print(alternativa_1, opcoes_1[alternativa_1])

resposta_user_1 = int(input('Digite entres os números 0, 1, 2, 3 para dar a resposta: '))
if resposta_user_1 == 3:
    print('Certa resposta.')
else:
    print('Ops!! Resposta errada, tente novamente')

pergunta_2 = perguntas[1].get('perguntas')
opcoes_2 = perguntas[1].get('opções')
resposta_2 = perguntas[1].get( 'resposta')

print(pergunta_2)

alternativas_questao_2 = range(len(opcoes_2))
for alternativa_2 in alternativas_questao_2:
    print(alternativa_2, opcoes_2[alternativa_2])

resposta_user_2 = int(input('Digite entres os números 0, 1, 2, 3 para dar a resposta: '))
if resposta_user_2 == 0:
    print('Certa resposta.')
else:
    print('Ops!! Resposta errada')

pergunta_3 = perguntas[2].get('perguntas')
opcoes_3 = perguntas[2].get('opções')
resposta_3 = perguntas[2].get( 'resposta')

print(pergunta_3)

alternativas_questao_3 = range(len(opcoes_3))
for alternativa_3 in alternativas_questao_3:
    print(alternativa_3, opcoes_3[alternativa_3])

resposta_user_3 = int(input('Digite entres os números 0, 1, 2, 3 para dar a resposta: '))
if resposta_user_3 == 1:
    print('Certa resposta.')
else:
    print('Ops!! Resposta errada')
