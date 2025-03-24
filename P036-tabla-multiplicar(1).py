## Imprime la tabla de multiplicar de t hata n
while(True):
    import os
    os.system('clear')
    print('Imprimiendo tabla de multiplicar \n')
    t= int(input('Que tabla quieres ? '))
    n = int(input('Hasta donde ? '))
    k = 1
    while k <= n:
        print(f'{t} X {k} = {t * k}')
        k +=1
    if input('Deseas continuar (S/N) ?').upper() == 'N' : break
print('Proceso terminado')