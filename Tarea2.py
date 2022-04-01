'''Realiza un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar, debe repetise el 
proceso hasta que lo introduzca correctamente.'''

def impar():
    a=int(input('Ingrese un número entero impar: '))
    if a%2==0:
        print('Error, No es un número impar')
        return impar()
    else:
        a%2==1
        print(f'Correcto, el número {a} es impar')
impar()