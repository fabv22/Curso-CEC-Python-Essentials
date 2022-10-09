# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:42:34 2022

@author: Francisco Barreno
"""

def readint(prompt,minimo,maximo):
    try:
        num=int(input("Ingrese el numero: "))
    except ValueError:
            print("Por favor no ingrese letras ni decimales solo enteros.")
            num=int(input("Ingrese el numero nuevamente: "))
    minimo=int(input("Ingrese el limite inferior: "))
    maximo=int(input("Ingrese el limite superior: ")) 
    if num<minimo:
        print("El numero es menor al minimo")
    elif num>maximo:
        print("El numero es mayor al maximo") 
    print("El numero ingresado es correcto y es: ",num)

#readint(a=int(input("Ingrese el numero: ")),b=int(input("Ingrese el limite inferior: ")),c=int(input("Ingrese el limite superior: ")))
readint(1,2,3)
print("El numero esta dentro del rango")