#iteracyjna i rekurencyjna realizacja algorytmu Euklidesa

def nwd(a, b): return nwd(b, a%b) if b else a #recursive

#^the same
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

#iteration
def nwd2(a, b):
    while b:
        a, b = b, a%b
    return a

def nww(a, b): return a*b//nwd(a, b)
