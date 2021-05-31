#DESAFIO!!!
#1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
print('Digite o conteúdo de duas variaveis: ')
x = input()
y = input()
z = x
x = y
y = z
print('Conteúdo das variaveis trocadas: x = '+x+' y = '+y)

#2) Agora faca sem utilizar uma terceira variavel temporaria.
#OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
print('\nDigite o conteúdo de duas variaveis: ')
x = input()
y = input()
x, y = y, x
print('Conteúdo das variaveis trocadas: x = '+x+' y = '+y)
