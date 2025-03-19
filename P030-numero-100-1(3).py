# Imprime numeros del n a 1


n = int (input('Hasta donde? '))
d = int (input('Decremento? '))
c = n
while c >= 1:
    print(c, end= ' ')
    c -= d
else :
    print('\n Valor final de c', c)
print('\n' "Proceso terminado")