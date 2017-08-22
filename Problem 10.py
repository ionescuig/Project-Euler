n= 2000000
lista = [None, None]+list(range(2,n))
for i in range(2,int(n**0.5)):
    if lista[i]:
        for j in range(i*i,n,i):
            lista[j] = None

primes = [el for el in lista if el]
suma = 0
for i in primes:
    suma += i
print(suma)
