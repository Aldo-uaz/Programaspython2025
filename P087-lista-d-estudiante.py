# Procesar una lista de estudiantes usando una lista de diccionarios
# Se calcula la suma de los promedios y el promedio general del grupo


import os ; os.system('cls')

grupo = [
    {'Nombre':'Carlos','Edad':45,'Carrera':'Sistemas','Promedio':9},
    {'Nombre':'Rocio','Edad':35,'Carrera':'Sistemas','Promedio':10},
    {'Nombre':'jose','Edad':30,'Carrera':'Electronica','Promedio':8}
]
print(f'Grupo completo {grupo} - {len(grupo)}')
while True:
    print('\nDame los datos del estudiante')
    datos = {}
    Nombre = input('Nombre: ')
    if Nombre != '':
        datos['Nombre'] = Nombre
        datos['Edad']= int(input('Edad: '))
        datos['Carrera'] = input('Carrera: ')
        datos['Promedio'] = float(input('Promedio: '))
        grupo.append(datos)
    else:break
print(f'Grupo completo {grupo} - {len(grupo)}')
#imprimir una tabla con los datos de los autos
print('\nDatos de los autos en forma de tabla\n')
#imprimimos los encabezados
for llave in grupo[0].keys():
    print(f'{llave:<15}',end='')
print()
print('-'*50)

#imprimir cada uno de cada auto
for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<15}',end='')
    print()
print('-'*50)

suma = 0
for alumno in grupo:
    suma = suma + alumno['Promedio']
print(f'La suma de promedio es: {suma}')
print(f'El promedio del grupo es: {suma/ len(grupo)}')