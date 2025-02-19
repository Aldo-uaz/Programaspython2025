# Calcular la 2da ley de newton dada la fuerza, la masa o la aceleracion

import os; os.system('clear')

print('Calcula los calores de la segunda ley de newton')
print('Para calculas la fuerza presiona [1]')
print('Para calculas la masa presiona [2]')
print('Para calculas la aceleracion presiona [3]')

op=int(input('Selecciona una opcion: '))

if op == 1:
    print('Cacluando la fuerza...')
    m = float(input('Dame la masa: '))
    a = float(input('Dame la aceleracion: '))
    f = m * a
    print(f'La fuerza es {f:.2f}, de la masa {m} y la aceleracion {a}')
elif op == 2:
    print('Cacluando la masa...')
    f = float(input('Dame la fuerza: '))
    a = float(input('Dame la aceleracion: '))
    m = f / a
    print(f'La masa es {m:.2f}, de una fuerza de {f} y una aceleracion de {a}')
elif op == 3:
    print('Cacluando la aceleracion...')
    f = float(input('Dame la fuerza: '))
    m = float(input('Dame la masa: '))
    a = f / m
    print(f'La aceleracion es {a:.2f}, de una fuerza de {f} y una masa de {m}')
else:
    print('Opcion invalida, intenta seleccionar un numero del 1 al 3')