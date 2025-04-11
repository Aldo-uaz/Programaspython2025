# El usuario introduce un numero hasta donde quiere saber los numeros imapres que tiene
# calcual e imprime la suma y el promedio de los numeros
# muestra los numeros que se pueden dividir entre 3 y los suma 
# puede el usuario pedir un elemento a buscar en la lista original y decir si esta y en que posicion

import os ; os.system('cls')
nums= []
nums2 = []
s = p = s3= 0
print('leyendo los elementos de la lista ')
n = int(input('Dame un numero: '))
for i in range(n):
    n=int(input(f'numero: [{i+1}]= '))
    if n %2 !=0: 
        nums.append(n)
    elif n % 3 == 0:
        nums2.append(n)
    else: print('>(')

print(f'\nLista: {nums}')
s = sum(nums)
p = s / len(nums)
s3= sum(nums2)
print(f'La suma es:                              {s}')
print(f'El promedio es:                          {p}')
print(f'\nnumeros divisibles entre 3: {nums2} y  su suma es {s3}')