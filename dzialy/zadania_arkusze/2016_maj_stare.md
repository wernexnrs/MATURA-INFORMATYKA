<h1 align="center">2016 maj (stara formuła)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/MIN-R1_1P-162.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/MIN-R2_1P-162.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/Dane_PR2.zip) --- [ODPOWIEDZI](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/zasady_oceniania/MIN-R1-S.pdf)

## 2.1, 2.2 i 2.3

```py
def popularnosc(A):
    n = len(A)
    maks = 1
    nr = 0
    porownania = 0      # wiersz 5.
    wiersz6 = 0
    wiersz8 = 0
    for i in range(n):
        k = 0
        for j in range(i, n):
            porownania += 1
            if A[i] == A[j]:
                k += 1
                wiersz6 += 1
        if k > maks:
            maks = k
            nr = i
            wiersz8 += 1
    return A[nr], porownania, wiersz6, wiersz8


# 2.1
for A in [[1, 2, 1, 2, 1], [2, 4, 4, 2, 4, 2], [2, 3, 3, 4, 4, 3, 2, 2, 3]]:
    print(popularnosc(A)[0])

# 2.2 - liczba porownan w wierszu 5.
for n in [2, 3, 7, 10, 15, 1000]:
    print(n, popularnosc([0] * n)[1])

# 2.3 - wszystkie elementy rowne
n = 10
wynik, porownania, wiersz6, wiersz8 = popularnosc([5] * n)
print(wiersz6, n * (n + 1) // 2, wiersz8)
```

**Odpowiedź:** 2.1: 1; 2; 3. 2.2: 3; 6; 28; 55; 120; 500500 (czyli n(n+1)/2). 2.3: wiersz 6. — n(n+1)/2 razy, wiersz 8. — 1 raz

## 3.1 i 3.3

```py
def suma_przekatnej(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i * (n - i + 1)
    return suma


print(suma_przekatnej(1), suma_przekatnej(6), suma_przekatnej(8))
```

**Odpowiedź:** 3.1: 120 (3.2: liczba piątek na n-tej przekątnej to n − 4)

## 4.1, 4.2 i 4.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def doswiadczenie(porcja):
    substancja = 4000.0
    woda = 1000.0
    dolana_woda = 0
    stan_191 = None
    najmniejsze_stezenie = 1
    for minuta in range(1, 1501):
        if minuta == 191:
            stan_191 = (substancja + woda, woda, substancja)
        # koniec parzystej minuty - dozownik pobiera porcje roztworu
        if minuta % 2 == 0:
            objetosc = substancja + woda
            substancja -= porcja * substancja / objetosc
            woda -= porcja * woda / objetosc
        # co 50 minut (51., 101., ...) robot dolewa wode do 5 litrow
        if minuta % 50 == 1 and minuta > 1:
            dolewka = 5000 - (substancja + woda)
            woda += dolewka
            dolana_woda += dolewka
        najmniejsze_stezenie = min(najmniejsze_stezenie, substancja / (substancja + woda))
    stezenie = substancja / (substancja + woda)
    return stan_191, stezenie, dolana_woda, najmniejsze_stezenie


stan_191, stezenie, dolana_woda, _ = doswiadczenie(20)
print("4.1", [round(x, 2) for x in stan_191])
print("4.2", round(stezenie * 100, 2), round(dolana_woda, 2))

# 4.4 - zwiekszamy porcje co 0,01 ml, dopoki stezenie nie spadnie ponizej 1%
setne = 2000
while doswiadczenie((setne + 1) / 100)[3] >= 0.01:
    setne += 1
print("4.4", setne / 100)
```

**Odpowiedź:** 4.1: roztwór 4600,00 ml, woda 1917,28 ml, substancja X 2682,72 ml (w kluczu CKE wartości wody i substancji są zamienione miejscami — stężenie 0,8·0,9³ = 58,32% daje 2682,72 ml substancji); 4.2: 3,77%, 14 500 ml; 4.4: 28,04 ml

## 4.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
# dane do wykresu liniowego: minuta, woda, substancja X
substancja = 4000.0
woda = 1000.0

with open("wykres_4_3.txt", "w") as wynik:
    wynik.write("minuta;woda;substancja\n")
    for minuta in range(0, 1501):
        wynik.write(f"{minuta};{woda:.2f};{substancja:.2f}\n")
        if minuta % 2 == 0 and minuta > 0:
            objetosc = substancja + woda
            substancja -= 20 * substancja / objetosc
            woda -= 20 * woda / objetosc
        if minuta % 50 == 1 and minuta > 1:
            woda += 5000 - (substancja + woda)
```

**Odpowiedź:** wykres liniowy dwóch serii (woda — rośnie „ząbkami”, substancja X — maleje) tworzymy z pliku `wykres_4_3.txt`

## 5.1, 5.2 i 5.3

