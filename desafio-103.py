#DESAFIO!!!
#Implemente um algoritmo para inverter a ordem de uma string em sua
#linguagem de programacao favorita. Nao use funcoes/metodos prontos.
print('Digite uma palavra: ')
palavra = input()
tamanho = len(palavra)
palavra_invertida = []
while tamanho:
    tamanho -= 1
    palavra_invertida.append(palavra[tamanho])
palavra_invertida = ''.join(palavra_invertida)
print(palavra_invertida)
