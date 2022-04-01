'''Realiza un programa que pida al usuario un número entero del 0 al 9,
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:'''
import numpy as np
import random
def lista():
        b= int(random.randint(0,9))
        a=int(input('Ingrese un número del 0 al 9: '))
        if b==a:
            print(f'El número {a} se encuentra en la lista')
        else:
            print('error vuelva a intentarlo')
            return lista() 
lista()

    