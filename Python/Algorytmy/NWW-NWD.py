def nwd(a, b): return nwd(b, a%b) if b else a #recursive

#^the same
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

#iteration
def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a
