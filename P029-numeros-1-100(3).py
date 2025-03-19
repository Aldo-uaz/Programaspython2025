# Imprime numeros del 1 a n

c = 0
n = int (input('Hasta donde? '))
d = int (input('Incremento? '))

while c <= n:
    print(c, end= ' ')
    c += d
else :
    print('\n Valor final de c', c)
print('\n' "Proceso terminado")