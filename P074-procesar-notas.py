# Leer n notas hasta introduccir un 0
import os ; os.system('cls')

print('Procesamiento de notas')
notas = []
mp = []
s = p = 0
n=1
while n !=0:
    n = float(input('Notas [0-100] -->'))
    if n > 0 and n <= 100:
        notas.append(n)
    else: print('>(')
notas.sort()

print(f'\nFin > {notas} \nLa longuitid es:  {len(notas)}')
s = sum(notas)
p = s / len(notas)

for n in notas:
    if n < p:
        mp.append(n)


print('\n\nLa estadistica es:')
print(f'Los numeros son: {notas}')
print(f'La suma es:                              {s}')
print(f'El promedio es:                          {p}')
print(f'Menor al promedio > {mp}\nLa notas menores son: {len(mp)}')
print(f'La nota minima es: {min(notas)}')
print(f'La nota maxima es: {max(notas)}')