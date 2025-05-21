# Convierte una temperatura de grados Celsius a Fahrenheit y viceversa.

import os

def farenheit(t): # Convierte de Celsius a Fahrenheit
    r = (t * 9 / 5) + 32
    return r
def celsius(t): # Convierte de Fahrenheit a Celsius
    r = (t - 32) * 5 / 9
    return r
os.system('cls')
print('Convertidor de temperatura')
print('[F] farenheit a Celsius')
print('[C] Celsius a Farenheit')
opcion = input('Opcion: ')
if opcion == 'F':
    t = float(input('Temperatura en Farenheit: '))
    print(f'{t} Farenheit son {celsius(t)} Celsius') # llama a la funcion celsius
elif opcion == 'C':
    t = float(input('Temperatura en Celsius: '))
    print(f'{t} Celsius son {farenheit(t)} Farenheit') # llama a la funcion farenheit
else:
    print('Opcion no valida')
# Fin del programa
print('Gracias por usar el convertidor de temperatura')
