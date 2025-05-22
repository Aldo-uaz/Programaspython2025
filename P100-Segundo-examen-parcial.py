# Se desea procesar los empleados de una empresa de muebles, para lo cual deberá solicitar al usuario los datos:
import os ; os.system('cls')
# Tomando los datos de los empleados
# nombre, edad, sexo, pasatiempos y sueldo
print('Mueblería Muebles Dico')
print('Sistema de Procesamiento de Empleados')
print('Captura de datos de los empleados (* para terminar):\n')

empleados = []

while True:
    nombre = input('Nombre (* para terminar): ')
    if nombre == '*':
        print('Captura de datos terminada.')
        break
    edad = int(input('Edad: '))
    sexo = input('Sexo (h/m): ').lower()
    pasatiempos = input('Pasatiempos (separados por coma): ').lower()
    sueldo = float(input('Sueldo: '))

    empleado = {
        'nombre': nombre,
        'edad': edad,
        'sexo': sexo,
        'pasatiempos': [p.strip() for p in pasatiempos.split(',')], # separar por comas y quitar espacios y la convierte a lista
        'sueldo': sueldo
    }
    empleados.append(empleado)

print('\nDatos guardados en la lista de diccionarios:')
print(empleados)

print('\nTabla de los datos de los empleados:')
print(f'{'Nombre':<10} {'Edad':<5} {'Sexo':<6} {'Sueldo':<10} {'Pasatiempos':<5}')
for e in empleados:
    print(f'{e['nombre']:<10} {e['edad']:<5} {e['sexo']:<6} ${e['sueldo']:<10,.2f} {', '.join(e['pasatiempos'])}') # .join() une los elementos de la lista con una coma y un espacio

# Procesamiento de resumen
total_empleados = len(empleados)
hombres = 0
mujeres = 0
pasatiempos_total = {}
suma_edades = 0
suma_sueldo = 0
mayor = None
menor = None # se pone None para que no de error al comparar, porque si ponemos 0 no se puede comparar con la edad

for e in empleados:
    if e['sexo'] == 'h':
        hombres += 1
    elif e['sexo'] == 'm':
        mujeres += 1

    suma_edades += e['edad']
    suma_sueldo += e['sueldo']
# el ciclo for de abajo recorre la lista de pasatiempos y cuenta cuantas veces se repite cada uno
# y lo guarda en un diccionario
    for p in e['pasatiempos']:
        if p in pasatiempos_total:
            pasatiempos_total[p] += 1
        else:
            pasatiempos_total[p] = 1

    if mayor is None or e['edad'] > mayor['edad']: # si mayor es None o la edad del empleado es mayor que la edad del mayor
        mayor = e # se guarda el empleado con la mayor edad
    if menor is None or e['edad'] < menor['edad']: # si menor es None o la edad del empleado es menor que la edad del menor
        menor = e # se guarda el empleado con la menor edad

promedio_edad = suma_edades / total_empleados 
promedio_sueldo = suma_sueldo / total_empleados 

print('\nResumen:')
print(f'Empleados : {total_empleados}')
print(f'Mujeres   : {mujeres}')
print(f'Hombres   : {hombres}')

print('Pasatiempos:', end=' ')
print(', '.join([f"{k}/{v}" for k, v in pasatiempos_total.items()])) # separar por comas y un espacio y lo muestra en el formato k/v

print(f'Edad -> suma: {suma_edades}, promedio: {promedio_edad:.1f}')
print(f"Sueldo -> suma: ${suma_sueldo:,.2f}, promedio: ${promedio_sueldo:,.2f}")
print(f"{mayor['nombre']} de {mayor['edad']} es el mayor, {menor['nombre']} de {menor['edad']} es el menor.")
