# Multiplica dos listas de n numeros introducidas por el usuario

import os ; os.system('cls')
lista1=[]
lista2=[]
lista3=[]
MAX = 5
n = 0
print('Multiplicar los elementos de dos listas')
print('leyendo los elementos de la lista 1')

for i in range(MAX):
    n=int(input(f'lista1[{i+1}]= '))
    lista1.append(n)

print('\nleyendo los elementos de la lista 2\n')

for i in range(MAX):
    n=int(input(f'lista2[{i+1}]= '))
    lista2.append(n)
print(f'\nLista 1: {lista1}')
print(f'\nLista 2: {lista2}')

for i in range(MAX):
    lista3.append(lista1[i] * lista2[i])
print(f'\nLista 3: {lista3}')