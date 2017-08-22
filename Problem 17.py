"""
1 one	3			11 eleven	5									100 one hundred	3+7
2 two	3			12 twelve	5			20 twenty	6		 101 one hundred and one	3+7+3+3
3 three	5		  13 thirteen	4+4		30 thirty	6		 200 two hundred	3+7
4 four	4		   14 fourteen	4+4		40 fourty	6
5 five	4		   15 fifteen	3+4		 50 fifty	5
6 six	3			16 sixteen	3+4		 60 sixty	5
7 seven	5		  17 seventeen	5+4	   70 seventy	7
8 eight	5		  18 eighteen	4+4		80 eighty	6
9 nine	4		   19 nineteen	4+4		90 ninety	6		1000 one thousand 3+8
10 ten	3
"""

def words(n):
	total = 0
	if len(n) == 1:
		if n in ['1','2','6']:
			total = 3
		elif n in ['4','5','9']:
			total = 4
		elif n in ['3','7','8']:
			total = 5
	elif len(n) == 2:
		if n[0] == 1:
			if n == '10':
				total = 3
			elif n in ['11','12']:
				total = 5
			elif n in ['15','16']:
				total = 7
			elif n in ['13','14','18','19']:
				total = 8
			elif n == '17':
				total = 9
		elif n[0] in ['5','6']:
			total = 5 + words(n[1])
		elif n[0] in ['2','3','4','8','9']:
			total = 6 + words(n[1])
		elif n[0] == '7':
			total = 7 + words(n[1])
	return(total)

sumaone = 0
suma = 0
for i in range(1,100):
	sumaone += words(str(i))
suma += sumaone

for i in range(1,10):
	suma += words(str(i))
	suma += 7
	suma += (13*99) +sumaone

suma += 11

print(suma)
