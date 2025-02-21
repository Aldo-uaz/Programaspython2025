# Dado 3 numeros enteros cual es el mayor

print('Dado 3 numeros enteros ¿Cual es el mayor? ')
print('Dame 3 numeros enteros: ')
n1, n2, n3 = int(input()),int(input()),int(input())

if n1 > n2 and n1 > n3:
    print(f'El {n1} es mayor que {n2} y {n3}')
elif n2 > n1 and n2 > n3:
    print(f'El {n2} es mayor que {n1} y {n3}')
else:
    print(f'El {n3} es mayor que {n1} y {n2}')