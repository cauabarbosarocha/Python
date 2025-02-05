# Funções decoradas e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradas são funçoes que decoram outras funções
# Decoradoes são usados para fazer o Python
# usar as funções decoradas em outras funções.
# Decorações são "Syntax Sugar" (Açúcar Sintático)

def criar_funcao(func): # Função decoradora
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print("Estou decorando...")
        return resultado
    return interna

@criar_funcao # função própria do Python chamada de Syntax Sugar
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametrô deve ser uma string')

# inverte_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_checando_parametro('dfsa')
invertida = inverte_string('dfsa')
print(invertida)
