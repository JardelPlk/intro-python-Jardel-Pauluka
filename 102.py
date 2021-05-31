#########
# Exercicios - Listas
# Faca sem usar loops
#########

weekdays = ['mon','tues','wed','thurs','fri']
print(weekdays)

days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')
print(days_list)

list = ['a', 1, 3.14159265359]
print(list)

# Como selecionar 'wed' pelo indice?
print(weekdays[2])

# Como verificar o tipo de 'mon'?
print(type(weekdays[0]))

# Como separar 'wed' até 'fri'?
print(weekdays[2:5])

# Quais as maneiras de selecionar 'fri' por indice?
print(weekdays[4])
print(weekdays[-1])

# Qual eh o tamanho dos dias e days_list?
print('Dia 1:', len(days_list[0]), '\nDia 2:', len(days_list[1]), '\nDia 3:', len(days_list[2]), '\nDia 4:', len(days_list[3]), '\nDia 5:', len(days_list[4]), '\nDia 6:', len(days_list[5]), '\nDia 7:', len(days_list[6]), '\nQuantidade de dias na lista = ',len(days_list))

# Como inverter a ordem dos dias?
print(weekdays[::-1])

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1,'zero')
print(list)

# Como limpar list?
list.clear()
print(list)

# Como deletar list?
del list

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
list = ['a', 1, 3.14159265359]
ultimo_elemento = list.pop()
print(ultimo_elemento)
