import random
import string
 
def contra(uchars, lchars, dchars):
   	
	bu= uchars	
	bl= lchars
	bd= dchars
	

	str_uchars, str_lchars, str_dchars = '', '', ''

	#print bu
	str_uchars += random.SystemRandom().choice(string.ascii_uppercase)
	bu = bu - 1			
	#print str_uchars	
		#elif bl > 0:
	str_uchars += random.SystemRandom().choice(string.ascii_lowercase)
	bl = bl - 1
	#print str_uchars
		#elif bd > 0:
	str_uchars += random.SystemRandom().choice(string.digits)
	bd = bd -1 
	if bu < 0 and bl <  0 and bd < 0:
		contra(5,2,3)
	else:
		random_str = str_uchars + str_lchars + str_dchars 
		random_str = ''.join(random.sample(random_str, len(random_str)))
		print random_str #RETURN
 


contra(5,2,3)
