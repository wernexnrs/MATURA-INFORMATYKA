<h1 align="center">Matura 2024 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

```py
# 1.1
def tablica(n, w, k):
    cyfry = bin(n)[2:]
    for i in range(w):
        wiersz = [cyfry[(i * k + j) % len(cyfry)] for j in range(k)]
        print(*wiersz)


tablica(179, 4, 5)


# 1.2 - tylko operacje arytmetyczne
def prawy_dolny(w, k, n):
    dl = 0             # liczba cyfr w zapisie binarnym n
    pom = n
    while pom > 0:
        pom = pom // 2
        dl = dl + 1
    poz = (w * k - 1) % dl   # pozycja cyfry w zapisie n, liczona od lewej od 0
    for i in range(dl - 1 - poz):
        n = n // 2
    return n % 2


print(prawy_dolny(5, 3, 19))
print(prawy_dolny(4, 5, 179))

# sprawdzenie z bezpośrednim wypełnianiem tablicy
for n in range(1, 300):
    for w in range(1, 8):
        for k in range(1, 8):
            cyfry = bin(n)[2:]
            assert prawy_dolny(w, k, n) == int(cyfry[(w * k - 1) % len(cyfry)])
```

**Odpowiedź:** 1.1: 1 0 1 1 0 / 0 1 1 1 0 / 1 1 0 0 1 / 1 1 0 1 1. 1.2: funkcja `prawy_dolny` — w prawym dolnym rogu stoi cyfra o numerze (w · k − 1) mod (liczba cyfr n) licząc od lewej od 0 (dla w = 5, k = 3, n = 19 wynik 1).

## 2.1 i 2.2

```py
wywolania = 0


def F(x):
    global wywolania
    wywolania += 1
    if x == 0:
        return 0
    return 2 + F(x // 2)


# 2.1
for x in [3, 16, 35]:
    wywolania = 0
    print(x, F(x), wywolania)

# 2.2
x_18 = [x for x in range(2000) if F(x) == 18]
print(min(x_18), max(x_18))
```

**Odpowiedź:** 2.1: 3 → 4, 3 wywołania; 16 → 10, 6 wywołań; 35 → 12, 7 wywołań. 2.2: najmniejsza 256, największa 511 (F(x) to podwojona liczba cyfr zapisu binarnego x, więc szukamy liczb 9-cyfrowych w systemie binarnym).

## 3.1, 3.2 i 3.3

```py
with open("slowa.txt") as file:
    slowa = [wiersz.strip() for wiersz in file]

# 3.1
ile = 0
for slowo in slowa:
    for i in range(len(slowo) - 2):
        if slowo[i] == "k" and slowo[i + 2] == "t":
            ile += 1
            break
print("3.1", ile)


# 3.2
def rot13(slowo):
    wynik = ""
    for litera in slowo:
        wynik += chr((ord(litera) - ord("a") + 13) % 26 + ord("a"))
    return wynik


dobre = [slowo for slowo in slowa if rot13(slowo) == slowo[::-1]]
print("3.2", len(dobre))
print(max(dobre, key=len))

# 3.3
print("3.3")
for slowo in slowa:
    for litera in set(slowo):
        if 2 * slowo.count(litera) >= len(slowo):
            print(slowo)
            break
```

**Odpowiedź:** 3.1: 26. 3.2: 5 słów, najdłuższe: rhszzohhubwbojohuubmmfue. 3.3: vzwzwgszezvzzlzzzzzzouz, azaaasfakaaaxbaaaaau, ppppppnoppnoclpop, zggggggpegpnovzgg, nyrpvqycpaylffffffffffffff, kkkkkkkkkkwpijccdbl, tstevttebttktnetitbttti, gvsvjvvvvvqppvuvcvvvi.

## 4.1

```py
odbiorca = [0, 3, 1, 6, 5, 4, 5]   # odbiorca[i] - odbiorca komputera i (indeks 0 pomijamy)
n = 6
pozycja = list(range(n + 1))       # pozycja[p] - komputer z pakietem p
for runda in range(1, 5):
    pozycja = [odbiorca[pozycja[p]] if p > 0 else 0 for p in range(n + 1)]
    print(runda, *pozycja[1:])
```

**Odpowiedź:** po 2. rundzie: 6 3 5 4 5 4; po 3. rundzie: 5 6 4 5 4 5; po 4. rundzie: 4 5 5 4 5 4 (kolejno pakiety 1–6).

## 4.2, 4.3 i 4.4

```py
with open("odbiorcy.txt") as file:
    odbiorca = [0] + [int(wiersz) for wiersz in file]   # numeracja od 1
n = len(odbiorca) - 1

# 4.2
czy_odbiorca = [False] * (n + 1)
for i in range(1, n + 1):
    czy_odbiorca[odbiorca[i]] = True
print("4.2", czy_odbiorca[1:].count(False))

# 4.3
pozycja = list(range(n + 1))   # pozycja[p] - komputer, w którym jest pakiet p
runda = 0
znaleziony = 0
while znaleziony == 0:
    runda += 1
    for p in range(1, n + 1):
        pozycja[p] = odbiorca[pozycja[p]]
    for p in range(1, n + 1):
        if pozycja[p] == p:
            znaleziony = p
            break
print("4.3", runda, znaleziony)

# 4.4
pozycja = list(range(n + 1))
wyniki = []
for runda in range(1, 9):
    for p in range(1, n + 1):
        pozycja[p] = odbiorca[pozycja[p]]
    if runda in [1, 2, 4, 8]:
        ile = [0] * (n + 1)
        for p in range(1, n + 1):
            ile[pozycja[p]] += 1
        wyniki.append(max(ile))
print("4.4", *wyniki)
```

**Odpowiedź:** 4.2: 395. 4.3: runda 3, pakiet 436. 4.4: 6 8 15 20.
