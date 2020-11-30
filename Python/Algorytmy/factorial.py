def factorial(n):
    return n*factorial(n-1) if n > 1 else 1

#Wersja rozpisana

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    return 1
    
#Algorytm iteracyjny

def factorial(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s
