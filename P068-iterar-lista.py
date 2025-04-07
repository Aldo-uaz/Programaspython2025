# Ejemplificar como se iterar sobre una lista de numeros

import os ; os.system('cls')

print('Diferentes formas de iterar (pasar por los elementos a una lista) existente')
nums= [2,4,6,8,10,12,14,16]
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')

print('\n\n1.Iterar sobre la lista, usando un ciclo for sin subindice')
for n in nums:
    print(n, end= ' ')
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')

print('\n\n2.Iterar sobre la lista, usando un ciclo for con subindice')
for _ in range( len(nums)):
    print( nums[_], end= ' ')
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')

print('\n\n1b. Iterar sobre la lista, imprimir cada valor sumandole 2')
for n in nums:
    print(n+2, end= ' ')
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')

print('\n\n2b.Iterar sobre la lista, usando el subindice para modificat cada elemento y elevarlo al cuadrado')
for _ in range( len(nums)):
    print( nums[_], end= ' ')
    nums[_] = nums [_] **2
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')