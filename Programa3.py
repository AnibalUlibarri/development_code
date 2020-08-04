#--coding: utf-8--
'''
    Desarrollador: Jorge Aníbal Quezada Ulibarri
    Función:
    Definir una función
    que calcule la longitud de una cadena dada
    Fecha: Jueves  8 de Marzo del 2018
'''
def calcula(txt):
        x=0
	print ("Haz introducido: ", txt)
	for i in txt:
		print  str(i),(" Posición "), str(x)
		x+=1
	print ("Total de letras: "), str(x)
if  __name__ == "__main__":
	eltxt = raw_input("Introduce una palabra: ")
	calcula(eltxt)                               #'''add total: 10'''