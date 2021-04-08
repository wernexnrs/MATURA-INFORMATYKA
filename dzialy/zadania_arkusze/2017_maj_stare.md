<h1 align="center">2017 maj Matura stara</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

# 4.1
```py
count = 0
maxi = 0
with open("Dane_PR/binarne.txt") as file:
    for line in file:
        line = line.strip()
        pol = int(len(line) / 2)
        l = line[:pol]
        r = line[pol:]

        if l == r:
            count += 1
            if len(line) > maxi:
                maxi = len(line)
                napis = line

print(count, napis, maxi)

```


# 4.2
```py
count = 0
dlugosc = 99999999
with open("Dane_PR/binarne.txt") as file:
    for line in file:
        line = line.strip()
        res = [int((line[i:i + 4]), 2) for i in range(0, len(line), 4)] # jakis błąd syntaxu pycharm widzi tu

        if any(i > 9 for i in res):
            count += 1
            if len(line) < dlugosc:
                dlugosc = len(line)

print(count, dlugosc)

```

# 4.3
```py
maxi = 0

with open("Dane_PR/binarne.txt") as file:
    for line in file:
        line = line.strip()
        liczba = int(line, 2)

        if liczba <= 65535:
            if liczba > maxi:
                maxi = liczba

print(maxi, str(bin(maxi))[2:])

```
