# Crear un diccionario de llave numeria dias

import os; os.system('cls')

semana = {1:'Lunes',2 :'Martes',3:'Miercoles',4 :'Jueves',5:'Viernes',6:'Sabado',7:'Domingo'}
print(f'El diccionario:{semana},\nElementos: {len(semana)}')

d = semana[1]
print(f'\nEl primer elemento es: {d}')
df = semana[7]
print(f'\nEl ultimo elemento es: {df}')

print(f'\nEl quinto elemento es: {semana.get(5)}')
print(f'\nEl Septimo elemento es: {semana.get(7)}')

print('Numero ----------- Dia')
for k, v in semana.items():
    print(f'   {k:<13} : {v}')