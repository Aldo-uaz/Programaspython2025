#Examen parcial, inscripcion a un evento academico

import os; os.system('cls')
sumatotal=0
while(True):
    
    print('Universidad Patito SA de CV')
    print('Sistema de Inscripción Congreso de Sistemas \n')
    tu=int(input('Tipo de usiario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500:    '))
    tp=int(input('Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con Kit de acceso $900:    '))
    c=int(input('Cuantos paquetes gustas comprar?   '))
    sum=total=0
    if tu==1:
        a=100
        if tp==1:
            cp=600
            sum=(a+cp)*c
            if sum > 5000:
                to= sum *0.20
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Alumno y tu paquete es Solo conferencia y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 20% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Alumno y tu paquete es Solo conferencia y los paquetes que compraste son: {c} \nTu total es: {sum}')
            
        elif tp==2:
            cp=800
            sum=(a+cp)*c
            if sum > 5000:
                to= sum *0.20
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Alumno y tu paquete es con Eventos sociales y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 20% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Alumno y tu paquete es con Eventos sociales y los paquetes que compraste son: {c} \nTu total es: {sum}')
        else:
            cp=900
            sum=(a+cp)*c
            if sum > 5000:
                to= sum *0.20
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Alumno y tu paquete es con kit de acceso y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 20% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Alumno y tu paquete es con kit de acceso y los paquetes que compraste son: {c} \nTu total es: {sum}')
    if tu==2:
        t=200
        if tp==1:
            cp=600
            sum=(t+cp)*c
            if sum > 5000:
                to= sum *0.10
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Trabajador y tu paquete es Solo Conferencias y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 10% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Trabajador y tu paquete es Solo Conferencia y los paquetes que compraste son: {c} \nTu total es: {sum}')       
        elif tp==2:
            cp=800
            sum=(t+cp)*c
            if sum > 5000:
                to= sum *0.10
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Trabajador y tu paquete es con Eventos sociales y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 10% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Trabajador y tu paquete es con Eventos sociales y los paquetes que compraste son: {c} \nTu total es: {sum}')
        else:
            cp=900
            sum=(t+cp)*c
            if sum > 5000:
                to= sum *0.10
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Trabajador y tu paquete es con kit de acceso y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 10% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Trabajador y tu paquete es con kit de acceso y los paquetes que compraste son: {c} \nTu total es: {sum}')
    if tu==3:
        d=500
        if tp==1:
            cp=600
            sum=(d+cp)*c
            
            if sum > 5000:
                to= sum *0.05
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Docente y tu paquete es Solo Conferencias y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 5% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Docente y tu paquete es Solo Conferencia y los paquetes que compraste son: {c} \nTu total es: {sum}')
            
        elif tp==2:
            cp=800
            sum=(d+cp)*c
            if sum > 5000:
                to= sum *0.05
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Docente y tu paquete es con Eventos sociales y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 5% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Docente y tu paquete es con Eventos sociales y los paquetes que compraste son: {c} \nTu total es: {sum}')
        else:
            cp=900
            sum=(d+cp)*c
            if sum > 5000:
                to= sum *0.05
                total= sum - to
                sumatotal +=total
                print(f'Tu usuario es Docente y tu paquete es con kit de acceso y los paquetes que compraste son: {c} \nTu subtotal es: {sum} y con un descuento del 5% Total de costo es: {total}')
            else:
                sumatotal +=sum
                print(f'Tu usuario es Docente y tu paquete es con kit de acceso y los paquetes que compraste son: {c} \nTu total es: {sum}')
            
    if input('\n Deseas continuar (S/N) ?').upper() == 'N' : break
    
print(f'\n Suma total de ventas: {sumatotal}')
print('\n Proceso terminado')
