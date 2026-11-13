<h1 align="center">Matura 2020 — czerwiec (termin główny), poziom rozszerzony (stara formuła)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def algorytm(A):
    # zwraca x, y oraz liczbę porównań w wierszach (*)
    A = A[:]
    n = len(A)
    porownania = 0
    # w każdej parze (A[i], A[i+1]) mniejszy element trafia na lewo
    i = 0
    while i < n - 1:
        porownania += 1
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
        i = i + 2
    # x - minimum z lewych elementów par, y - maksimum z prawych
    i = 0
    x = A[i]
    y = A[i + 1]
    while i < n - 3:
        porownania += 2
        if A[i + 2] < x:
            x = A[i + 2]
        if A[i + 3] > y:
            y = A[i + 3]
        i = i + 2
    return x, y, porownania


A = [5, 8, 10, 14, 20, 12, 19, 23, 38, 30]
x, y, porownania = algorytm(A)
print(x, y)
print(porownania, 3 * len(A) // 2 - 2)  # n/2 + 2*(n/2 - 1) = 3n/2 - 2
```
**Odpowiedź:** 1.1: x = 5, y = 38. 1.2: a) A (najmniejsza liczba), b) B (największa liczba). 1.3: D (3n/2 − 2)

## 2.1 i 2.2

```py
def kod_bcd(L):
    # każda cyfra dziesiętna -> 4 bity
    kod = ""
    for cyfra in str(L):
        kod += format(int(cyfra), "04b")
    return kod


def z_bcd(kod):
    liczba = ""
    for i in range(0, len(kod), 4):
        liczba += str(int(kod[i:i + 4], 2))
    return int(liczba)


def jedynki_bcd(L):
    # 2.2 - tylko operacje arytmetyczne
    w = 0
    while L > 0:
        cyfra = L % 10
        while cyfra > 0:
            if cyfra % 2 == 1:
                w += 1
            cyfra = cyfra // 2
        L = L // 10
    return w


# 2.1
for L in [259, 15893]:
    print(L, kod_bcd(L), jedynki_bcd(L))
for kod in ["0010000000010111", "00100011010101110100"]:
    print(z_bcd(kod), kod, kod.count("1"))
```
**Odpowiedź:** 2.1: 259 — 001001011001, 5 jedynek; 2017 — 0010000000010111; 23574 — 00100011010101110100; 15893 — 00010101100010010011, 8 jedynek. 2.2: algorytm `jedynki_bcd` powyżej

## 4.1

```py
def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


pierwsze = []
with open("dane.txt") as file:
    for line in file:
        liczba = int(line)
        if czy_pierwsza(liczba):
            pierwsze.append(liczba)

with open("wyniki4_1.txt", "w") as wynik:
    print("Liczba liczb pierwszych:", len(pierwsze), file=wynik)
    print("Największa liczba:", max(pierwsze), file=wynik)
    print("Najmniejsza liczba:", min(pierwsze), file=wynik)
```
**Odpowiedź:** liczb pierwszych: 501; największa: 99767; najmniejsza: 311

## 4.2

```py
licznik = 0
with open("dane.txt") as file:
    for line in file:
        zapis = bin(int(line))[2:]
        # dopisanie zer z przodu = usunięcie zer z końca zapisu
        zapis = zapis.rstrip("0")
        if zapis == zapis[::-1]:
            licznik += 1

with open("wyniki4_2.txt", "w") as wynik:
    print(licznik, file=wynik)
```
**Odpowiedź:** 107

## 4.3

```py
ile = {}  # zbiór cyfr liczby (jako napis) -> ile liczb ma dokładnie te cyfry
with open("dane.txt") as file:
    for line in file:
        cyfry = "".join(sorted(set(line.strip())))
        ile[cyfry] = ile.get(cyfry, 0) + 1

# z k liczb o tym samym zbiorze cyfr można utworzyć k*(k-1)/2 par
pary = 0
for k in ile.values():
    pary += k * (k - 1) // 2

with open("wyniki4_3.txt", "w") as wynik:
    print(pary, file=wynik)
```
**Odpowiedź:** 23515
