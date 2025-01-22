# Entendendo os seus próporios módulos em Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outros módulos inteiros ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__
# por padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula_63

print('Este módulo se chama', __name__)
