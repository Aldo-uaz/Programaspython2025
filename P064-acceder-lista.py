# Ejemplificar el acceso a una lista de numeros

import os ; os.system('cls')
 
nums= [10,20,30,40,50,70,10,20,99] # se empieza a contar desde 0 en los elementos de la lista

print('Acceder a los elementos de una lista: ')
print(f'La lista completa es: {nums}, tiene {len(nums)} elementos')
print(f'Primer elemento : {nums[0]}, Ultimo elemento: {nums[8]}')
print(f'Primer elemento : {nums[-9]}, Ultimo elemento: {nums[-1]}')
print(f'Elementos del 2:6 : {nums[2:6]}')
print(f'Los primeros 3 : {nums[:3]}')
print(f'Los ultimos 3 : {nums[6:]}')