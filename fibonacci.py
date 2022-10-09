# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:11:31 2022

@author: Francisco Barreno
"""

def fib(n): #definición de la función para calcular la serie Fibonacci hasta el
            # "n" término
    a = 0 #primer término de la serie
    b = 1 #segundo término de la serie
    for i in range(n): #for que calcula los "n" términos de la serie
        c = b+a #cada término nuevo de la serie de fibonacci se obtiene sumando
                #los dos términos anteriores
        a = b #se actualiza el valor de "a" para calcular un nuevo término
              #en la siguiente iteración
        b = c   #se actualiza el valor de "a" para calcular un nuevo término    
    return a #retorna el valor "n" en el cual se encuentra la serie
