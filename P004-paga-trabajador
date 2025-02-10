# Calcualar la paga total de un trabajador en base a las horas trabajadas y a la paga por hora
# entrada: nombre, horas, paga
# salida : paga bruta (antes de impuesto), impuesto (paga*impuesto), paga neta (paga despues del impiesto)

print('Calculando la paga de un trabajador \n')

# Entrada de datos
nombre = input('Nombre del trabajador : ')
horas  = int(input ('Horas trabajadas : '))
paga   = float(input('Paga X hora trabajada : '))
tasa   = 0.03

# Calculos
pagabruta= horas * paga
impuesto = pagabruta*tasa
paganeta = pagabruta-impuesto
# Salida
print('\n Resumen de pagos')
print(f'El trabajador {nombre}, trabajo {horas} horas, a una paga de {paga} pesos, a una tasa {tasa} de impuesto ')
print(f'Paga bruta (antes de impiesto) : {pagabruta:,.2f}')
print(f'Impuesto                       : {impuesto:,.2f}')
print(f'Paga neta (despues de impiesto): {paganeta:,.2f}')
