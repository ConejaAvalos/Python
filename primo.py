
def primo(n):
	for i in range(2,n):
		if n%i==0:
			print n, "No es primo"   
		else:
			print n, "Si es primo"

primo(7)
