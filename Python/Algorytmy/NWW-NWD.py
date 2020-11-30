def nwd(a, b): 
    return nwd(b, a%b)
    
def nww(a, b): 
    return a*b//nwd(a, b)
    
    
    
'''
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

NWD iteracyjnie

def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a

rozjasnienie up

def nwd_i(a, b):
    while b:
        temp = a
        a = b
        b = temp%b
    return a

'''
