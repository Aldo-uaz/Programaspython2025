# Mostras las operaciones de conjuntos que se pueden realizar con conjuntos

import os; os.system('cls')
c1={1,2,3,4,5}
c2 ={5,6,7,8,9,10}
c3 = {9,10,11,12,13}
c4 = {3,4,5}
print('Ejemplificando las operaciones de conjuntos')
print(f'C1: {c1}')
print(f'C2: {c2}')
print(f'C3: {c3}')
print(f'C4: {c4}')
print('Union de conjuntos')
print(f'C1 U C2: {c1.union(c2)}')
print(f'C1 U C3: {c1 | c3}')
print('\nInterseccion de conjuntos')
print(f'C1 n C2: {c1.intersection(c2)}')   
print(f'C1 n C3: {c2 & c3}') 
print('\nDiferencia de conjuntos')
print(f'C1 - C4: {c1.difference(c4)}')
print(f'C2 - C3: {c2 - c3}')
print('\nDiferencia simetrica de conjuntos')
print(f'C1 ^ C2: {c1.symmetric_difference(c2)}')
print(f'C2 ^ C3: {c2 ^ c3}')
print('\nSubconjuntos')
print(f'C4 es subconjunto de C1: {c4.issubset(c1)}')
print(f'C1 es subconjunto de C4: {c3 <= c2}')
print('\nSuperconjuntos')
print(f'C1 es superconjunto de C4: {c1.issuperset(c4)}')
print(f'C2 es superconjunto de C3: {c2 >= c3}')
print('verificando la presencia de un elemento en un conjunto')
print(f'5 en C1: {5 in c1}')
print(f'5 en C2: {5 in c2}')