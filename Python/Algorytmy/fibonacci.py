#iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def recur_f(n):
   if n <= 1:
       return n
   return(recur_f(n-1) + recur_f(n-2))
    
for i in range(10): #first 10 numbers
    print(f(i))
    
for i in range(10): #first 10 numbers    
    print(recur_f(i))
