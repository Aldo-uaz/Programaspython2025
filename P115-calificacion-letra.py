# Ejemplificar de una funcion que recibe un parametro y retorna dos valores
import os
# Ejemplificar el uso de una funcion que recibe un parametro y retorna dos valores
def calificacion_letra(p):
    l=''
    m=''
    if p >= 90 and p <= 100:
        l = 'A'
        m = 'Excelente'
    elif p >= 80 and p < 90:
        l = 'B'
        m = 'bien'
    elif p >= 70 and p < 80:
        l = 'C'
        m = 'Suficiente'
    elif p >= 60 and p < 70:
        l = 'D'
        m = 'Deficiente'
    elif p >= 0 and p < 60:
        l = 'F'
        m = 'Reprobado'
    return l, m

os.system('cls')
print('Dame tu promedio y te dare tu calificacion con letra y un mensaje')
while True:
    p = float(input('Promedio: '))
    if p >= 0 and p <= 100:
        break
l, m = calificacion_letra(p)
print(f'Tu promedio de {p} tiene una calificacion de letra: {l} y el mensaje es: {m}')