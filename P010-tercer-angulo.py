# Calcualndo el tercer angulo de un triangulo

print('Calcuando el tercer angulo de un triangulo con dos angulos ')
print('Dame dos aungulos separados por un espcio')

A1, A2 = input().split()
A1, A2 = int(A1), int(A2)

A3 = 180 - (A1 + A2)

print(f'El tercer angulo del triangulo con los angulos {A1}, {A2} es de : {A3}')