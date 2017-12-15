#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []

def aprueba_becario(nombre_completo):
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n in ['Gerardo', 'Alan', 'Guadalupe', 'Rafael', 'Karina']:
            return False
    aprobados.append(nombre_completo.upper())
    aprobados.sort()
    return True


def borrar_becario(nombre):
     if nombre in aprobados:
	aprobados.remove(nombre)
	print "Se borró el becario" 
	return True
    
     else:
	
	print "No se borro" 
	print nombre
	return False 
    
	


becarios = ['Becerra Alvarado Hugo Alonso',
            'Cabrera Balderas Carlos Eduardo',
            'Corona Lopez Gerardo',
            'Diez Gutierrez Gonzalez Rafael'
            'Disner Lopez Marco Antonio',
            'Garcia Romo Claudia Fernanda',
            'Gonzalez Ramirez Miguel Angel',
            'Gonzalez Vargas Andrea Itzel',
            'Orozco Avalos Aline Karina',
            'Palacio Nieto Esteban',
            'Reyes Aldeco Jairo Alan',
            'Santiago Mancera Arturo Samuel',
            'Sarmiento Campos Jose',
            'Sarmiento Campos Maria Guadalupe',
            'Valle Juarez Pedro Angel',
            'Viveros Campos Ulises']

for b in becarios:
    if aprueba_becario(b):
        print 'APROBADOO: ' + b
    else:
        print 'REPROBADO: ' + b


borrar_becario("BECERRA ALVARADO HUGO ALONSO")
borrar_becarcio ("CABRERA")

print aprobados
