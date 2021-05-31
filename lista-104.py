###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
def lista_igual(lista1, lista2):
    if lista1 == lista2:
        return True
    else:
        return False

print('Digite quantos elementos terá as duas listas: ')
qtde_elementos = input()
lista1 = []
i = 0
while (i < int(qtde_elementos)):
    print('Digite o',i,'elemento da lista 1: ')
    lista1.append(input())
    i += 1

print()
lista2 = []
i = 0
while (i < int(qtde_elementos)):
    print('Digite o',i,'elemento da lista 2: ')
    lista2.append(input())
    i += 1

print()
resultado = lista_igual(lista1, lista2)
print(resultado)

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
# OBS.: Utilize apenas o que foi estudado ate agora
def comparacao_strings(palavra1, palavra1_invertida, palavra2, palavra2_invertida):
    if palavra1 == palavra1_invertida and palavra2 == palavra2_invertida:
        print(True)
    else:
        print(False)

print('Digite duas strings: ')

palavra1 = input()
palavra2 = input()

palavra1_comparacao = palavra1.replace(' ', '')
palavra1_comparacao = palavra1_comparacao.lower()
palavra1_comparacao_invertida = palavra1_comparacao[::-1]

palavra2_comparacao = palavra2.replace(' ', '')
palavra2_comparacao = palavra2_comparacao.lower()
palavra2_comparacao_invertida = palavra2_comparacao[::-1]

resposta = comparacao_strings(palavra1_comparacao, palavra1_comparacao_invertida, palavra2_comparacao, palavra2_comparacao_invertida)
print('\n'+resposta)
