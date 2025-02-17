# Calcualndo la paga de un trabajador considerando que las horas extras se pagan dobles

import os; os.system('clear')

print('Calcualndo la paga de un trabajador considerando que las horas extras se pagan dobles')

nombre = input('Nombre del trabajador ? ')
horas = int(input('Horas trabajadas ? '))
paga = float(input('Paga x hora ? '))
pextra = extra = total = 0
if horas > 40:
    extra = horas - 40
    pextra = extra * (2 * paga)
    total = (40 * paga ) + pextra
else :
    total = paga * horas


print(f'{nombre} trabajo {horas} horas, con una paga de {paga} pesos, paga extra {pextra} pesos, pago total {total}')