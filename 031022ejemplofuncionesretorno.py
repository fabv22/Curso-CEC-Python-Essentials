# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:47:09 2022

@author: Francisco Barreno
"""

def mult(a,b):
    return a*b
mult(5,9)
resultado=mult(15,5)   
print(resultado)

def limite():
    q=int(input("ingrese limite: "))
    return q
w=limite()
print("El contador llegará hasta: ",w)
y=1
while True:
    print(y)
    y=y+1
    if y>w:
        break