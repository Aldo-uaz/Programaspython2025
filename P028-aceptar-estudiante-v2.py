# Aceptacion de estudiantes para La Universidad Kitty Kat SA

print('Aceptacion de estudiantes para La Universidad Kitty Kat SA')
n = input('Dame tu nombre: ')
s = input('Sexo h o m: ')
e = int(input('Dame tu edad: '))
print('Dame 3 calificaciones: ')
c1,c2,c3 = int(input()),int(input()),int(input())
p = float((c1+c2+c3)/3)
if s.lower() != 'm':
   print(f'{n}, solo aceptamos mujeres')
elif e <= 21:
   print(f'{n}, eres mujer, pero no tienes la edad, solo aceptamos mayores de 21')
elif p < 8 or p > 9.5:
   print(f'{n}, eres mujer, tienes la edad {e}, pero no tienes el promedio, solo aceptamos promedios de 8 a 9.5')
else:
   print(f'{n}, Has sido aceptada, tu edad {e} y tu promedio {p}, lo permiten.\nBienvenida a La Universidad Kitty Kat SA ')