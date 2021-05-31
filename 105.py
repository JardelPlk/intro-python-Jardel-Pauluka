#DESAFIO!!!
#1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
#2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para #percorrer a lista ateh encontrar o primeiro multiplo de 5.
#OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.

###
# Exercicios
###

## Usando a lista: ['a','b','c']
# 1) Faca um loop dentro de uma funcao que irah retornar: ['A','B','C']
def maiuscula(lista):
    lista2 = []
    for i in lista:
        lista2.append(i.upper())
    return lista2

lista = ['a','b','c']
lista2 = maiuscula(lista)
for i in lista2:
    print(i)

## Usando a lista: [0, 1, 7, 4, 5]
# 2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas. A funcao deve receber a lista como parametro.
print()
def soma(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

lista = [0, 1, 7, 4, 5]
resultado = soma(lista)
print(resultado)

# 3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da lista recebida
print()
def impares(lista):
    lista_impares = []
    for i in lista:
        if i % 2 != 0:
            lista_impares.append(i)
    return lista_impares

lista = [1, 8, 10, 31, 22]
lista_impares = impares(lista)
for i in lista_impares:
    print(i)

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list comprehension e depois usando list comprehension.
print()
texto = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
i = 0
qtde = 0
for t in texto:
    if t == ' ':
        if i >= 5:
            qtde += 1
            i = 0
    i += 1
print(qtde)

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
print()
multiplos = [numero for numero in range(100) if numero % 3 == 0]
for i in multiplos:
    print(i)

# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for
print()
list = range(2,11)
cont = 0
for l in list:
    for n in range(1, l+1):
        if l % n == 0:
            cont += 1
    if cont > 2:
        print(l,'não é um número primo.')
    else:
        print(l,'é um número primo.')
    cont = 0
