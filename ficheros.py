#!/usr/bin/python3

fich = open('/etc/passwd', 'r')

dicc={}
lineas = fich.readlines()
fich.close

for linea in lineas:
	Elemento = linea.split(':')
	print(Elemento[0])
	
print("Hay " + str(len(lineas)) + " maquinas")

