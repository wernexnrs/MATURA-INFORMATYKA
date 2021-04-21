
## 6.1
```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


count = 0

with open("dane/dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        if is_prime(line):
            count += 1

print(count)
```

## 6.2
```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


lista = []

with open("dane/dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        if is_prime(line):
            lista.append(line)

print("max:", max(lista), "min", min(lista))
```

## 6.3
```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


liczby = []

with open("dane/dane4.txt") as file:
    for line in file:
        liczby.append(int(line.strip()))

count = 0
for i in range(1, len(liczby)):
    if is_prime(liczby[i - 1]) and is_prime(liczby[i]) and abs(liczby[i - 1] - liczby[i]) == 2:
        count += 1
        print(liczby[i - 1], liczby[i])
print(count)
```
