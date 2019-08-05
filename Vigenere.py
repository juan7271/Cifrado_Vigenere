#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, argparse
from time import time
import numpy as np
import base64
import hashlib
parser = argparse.ArgumentParser()
# Opciones algoritmos.
parser.add_argument("-vig", help="SUSTITUCIÓN POLIALFABETICA ALGORITMO VIGENERE ", action="store_true")
parser.add_argument("-c", help="OPCIÓN PARA CIFRAR", action="store_true")
parser.add_argument("-d", help="OPCIÓN PARA DESCIFRAR", action="store_true")
parser.add_argument("-texto", type=str, help="NOMBRE DEL ARCHIVO A CIFRAR O DESCIFRAR", default=os.getcwd(), required=False)
parser.add_argument("-clave", type=str, help="NOMBRE DEL ARCHIVO QUE CONTIENE LA CLAVE", default=os.getcwd(), required=False)
args=parser.parse_args()




if args.vig == True and args.vig == True and args.c == False and args.d == False:


	print("""
        				    UNIVERSIDAD DE MANIZALES
        --------------------------SUSTITUCIÓN POLIALFABETICA ALGORITMO VIGENERE--------------------------
      	  			
	Consideraciones:
		 
		Archivos a cifrar y descifrar sin espacios
		Clave a utilizar sin espacios
		Se realiza Codificacion de los archivos a base 64 para su posterior cifrado y descifrado

	                                                                          			
	               							  			
        Sintaxis: 
.		Cifrar:   python3 ./Vigenere.py -vig -c -texto <ArchivoEntrada> -clave <ArchivoClave>	
                Descifrar:python3 ./Vigenere.py -vig -d -texto <ArchivoEntrada> -clave <ArchivoClave> 		

	  Realizado por: Juan David Rodriguez Valencia.      	juan7271@hotmail.com  			
			 Dalton Antonio Salazar Castro		dasalazar86@gmail.com
        """)


################CIFRAR#############################

if args.vig == True and args.c == True:

	
	tiempo_inicial = time()    #Tiempo Inicial
				 
	mensaje = open (args.texto, 'r',encoding="ISO-8859-1") #Mensaje a Cifrar, estandar latino
	mensaje = mensaje.read()
	mensaje2 = mensaje.strip()  #Borrar espacios

	conversion = mensaje2.encode("utf-8")  #Codificar base 64
	encoded = base64.b64encode(conversion)
	MensajeCod = encoded.decode("utf-8")

	
	clave=open(args.clave,'r')	#Se carga la clave inicial
	clave = clave.read()
	clave2 = clave.strip()   #Borrar espacios

	print("clave_original: ", clave2)

	alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="	#Alfabeto


	### operacion personalizada para agregar caracteres a la clave inicial formula 
	##NuevaLetraClave = [(POSLetraClaveOriginal) + (LongitudOriginalClave)] modulo [(LongitudOriginalClave)*2] ----> se añade a la clave
	clave_agrego = []
	for letras in clave2:
		clave_agrego.append(letras)
	operacion = ""
	clave_operacion = clave2
	Suma_fija = 0
	Suma_fija = len (clave2)	

	for x in range(0,(len(clave2))):
		
		operacion = (alfabeto.index(clave_agrego[x])+Suma_fija) % (len (clave2)* 2)
		clave_operacion = clave_operacion + alfabeto[operacion]

	print("clave_operacion: ", clave_operacion)
	
	########################## fin operacion personalizada############## 	

	
	clave_modificada=""	#Clave a utilizar de acuerdo al tamaño del mensaje

	#####Ajustar clave, de acuerdo al tamaño del texto###
	
	#Si Mensaje es mayor que la clave, se rellena con la misma clave hasta tener igual tamaño que el mensaje
	if len(MensajeCod)>len(clave_operacion):	
		for i in range(int(len(MensajeCod)/len(clave_operacion))):		
			clave_modificada += clave_operacion			
		clave_modificada += clave_operacion[:len(MensajeCod)%len(clave_operacion)]	
	
	#Si Mensaje es menor que clave, se recorta o trunca la clave hasta tener igual tamaño que el mensaje
	elif len(MensajeCod)<len(clave_operacion):	
		clave_modificada = clave_operacion[:len(MensajeCod)]	

	# Si el Mensaje es igual que clave, se deja igual
	elif len(MensajeCod)==len(clave_operacion):	
		clave_modificada = clave_operacion	

	else:
		print ('Error al asignar clave al mensaje')
		sys.exit(1)
	
	######### fin ajusta clave##############


	clave_lista = []	#array para agregar el string de la clave
	


	####Ciclo, agrego el string al array, para la clave####
	for letras in clave_modificada:
		clave_lista.append(letras)
	
	
	
	posicion_clave = []  	  #array para las posiciones del alfabeto de la clave

	cifrado = ""		#String para numero de la letra cifrada
	msg_cifrado = ""	#String para concatenar el mensaje cifrada
	
	
	##Formula Cifrado Vigenere####
	for x in range(0,(len(MensajeCod))):
		
		cifrado = (alfabeto.index(MensajeCod[x]) + alfabeto.index(clave_lista[x])) % len (alfabeto)  #Operacion con la posicion de clave y mensaje
		msg_cifrado = msg_cifrado + alfabeto[cifrado]			##Convierto la posicion en la letra correspondiente del alfabeto

	#Guardar el String cifrado en archivo
	salida = args.texto
	punto = salida.index(".")
	salida = salida[0:punto] + ".cif"
	cripto = open(salida, "w",encoding="ISO-8859-1")
	cripto.write(msg_cifrado)


	#Tiempo Total de ejecucion
	tiempo_final = time()
	tiempo_total = tiempo_final-tiempo_inicial
	print("Tiempo total: ", tiempo_total)


