# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 18:26:32 2022

@author: Francisco Barreno
"""

lista=[]
file=open("devices.txt")
for i in file:
    i=i.strip()
    lista.append(i)
file.close()
print(lista)