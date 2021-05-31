###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla
print(f'Métodos para listas: \n{dir(list)}\n')
print(f'Métodos para tuplas: \n{dir(tuple)}\n')

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
def diferencas_metodos():
    metodos_lista = dir(list)
    metodos_tupla = dir(tuple)

    metodos_diferentes = []
    for metodo in metodos_lista:
        if metodo not in metodos_tupla:
            metodos_diferentes.append(metodo)

    print(f'Métodos não existetes para a tupla: \n{metodos_diferentes}\n')

diferencas_metodos()

#3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.

professor1 = {'id': 42,'name': 'Alexandre Abreu','age': 30,'state_origin': 'Minas Gerais','courses': ['Inteligência Artificial','Mineração de Dados','Programação para Internet I','Programação para Internet II']}

professor2 = {'id': 37,'name': 'Denilson Barbosa','age': 40,'state_origin': 'Paraná','courses': ['Inteligência Artificial','Banco de Dados I','Banco de Dados II','Programação para Internet I']}

professor3 = dict(id=28, name='Jorge Armino', idade=37)

professor1['coordenadas'] = ('18574620', '75486135')
professor2['coordenadas'] = ('85647213', '07214963')
professor3['coordenadas'] = ('90457621', '10758942')

print('Coordenadas do professor 1: {}' .format(professor1['coordenadas']))
print('Coordenadas do professor 2: {}' .format(professor2['coordenadas']))
print('Coordenadas do professor 3: {}' .format(professor3['coordenadas']))
