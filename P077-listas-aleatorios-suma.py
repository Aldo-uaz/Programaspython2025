# Se genera dos listas de numeros aleatorios y la suma los elementos que son impares una tercera lista

import os ; os.system('cls')
import random
lista1=[]
lista2=[]
lista3=[]
MAX=10
print('Se genera dos listas de numeros aleatorios y la suma en una tercera lista')
print('generando dos listas de numeros aleatorios')
for n in range(MAX):
    lista1.append(random.randint(1,10))
    lista2.append(random.randint(1,10))
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print('\nLa suma de los impares')
for i in range(MAX):
    if lista1[i] % 2 !=0 and lista2[i] % 2 !=0:
        lista3.append(lista1[i]+ lista2[i] )

print(f'Lista 3: {lista3}')

