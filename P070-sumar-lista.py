# Suma dos listas de n numeros introducidas por el usuarii

import os ; os.system('cls')
lista1=[]
lista2=[]
lista3=[]
MAX = 4
n = 0
print('Suamr los elementos de dos listas')
print('leyendo los elementos de la lista 1')

for i in range(MAX):
    n=int(input(f'\nlista1[{i+1}]= '))
    lista1.append(n)
print(f'\nLista 1: {lista1}')

for i in range(MAX):
    n=int(input(f'\nlista2[{i+1}]= '))
    lista2.append(n)
print(f'\nLista 2: {lista2}')

for i in range(MAX):
    lista3.append(lista1[i] + lista2[i])
print(f'\nLista 3: {lista3}')