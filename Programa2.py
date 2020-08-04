# -*- coding: utf-8 -*-
'''
    Desarrollador: Jorge Aníbal Quezada Ulibarri
    Funcion del programa:
	Definir una función max() que tome como argumento tres números y devuelva el
        mayor de ellos.
	Fecha: Jueves  1 de Marzo del 2018
'''
n1=18
n2=5
n3=80                                   #'''add 1'''
def max_de_tres(n1, n2, n3):                            #'''mod 1'''
    if (n1 > n2 and n1 > n3):                             #'''mod 2'''
        print (n1)
        print ('el mayor es el primero')
    if (n2 > n1 and n2 > n3):                             #'''mod 3'''
        print (n2)
        print ('el mayor es el segundo')
    if (n3 > n1 and n3 > n2):              # '''add 1'''
        print (n3)                          #'''add 2'''
        print ('el mayor es el tercero')    #'''add 3'''
max_de_tres(n1,n2,n3)                                   #'''mod 4'''