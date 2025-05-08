# Crear un diccionario de llaves de cadena paises, con los siguientes elementos
#el cual podamos modificar sus elementos

import os; os.system('cls')

paises = {'Argentina':100,'Brasil':200,'Colombia':300,'Chile':400,'Ecuador':500,'Bolivia':600,'Jamaica':700}

print(f'El Diccionario es: {paises},\nSus elementos son: {len(paises)}')

paises ['Brasil'] = 250
paises ['Chile'] = 450
paises.update({'Bolivia':650})
paises.update({'Jamaica':750})

print('El Diccionario actualizado es:')
print('Paises-------- Valores')
for k, v in paises.items():
    print(f'{k:<13} : {v}')