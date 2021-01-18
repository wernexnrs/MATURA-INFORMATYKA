def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

for i in range(10): #first 10 numbers
    print(f(i))
