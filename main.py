"""
    Introdução ao try/excepet
    try    -> tentar executar o código
    except -> ocorreu algum erro ao tentar executar
"""
numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print(f'str: {numero_str}')
    numero_float = float(numero_str)
    print(f'float: {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     print(f'O dobro de {numero_str} é {float(numero_str) * 2:.2f}')
# else:
#     print('O valor digitado não é um número')
# print(numero_str.isdigit)
