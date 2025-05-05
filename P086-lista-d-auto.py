# usar una lista de diccionarios para almacenar los datos de diferentes autos
#calcular la suma de los años de cada auto
import os ; os.system('cls')

autos =[
    {'marca':'ford','modelo':'mustang','año':1964},
    {'marca':'vw','modelo':'jetta','año':2015},
    {'marca':'renault','modelo':'duster','año':2019}
]
print(f'Los autos : {autos} - {len(autos)}')
autos.append({'marca':'honda','modelo':'crv','año':2025})
print(f'Los autos : {autos} - {len(autos)}')

#iterar por cada elemento de la lista e impirimir cada uno de los diccionarios que la conforman
print('\nLos elementos (diccionarios) invididuales que contiene la lista:')
for auto in autos:
    print(auto)

#imprimir una tabla con los datos de los autos
print('\nDatos de los autos en forma de tabla\n')
#imprimimos los encabezados
for llave in autos[0].keys():
    print(f'{llave:<15}',end='')
print()
print('-'*40)

#imprimir cada uno de cada auto
for auto in autos:
    for v in auto.values():
        print(f'{v:<15}',end='')
    print()

# imprimir todos los datos de los autos en forma de regitro 1 a la vez
print(f'\nDatos en forma de registro, de los {len(autos)} autos: \n')
for auto in autos:
    for llave, valor, in auto.items():
        print(f'{llave:<12} : {valor}')
    print()