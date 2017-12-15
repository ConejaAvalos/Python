import sys
import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib
import csv

hpre = []
hapa = []
h22 = []
h53 = []
h80 = []
h443 = []
iapa = []
ipre = []
i22 = []
ih = []
ido = []
hd = []
ha = []
hdio = []
hn = []
ho = []



def hash(archivo):
	md=hashlib.md5()
	md.update(open('~/Desktop/nmap.xml').read())
	print md.hexdigest()
	
	sh=hashlib.sha1()
	sh.update(open('~/Desktop/nmap.xml').read())
	print sh.hexdigest()


def lee_xml(archivo_passwd):
	with open(archivo_nmap,'r') as nmap:
		root = ET.fromstring(nmap.read())
  		for n in root.findall('host'):  #Pueros abieros
            		hpr = n.find('status').get('state')
				if hpre == 'up':
					hpre.append(hpre)
       			ha = n.find('status').get('state')
				if ha == 'down':
					hapa.append(ha)
			h2 = n.find('port').get('portid')
			a = n.find('state').get('state')
				if h2 == '22' and a == "open":
					h22.append(h2)
			h5 = n.find('port').get('portid')
			a = n.find('state').get('state')
				if h5 == '53' and a == "open":
					h53.append(h5)
			h8 = n.find('port').get('portid')
			a = n.find('state').get('state')
				if h8 == '80' and a == "open":
					h80.append(h8)
			h4 = n.find('port').get('portid')
			a = n.find('state').get('state')
				if h4 == '443' and a == "open":
					h443.append(h4)
			d = n.find('hostname').get('name')
			hd.append(d)
			var = n.find('service').get('product') #Servicios http
				if var == 'nginx':
					hn.append(var)
			vaa = n.find('service').get('product')
				if vaa == 'Apache':
					ha.append(vaa)
			vd = n.find('service').get('product')
				if vd == 'Dionaea':
					hdio.append(vd)
			o = n.find(('service').get('product')
				if o != 'Apache' and o != 'Dionaea' and o != 'nginx':
					ho.append(o)
			ipa = n.find(('address').get('addr')   #Segunda parte del examen
			hpr = n.find('status').get('state')
				if hpr == 'down':
					iapa.append(ipa)
			ipr = n.find(('address').get('addr')
			hpr = n.find('status').get('state')
				if hpr == 'up':
					ipren.append(ipr)
			i2 = n.find(('address').get('addr')
			h2 = n.find('port').get('portid')
			a = n.find('state').get('state')
				if h2 == '22' and a == "open":
					i22.append(i2)
			iho = n.find(('address').get('addr')
			hs = n.find('service').get('name')
				if hs == 'honeypot':
					ih.append(iho)
			idom = n.find(('address').get('addr')
			hn = n.find('hostname').get('name')
					ido.append(idom)
#Mostrar Host

print "Cantidad de Host Prendidos:" len(hpre)
print "Cantidad de Host Apagados:" len(hapa)
print "Cantidad de Host Con Puerto 22 Abierto:" len(h22)
print "Cantidad de Host Con Puerto 53 Abierto:" len(h53)
print "Cantidad de Host Con Puerto 80 Abierto:" len(h80)
print "Cantidad de Host Con Puerto 443 Abierto:" len(h443)
print "Cantidad de Host Con Nombre de Dominio:" len(hd)
print "Cantidad de Host que utilizan Apache:" len(ha)
print "Cantidad de Host que utilizan nginx:" len(hn)
print "Cantidad de Host que utilizan Dionaea:" len(hdio)
print "Cantidad de Host que utilizan otro servicio:" len(ho)

#Creacion archivos csv

file = open("apagados.csv", "w". newline='')
spamreader = csv.writer(file)
spamreader = writerow(iapa)
file.close()

file = open("prendidos.csv", "w". newline='')
spamreader = csv.writer(file)
spamreader = writerow(ipren)
file.close()

file = open("puerto22.csv", "w". newline='')
spamreader = csv.writer(file)
spamreader = writerow(i22)
file.close()

file = open("honey.csv", "w". newline='')
spamreader = csv.writer(file)
spamreader = writerow(ih)
file.close()

file = open("dominios.csv", "w". newline='')
spamreader = csv.writer(file)
spamreader = writerow(ido)
file.close()

            
