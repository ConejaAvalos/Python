


import random
import string
 
"""
Genera una contraseña 
Recibe un 3 numeros qe dfiniran el numero de minusculas, mayusculas y digitos
"""

 
def contra(u, l, d):
   
    str_u, str_l, str_d = '', '', ''
 

    for i in range(u):
        str_u += random.SystemRandom().choice(string.ascii_uppercase)
 
    for i in range(l):
        str_l += random.SystemRandom().choice(string.ascii_lowercase)
 
    for i in range(d):
        str_d += random.SystemRandom().choice(string.digits)

 
    random_str = str_u + str_l + str_d 
    random_str = ''.join(random.sample(random_str, len(random_str)))
    print random_str
 

get_random_string(5,2,3)
