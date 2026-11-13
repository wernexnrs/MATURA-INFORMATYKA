<h1 align="center">Matura 2022 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def suma_kw_cyfr(n):
    suma = 0
    while n > 0:
        cyfra = n % 10
        suma += cyfra * cyfra
        n //= 10
    return suma


def czy_nudna(n):
    # n < 1000, więc po pierwszym kroku wszystkie wyrazy ciągu są <= 243
    # zapamiętujemy, które liczby już wystąpiły - powtórzenie oznacza cykl bez 1
    byla = [False] * 1000
    while n != 1:
        if byla[n]:
            return False
        byla[n] = True
        n = suma_kw_cyfr(n)
    return True


# 1.1
for n in [4, 229, 82]:
    print(n, "TAK" if czy_nudna(n) else "NIE")

# 1.2
print(suma_kw_cyfr(123))
```

**Odpowiedź:** 1.1: 229 – NIE, 82 – TAK. 1.2: funkcja `suma_kw_cyfr`. 1.3: funkcja `czy_nudna` – liczymy kolejne sumy kwadratów cyfr aż do 1 (nudna) albo do powtórzenia wartości (ciekawa).

## 2.1, 2.2 i 2.3

```py
wywolania = 0


def koduj(n):
    global wywolania
    wywolania += 1
    if n == 1:
        return ""
    k = n // 2
    if k % 2 == 0:
        return koduj(k) + "A"
    else:
        return "B" + koduj(k)


# 2.1 i 2.2
for n in [1, 2, 12, 33, 158, 1022]:
    wywolania = 0
    kod = koduj(n)
    print(n, repr(kod), wywolania)

# 2.3 - kod ma 6 znaków dla liczb 7-bitowych (64..127); szukamy dwóch o tym samym kodzie
kody = {}
for n in range(64, 128):
    kody.setdefault(koduj(n), []).append(n)
for kod, lista in kody.items():
    if len(lista) > 1:
        print(kod, lista)
        break
```

**Odpowiedź:** 2.1: 12 → BBA, 33 → BAAAA, 158 → BBBBBAA. 2.2: 12 → 4, 33 → 6, 1022 → 10. 2.3: np. 64 i 65 (kod BAAAAA) – liczby 7-cyfrowe binarnie, różniące się tylko ostatnim bitem (klucz podaje np. 66 i 67 albo 94 i 111).

## 4.1, 4.2, 4.3 i 4.4

```py
liczby = []
with open("liczby.txt") as file:
    for line in file:
        liczby.append(int(line))


def odbicie(n):
    return int(str(n)[::-1])


def czy_pierwsza(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# 4.1
print("4.1")
for n in liczby:
    if odbicie(n) % 17 == 0:
        print(odbicie(n))

# 4.2
najwieksza_roznica = -1
najlepsza = 0
for n in liczby:
    roznica = abs(n - odbicie(n))
    if roznica > najwieksza_roznica:
        najwieksza_roznica = roznica
        najlepsza = n
print("4.2", najlepsza, najwieksza_roznica)

# 4.3
print("4.3")
for n in liczby:
    if czy_pierwsza(n) and czy_pierwsza(odbicie(n)):
        print(n)

# 4.4
ile_razy = {}
for n in liczby:
    ile_razy[n] = ile_razy.get(n, 0) + 1
dwa = 0
trzy = 0
for n in ile_razy:
    if ile_razy[n] == 2:
        dwa += 1
    if ile_razy[n] == 3:
        trzy += 1
print("4.4", len(ile_razy), dwa, trzy)
```

**Odpowiedź:** 4.1: 1156, 102, 51, 765, 119, 119, 731; 4.2: 1129 8082; 4.3: 157, 31, 347, 929, 941, 761; 4.4: 85 13 1
