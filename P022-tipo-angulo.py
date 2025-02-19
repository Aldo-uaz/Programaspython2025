# Dado un angulo de 0 a 360, se mostrara el tipo de angulo

print('Mostrando el tipo de angulo en base a los grados')
a = int(input('Dame un angulo de 0 a 360: '))
print(f'El angulo tiene {a} grados por lo tanto es un angulo: ', end='')
if a < 90:
    print('Agudo')
elif a == 90:
    print('Recto')
elif a > 90 and a < 180 :
    print('Obtuso')
elif a == 180:
    print('Llano')
elif a > 180 and a < 360:
    print('Concavo')
else:
    print(f'Angulo {a} fuera de rango de 0 a 360')