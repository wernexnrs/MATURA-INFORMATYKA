def nwd(a, b): return nwd(b, a%b) if b else a

#^the same
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a

#^the same
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

#iteracyjnie
def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a

#iteracyjnie ze zmienna pomocnicza
def nwd_i(a, b):
    while b:
        temp = a
        a = b
        b = temp%b
    return a
