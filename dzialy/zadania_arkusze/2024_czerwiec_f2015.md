<h1 align="center">Matura 2024 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

```py
# 1.2 - sprawdzamy kolejne cyfry binarne od końca
def czy_nieliczna(k):
    poprzednia = 0
    while k > 0:
        cyfra = k % 2
        if cyfra == 1 and poprzednia == 1:
            return False
        poprzednia = cyfra
        k = k // 2
    return True


# 1.1
for zapis, podstawa in [("20012", 8), ("3574", 16)]:
    L = int(zapis, podstawa)
    print(zapis, podstawa, bin(L)[2:], czy_nieliczna(L))
```

**Odpowiedź:** 1.1: 20012₈ = 10000000001010₂ – PRAWDA; 3574₁₆ = 11010101110100₂ – FAŁSZ. 1.2: funkcja `czy_nieliczna`.

## 2.1, 2.2 i 2.3

```py
def algorytm1(A):                   # A[0] to element A[1] z treści
    n = len(A)
    p, m = 1, 1
    porownania = 0
    for i in range(1, n + 1):
        licz = 0
        for j in range(1, n + 1):
            porownania += 1
            if A[i - 1] == A[j - 1]:
                licz += 1
        if licz > m:
            p, m = i, licz
    return p, A[p - 1], m, porownania


# 2.3 - porównujemy A[i] tylko z elementami dalej w tablicy
def algorytm2(A):
    n = len(A)
    p, m = 1, 1
    porownania = 0
    for i in range(1, n):            # i = 1, 2, ..., n - 1
        licz = 1                     # A[i] liczy się samo
        for j in range(i + 1, n + 1):    # j = i + 1, ..., n
            porownania += 1
            if A[i - 1] == A[j - 1]:
                licz += 1
        if licz > m:
            p, m = i, licz
    return p, A[p - 1], m, porownania


A = [7, 9, 15, 0, 6, 7, 6, 10, 15, 6, 0]
print(algorytm1(A))                  # 2.1 (p, A[p], m, liczba porównań)
print(algorytm1([1, 2, 3])[3])       # 2.2 dla n = 3
print(algorytm2(A))                  # 2.3 - ten sam wynik, n(n-1)/2 = 55 porównań
```

**Odpowiedź:** 2.1: p = 5, A[p] = 6, m = 3. 2.2: n = 3 → 9, dla n → n². 2.3: `dla i = 1, 2, ..., n - 1`, `licz ← 1`, `dla j = i + 1, i + 2, ..., n`.

## 4.1, 4.2, 4.3 i 4.4

```py
with open("slowa.txt") as file:
    slowa = [linia.strip() for linia in file if linia.strip()]

wynik = open("wyniki4.txt", "w")

# 4.1
ile = 0
for slowo in slowa:
    for i in range(len(slowo) - 2):
        if slowo[i] == "k" and slowo[i + 2] == "t":
            ile += 1
            break
print("4.1", ile, file=wynik)

# 4.2
fragmenty = []
for slowo in slowa:
    for i in range(len(slowo) - 4):
        if slowo[i] == "e" and slowo[i + 4] == "e":
            fragmenty.append(slowo[i:i + 5])
print("4.2", *fragmenty, file=wynik)


# 4.3
def rot13(slowo):
    wynik_rot = ""
    for c in slowo:
        wynik_rot += chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
    return wynik_rot


dobre = [slowo for slowo in slowa if rot13(slowo) == slowo[::-1]]
najdluzsze = max(dobre, key=len)
print("4.3", len(dobre), najdluzsze, file=wynik)

# 4.4
print("4.4", file=wynik)
for slowo in slowa:
    if 2 * max(slowo.count(c) for c in slowo) >= len(slowo):
        print(slowo, file=wynik)

wynik.close()
```

**Odpowiedź:** 4.1: 26. 4.2: ebeee eeeie eipqe eqgle ejoge ecype evuye enmje ellye elome exsxe ezobe elnne ehcye evrue esfxe etrfe eryae exdye etcce etuke evtte. 4.3: 5 słów, najdłuższe: rhszzohhubwbojohuubmmfue. 4.4: vzwzwgszezvzzlzzzzzzouz, azaaasfakaaaxbaaaaau, ppppppnoppnoclpop, zggggggpegpnovzgg, nyrpvqycpaylffffffffffffff, kkkkkkkkkkwpijccdbl, tstevttebttktnetitbttti, gvsvjvvvvvqppvuvcvvvi.
