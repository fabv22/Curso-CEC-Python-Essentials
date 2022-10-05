# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:59:54 2022

@author: Francisco Barreno
"""

acl=int(input("ingrese el numero de ACL: "))
if acl >=1 and acl <= 99:
    print("es un acl standard")
elif acl >=100 and acl <= 199:
    print("es un acl tipo extendido")
else:
    print("no es un acl")