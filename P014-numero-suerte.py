# Calculando el numero de la suerte

# Solicitar el año de nacimiento al usuario
a = int(input('Introduce tu año de nacimiento en 4 dígitos: '))

# Separar los dígitos individuales
d1 = a // 1000         # Primer dígito
d2 = (a // 100) % 10  # Segundo dígito
d3 = (a // 10) % 10   # Tercer dígito
d4 = a % 10            # Cuarto dígito

print('Calculando su numero de la suerte')
num_suerte = d1 + d2 + d3 + d4

print(f"Dígitos individuales del año: ")
print(f'Primer numero:  {d1}')
print(f'Segundo numero: {d2}')
print(f'Tercer numero:  {d3}')
print(f'Cuarto numero:  {d4}')
print(f"Suma de los dígitos: {num_suerte}")

