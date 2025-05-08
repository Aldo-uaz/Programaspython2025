# Agregar un diccionario de llaves de cadena, ventanas, con los siguientes elementos
# el cual podamos agregar, modificar

import os; os.system('cls')
clientes = {'Juan':1550,'Jose':2600,'Maria':2220}
print(f'El Diccionario es: {clientes},\nSus elementos son: {len(clientes)}')
clientes ['Rocio'] = 2700
clientes['Mateo'] = 1567
clientes.update({'Andrea':9567})
clientes.update({'Migel':1234})
print('El Diccionario actualizado es:')
print('Clientes------ Ventas')
for k, v in clientes.items():
    print(f'{k:<13} : {v}')
print(f'\nSus elementos son: {len(clientes)}')