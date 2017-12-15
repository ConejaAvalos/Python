#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']
s = ","

#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
#r1 = (lambda x,y,z,k:x+y+z+k )(sistemas, op_interna, incidentes, auditorias)
#print r1

# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
#r2 = filter(lambda nombre: 'i' in nombre, (lambda x,y,z,k:x+y+z+k )(sistemas, op_interna, incidentes, auditorias))
#print r2


# 3) convierta a mayusculas el resultado anterior

"""r3 = map(lambda nombre: nombre.upper(), filter(lambda nombre: 'i' in nombre, (lambda x,y,z,k:x+y+z+k )(sistemas, op_interna, incidentes, auditorias)))
print r3"""

#((lambda x,y,z,k:x+y+z+k )(sistemas, op_interna, incidentes, auditorias))

s.join(map((lambda nombre: nombre.upper()), filter((lambda nombre: 'i' in nombre), (lambda x,y,z,k:x+y+z+k )(sistemas, op_interna, incidentes, auditorias))))

#UNA SOLA EXPRESION
