# Revisar si los numeros son consecutivos.

print('Revisando si  3 numeros enteros son cosecutivos o no. ')
print('Dame 3 numeros enteros: ')
n1, n2, n3 = int(input()),int(input()),int(input())

if n1 - n2 == -1 and n2 - n3 == -1:
    print('Los numeros son consecutivos.')
else:
    print('Error: Los numeros no son cosecutivos')