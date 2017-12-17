#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import re
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError
from http import client
import urllib2


def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='Imprime la información detallada de la ejecucuión del programa.')
    parser.add_option('-ps','--phpversion', dest='phpversion', default='80', help='Habilita el método para obtener la versión de php.')
    parser.add_option('-sv','--serverversion', dest='serverversion', default=None, help='Habilita el método para obtener la versión se servidor web')
    parser.add_option('-r','--reporte', dest='reporte', default=None, help='Se guardan los reportes en un archivo txt.')
    parser.add_option('-m', '--metodos' dest='metodos' default=None, help='Habilita el método para obtener los métodos que tiene habilitados el servidor'.)
    parser.add_option('-c', '--cms' dest='cms' default=None, help='Habilita el método para obtener los cms del servicio web.')
    parser.add_option('-cs', '--correos' dest='correos' default=None, help='Habilita el método para obtener los correos de la página.')
    parser.add_option('-b', '--busqueda', dest='busqueda', default=None, help='Habilita el método para la búqueda de archivos/directorios en el servidor.')
    parser.add_option('-t', '--tor', dest='tor', default=None, help='Habilita el método para enviar peticiones a través de tor.')
    parser.add_option('-conf', '--configuracion', dest='configuración', default=None, help='Habilita la opción para pasar banderas a través de un archivo de configuración')
    opts,args = parser.parse_args()
    return opts

def lee_configuracion(archivo, opts):
"""
Método para leer configuraciones desde un archivo de texto
y pasarlas a opciones [argumentos] de la función
Recibe:
UN archivo de texto y las opciones
"""
	with open(archivo,'r') as configuraciones:
		for linea in configuraciones.readlines():
			linea = linea.split('=')
			opcion = linea[0]
			valor = linea[1]
			if (opcion == "verbose" or opcion =="v"):
				verbose.default = (x: if x == True then True else False)
			elif (opcion == "phpversion" or opcion == "ps"):
				phpversion.default = (x: if x == True then x)
			elif (opcion == "serverversion" or opcion == "sv"):
				phpversion.default = (x: if x == True then x)
			elif (opcion == "reporte" or opcion == "r"):
				phpversion.default = (x: if x == True then x)
			elif (opcion == "metodos" or opcion == "m"):
				phpversion.default = (x: if x == True then x)
			elif (opcion == "cms" or opcion == "c"):
				phpversion.default = (x: if x == True then x)
			elif (opcion == "correos" or opcion == "cs"):
				phpversion.default = (x: if x == True then x)
			elif (opcion == "busqueda" or opcion == "b"):
				phpversion.default = (x: if x == True then x)
			elif (opcion == "tor" or opcion == "t"):
				phpversion.default = (x: if x == True then x)

def obten_version_servidor(opts,host,user):
""" 
Función para obtener la versión del servidor web
Recibe:
Las opciones, el host y el usuario
Regresa:
La version del servidor web
"""
    if options.web_v != None:
        try:
            ver=get(host,headers=user)
            try:
                ver2=ver.headers['server']
                print "Version del servidor web:",ver2
            except:
                print "No está disponible la version web"
        except ConnectionError:
            print('Error en la conexion para obtener la version web')
    else:
        pass

def obten_version_php(opts,host,user):
""" 
Función para obtener la versión de php
Recibe:
La opción, el hsot y el usuario
Regresa:
La version de php
"""
   if options.phpversion != None:
        try:
            ver=get(host,headers=user)
            try:
                ver2=ver.headers['x-powered-by']
                print "Version de PHP:",ver2
            except:
                print('No está disponible la versión de PHP')
        except ConnectionError:
            print('Error en la conexion para obtener la version de php')

def determina_metodos(opts, host, user):
"""
Función para determinar los métodos http habilitados en el servidor
Recibe:
la url a analizar
Regresa:
una lista con los métodos habilitados
"""
if options.metodos != None:
        try:
            metodo=get(host,headers=user)
            try:
            	listam = []
                for metods in metodo.headers['']:
                	listam.append(metods)
                print "Métodos habilitados:",listam
            except:
                print('No están disponibles los métodos habilitados')
        except ConnectionError:
            print('Error en la conexion para obtener los métodos habilitados')


def obtener_cms(opts, host, user):
"""
Función para determinar los cms
Recibe:
la opción, el host y el usuario
Regresa:
una lista con los cms
"""
if options.cms != None:
        try:
            cmss=get(host,headers=user)
            try:
            	listacms = []
                for c in cmss.headers['generator']:
                	listam.append(c)
                print "cms:",listacms
            except:
                print('No están disponibles los cms')
        except ConnectionError:
            print('Error en la conexion para obtener los cms')

def extraer_correos(opts, url):
"""
Función para extraer correos del servidor
Recibe:
la opción, el host y el usuario
Regresa:
una lista con los correos encontrados.
"""
if options.correos != None:
        try:
            pagina = urllib.request.urlopen(url)
    		exp = re.compile(r'[-a-z0-9._]+@([-a-z0-9]+)(\.[-a-z0-9]+)+', re.IGNORECASE
    		correo = reg_ex.search_all(page)
                print "correos:",correo.group()
            except:
                print('No están disponibles los correos')
        except ConnectionError:
            print('Error en la conexion para obtener los correos')	

def buscar_archivos(opts, host, user):
"""
Función para extraer correos del servidor
Recibe:
la url a analizar
Regresa:
una lista con los correos encontrados.
"""


def genera_reporte(archivo):
"""
Función para generar un reporte con extension .txt
Recibe:
Un archivo para escritura
Regresa:
una archivo txt.
"""	

def implementa_modo_verboso():
"""
"""
def envia_peticiones_tor():
