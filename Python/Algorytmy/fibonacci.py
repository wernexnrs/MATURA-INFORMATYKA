def fibonacci_list(n):
    fibonacci = [0,1]
    for i in range(n-1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci
    
fibonacci_list(4)[4] #nth  
