# Exercício - Sistema de perguntas e respostas

perguntas = [
    {
        'perguntas': 'Quem descobriu o Brasil?',
        'opções': ['Peter Parker', 'LVCAS', 'Dio Brando', 'Pedro Alvares Cabral'],
        'resposta': 'Pedro Alvares Cabral'
    },
    {
        'perguntas': 'Qual o valor de X (4x + 2 = 38)?',
        'opções': ['9', '13', '5', '40'],
        'resposta': '9'
    },
    {
        'perguntas': 'Qual a forma correta do verbo "haver" no pretérito perfeito?',
        'opções': ['Houveram', 'Houve', 'Houver', 'Houverão'],
        'resposta': 'Houve' # Caso esteja errado, culpe o ChatGPT, não tive criatividade para elaborar uma terceira pergunta
    }
]

def perguntar_responder(pergunta, opcoes, resposta_certa):
    print(pergunta)
    for i, alternativas in enumerate(opcoes):
        print(f'{i}) {alternativas}')

    resposta_user = int(input("Digite o número da alternativa correta: "))

    if opcoes[resposta_user] == resposta_certa:
        print('Você acertou, parabêns!!')
    else:
        print('Resposta errada, tente novamente no fim das perguntas.')

for pergunta in perguntas:
    perguntar_responder(pergunta['perguntas'], pergunta['opções'], pergunta['resposta'])
