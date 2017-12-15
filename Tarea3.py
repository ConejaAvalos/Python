#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

from random import choice
import re

o = ('O','o','0','*','.')
a = ('A','a','4','#')
i = ('I','i','1','¡')
e = ('E','e','3', '?')
l = ('L','l','1','!')
s = ('S','s','5','$')
g = ('G','g','6','¿')
t = ('T','t','7','%')
b = ('B','b','8','&')
z = ('Z','z','2')
q = ('Q','q','9')
c = ('(', '[')

patrono = '[oO0]'
patrona = '[aA4]'
patroni = '[Ii1]'
patrone = '[eE3]'
patronl = '[Ll1]'
patrons = '[Ss5]'
patrong = '[Gg6]'
patront = '[Tt7]'
patronb = '[Bb8]'
patronz = '[Zz2]'
patronq = '[Qq9]'
patronc = '[Cc]'

todas = []

def crea_contrasenas(archivo1, archivo2):
	with open(archivo1, 'r') as entrada, open(archivo2, 'w') as salida:
		for linea in entrada.readlines():		
			linea = linea.split(':')
			cadena = linea[1]
			for patrono in cadena:
				cadena = cadena.replace(patrono, choice(o))
				salida.write(cadena)
				todas.append(cadena)
			for patrona in cadena:
				cadena = cadena.replace(patrona, choice(a))
				salida.write(cadena)
				todas.append(cadena)
			for patroni in cadena:
				cadena = cadena.replace(patroni, choice(i))
				salida.write(cadena)
				todas.append(cadena)
			for patrone in cadena:
				cadena = cadena.replace(patrone, choice(e))
				salida.write(cadena)
				todas.append(cadena)
			for patronl in cadena:
				cadena = cadena.replace(patronl, choice(l))
				salida.write(cadena)
				todas.append(cadena)
			for patrons in cadena:
				cadena = cadena.replace(patrons, choice(s))
				salida.write(cadena)
				todas.append(cadena)
			for patrong in cadena:
				cadena = cadena.replace(patrong, choice(g))
				salida.write(cadena)
				todas.append(cadena)
			for patront in cadena:
				cadena = cadena.replace(patront, choice(t))
				salida.write(cadena)
				todas.append(cadena)
			for patronb in cadena:
				cadena = cadena.replace(patronb, choice(b))
				salida.write(cadena)
				todas.append(cadena)
			for patronz in cadena:
				cadena = cadena.replace(patronz, choice(z))
				salida.write(cadena)
				todas.append(cadena)
			for patronq in cadena:
				cadena = cadena.replace(patronq, choice(q))
				salida.write(cadena)
				todas.append(cadena)
			for patronc in cadena:
				cadena = cadena.replace(patronc, choice(c))
				salida.write(cadena)
				todas.append(cadena)
		salida.write(crea_combinaciones(todas))

	entrada.close()
	salida.close()

def calcula_potencia(lista):
	if len(lista) == 0:
		return [[]]
	conjunto = calcula_potencia(lista[:-1])
	resultado = conjunto + [x + [lista[-1]] for x in conjunto]
	return resultado

def crea_combinaciones(lista):
#	with open(archivo1, 'r') as entrada:
	#for linea in entr.readlines():		
	linea = lista.split(':')
	#cadena = linea[1]
	#cadenas = []
	#for cadena in linea:
		#cadenas.append(cadena)
	potencia = calcula_potencia(linea)
	if len(potencia) <= 4:
		potencia.split(',')
		uno = str(potencia[0])
		dos = str(potencia[1])
		tres = str(potencia[2])
		cuatro = str(potencia[3])
	return uno + dos + tres + cuatro

crea_contrasenas('prueba.txt', 'contrasena.txt')