# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 18:00:25 2022

@author: Francisco Barreno
"""

file=open("devices.txt")
for i in file:
    print (i)
file.close()

#sin espacios
"""
file=open("devices.txt")
for i in file:
    i=i.strip()
    print (i)
file.close()