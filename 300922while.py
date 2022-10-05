# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:51:03 2022

@author: Francisco Barreno
"""

x=input("ingrese limite a contar: ")
x=int(x)
contador=1
while x>=contador:
    print (contador)
    contador=contador+1
    
"""
Crmodificacion
"""

x=input("ingrese limite a contar: ")
x=int(x)
contador=1
while True:
    print (contador)
    contador=contador+1
    if contador>x:
        break
