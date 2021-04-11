## 5a
```py
count = 0
with open("dane_PP/pary_liczb.txt") as file:
    for line in file:
        a, b = map(int, line.strip().split())
        if a % b == 0 or b % a == 0:
            count += 1

print(count)

```

## 5b
```py
def nwd(a, b): return nwd(b, a % b) if b else a


count = 0
with open("dane_PP/pary_liczb.txt") as file:
    for line in file:
        a, b = map(int, line.strip().split())
        if nwd(a, b) == 1:
            count += 1

print(count)

```

## 5c
```py
count = 0
with open("dane_PP/pary_liczb.txt") as file:
    for line in file:
        a, b = line.strip().split()
        suma_a = sum(int(i) for i in a)
        suma_b = sum(int(i) for i in b)
        if suma_a == suma_b:
            count += 1


print(count)

```
