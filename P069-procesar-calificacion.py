#Procesar n calificaciones introducidas por el usuario


import os; os.system('cls')
print('Procesamiento de calificaciones')
nums = []
mp = []
n = s = p = 0
while n != 99:
    n = float(input('Calificaciones [1-10] -->'))
    if n > 0 and n <= 10:
        nums.append(n)
    else: print('>(')
nums.sort()

print(f'\nFin > {nums} \nLa longuitid es:  {len(nums)}')
s= sum(nums)
p = s/ len(nums)

for n in nums:
    if n >= p:
        mp.append(n)


print('\n\nLa estadistica es:')
print(f'La suma es:                              {s}')
print(f'El promedio es:                          {p}')
print(f'Mayor o igual al promedio > {mp}\nLa longuitid es: {len(mp)}')
