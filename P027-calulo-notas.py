# Promedio de  5 calificaciones
import os ; os.system('clear')

print('Dame 5 calificaciones separadas por <enter>')
c1,c2,c3,c4,c5= int(input()),int(input()),int(input()),int(input()),int(input())

p = float((c1 + c2 + c3 + c4 + c5)/5)
print(f'Tus calificaciones son {c1,c2,c3,c4,c5} y tu promedio es {p:.1f}')
if p > 0 and p < 6:
    print('Estas Reprobado')
elif p >= 6 and p < 7:
    print('Pasas de Panzazo')
elif p >= 7 and p < 8:
    print('Muy bien, puedes mejorar')
elif p >= 8 and p < 9:
    print('Exelente sigue asi')
elif p >= 9 and p <= 10:
    print('Perfecto tu esfuerzo valio la pena')
else:
    print('Vuelve a intentar')