<h1 align="center">2021 Kwiecień (próbna)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

> Rozwiązanie nieprzetestowane na danych CKE.

W pliku `liczby.txt` każdy wiersz zawiera jedną liczbę zapisaną w systemie pozycyjnym, a ostatnia cyfra wiersza oznacza podstawę tego systemu (np. `10112` to liczba `1011` w systemie dwójkowym). Treść podpunktów odtworzono na podstawie wcześniejszego rozwiązania z repozytorium.

## 6.1

```py
# ile liczb jest zapisanych w systemie szóstkowym
ile = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        if line[-1] == "6":
            ile += 1

print(ile)
```

## 6.2

```py
# ile liczb zapisanych w systemie siódemkowym nie zawiera cyfry 6
ile = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], line[-1]
        if podstawa == "7" and "6" not in cyfry:
            ile += 1

print(ile)
```

## 6.3

```py
# ile liczb zapisanych w systemie dwójkowym jest nieparzystych
ile = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], line[-1]
        if podstawa == "2" and int(cyfry, 2) % 2 == 1:
            ile += 1

print(ile)
```

## 6.4

```py
# suma (dziesiętnie) wszystkich liczb zapisanych w systemie czwórkowym
suma = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], line[-1]
        if podstawa == "4":
            suma += int(cyfry, 4)

print(suma)
```

## 6.5

```py
# największa i najmniejsza liczba w pliku (zapis z pliku i wartość dziesiętna)
liczby = []

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], int(line[-1])
        liczby.append((int(cyfry, podstawa), line))

najwieksza = max(liczby)
najmniejsza = min(liczby)
print(najwieksza[1], najwieksza[0])
print(najmniejsza[1], najmniejsza[0])
```
