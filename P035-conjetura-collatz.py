# Calcula la conjetura de collatz
while(True):
    import os; os.system('clear')

    print('Imprime la conjetura de Collatz')

    n= int(input('Dame un numero entero positivo ?'))
    c=0
    while n !=1 :
        print(n, end= ' ')
        c += 1
        if n% 2 == 0:
            n=n//2
        else:
            n=n*3+1
    print(n,end=' ')
    print( '\n pasos:', c)
    if input('Deseas continuar (S/N) ?').upper() == 'N' : break
print('Proceso terminado')