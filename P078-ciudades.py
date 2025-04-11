# El usuario introduce nombres de ciudades

import os ; os.system('cls')

ciudades = []
print('El usuario introduce nombres de cuidades')
while(True):
    ciudad = input('Ciudad: ')
    if ciudad=='$':
        break
    ciudades.append(ciudad)

print(f'ciudades: {ciudades}, se introdujeron: {len(ciudades)} ciudades')

ciudades.sort(reverse=True)
print("\nLista ordenada en orden descendente:", ciudades)

consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
ciudades_con_consonante = [c for c in ciudades if c.startswith(tuple(consonantes))]

print(f"\nNúmero de ciudades que empiezan con consonante: {len(ciudades_con_consonante)}")
print("Ciudades con consonante inicial:", ciudades_con_consonante)