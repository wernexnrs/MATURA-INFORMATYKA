<h1 align="center">Matura 2021 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

```py
def zachlanna(n):
    # 1.2 - długość reprezentacji metodą zachłanną, bez funkcji pierwiastek
    kw = 1
    while (kw + 1) * (kw + 1) <= n:
        kw += 1
    dl = 0
    s = n
    while s > 0:
        if kw * kw <= s:
            s -= kw * kw
            dl += 1
        else:
            kw -= 1
    return dl


def najkrotsza(n):
    # długość najkrótszej reprezentacji (programowanie dynamiczne) - do sprawdzenia 1.1
    najkrotsze = [0] * (n + 1)
    for i in range(1, n + 1):
        najkrotsze[i] = i  # same jedynki
        k = 1
        while k * k <= i:
            najkrotsze[i] = min(najkrotsze[i], najkrotsze[i - k * k] + 1)
            k += 1
    return najkrotsze[n]


print(zachlanna(12))
print(zachlanna(23), najkrotsza(23))
# 1.1 - pierwsza liczba n > 23, dla której metoda zachłanna nie daje najkrótszej reprezentacji
n = 24
while zachlanna(n) == najkrotsza(n):
    n += 1
print(n, zachlanna(n), najkrotsza(n))
```
**Odpowiedź:** 1.1: 23 = 3² + 3² + 2² + 1²; np. n = 32: zachłannie 5² + 2² + 1² + 1² + 1², krócej 4² + 4². 1.2: algorytm powyżej (dla n = 12: dl = 4)

> W kluczu CKE przykładowy pseudokod do 1.2 ma warunek `kw * kw < s` — powinno być `kw * kw ≤ s` (z `<` np. dla n = 12 pętla się nie kończy).

## 2.1 i 2.2

```py
def modyfikuj(T, n, s, k):
    # T[0] nieużywane - tablica indeksowana od 1; zwraca liczbę wywołań
    wywolania = 1
    if s + k < n:
        wywolania += modyfikuj(T, n, s + k, k)
    i = s + 1
    while i <= n and i <= s + k:
        T[s] = T[s] + T[i]
        i += 1
    return wywolania


# 2.1
for T, s, k in [([1, 4, 2, 8, 3, 6, 2, 9, 1, 5], 5, 6),
                ([4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3], 3, 5),
                ([4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3], 4, 4)]:
    T = [None] + T
    modyfikuj(T, len(T) - 1, s, k)
    print(T[1:])

# 2.2
for n, s, k in [(5, 1, 3), (2021, 1, 100), (2021, 20, 35)]:
    T = [None] + [0] * n
    print(n, s, k, modyfikuj(T, n, s, k))
```
**Odpowiedź:** 2.1: [1, 4, 2, 8, 26, 6, 2, 9, 1, 5]; [4, 2, 46, 2, 9, 3, 5, 21, 7, 4, 3, 2, 3]; [4, 2, 6, 40, 9, 3, 5, 21, 7, 4, 3, 5, 3]. 2.2: 21 i 58

> W kluczu CKE w drugim wierszu 2.1 jest literówka: [1,4,2,8,26,6,2,**6**,1,5] — ósmy element nie jest zmieniany i wynosi 9.

## 4.1, 4.2, 4.3 i 4.4

```py
napisy = []
with open("napisy.txt") as file:
    for line in file:
        napisy.append(line.strip())

# 4.1
cyfry_razem = 0
for napis in napisy:
    for znak in napis:
        if znak.isdigit():
            cyfry_razem += 1

# 4.2 - w wierszu 20*j litera na pozycji j (numeracja od 1)
haslo2 = ""
for nr in range(20, 1001, 20):
    haslo2 += napisy[nr - 1][nr // 20 - 1]

# 4.3 - dopisanie znaku na końcu: napis[1:] musi być palindromem, środek to napis[25];
#       dopisanie na początku: napis[:-1] musi być palindromem, środek to napis[24]
haslo3 = ""
for napis in napisy:
    if napis[1:] == napis[1:][::-1]:
        haslo3 += napis[25]
    elif napis[:-1] == napis[:-1][::-1]:
        haslo3 += napis[24]

# 4.4 - cyfry z wiersza w parach, koniec po trzech kolejnych X (także z różnych wierszy)
haslo4 = ""
for napis in napisy:
    cyfry = []
    for znak in napis:
        if znak.isdigit():
            cyfry.append(znak)
    for j in range(0, len(cyfry) - 1, 2):
        liczba = int(cyfry[j] + cyfry[j + 1])
        if 65 <= liczba <= 90:
            haslo4 += chr(liczba)
            if haslo4.endswith("XXX"):
                break
    if haslo4.endswith("XXX"):
        break

with open("wyniki4.txt", "w") as wynik:
    print("4.1.", cyfry_razem, file=wynik)
    print("4.2.", haslo2, file=wynik)
    print("4.3.", haslo3, file=wynik)
    print("4.4.", haslo4, file=wynik)
```
**Odpowiedź:** 4.1: 11844; 4.2: SZYBKOROZWIAZUJEPROGRAMISTYCZNEZADANIAZINFORMATYKI; 4.3: ZADANIEMATURALNE; 4.4: LITWOOJCZYZNOMOJATYJESTESJAKZDROWIEILECIETRZEBACENIC…KRETYJAKWAZBOAXXX
