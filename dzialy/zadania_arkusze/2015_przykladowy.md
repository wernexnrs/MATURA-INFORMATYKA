<h1 align="center">Przykładowy arkusz CKE — formuła 2015</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona-odpowiedzi.pdf)

## 2a, 2b i 2c

```py
def pierwiastek_liniowo(n):
    # 2a - brakująca instrukcja: k <- k + 1
    k = 1
    sprawdzenia = 0
    while True:
        sprawdzenia += 1  # sprawdzenie warunku z wiersza (2)
        if not (k + 1) * (k + 1) <= n:
            break
        k = k + 1
    return k, sprawdzenia


def pierwiastek_binarnie(n):
    # 2b - brakująca instrukcja: k <- s (wyszukiwanie binarne w przedziale [k, m])
    k = 1
    m = n
    sprawdzenia = 0
    while True:
        sprawdzenia += 1
        if not (k + 1) * (k + 1) <= n:
            break
        s = (k + m) // 2
        if s * s <= n:
            k = s
        else:
            m = s
    return k, sprawdzenia


for n in [32, 1024]:
    print(n, pierwiastek_liniowo(n)[1], pierwiastek_binarnie(n)[1])
```
**Odpowiedź:** 2a: k ← k + 1; liczba sprawdzeń: 5 (n = 32) i 32 (n = 1024). 2b: k ← s. 2c: 6 (n = 32) i 6 (n = 1024).

## 3a

```py
def schody(a):
    # zwraca listę (schody, długość, liczba progów)
    wynik = []
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i + 1] <= a[i]:
            j = i
            progi = 0
            while j < n - 1 and a[j + 1] <= a[j]:
                if a[j + 1] < a[j]:
                    progi += 1
                j += 1
            wynik.append((a[i:j + 1], j - i + 1, progi))
            i = j
        else:
            i += 1
    return wynik


ciag = [2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]
for schodki, dlugosc, progi in schody(ciag):
    print(schodki, dlugosc, progi)
```
**Odpowiedź:** (2, 2, 2) 3 0; (3, 1, 1) 3 1; (3, 3, 1) 3 1; (11, 7, 7, 6) 4 2; (7, 7) 2 0; (9, 9, 7) 3 1

## 3b

```py
def liczba_progow(a):
    licznik = 0
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            licznik += 1
    return licznik


print(liczba_progow([2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]))
```
**Odpowiedź:** algorytm powyżej (dla ciągu z 3a: 5 progów)

## 3c i 3d

```py
def najw_liczba_progow(a):
    najw = 0
    w_schodach = 0
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            # a[i + 1] może być początkiem nowych schodów
            if w_schodach > najw:
                najw = w_schodach
            w_schodach = 0
        elif a[i] > a[i + 1]:
            w_schodach += 1
    # schody mogą kończyć się ostatnim elementem ciągu
    if w_schodach > najw:
        najw = w_schodach
    return najw


print(najw_liczba_progow([3, 7, 7, 6, 5, 4, 4, 4, 5]))
print(najw_liczba_progow([2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]))
```
**Odpowiedź:** 3c: algorytm powyżej (dla przykładu z treści: 3). 3d: 2(n − 1) porównań — w każdym z n − 1 obrotów pętli w najgorszym razie wykonywane są dwa porównania (wykrycie nowych schodów i wykrycie progu).

## 4a i 4b

```py
wiersze_z_anagramami = 0
ile = {}  # posortowane cyfry liczby -> ile liczb ma taki zestaw cyfr

with open("dane_anagramy.txt") as file:
    for line in file:
        a, b = line.split()
        # anagramy cyfrowe mają ten sam posortowany zapis cyfr
        klucz_a = "".join(sorted(a))
        klucz_b = "".join(sorted(b))
        if klucz_a == klucz_b:
            wiersze_z_anagramami += 1
        ile[klucz_a] = ile.get(klucz_a, 0) + 1
        ile[klucz_b] = ile.get(klucz_b, 0) + 1

with open("wyniki_anagramy.txt", "w") as wynik:
    print("a)", wiersze_z_anagramami, file=wynik)
    print("b)", max(ile.values()), file=wynik)
```
**Odpowiedź:** a) 258; b) 11
