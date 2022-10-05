# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:31:58 2022

@author: Francisco Barreno
"""

def isPrime(a): #definicion de la función solicitada para evaluar si un número 
                #es primo
  for i in range(2,a): #bucle for que permite evaular si el número es primo
    if (a%i) == 0: #condicional usa una variable auxiliar i que va desde 1 
                    #hasta el número a, si el residuo entre el número y la
                    #variable auxiliar i es 0 significa que el número evaluado
                    # es divisible para otro número diferente a sí mismo
                    # por tanto la función retorna un valor falso
      return False
  return True #si el número no es divisible, es decir si el residudo 
              #es diferente a 0 para un número menor al evaluado, este es par
              #la función retorna un valor verdadero

for i in range (1,20):
    if isPrime(i+1):
        print(i+1,end=" ")
print()