<h1 align="center">Matura 2016 — maj, poziom rozszerzony (stara formuła)</h1>
 
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

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

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

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

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
