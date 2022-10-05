# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:54:28 2022

@author: Francisco Barreno
"""
"""Ejercicio en clase
programa q pide un numero para contar
"""
while True:
    x=input("ingrese un limite para contar: ")
    if x=='q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
        print (y)
        y=y+1
        if y>x:
            break