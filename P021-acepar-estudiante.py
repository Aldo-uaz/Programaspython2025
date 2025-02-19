# Aceptacion de estudiante a la universidad dependiendo su edad y sus calificaciones

import os; os.system('celar')

print('Registro de aceptacion a la Universidad de AAOL SA de CV')
nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))
if edad < 18:
    print('SOLO ACEPTAMOS MAYORES DE 18 AÑOS, LO SENTIMOS.')
else:
    print('Dame dos calificaciones separadas por enter: ')
    c1, c2 = int(input()),int(input())
    if c1 < 8 or c2 < 8:
        print('Cumples con solo el requisito de la edad, otro de nuestros requisitos')
        print('es que las calificaciones sean mayores a 8, lo sentimos')
    else:
        print('Felicidades')
        print(f'{nombre} Le damos la bienvenida a la Universidad AAOL \ntu edad {edad} y tus calificaciones {c1} y {c2}')
        print('Cumplen con nuestros requisitos de nuevo ingreso')