```py
def sasiedzi(plansza, w, k):
    n, m = len(plansza), len(plansza[0])
    licznik = 0
    for dw in (-1, 0, 1):
        for dk in (-1, 0, 1):
            if (dw != 0 or dk != 0) and plansza[(w + dw) % n][(k + dk) % m] == "X":
                licznik += 1
    return licznik


def nastepne_pokolenie(plansza):
    nowa = []
    for w in range(len(plansza)):
        wiersz = ""
        for k in range(len(plansza[0])):
            s = sasiedzi(plansza, w, k)
            if s == 3 or (plansza[w][k] == "X" and s == 2):
                wiersz += "X"
            else:
                wiersz += "."
        nowa.append(wiersz)
    return nowa


def zywe(plansza):
    return sum(wiersz.count("X") for wiersz in plansza)


plansza = []
with open("gra.txt") as file:
    for line in file:
        if line.strip():
            plansza.append(line.strip())

pokolenia = {1: plansza}
for p in range(2, 101):
    pokolenia[p] = nastepne_pokolenie(pokolenia[p - 1])

print("5.1", sasiedzi(pokolenia[37], 1, 18))
print("5.2", zywe(pokolenia[2]))
for p in range(2, 101):
    if pokolenia[p] == pokolenia[p - 1]:
        print("5.3", p, zywe(pokolenia[p]))
        break
```

**Odpowiedź:** 5.1: 4; 5.2: 8; 5.3: w 51. pokoleniu, 8 żywych komórek

## 6.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
malarze = {}
with open("malarze.txt") as file:
    next(file)
    for line in file:
        id_malarza, nazwisko, imie = line.strip().split("\t")
        malarze[id_malarza] = imie + " " + nazwisko

wystawione = {}
with open("obrazy.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_obrazu, tytul, id_malarza, id_oddzialu, stan = line.strip().split("\t")
        if stan in ("ekspozycja stala", "ekspozycja czasowa"):
            wystawione[id_malarza] = wystawione.get(id_malarza, 0) + 1

ranking = sorted(wystawione.items(), key=lambda x: x[1], reverse=True)
for id_malarza, ile in ranking[:2]:
    print(malarze[id_malarza], ile)
```

**Odpowiedź:** Jacek Malczewski 25, Jan Matejko 11

## 6.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
malarze = {}
with open("malarze.txt") as file:
    next(file)
    for line in file:
        id_malarza, nazwisko, imie = line.strip().split("\t")
        malarze[id_malarza] = imie + " " + nazwisko

with open("obrazy.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_obrazu, tytul, id_malarza, id_oddzialu, stan = line.strip().split("\t")
        if "polowanie" in tytul or "Polowanie" in tytul:
            print(tytul, "-", malarze[id_malarza])
```

**Odpowiedź:** Zjazd na polowanie — Józef Chełmoński; Polowanie na kaczki — Julian Fałat; Wyjazd na polowanie, Polowanie w lesie — Maksymilian Gierymski; Polowanie w Poturzycy, Polowanie na lisa — Juliusz Kossak

## 6.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
# plik oddzialy.txt jest zapisany w UTF-16
miejscowosc = {}
with open("oddzialy.txt", encoding="utf-16") as file:
    next(file)
    for line in file:
        id_oddzialu, nazwa = line.strip().split("\t")
        miejscowosc[id_oddzialu] = nazwa

stany = ["ekspozycja czasowa", "ekspozycja stala", "w magazynie", "wypozyczony"]
zestawienie = {}
with open("obrazy.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_obrazu, tytul, id_malarza, id_oddzialu, stan = line.strip().split("\t")
        nazwa = miejscowosc[id_oddzialu]
        if nazwa not in zestawienie:
            zestawienie[nazwa] = {s: 0 for s in stany}
        zestawienie[nazwa][stan] += 1

print("miejscowosc", *stany, sep=";")
for nazwa in sorted(zestawienie):
    print(nazwa, *[zestawienie[nazwa][s] for s in stany], sep=";")
```

**Odpowiedź:** (ekspozycja czasowa; stała; w magazynie; wypożyczony) Gdansk 1 15 2 1, Krakow 7 20 9 8, Nieborow 4 10 2 2, Warszawa 68 65 47 52, Wroclaw 4 15 6 1

## 6.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
with open("oddzialy.txt", encoding="utf-16") as file:
    next(file)
    for line in file:
        id_oddzialu, nazwa = line.strip().split("\t")
        if nazwa == "Warszawa":
            id_warszawy = id_oddzialu

litery = {}
with open("obrazy.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_obrazu, tytul, id_malarza, id_oddzialu, stan = line.strip().split("\t")
        if id_oddzialu == id_warszawy:
            litera = tytul[0].upper()
            litery[litera] = litery.get(litera, 0) + 1

print(max(litery, key=litery.get))
```

**Odpowiedź:** P

## 6.5

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
malarze = {}
with open("malarze.txt") as file:
    next(file)
    for line in file:
        id_malarza, nazwisko, imie = line.strip().split("\t")
        malarze[id_malarza] = imie + " " + nazwisko

wypozyczone = {}
with open("obrazy.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_obrazu, tytul, id_malarza, id_oddzialu, stan = line.strip().split("\t")
        if stan == "wypozyczony":
            wypozyczone[id_malarza] = wypozyczone.get(id_malarza, 0) + 1

najlepszy = max(wypozyczone, key=wypozyczone.get)
print(malarze[najlepszy], wypozyczone[najlepszy])
```

**Odpowiedź:** Jacek Malczewski
