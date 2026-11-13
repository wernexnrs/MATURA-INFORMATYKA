<h1 align="center">Matura 2015 — maj, poziom rozszerzony (stara formuła)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/MIN-R1_1P-152.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/MIN-R2_1P-152.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/Dane_PR2.zip) --- [ODPOWIEDZI](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/odpowiedzi/MIN-R1-S.pdf)

## 1.1

```py
def skladniki(n):
    wynik = []
    potega = 1
    while n > 0:
        if n % 2 == 1:
            wynik.append(potega)
        n = n // 2
        potega *= 2
    return wynik


for n in [11, 23, 50]:
    print(n, "=", " + ".join(str(x) for x in skladniki(n)))
```

**Odpowiedź:** 23 = 1 + 2 + 4 + 16, 50 = 2 + 16 + 32

## 1.2

```py
def liczba_poteg(n):
    lp = 0
    while n > 0:
        lp += n % 2
        n = n // 2
    return lp


print(liczba_poteg(18))
```

**Odpowiedź:** dla n = 18 wynik lp = 2 (liczba jedynek w zapisie binarnym n)

## 2.1 i 2.2

```py
# zabawki: (nazwa, masa, cena)
zabawki = [("rowerek", 8, 320), ("wozek dla lalek", 4, 152), ("lalka", 1, 37), ("duzy mis", 2, 70),
           ("klocki", 3, 99), ("hulajnoga", 5, 155), ("maly mis", 1, 30)]


def koszyk_z_powtorzeniami(lista, mk):
    # algorytm z zadania 2.2 - zachlannie, kazda zabawka moze wystapic wiele razy
    K = [0] * len(lista)
    w = 0                              # krok 2
    i = 0
    while i < len(lista) and mk > 0:
        nazwa, masa, cena = lista[i]
        K[i] = mk // masa
        mk = mk % masa
        w = w + K[i] * cena            # krok 7
        i += 1
    return K, w


strategie = {
    "I": sorted(zabawki, key=lambda z: (-z[2], z[1])),     # od najdrozszej, przy remisie lzejsza
    "II": sorted(zabawki, key=lambda z: (z[1], -z[2])),    # od najlzejszej, przy remisie drozsza
    "III": sorted(zabawki, key=lambda z: -z[2] / z[1]),    # od najwiekszego ilorazu cena/masa
}

for nazwa_strategii, lista in strategie.items():
    K, w = koszyk_z_powtorzeniami(lista, 10)
    zawartosc = [f"{K[i]}x {lista[i][0]}" for i in range(len(lista)) if K[i] > 0]
    print(nazwa_strategii, zawartosc, w)
```

**Odpowiedź:** I: rowerek + duży miś, 390 zł; II: 10x lalka, 370 zł; III: rowerek + 2x lalka, 394 zł. Uzupełnienie algorytmu: krok 2: `w ← 0`, krok 7: `w ← w + K[i] * CENA[i]`

## 2.3 i 2.4

```py
zabawki = [("rowerek", 8, 320), ("wozek dla lalek", 4, 152), ("lalka", 1, 37), ("duzy mis", 2, 70),
           ("klocki", 3, 99), ("hulajnoga", 5, 155), ("maly mis", 1, 30)]


def koszyk_bez_powtorzen(lista, mk):
    # algorytm z zadania 2.4 - kazda zabawka co najwyzej raz
    K = [0] * len(lista)
    w = 0
    for i in range(len(lista)):
        nazwa, masa, cena = lista[i]
        if masa <= mk:
            K[i] = 1
            mk -= masa
            w += cena
    return K, w


strategie = {
    "I": sorted(zabawki, key=lambda z: (-z[2], z[1])),
    "II": sorted(zabawki, key=lambda z: (z[1], -z[2])),
    "III": sorted(zabawki, key=lambda z: -z[2] / z[1]),
}

for nazwa_strategii, lista in strategie.items():
    K, w = koszyk_bez_powtorzen(lista, 10)
    zawartosc = [lista[i][0] for i in range(len(lista)) if K[i] == 1]
    print(nazwa_strategii, zawartosc, w)
```

**Odpowiedź:** I: rowerek, duży miś — 390 zł; II: lalka, mały miś, duży miś, klocki — 236 zł; III: rowerek, lalka, mały miś — 387 zł

## 4.1

```py
licznik = 0

with open("slowa.txt") as file:
    for line in file:
        slowo = line.strip()
        if slowo.count("0") > slowo.count("1"):
            licznik += 1

print(licznik)
```

**Odpowiedź:** 441

## 4.2

```py
licznik = 0

with open("slowa.txt") as file:
    for line in file:
        slowo = line.strip()
        # dokladnie dwa bloki: najpierw same zera, potem same jedynki
        zera = len(slowo) - len(slowo.lstrip("0"))
        if 0 < zera < len(slowo) and slowo[zera:] == "1" * (len(slowo) - zera):
            licznik += 1

print(licznik)
```

**Odpowiedź:** 44

## 4.3

```py
def najdluzszy_blok_zer(slowo):
    najdluzszy = biezacy = 0
    for znak in slowo:
        if znak == "0":
            biezacy += 1
            najdluzszy = max(najdluzszy, biezacy)
        else:
            biezacy = 0
    return najdluzszy


slowa = []
with open("slowa.txt") as file:
    for line in file:
        slowa.append(line.strip())

maks = 0
for slowo in slowa:
    maks = max(maks, najdluzszy_blok_zer(slowo))

print(maks)
for slowo in slowa:
    if najdluzszy_blok_zer(slowo) == maks:
        print(slowo)
```

