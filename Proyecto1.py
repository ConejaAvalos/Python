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
import socks
import socket


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
	i=0
    	e=[]
    	try:
        	if opt.search is not None and opt.buscar_archivos != 'False':
             		   with open(opt.search,'r') as arch:
        	  	   for l in arch.readlines():
                    	   url = host+'/'+l[:-1]
                   	   buscar=makeRequest(url,user)
                   	   if buscar is not None:
                       		 i+=1
                       		 found.append(e)
               			 if i==0:
                 			   b='No hay archivos: %s\n' %(opt.buscar_archivos)
                 			   print b
                 			   return b
               			 else:
                    			j='\n'.join(e)
                  		        t = 'Archivos o directorios encontrados:\n%s\n' %(xyz)
                    			print t
                    			return t
       			  else:
           				 return ''
   	 except IOError as ioe:
		print 'Erroren buacar: %s' %(opt.buscar_archivos)


def genera_reporte(archivo):
"""
Función para generar un reporte con extension .txt
Recibe:
Un archivo para escritura
Regresa:
una archivo txt.
"""
	try:          
    if opts.reporte:
        r = reportResults()
        if r == 1:
            print "\nLa fecha de ejecucion del programa es: "+ str("FECHA: " + datetime.now()) + "\nIP: " + opts.server)
            opts.verbose=True
        elif r==2:
            reporte.write("\nFECHA "+ str(datetime.now()) + "\nIP: " + opts.server)
        elif r==3:
            print "\nFECHA: "+ str(datetime.now()) + "\nIP: " + opts.server)
            opts.verbose=True
            reporte.write("\nFECHA "+ str(datetime.now()) + "\nIP: " + opts.server)        	
    if opts.archivo:
        opts=lee_configuracion(opts)
    if opts.cms:
        f1=open('archivo.txt','w')
        f1.write(gethtml(url))
        f1.close()
        f1=open('archivo.txt','r')
        cont=0
        for a in f1.readlines():
        	if opts.verbose:
        		print a
        	var = re.findall('<name=\"genor\" content=\".*\"',a)
        	if var!= []:
        		cont=1
        		if opts.reporte:
        			reporte.write("CMS: " + var[0].split(">")[0].split("\"")[3] + "\n")
        		print "El cms es: " + var[0].split(">")[0].split("\"")[3] + "\n"
        if(cont==0):
        	print "No hay CMS" + "\n"
        f1.close()
    if opts.metodos:
        try:
        	if opts.reporte:
        		reporte.write("Metodos http: " + requests.options(url).headers['allow'] + "\n")
        	print "Metodos http: " + requests.options(url).headers['allow'] + "\n"
        except Exception as e:
        	print "No hay metodos" + "\n"
    if opts.serverversion:
        if opts.reporte:
        	reporte.write("URL del servidor:" + opts.serverversion  + "\n")
        print "URL de servidor:" + opts.server  + "\n"
    if opts.busqueda:
        implementar_busqueda(opts,url)
    if opts.tor:
        if opts.user:
        	if opts.password:
        		peticion_tor(opts,url)
        	else:
        		print "Especifique contraseña y usuario para usar tor"
        else:
        	print "Especifique contraseña y usuario para usar tor" + "\n"
     if opts.correo:
        f1=open('archivo.txt','w')
        f1.write(gethtml(url))
        f1.close()
        f1=open('archivo.txt','r')
        cont=0
        for a in f1.readlines():
        	if opts.verbose:
        		print a
        	var = re.findall('[a-zA-Z_\.]+@[a-zA-Z\.]+',a)
        	if var!= []:
	        	if opts.reporte:
	        		reporte.write("Correo: " + var[0] + "\n")
        		cont=1
        		print "Correo: " + var[0] + "\n"
        if(cont==0):
        	print "No hay correos" + "\n"
        f1.close()
    if opts.cabeceras:
        try:
        	if opts.reporte:
        		reporte.write("Version Servidor: " + get(url).headers['server'] + "\n")
        	print "Version Servidor: " + get(url).headers['server'] + "\n"
        except Exception as e:
        	print "No se encuentra la version del servidor" + "\n"
        try:
        	if opts.reporte:
        		reporte.write("Version PHP: " + get(url).headers['x-powered-by'] + "\n")
        	print "Version PHP: " + get(url).headers['x-powered-by'] + "\n"
        except Exception as e:
        	print "No se encuentra version de PHP" + "\n"
except Exception as e:
    printError('Error en reportes')
reporte.close()

def makeRequest(host, user, password):
    """
  Valida Credenciales 
    """
    try:
    	response = get(host, auth=(user,password))
    	if response.status_code == 200:
    	    print 'CREDENCIALES ENCONTRADAS: %s\t%s' % (user,password)
            archivo=open('archivo2.txt','w')
            archivo.write(user+','+password)
            archivo.close()
            return True
    	else:
    	    print 'NO FUNCIONO :c '
            return False
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

def implementa_modo_verboso():
"""
"""

def agente(opts):
    """
    Modifica el nombre de agente  
   
    """
    try:
    	f1=open(opts.agente,'r')
    	for a in f1.readlines():
    		primer_valor = a[:-1].split('=')[0]
    		segundo_valor = a[:-1].split('=')[1]
    		if opts.verbose:
    			print primer_valor
    			print segundo_valor
    		if re.match('agente',primer_valor):
    			if opts.report:
    				write("Agente" + segundo_valor)
    			return segundo_valor
    	f1.close()	
    except Exception as e:
printError('Error en Agente')

def envia_peticiones_tor():
"""Envia peticiones por medio de tor
"""
	i=0
	try:
		if options.tor != None:
        		print '\n  Tor se esta utilizando'
        		socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
        		socket.socket = socks.socksocket
   			l = urllib2.build_opener()
            		if opts.agent:
                		agente= agente(opts)
               			 if opts.verbose:
                		        print agente
                			l.addheaders = [('Agente', agente)]
            			else:
                			l.addheaders = [('Agente', 'Cabecera')]
            				l.open(url)
          			  if opts.report:
            				write("Se esta realizando la peticion "+url+opts.upser+opts.password)
          			        makeRequest(url, opts.user, opts.password) 
					i+=1
		elif options.tor == None:
          	         socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
           		 socket.socket = socks.socksocket 
            		 l = urllib2.build_opener()
           		 if opts.agente:
               	 		agente= agente(opts)
               			 if opts.verbose:
                   			 print agente
                			l.addheaders = [('Agente', agente)]
          			  else:
                			l.addheaders = [('Agente', 'Cabecera')]
            				l.open(url)
          			        f2= open(opts.password,'r')
           			        for lines in f2.readlines():
              					  if opts.verbose:
                    					print lines
                					password = lines[:-1]
                						if opts.report:
                  						  write("Haciendo Peticion "+url+opts.upser+password)
               							  makeRequest(url, opts.user, password)
							f2.close()
