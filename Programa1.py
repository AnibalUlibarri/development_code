# -*- coding: utf-8 -*-
''' Desarrollador: Jorge Aníbal Quezada Ulibarri
    Función del Programa: Definir una funcion max() que compare dos numeros y
                        muestre cual es mayor.
Fecha: 19 de octubre del 2017
'''
print ("Los numeros 5 y 10")
numero1 = 10
numero2 = 5
def calcular_max(numero1, numero2):
    if(numero1 > numero2):
        print ("el mayor es: ",numero1)
    elif(numero2 > numero1):
        print ("el mayor es: ",numero2)
    else:
        print ("son iguales")
calcular_max(numero1, numero2)