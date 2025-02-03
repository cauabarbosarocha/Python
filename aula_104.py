# Funções decoradas e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradas são funçoes que decoram outras funções
# Decoradoes são usados para fazer o Python
# usar as funções decoradas em outras funções.

def criar_funcao(func): # Função decoradora
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametrô deve ser uma string')

inverte_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_checando_parametro('dfsa')
print(invertida)
