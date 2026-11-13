<h1 align="center">Matura próbna 2024 — grudzień (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2024-grudzien-probna-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2024-grudzien-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2024-grudzien-probna-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

```py
# 1.2 - wypisuje kolejne elementy J(n) (tylko operacje na liczbach całkowitych)
def J(n):
    pozycja = 1
    while n > 0:
        if n % 2 == 1:
            print(pozycja, end=" ")
        n = n // 2
        pozycja = pozycja + 1
    print()


# 1.1
for n in [19, 6, 42, 75]:
    print(n, bin(n)[2:], end=": ")
    J(n)
# brakująca liczba n dla J(n) = (1, 2, 4, 7): 2^0 + 2^1 + 2^3 + 2^6
print(1 + 2 + 8 + 64)
```

**Odpowiedź:** 1.1: J(6) = (2, 3); 42 = 101010₂, J(42) = (2, 4, 6); J(n) = (1, 2, 4, 7) dla n = 75 = 1001011₂. 1.2: funkcja `J`.

## 2.1 i 2.2

```py
wywolania = 0


def F(x, p):
    global wywolania
    wywolania += 1
    if x == 0:
        return 0
    c = x % p
    if c % 2 == 1:
        return F(x // p, p) + c
    return F(x // p, p) - c


# 2.1
for x, p in [(125, 2), (130, 3), (220, 4)]:
    wywolania = 0
    wynik = F(x, p)
    print(x, p, wynik, wywolania)

# 2.2 - największe x < 100, dla którego F(x, p) = 0
for p in [3, 4]:
    x = 99
    while F(x, p) != 0:
        x -= 1
    print(p, x)
```

**Odpowiedź:** 2.1: F(130, 3) = 2 (6 wywołań), F(220, 4) = 7 (5 wywołań). 2.2: p = 3 → x = 96, p = 4 → x = 97.

## 3.1, 3.2 i 3.3

```py
with open("liczby.txt") as file:
    liczby = [int(linia) for linia in file if linia.strip()]

# 3.1
kwadraty = []
for x in liczby:
    k = 1
    while k * k < x:
        k += 1
    if k * k == x:
        kwadraty.append(x)
print("3.1", len(kwadraty), kwadraty[0])


# 3.2
def rozne_dzielniki_pierwsze(n):
    ile = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            ile += 1
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ile += 1
    return ile


print("3.2")
for x in liczby:
    if rozne_dzielniki_pierwsze(x) >= 5:
        print(x)

# 3.3
mniejsze = 0
wieksze = 0
rowne = []
for x in liczby:
    cyfry = sorted(str(x))
    najmniejsza = int("".join(cyfry))
    najwieksza = int("".join(reversed(cyfry)))
    roznica = najwieksza - najmniejsza
    if roznica < x:
        mniejsze += 1
    elif roznica > x:
        wieksze += 1
    else:
        rowne.append(x)
print("3.3", mniejsze, wieksze, rowne)
```

**Odpowiedź:** 3.1: 20 kwadratów, pierwszy to 4489. 3.2: 2730, 8190, 2310, 4620, 7770, 8610, 4830, 4290, 6930, 6630. 3.3: mniejszych 947, większych 1052, równa: 6174.

## 4.1, 4.2 i 4.3

```py
prostokaty = []
with open("prostokaty.txt") as file:
    for linia in file:
        if linia.strip():
            h, s = map(int, linia.split())
            prostokaty.append((h, s))

# 4.1
pola = [h * s for h, s in prostokaty]
print("4.1", min(pola), max(pola))

# 4.2
najdluzszy = 1
koniec = 0
dlugosc = 1
for i in range(1, len(prostokaty)):
    h, s = prostokaty[i]
    h_pop, s_pop = prostokaty[i - 1]
    if s <= s_pop and h <= h_pop:
        dlugosc += 1
    else:
        dlugosc = 1
    if dlugosc > najdluzszy:
        najdluzszy = dlugosc
        koniec = i
print("4.2", najdluzszy, prostokaty[koniec][0], prostokaty[koniec][1])

# 4.3 - dla każdej wysokości bierzemy k najszerszych prostokątów
szerokosci = {}
for h, s in prostokaty:
    if h not in szerokosci:
        szerokosci[h] = []
    szerokosci[h].append(s)
for k in [2, 3, 5]:
    najlepsza = 0
    for h in szerokosci:
        lista = sorted(szerokosci[h], reverse=True)
        if len(lista) >= k:
            najlepsza = max(najlepsza, sum(lista[:k]))
    print("4.3", k, najlepsza)
```

**Odpowiedź:** 4.1: najmniejsze pole 10425, największe 1545605418. 4.2: `10 1001 627`. 4.3: 2 prostokąty: 79506, 3 prostokąty: 118786, 5 prostokątów: 180895.

## 6

```py
def na_dziesietny(napis, podstawa):
    liczba = 0
    for c in napis:
        liczba = liczba * podstawa + int(c)
    return liczba


def z_dziesietnego(liczba, podstawa):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % podstawa) + wynik
        liczba = liczba // podstawa
    return wynik


a = na_dziesietny("2024", 5)
b = na_dziesietny("1044", 5)
print(z_dziesietnego(a + b, 5), z_dziesietnego(a - b, 5))
```

**Odpowiedź:** 2024₅ + 1044₅ = 3123₅, 2024₅ − 1044₅ = 430₅.
