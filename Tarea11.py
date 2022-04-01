'''Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

Nota: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24'''
def intermedio():
    a=int(input('Ingrese un número: '))
    b=int(input('Ingrese otro número: '))
    medio=(a+b)/2
    print('El número intermedio entre los dos números ingresados es: ',medio)
intermedio()