# Dadas dos listas, los dias de la semana y la paga, encontrar la paga correcpondiente

import os ; os.system('cls')

dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
paga = [700,600,500,400,300,200,100]
pos = total = 0
print('Dadas dos listas, los dias de la semana y la paga, encontrar la paga correcpondiente')

while(True):
    dia = input('Dia de la semana de lunes a domingo: ').lower() # transforma las letras mayusculas en minusculas
    if dia in dias: break
print(f'Elegiste trabajar el: {dia}')
pos = dias.index(dia)

if pos==5 or pos==6:
    total = paga[pos] * 4
else:
    total = paga[pos]
print(f'Paga = {total}')