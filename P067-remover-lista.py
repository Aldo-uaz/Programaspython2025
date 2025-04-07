# Quitar un elemento de una lista que no se necesite

import os ; os.system('cls')

print('Quitar elementos a una lista existente')
nums= [1,3,5,7,9,11,99,15,88,19,100]
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')

print('Quitar la primer ocurrencia de un elemento usando el metodo remove()')
nums.remove(99)
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')

print('Quitar elemento en una posicion determinada y gusrdarlo usando el metodo pop()')
num= nums.pop(8)
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos, elemento removido {num}')

print('Quitar el ultimo elemento y gurdarlo usando el metodo pop()')
num= nums.pop()
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos, elemento removido {num}')

print('Quitar elemento en una posicion determinada usando el metodo del[:]')
del nums [2:5]
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')

print('Quitar elementos al final de la lista usando el metodo clear()')
nums.clear()
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')