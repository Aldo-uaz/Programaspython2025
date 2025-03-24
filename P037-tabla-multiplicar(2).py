## Imprime las tablas de 1 a n, hasta el 10
while(True):
    import os
    os.system('clear')
    n= int(input('Hasata que tabla quieres ? '))
    m= int(input('Hasta donde? '))
    t = 1
    while t <= n:
        print(f'\n Tabla {t}\n')

        c = 1
        while c <= m:
            print(f'{t} X {c} = {t * c}')
            c += 1
        t += 1
    if input('Deseas continuar (S/N) ?').upper() == 'N' : break
print('Proceso terminado')