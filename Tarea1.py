



 """
    Regresa palindromo msá grande
    Recibe:
        tipo (str) - cadena con palindromos
    """

def pal(a):
	count=[]
	for j in range(len(a)):
    		for i in range(j,len(a)):
        		if a[j:i+1] == a[i:j-1:-1]:      
          		  count.append(i+1-j)
			  print("El palindromo tien de numero de letras :", max(count))
			  

pal("aabbbbbeeee")





