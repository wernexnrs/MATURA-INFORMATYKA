<h1 align="center">2016 Czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

## 6.1

```py
count = 0
with open("MIN-R2A1P-163_dane/liczby.txt") as file:
    for line in file:
        if line.strip()[-1] == "8":
            count += 1
print(count)

```

## 6.2

```py
count = 0
with open("MIN-R2A1P-163_dane/liczby.txt") as file:
    for line in file:
        line = line.strip()
        print(line[:-1])
        if line[-1] == "4" and "0" not in line[:-1]:
            count += 1
print(count)

```

## 6.3

```py
count = 0
with open("MIN-R2A1P-163_dane/liczby.txt") as file:
    for line in file:
        line = line.strip()
        if line[-1] == "2" and int(line[:-1], 2) % 2 == 0:
            count += 1
print(count)

```

## 6.4

```py
count = 0
with open("MIN-R2A1P-163_dane/liczby.txt") as file:
    for line in file:
        line = line.strip()
        if line[-1] == "8":
            count += int(line[:-1], 8)
print(count)

```

## 6.5

```py
lista = []
with open("MIN-R2A1P-163_dane/liczby.txt") as file:
    for line in file:
        line = line.strip()
        base = int(line[-1])
        lista.append((int(line), base, int(line[:-1], base)))

sort_end = sorted(lista, key=lambda x: x[2], reverse=True)

print(sort_end[0])
print(sort_end[-1])

```
