# Cree un diccionario de llaves de cadena municipios, con los siguientes elementos
# el cual podamos eliminar sus elementos

import os; os.system('cls')

municipios = {'Apozol':1863,'Calera':1868,'Fresnillo':1554,'Guadalupe':1821,'Jalpa':1824,'Jerez':1824,'Loreto':1931,'Mazapil':1824,'Momax':1857}
print(f'El Diccionario es: {municipios}\nSus elementos son: {len(municipios)}')
a = municipios.pop('Apozol')
c = municipios.pop('Fresnillo')
m = municipios.popitem()
print(f'El Diccionario actualizado es:')
print('Municipios--- Valores')
for k, v in municipios.items():
    print(f'{k:<13} : {v}')
municipios.clear()
print(f'\nEl Diccionario es: {municipios}\nSus elementos son: {len(municipios)}')