#######DESCIFRAR####################

if args.vig == True and args.d == True:

	tiempo_inicial = time()    #Tiempo Inicial
				 
	mensaje = open (args.texto, 'r',encoding="ISO-8859-1")  #Mensaje a descifrar
	mensaje = mensaje.read()
	#mensaje2 = mensaje.strip()  #Borrar espacios


	
	clave=open(args.clave,'r')	#Clave a utilizar
	clave = clave.read()
	clave2 = clave.strip()   #Borrar espacios

	
	print("clave_original: ", clave2)
	
	alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="	#Alfabeto

	
	### operacion personalizada para agregar caracteres a la clave inicial formula 
	##NuevaLetraClave = [(POSLetraClaveOriginal) + (LongitudOriginalClave)] modulo [(LongitudOriginalClave)*2] ----> se añade a la clave
	clave_agrego = []
	for letras in clave2:
		clave_agrego.append(letras)
	operacion = ""
	clave_operacion = clave2
	Suma_fija = 0
	Suma_fija = len (clave2)	

	for x in range(0,(len(clave2))):
		
		operacion = (alfabeto.index(clave_agrego[x])+Suma_fija) % (len (clave2)* 2)
		clave_operacion = clave_operacion + alfabeto[operacion]

	print("clave_operacion: ", clave_operacion)
	
	########################## fin operacion personalizada############## 

	
	clave_modificada=""	#Clave a utilizar de acuerdo al tamaño del mensaje


	#####Ajustar clave, de acuerdo al tamaño del texto###
	
	#Si Mensaje es mayor que la clave, se rellena con la misma clave hasta tener igual tamaño que el mensaje
	if len(mensaje)>len(clave_operacion):	
		for i in range(int(len(mensaje)/len(clave_operacion))):		
			clave_modificada += clave_operacion			
		clave_modificada += clave_operacion[:len(mensaje)%len(clave_operacion)]	
	
	#Si Mensaje es menor que clave, se recorta o trunca la clave hasta tener igual tamaño que el mensaje
	elif len(mensaje)<len(clave_operacion):	
		clave_modificada = clave_operacion[:len(mensaje)]	

	# Si el Mensaje es igual que clave, se deja igual
	elif len(mensaje)==len(clave_operacion):	
		clave_modificada = clave_operacion	

	else:
		print ('Error al asignar clave al mensaje')
		sys.exit(1)
	
	######### fin ajusta clave##############


	clave_lista = []	#array para agregar el string de la clave
	


	####Ciclo, agrego el string al array, para la clave####
	for letras in clave_modificada:
		clave_lista.append(letras)

	descifrado = ""		#String para numero de la letra cifrada
	msg_descifrado = ""	#String para concatenar el mensaje cifrada

		

	for x in range(0,(len(mensaje))):
		
		descifrado = (alfabeto.index(mensaje[x]) - alfabeto.index(clave_lista[x])) % len (alfabeto) #Operacion con la posicion de clave y mensaje (Restando)
		msg_descifrado = msg_descifrado + alfabeto[descifrado]   ##Convierto la posicion en la letra correspondiente del alfabeto



	conversion = base64.b64decode(msg_descifrado)

	descifrado = conversion.decode("utf-8")
		
	print("mensaje descifrado: ",descifrado)
	#Guardo el mensaje descifrado en un texto correspondiente
	salida = args.texto
	punto = salida.index(".")
	salida = salida[0:punto] + ".des"
	cripto = open(salida, "w",encoding="ISO-8859-1")
	cripto.write(descifrado)



	#Calculo el tiempo total de ejecuciòn del cifrado
	tiempo_final = time()
	tiempo_total = tiempo_final-tiempo_inicial
	print("Tiempo total", tiempo_total)



