#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def califica_instructores(archivo1, archivo2):
    with open(archivo1,'r') as instructores, open(archivo2,'w') as calificaciones:
        for linea in instructores.readlines():
            linea = linea.split('-')
            nombre_instructor = linea[0]
            calificacion = int(linea[1])
            if calificacion >= 8:
                calificaciones.write('%s RIFA MUCHO\n' % nombre_instructor.upper())
            elif calificacion >= 6:
                calificaciones.write('%s DEBE MEJORAR\n' % nombre_instructor.upper())
            else:
                calificaciones.write('%s NO DEBERIA DAR CLASE\n' % nombre_instructor.upper())


califica_instructores('instructores.txt', 'calificaciones.txt')
