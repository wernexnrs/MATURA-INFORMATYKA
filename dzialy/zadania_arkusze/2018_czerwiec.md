<h1 align="center">2018 Czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

## 4.1

```py
count = 0
with open("NM_DANE_PR/dane1.txt") as dane1, open("NM_DANE_PR/dane2.txt") as dane2:
    for (a, b) in zip(dane1, dane2):
        a, b = a.strip(), b.strip()
        if a[-3:] == b[-3:]:
            count += 1
print(count)

```

## 4.2

```py
count = parzyste = parzyste2 = 0

with open("NM_DANE_PR/dane1.txt") as dane1, open("NM_DANE_PR/dane2.txt") as dane2:
    for (a, b) in zip(dane1, dane2):
        a, b = a.strip().split(), b.strip().split()
        for i, j in zip(a, b):
            i, j = int(i), int(j)
            if i % 2 == 0:
                parzyste += 1
            if j % 2 == 0:
                parzyste2 += 1
        if parzyste == 5 and parzyste2 == 5:
            count += 1
        parzyste = parzyste2 = 0
print(count)

```

## 4.3

```py
index = 1
with open("NM_DANE_PR/dane1.txt") as dane1, open("NM_DANE_PR/dane2.txt") as dane2:
    for (a, b) in zip(dane1, dane2):
        a = list(set(a.strip().split()))
        b = list(set(b.strip().split()))

        if a == b:
            print(index)
        index += 1

```
