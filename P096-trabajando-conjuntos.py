# Muestra las operaciones básicas con conjuntos

import os; os.system('cls')

muns={'Zacatecas','Guadalupe','Fresnillo','Jerez','Fresnillo'}
print('Ejempificando las operaciones básicas con conjuntos')
print(f'Conjunto de municipios: {muns} - {len(muns)}  ')

print('Lista de municipios usando un ciclo:')
for mun in muns:
    print(mun, end=' ')
print('Zacatecas esta en el conjunto de municipios:', 'Zacatecas' in muns)

print('Agregando un elemento al conjunto')
muns.add('Teul')
print(f'Conjunto de municipios: {muns} - {len(muns)}  ')

print('Agregando varios elementos al conjunto')
otros = {'Luis moya','Ojocaliente','Tepetongo'}
muns.update(otros)
print(f'Conjunto de municipios: {muns} - {len(muns)}  ')

print('Eliminando un elemento del conjunto')
muns.remove('Zacatecas') # genera error si no existe el elemento
muns.discard('Ojocaliente') # no genera error si no existe el elemento
muns.pop() # elimina el primer elemento del conjunto
print(f'Conjunto de municipios: {muns} - {len(muns)}  ')

print('Elimando todos los elementos del conjunto')
muns.clear()
print(f'Conjunto de municipios: {muns} - {len(muns)}  ')