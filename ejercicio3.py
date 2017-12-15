#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
import poo1 

calificacion_alumno = {}
con=set()
listab=[]
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']
lista=list()
liste=list()

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

"""def aprorepro():
	for alumno in calificacion_alumno:
		if calificacion_alumno[alumno] >= 8:
			lista.append(alumno)		
		else:
			liste.append(alumno)
			
	t1=tuple(lista)
	t2=tuple(liste)
	print "Aprobados", t1 
	print "Reprobados", t2

def poo():
	for alumno in calificacion_alumno:
		b=poo1.Becario(alumno, calificacion_alumno[alumno])
		listab.append(b)	
	print listab"""

def promedio():
	c=0
	for alumno in calificacion_alumno:
		c+=calificacion_alumno[alumno]
	pro=c/len(calificacion_alumno)
	return pro


def conjunto():
	for alumno in calificacion_alumno:
		con.add(calificacion_alumno[alumno])
	return con			





	  

			
			

asigna_calificaciones()
imprime_calificaciones()	
c=conjunto()
print c
#print aprorepro()
#poo()
#p=promedio()
#print str(p)