**Odpowiedź:** 10; 001010000000000, 1001010001000000000011001

## 5.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
panstwo_zawodnika = {}
with open("zawodnicy.txt") as file:
    next(file)
    for line in file:
        id_zawodnika, nazwisko_imie, panstwo = line.strip().split(";")
        panstwo_zawodnika[id_zawodnika] = panstwo

zwyciestwa = {}
with open("puchar.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        if dane[1] == "1":
            panstwo = panstwo_zawodnika[dane[2]]
            zwyciestwa[panstwo] = zwyciestwa.get(panstwo, 0) + 1

for panstwo in sorted(zwyciestwa):
    print(panstwo, zwyciestwa[panstwo])
```

**Odpowiedź:** Austria 63, Czechy 6, Finlandia 49, Japonia 6, Niemcy 22, Norwegia 35, Polska 35, Slowenia 6, Szwajcaria 23

## 5.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
nazwisko = {}
with open("zawodnicy.txt") as file:
    next(file)
    for line in file:
        id_zawodnika, nazwisko_imie, panstwo = line.strip().split(";")
        nazwisko[id_zawodnika] = nazwisko_imie

wypisani = []
with open("puchar.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        nota = float(dane[5].replace(",", "."))
        if nota > 450 and dane[2] not in wypisani:
            wypisani.append(dane[2])
            print(nazwisko[dane[2]])
```

**Odpowiedź:** HAUTAMAEKI Matti, LJOEKELSOEY Roar, WIDHOELZL Andreas, ROMOEREN Bjoern-Einar, HAPPONEN Janne

## 5.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
with open("zawodnicy.txt") as file:
    next(file)
    for line in file:
        id_zawodnika, nazwisko_imie, panstwo = line.strip().split(";")
        if nazwisko_imie == "MALYSZ Adam":
            id_malysza = id_zawodnika

zawody_zakopane = set()
with open("zawody.txt") as file:
    next(file)
    for line in file:
        id_zawodow, data, skocznia, sezon = line.strip().split(";")
        if skocznia == "Zakopane":
            zawody_zakopane.add(id_zawodow)

licznik = 0
with open("puchar.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        if dane[1] == "1" and dane[2] == id_malysza and dane[6] in zawody_zakopane:
            licznik += 1

print(licznik)
```

**Odpowiedź:** 3

## 5.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
with open("zawodnicy.txt") as file:
    next(file)
    for line in file:
        id_zawodnika, nazwisko_imie, panstwo = line.strip().split(";")
        if nazwisko_imie == "MALYSZ Adam":
            id_malysza = id_zawodnika

sezon_zawodow = {}
with open("zawody.txt") as file:
    next(file)
    for line in file:
        id_zawodow, data, skocznia, sezon = line.strip().split(";")
        sezon_zawodow[id_zawodow] = sezon

# sezon -> [suma I serii, suma II serii, liczba zawodow]
sezony = {}
with open("puchar.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        if dane[2] == id_malysza:
            sezon = sezon_zawodow[dane[6]]
            if sezon not in sezony:
                sezony[sezon] = [0, 0, 0]
            sezony[sezon][0] += float(dane[3].replace(",", "."))
            sezony[sezon][1] += float(dane[4].replace(",", "."))
            sezony[sezon][2] += 1

for sezon in sorted(sezony):
    seria1, seria2, ile = sezony[sezon]
    print(sezon, round(seria1 / ile, 3), round(seria2 / ile, 3))
```

**Odpowiedź:** 2000/2001 142,23 125,43; 2001/2002 125,80 125,55; 2002/2003 138,28 133,68; 2003/2004 126,93 119,64; 2004/2005 138,94 138,79; 2005/2006 138,94 129,44; 2006/2007 143,73 124,93; 2007/2008 129,43 118,64; 2008/2009 134,00 123,93; 2009/2010 137,87 130,87

## 6.1, 6.2, 6.3 i 6.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
from datetime import date

POJEMNOSC = 2500000
woda = POJEMNOSC
dni_odprowadzania = 0
z_wodociagow = 0
najmniej = None
soboty_maja = []

with open("deszcz.txt") as file:
    next(file)
    for line in file:
        data, opady = line.split()
        dzien = date.fromisoformat(data)
        # stan rano
        if najmniej is None or woda < najmniej[1]:
            najmniej = (data, woda)
        odprowadzono = 0
        if opady == "1":
            woda *= 1.03
            if woda > POJEMNOSC:
                odprowadzono = woda - POJEMNOSC
                woda = POJEMNOSC
                dni_odprowadzania += 1
        else:
            woda -= 100 * 500 * 2      # zraszanie 100 dzialek po 500 m2, 2 l/m2
            woda *= 0.99               # parowanie
        dolano = 0
        if dzien.weekday() == 5:       # sobota
            dolano = min(500000, POJEMNOSC - woda)
            woda += dolano
            z_wodociagow += dolano
            if dzien.month == 5:
                soboty_maja.append((data, round(odprowadzono), round(dolano)))

print("6.1", dni_odprowadzania)
print("6.2", round(z_wodociagow))
print("6.3", najmniej[0], round(najmniej[1]))
print("6.4")
for wiersz in soboty_maja:
    print(*wiersz)
```

**Odpowiedź:** 6.1: 13; 6.2: 8 289 356 (lub 8 289 355); 6.3: 2014-09-20, 1 303 938 l; 6.4: 2014-05-03 0 176 193, 2014-05-10 75 000 0, 2014-05-17 0 109 538, 2014-05-24 0 354 118, 2014-05-31 0 500 000; 6.5 — wykres kolumnowy z kolumny „dolano” zestawienia 6.4
