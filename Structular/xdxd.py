from math import pow,sqrt,pi
x = []
y =[]

def catalan(n):
    if n <= 1: 
        return 1
    res = 0
    for i in range(n): 
        res += round(catalan(i) * catalan(n-i-1),2)
    return res

def liczby_catalana(n=1):
    n+=1
    lista = []
    for i in range(n): 
        lista.append(catalan(i))
    return lista

def f(n):
    return (4**n)/(n**(3/2)*sqrt(pi))

def iloraz(n):
    return round(catalan(n)/f(n),2)

for x in range(1,161,10):
    liczby_catalana(x)


