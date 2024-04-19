"""
Closure e funções que retornam outras funções
"""
def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = saudacao('Bom dia')
falar_boa_noite = saudacao('Boa noite')

for nomes in ['Cauã', 'Jorge', 'Tom']:
    print(falar_bom_dia(nomes))
    print(falar_boa_noite (nomes))
