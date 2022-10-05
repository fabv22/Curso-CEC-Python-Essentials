# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:37:34 2022

@author: Francisco Barreno
"""

lista=["R1","R2","R3","R4","S1","S2"]
for item in lista:
    if "S" in item:
        print (item)
        
        """
        Ej2 switches
        """
switches=[]
for item in lista:
    if "S" in item:
        switches.append(item)
print (switches)