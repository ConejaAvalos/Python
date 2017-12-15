"""
Recibe un entero
Define si es primo o no
"""


def primoa(n):
	l=[2]
	for i in range(n):
		if n % 2 == 1:
			l.append(i)
		print l

primoa(10)
