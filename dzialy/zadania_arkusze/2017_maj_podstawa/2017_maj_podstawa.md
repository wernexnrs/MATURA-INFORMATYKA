## 4.1
```py
count = 0

with open("dane_PP/liczby.txt") as file:
    for line in file:
        a, b, c = map(int, line.strip().split())
        if [a, b, c] == sorted([a, b, c]):
            count += 1
print(count)
```

## 4.2
```py
def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


suma = 0

with open("dane_PP/liczby.txt") as file:
    for line in file:
        a, b, c = map(int, line.strip().split())
        suma += nwd(nwd(a, b), c)
print(suma)
```


## 4.3
```py
def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


suma_cyfr = []

with open("dane_PP/liczby.txt") as file:
    for line in file:
        a, b, c = line.strip().split()

        wiersz = "".join([a, b, c])

        suma = 0

        for i in wiersz:
            suma += int(i)

        suma_cyfr.append(suma)

print(suma_cyfr.count(35), max(suma_cyfr), suma_cyfr.count(max(suma_cyfr)))
```
