#szybkie podnoszenie do potęgi

def fast_power(x,n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return x * x**(n-1)
    else:
        a = x**(n/2)
    return a**2

#albo
def fast_power2(x,n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return x * (x**((n-1)/2))**2
    return (x**(n/2))**2


print(fast_power(3,6))
print(fast_power2(3,6))
