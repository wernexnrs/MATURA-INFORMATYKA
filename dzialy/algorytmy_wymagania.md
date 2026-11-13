<a name="main"></a>
<h1 align="center"> Algorytmy wymienione w wymaganiach </h1>

1. __algorytmy na liczbach całkowitych:__
   - ![py] ![noc++] ![nojava] [reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym,](#konwersja)
   - ![py] ![noc++] ![nojava] [sprawdzanie, czy liczba jest liczbą pierwszą,](#is_prime)
   - ![py] ![noc++] ![nojava] [sito Eratostenesa,](#sito)
   - ![py] ![noc++] ![nojava] [sprawdzanie, czy liczba jest liczbą doskonałą,](#is_perfect)
   - ![py] ![noc++] ![nojava] [rozkładanie liczby na czynniki pierwsze,](#prime_factors)
   - ![py] ![noc++] ![nojava] [iteracyjna i rekurencyjna realizacja algorytmu Euklidesa + NWW,](#nwd)
   - ![py] ![noc++] ![nojava] [iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,](#fib)
   - ![py] ![noc++] ![nojava] [wydawanie reszty metodą zachłanną,](#zachlanna)

2. __algorytmy wyszukiwania i porządkowania (sortowania):__
   - ![py] ![noc++] ![nojava] [wyszukiwanie liniowe,](#liniowe)
   - ![py] ![noc++] ![nojava] [wyszukiwanie binarne (iteracyjne i rekurencyjne),](#binarne)
   - ![py] ![noc++] ![nojava] [jednoczesne wyszukiwanie minimum i maksimum,](#minmax)
   - ![py] ![c++] ![nojava] [bąbelkowy, ](#bob)
   - ![py] ![noc++] ![nojava] [przez wybór, ](#wybor)
   - ![py] ![noc++] ![nojava] [przez wstawianie liniowe lub binarne, ](#lin)
   - ![py] ![noc++] ![nojava] [przez scalanie,](#scalanie)
   - ![py] ![noc++] ![nojava] [szybki,](#fast)
   - ![py] ![noc++] ![nojava] [kubełkowy,](#box)

3. __algorytmy numeryczne__
   - ![py] ![noc++] ![nojava] [szybkie podnoszenie do potęgi,](#fast_power)
   - ![py] ![noc++] ![nojava] [wyznaczanie miejsc zerowych funkcji metodą połowienia,](#bisekcja)
   - ![py] ![noc++] ![nojava] [obliczanie pierwiastka kwadratowego metodą Herona (Newtona),](#heron)
   - ![py] ![noc++] ![nojava] [obliczanie wartości wielomianu za pomocą schematu Hornera,](#horner)
   - ![py] ![noc++] ![nojava] [obliczanie pola obszarów zamkniętych (metoda prostokątów i trapezów),](#pole)

4. __algorytmy na tekstach__
   - ![py] ![noc++] ![nojava] [sprawdzanie, czy dany ciąg znaków tworzy palindrom,](#palindrom)
   - ![py] ![noc++] ![nojava] [sprawdzanie, czy dany ciąg znaków tworzy anagram,](#anagram)
   - ![py] ![noc++] ![nojava] [porządkowanie alfabetyczne, (leksykograficzne)](#alfa)
   - ![py] ![noc++] ![nojava] [wyszukiwanie wzorca w tekście,](#pattern)
   - ![py] ![noc++] ![nojava] [obliczanie wartości wyrażenia w odwrotnej notacji polskiej (ONP),](#onp)

5. __algorytmy kompresji i szyfrowania__
   - kody znaków o zmiennej długości,
	 * ![py] ![noc++] ![nojava] [Kompresja danych (kod prefiksowy)](#len)
	 * ![py] ![noc++] ![nojava] [Kod Huffmana](#huffman)
	 * ![py] ![c++] ![nojava] [Alfabet Morse’a](#morse)
   - szyfry przestawieniowe,
	 * ![py] ![noc++] ![nojava] [Transpozycyjny](#przes)
   - szyfry podstawieniowe,
	 * ![py] ![noc++] ![nojava] [Szyfr AtBash](#atbash)
	 * ![py] ![c++] ![nojava] [Szyfr Cezara](#cezar)
	 * ![py] ![noc++] ![nojava] [Szyfr Vigenère’a](#vigenere)
   - szyfr z kluczem jawnym,
	 * ![py] ![noc++] ![nojava] [RSA + rozszerzony algorytm Euklidesa](#rsa)

6. __algorytmy geometryczne__
   - ![py] ![noc++] ![nojava] [sprawdzanie warunku trójkąta,](#trojkat)
   - ![py] ![noc++] ![nojava] [badanie położenia punktów względem prostej,](#punkt_prosta)
   - ![py] ![noc++] ![nojava] [badanie przynależności punktu do odcinka,](#punkt_odcinek)
   - ![py] ![noc++] ![nojava] [przecinanie się odcinków,](#odcinki)
   - ![py] ![noc++] ![nojava] [przynależność punktu do obszaru (wielokąta),](#punkt_wielokat)
   - konstrukcje rekurencyjne,
	 * ![py] ![noc++] ![nojava] [Krzywa Kocha](#koch)
	 * ![py] ![noc++] ![nojava] [Drzewo Pitagorasa](#pitagoras)

<a name="konwersja"></a>
## Reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#int("number_string",base) ANY --> DEC

dec_numbers = [15, 12, 2, 4, 7, 8]

dec_TO_bin = [bin(i)[2:] for i in dec_numbers]
dec_TO_oct = [oct(i)[2:] for i in dec_numbers]
dec_TO_hex = [hex(i)[2:] for i in dec_numbers]

bin_TO_dec = [int(i, 2) for i in dec_TO_bin]
oct_TO_dec = [int(i, 8) for i in dec_TO_oct]
hex_TO_dec = [int(i, 16) for i in dec_TO_hex]
```

```python
#recursive one-liner version DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, b):  # to_base(number,base), n >= 0, 2 <= b <= 36
    return BS[n] if n < b else to_base(n // b, b) + BS[n % b]
```

```python
#recursive version DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n, b):  # to_base(number,base), n >= 0, 2 <= b <= 36
    if n < b:
        return BS[n]
    return to_base(n // b, b) + BS[n % b]
```
<b>

```
BS <- "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n - liczba dziesiętna (n >= 0)
b - podstawa systemu (2 <= b <= 36)
mod - reszta z dzielenia
div - dzielenie całkowite

def to_base(n, b):
	Jeżeli n < b:
		Zwróć BS[n]
	W innym wypadku:
		Zwróć to_base(n div b, b) + BS[n mod b]
```
</b>

```python
#iterated version with slices DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, b):  # to_base(number,base), n >= 0, 2 <= b <= 36
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res += BS[n % b]
        n //= b
    return res[::-1]  # cyfry powstają od końca, więc odwracamy napis
```
<b>

```
BS <- "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n - liczba dziesiętna (n >= 0)
b - podstawa systemu (2 <= b <= 36)
mod - reszta z dzielenia
div - dzielenie całkowite

def to_base(n, b):
	Jeżeli n == 0
		Zwróć "0"
	res <- ""
	Dopóki n > 0
		res <- BS[n mod b] + res
		n <- n div b
	Zwróć res
```
</b>

```python
#manual version ANY --> DEC (schemat Hornera)

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_dec(liczba, b):  # to_dec("number_string", base), np. to_dec("1F", 16) == 31
    wynik = 0
    for znak in liczba.upper():
        wynik = wynik * b + BS.index(znak)  # BS.index(znak) - wartość cyfry
    return wynik
```
<b>

```
liczba[1..n] - napis z cyframi liczby w systemie o podstawie b
wartosc(c) - wartość cyfry c (0..9, A = 10, B = 11, ...)

def to_dec(liczba, b):
	wynik <- 0
	Dla i = 1, 2, ... n
		wynik <- wynik * b + wartosc(liczba[i])
	Zwróć wynik
```
</b>
</details>

<a name="is_prime"></a>
## Sprawdzanie, czy liczba jest liczbą pierwszą [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
```
<b>

```
x - sprawdzana liczba całkowita
mod - reszta z dzielenia

def is_prime(x):
	Jeżeli x <= 1
		Zwróć Fałsz
	Dla i = 2, 3, ... część całkowita z pierwiastka z x
		Jeżeli x mod i == 0
			Zwróć Fałsz
	Zwróć Prawdę
```
</b>
</details>

<a name="sito"></a>
## Sito Eratostenesa [⬆️](#)
<details><summary>Rozwiń</summary>

Wyznacza wszystkie liczby pierwsze z przedziału [2, n]. Zaczynamy od tablicy, w której każda liczba jest "kandydatem" na liczbę pierwszą, a następnie dla kolejnych liczb pierwszych i wykreślamy ich wielokrotności (zaczynając od i * i, bo mniejsze wielokrotności zostały już wykreślone).

```python
def sito(n):  # zwraca listę liczb pierwszych <= n
    if n < 2:
        return []
    pierwsza = [True] * (n + 1)
    pierwsza[0] = pierwsza[1] = False
    i = 2
    while i * i <= n:
        if pierwsza[i]:
            for j in range(i * i, n + 1, i):
                pierwsza[j] = False
        i += 1

    wynik = []
    for i in range(2, n + 1):
        if pierwsza[i]:
            wynik.append(i)
    return wynik


print(sito(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
<b>

```
n - górna granica przedziału
pierwsza[2..n] - tablica wartości logicznych

def sito(n):
	Dla i = 2, 3, ... n
		pierwsza[i] <- Prawda
	i <- 2
	Dopóki i * i <= n
		Jeżeli pierwsza[i]
			j <- i * i
			Dopóki j <= n
				pierwsza[j] <- Fałsz
				j <- j + i
		i <- i + 1
	Zwróć wszystkie i, dla których pierwsza[i] == Prawda
```
</b>
</details>

<a name="is_perfect"></a>
## Sprawdzanie, czy liczba jest liczbą doskonałą [⬆️](#)
<details><summary>Rozwiń</summary>

Liczba doskonała to liczba naturalna równa sumie swoich dzielników mniejszych od niej samej, np. 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14.

```python
#O(n) version

def is_perfect(n):
    s = 1
    for i in range(2, n):
        if n % i == 0:
            s += i
    if n == s and n != 1:
        return True
    return False
```
<b>

```
n - sprawdzana liczba naturalna
mod - reszta z dzielenia

def is_perfect(n):
	s <- 1
	Dla i = 2, 3, ... n - 1
		Jeżeli n mod i == 0
			s <- s + i
	Jeżeli n == s oraz n != 1
		Zwróć Prawdę
	W innym wypadku
		Zwróć Fałsz
```
</b>

```python
#O(sqrt(n)) version - dzielniki występują w parach (i, n // i)

def is_perfect(n):
    if n < 2:
        return False
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:  # drugi dzielnik z pary (nie dodajemy dwa razy pierwiastka)
                s += n // i
        i += 1
    return s == n
```
<b>

```
n - sprawdzana liczba naturalna
mod - reszta z dzielenia
div - dzielenie całkowite

def is_perfect(n):
	Jeżeli n < 2
		Zwróć Fałsz
	s <- 1
	i <- 2
	Dopóki i * i <= n
		Jeżeli n mod i == 0
			s <- s + i
			Jeżeli i != n div i
				s <- s + n div i
		i <- i + 1
	Zwróć s == n
```
</b>
</details>

<a name="prime_factors"></a>
## Rozkładanie liczby na czynniki pierwsze [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def prime_factors(n):  # dla n <= 1 zwraca pustą listę
    czynniki = []
    k = 2
    while n > 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)  # albo print(k)
        k += 1
    return czynniki


print(prime_factors(360))  # [2, 2, 2, 3, 3, 5]
```
<b>

```
n - liczba całkowita
div - dzielenie całkowite
mod - reszta z dzielenia

def prime_factors(n):
	czynniki <- []
	k <- 2
	Dopóki n > 1
		Dopóki n mod k == 0
			n <- n div k
			Dodaj k na koniec czynniki
		k <- k + 1
	Zwróć czynniki
```
</b>
</details>

<a name="nwd"></a>
## Iteracyjna i rekurencyjna realizacja algorytmu Euklidesa + NWW [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#recursive one-liner version

def nwd(a, b): return nwd(b, a % b) if b else a
```

```python
#recursive version

def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a
```
<b>

```
a - liczba całkowita
b - liczba całkowita
mod - reszta z dzielenia

def nwd(a, b):
	Jeżeli b > 0:
		Zwróć nwd(b, a mod b)
	W innym wypadku
		Zwróć a
```
</b>

```python
#iterated version

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a
```
<b>

```
a - liczba całkowita
b - liczba całkowita
mod - reszta z dzielenia

def nwd(a, b):
	Dopóki b != 0
		t <- a
		a <- b
		b <- t mod b
	Zwróć a
```
</b>

```python
#Najmniejsza wspólna wielokrotność (korzysta z funkcji nwd powyżej)

def nww(a, b): return a * b // nwd(a, b)
```
<b>

```
a - liczba całkowita
b - liczba całkowita
div - dzielenie całkowite

def nww(a, b):
	Zwróć a * b div nwd(a,b)
```
</b>
</details>

<a name="fib"></a>
## Iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#Iterated version

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
```
<b>

```
n - numer wyrazu ciągu (f(0) = 0, f(1) = 1)

def f(n):
	a <- 0
	b <- 1
	Dla i = 1, 2, ... n
		t <- a
		a <- b
		b <- t + b
	Zwróć a
```
</b>

```python
#Recursive version

def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)
```
<b>

```
def f(n)
	Jeżeli n <= 1
		Zwróć n
	W innym wypadku
		Zwróć f(n-1) + f(n-2)
```
</b>
</details>

<a name="zachlanna"></a>
## Wydawanie reszty metodą zachłanną [⬆️](#)
<details><summary>Rozwiń</summary>

W każdym kroku wybieramy największą monetę, która nie jest większa od kwoty pozostałej do wydania. Dla nominałów takich jak w Polsce (1, 2, 5, 10, ...) daje to najmniejszą liczbę monet, ale dla dowolnych nominałów nie zawsze (np. kwota 6 i monety [1, 3, 4] -> 4 + 1 + 1 zamiast 3 + 3).

```python
do_wydania = 6
monety = [1, 2, 5]

def wydawanie(do_wydania, monety):
    count = 0
    historia = []

    while do_wydania > 0:
        nominal = 0
        for i in range(len(monety)):
            if do_wydania >= monety[i] > nominal:
                nominal = monety[i]
        if nominal == 0:  # żadna moneta nie mieści się w kwocie - reszty nie da się wydać
            return None
        do_wydania -= nominal

        historia.append(nominal)
        count += 1

    return count, historia


wynik = wydawanie(do_wydania, monety)
if wynik is None:
    print("Nie da się wydać reszty tymi monetami")
else:
    print(f'Resztę wydasz w {wynik[0]} monetach, te monety to {wynik[1]}')
```
<b>

```
do_wydania - kwota do wydania
monety[1..n] - dostępne nominały (każdy w dowolnej ilości)

def wydawanie(do_wydania, monety):
	count <- 0
	historia <- []
	Dopóki do_wydania > 0
		nominal <- 0
		Dla i = 1, 2, ... n
			Jeżeli do_wydania >= monety[i] oraz monety[i] > nominal
				nominal <- monety[i]
		Jeżeli nominal == 0
			Zwróć "nie da się wydać reszty"
		do_wydania <- do_wydania - nominal
		Dodaj nominal na koniec historia
		count <- count + 1
	Zwróć count, historia
```
</b>
</details>

<a name="liniowe"></a>
## Wyszukiwanie liniowe [⬆️](#)
<details><summary>Rozwiń</summary>

Sprawdzamy po kolei wszystkie elementy tablicy (tablica nie musi być posortowana). Złożoność O(n).

```python
def linear_search(tab, x):  # indeks pierwszego wystąpienia x albo -1
    for i in range(len(tab)):
        if tab[i] == x:
            return i
    return -1
```
<b>

```
tab[1..n] - przeszukiwana tablica
x - szukana wartość

def linear_search(tab, x):
	Dla i = 1, 2, ... n
		Jeżeli tab[i] == x
			Zwróć i
	Zwróć -1
```
</b>
</details>

<a name="binarne"></a>
## Wyszukiwanie binarne [⬆️](#)
<details><summary>Rozwiń</summary>

Działa tylko dla tablicy posortowanej rosnąco. W każdym kroku porównujemy szukaną wartość ze środkowym elementem i odrzucamy połowę przedziału. Złożoność O(log n).

```python
#Iterated version

def binary_search(tab, x):  # indeks elementu równego x albo -1
    lewy, prawy = 0, len(tab) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if tab[srodek] == x:
            return srodek
        elif tab[srodek] < x:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1
```
<b>

```
tab[1..n] - tablica posortowana rosnąco
x - szukana wartość
div - dzielenie całkowite

def binary_search(tab, x):
	lewy <- 1
	prawy <- n
	Dopóki lewy <= prawy
		srodek <- (lewy + prawy) div 2
		Jeżeli tab[srodek] == x
			Zwróć srodek
		Jeżeli tab[srodek] < x
			lewy <- srodek + 1
		W innym wypadku
			prawy <- srodek - 1
	Zwróć -1
```
</b>

```python
#Recursive version - wywołanie: binary_search_rek(tab, x, 0, len(tab) - 1)

def binary_search_rek(tab, x, lewy, prawy):
    if lewy > prawy:
        return -1
    srodek = (lewy + prawy) // 2
    if tab[srodek] == x:
        return srodek
    if tab[srodek] < x:
        return binary_search_rek(tab, x, srodek + 1, prawy)
    return binary_search_rek(tab, x, lewy, srodek - 1)
```
<b>

```
tab[1..n] - tablica posortowana rosnąco
div - dzielenie całkowite
wywołanie: binary_search_rek(tab, x, 1, n)

def binary_search_rek(tab, x, lewy, prawy):
	Jeżeli lewy > prawy
		Zwróć -1
	srodek <- (lewy + prawy) div 2
	Jeżeli tab[srodek] == x
		Zwróć srodek
	Jeżeli tab[srodek] < x
		Zwróć binary_search_rek(tab, x, srodek + 1, prawy)
	W innym wypadku
		Zwróć binary_search_rek(tab, x, lewy, srodek - 1)
```
</b>
</details>

<a name="minmax"></a>
## Jednoczesne wyszukiwanie minimum i maksimum [⬆️](#)
<details><summary>Rozwiń</summary>

Wersja naiwna porównuje każdy element osobno z minimum i z maksimum, czyli wykonuje ok. 2n porównań. Metoda "parami" bierze po dwa elementy, najpierw porównuje je ze sobą, a potem mniejszy z minimum, a większy z maksimum - 3 porównania na 2 elementy, czyli ok. 3n/2 porównań.

```python
#Wersja naiwna (ok. 2n porównań)

def min_max_naiwnie(tab):
    if len(tab) == 0:
        return None
    mini = maks = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < mini:
            mini = tab[i]
        if tab[i] > maks:
            maks = tab[i]
    return mini, maks
```

```python
#Metoda "parami" (ok. 3n/2 porównań)

def min_max(tab):  # zwraca (minimum, maksimum) albo None dla pustej tablicy
    n = len(tab)
    if n == 0:
        return None
    if n % 2 == 1:  # nieparzysta liczba elementów - pierwszy element jest i min, i max
        mini = maks = tab[0]
        start = 1
    else:  # parzysta - pierwszą parę porównujemy ze sobą
        if tab[0] < tab[1]:
            mini, maks = tab[0], tab[1]
        else:
            mini, maks = tab[1], tab[0]
        start = 2

    for i in range(start, n - 1, 2):
        if tab[i] < tab[i + 1]:
            mniejszy, wiekszy = tab[i], tab[i + 1]
        else:
            mniejszy, wiekszy = tab[i + 1], tab[i]
        if mniejszy < mini:
            mini = mniejszy
        if wiekszy > maks:
            maks = wiekszy
    return mini, maks
```
<b>

```
tab[1..n] - tablica liczb (n >= 1)
mod - reszta z dzielenia

def min_max(tab):
	Jeżeli n mod 2 == 1
		mini <- tab[1]
		maks <- tab[1]
		i <- 2
	W innym wypadku
		Jeżeli tab[1] < tab[2]
			mini <- tab[1]
			maks <- tab[2]
		W innym wypadku
			mini <- tab[2]
			maks <- tab[1]
		i <- 3
	Dopóki i < n
		Jeżeli tab[i] < tab[i + 1]
			mniejszy <- tab[i]
			wiekszy <- tab[i + 1]
		W innym wypadku
			mniejszy <- tab[i + 1]
			wiekszy <- tab[i]
		Jeżeli mniejszy < mini
			mini <- mniejszy
		Jeżeli wiekszy > maks
			maks <- wiekszy
		i <- i + 2
	Zwróć mini, maks
```
</b>
</details>

<a name="bob"></a>
## Sortowanie bąbelkowe [⬆️](#)

<details><summary>Rozwiń  C++</summary>

Sortuje rosnąco (zamiana, gdy tab[j] > tab[j + 1]), tak samo jak wersja w Pythonie.

```cpp
#include <iostream>

using namespace std;

void babelkowe(int* tab, int rozmiar) {
	int k { 0 };

	for (int i = 0; i < rozmiar; i++) {
		for (int j = 0; j < rozmiar - i - 1; j++) {
			if (tab[j] > tab[j + 1]) {
				k = tab[j + 1];
				tab[j + 1] = tab[j];
				tab[j] = k;
			}
		}
	}

	for (int i = 0; i < rozmiar; i++) cout << tab[i] << " ";
}
```
</details>

<details><summary>Rozwiń Python</summary>

```python
#In place

def bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]
```
<b>

```
A[1..n] - sortowana tablica

Dla i = 1, 2, ... n
	Dla j = 1, 2, ... n – i
		Jeżeli A[j] > A[j + 1]
			t <- A[j + 1]
			A[j + 1] <- A[j]
			A[j] <- t
```
</b>

```py
# Wersja zoptymalizowana - kończy pracę, gdy w całym przebiegu nie było żadnej zamiany
arr = [1,1,1,1,1,1,2]


def swap(arr,x,y): #to albo swap jak wyżej
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def bubblesort(arr):

    for i in range(len(arr)):
        issorted = True
        for j in range(1,len(arr)-i):
            if arr[j] < arr[j-1]:
                swap(arr,j ,j-1)
                issorted = False
        if issorted:
            break

bubblesort(arr)
print(arr)
```
<b>

```
A[1..n] - sortowana tablica

Dla i = 1, 2, ... n
	posortowana <- Prawda
	Dla j = 2, 3, ... n – i + 1
		Jeżeli A[j] < A[j - 1]
			Zamień A[j] z A[j - 1]
			posortowana <- Fałsz
	Jeżeli posortowana
		Zakończ sortowanie
```
</b>
</details>

<a name="wybor"></a>
## Sortowanie przez wybór [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#In place

def selection_sort(tab):
    for i in range(len(tab)):
        mini = i
        for j in range(i+1, len(tab)):
            if tab[mini] > tab[j]:
                mini = j
        tab[i], tab[mini] = tab[mini], tab[i]
```
<b>

```
A[1..n] - sortowana tablica
n - ilość liczb

Dla i = 1, 2, ... n
	mini <- i
	Dla j = i + 1, ... n
		Jeżeli A[mini] > A[j]
			mini <- j
	t <- A[i]
	A[i] <- A[mini]
	A[mini] <- t
```
</b>
</details>

<a name="lin"></a>
## Sortowanie przez wstawianie liniowe lub binarne [⬆️](#)
<details><summary>Rozwiń</summary>

### Wstawianie liniowe
Kolejny element wstawiamy do posortowanej już części tablicy, przesuwając większe elementy o jedno miejsce w prawo.

```python
#In place

def insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]
        j = i
        while j > 0 and A[j - 1] > liczba:
            A[j] = A[j - 1]
            j -= 1
        A[j] = liczba
```
<b>

```
n - długość tablicy
A[1..n] - sortowana tablica

Dla i = 2, 3, ... n
	liczba <- A[i]
	j <- i
	Dopóki j > 1 oraz A[j - 1] > liczba
		A[j] <- A[j - 1]
		j <- j - 1
	A[j] <- liczba
```
</b>

### Wstawianie binarne
Miejsce dla kolejnego elementu w posortowanej części tablicy szukamy wyszukiwaniem binarnym (mniej porównań), a potem przesuwamy elementy w prawo i wstawiamy go.

```python
#In place

def binary_insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]
        # szukamy binarnie pierwszej pozycji w A[0..i-1], na której stoi element > liczba
        lewy, prawy = 0, i
        while lewy < prawy:
            srodek = (lewy + prawy) // 2
            if A[srodek] <= liczba:
                lewy = srodek + 1
            else:
                prawy = srodek
        # przesuwamy A[lewy..i-1] o jedno miejsce w prawo
        for j in range(i, lewy, -1):
            A[j] = A[j - 1]
        A[lewy] = liczba
```
<b>

```
n - długość tablicy
A[1..n] - sortowana tablica
div - dzielenie całkowite

Dla i = 2, 3, ... n
	liczba <- A[i]
	lewy <- 1
	prawy <- i
	Dopóki lewy < prawy
		srodek <- (lewy + prawy) div 2
		Jeżeli A[srodek] <= liczba
			lewy <- srodek + 1
		W innym wypadku
			prawy <- srodek
	Dla j = i, i - 1, ... lewy + 1
		A[j] <- A[j - 1]
	A[lewy] <- liczba
```
</b>
</details>

<a name="scalanie"></a>
## Sortowanie przez scalanie [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#In place (sortuje przekazaną tablicę, dodatkowo ją zwraca)

def merge_sort(tab):
    if len(tab) < 2:
        return tab

    i = j = k = 0
    mid = len(tab) // 2
    L, R = tab[:mid], tab[mid:]
    merge_sort(L)
    merge_sort(R)

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            tab[k] = L[i]
            i += 1
        else:
            tab[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        tab[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        tab[k] = R[j]
        j += 1
        k += 1

    return tab
```
<b>

```
tab[1..n] - sortowana tablica
n - długość tablicy
dł() - długość tablicy
div - dzielenie całkowite

def merge_sort(tab):
	Jeżeli n < 2
		Zwróć tab
	mid <- n div 2
	L <- tab[1..mid]
	R <- tab[mid + 1..n]
	merge_sort(L)
	merge_sort(R)

	i <- 1
	j <- 1
	k <- 1
	Dopóki i <= dł(L) oraz j <= dł(R)
		Jeżeli L[i] <= R[j]
			tab[k] <- L[i]
			i <- i + 1
		W innym wypadku
			tab[k] <- R[j]
			j <- j + 1
		k <- k + 1

	Dopóki i <= dł(L)
		tab[k] <- L[i]
		i <- i + 1
		k <- k + 1

	Dopóki j <= dł(R)
		tab[k] <- R[j]
		j <- j + 1
		k <- k + 1
	Zwróć tab
```
</b>
</details>

<a name="fast"></a>
## Sortowanie szybkie [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def quicksort(t):
    # jeżeli tablica jest pusta lub ma jeden element, to nie trzeba nic robić, można ją zwrócić.
    if len(t) <= 1:
        return t

    # wybierasz pivot (tutaj na końcu)
    pivot = t[-1]
    smaller = []
    greater = []

    # wszystkie mniejsze lub równe wartości od pivota idą do listy smaller a większe do greater.
    # len(t) - 1, bo pracujemy na elementach bez ostatniego, którym jest pivot.
    for i in range(0, len(t) - 1):
        if t[i] <= pivot:
            smaller.append(t[i])
        else:
            greater.append(t[i])

    # zwracasz tablicę, gdzie wszystkie mniejsze wartości są po lewej, a większe po prawej od pivota,
    # a pivot trafia na miejsce końcowe w tablicy wyjściowej.
    return quicksort(smaller) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    arr = [60, 20, 11, 122, 214, 345, 1324, 1, 2, 3, 6, 74, 3, 9]
    print(quicksort(arr))

```
<b>

```
tab[1..n] - tablica wejściowa
dł() - funkcja zwracająca rozmiar tablicy

def quicksort(tab)
	Jeżeli dł(tab) <= 1:
		Zwróć tab

	pivot <- tab[dł(tab)]
	smaller <- []
	greater <- []

	Dla i = 1,2,3, ... , dł(tab) - 1
		Jeżeli tab[i] <= pivot
			Dodaj element tab[i] na koniec smaller
		W innym wypadku
			Dodaj element tab[i] na koniec greater

	Zwróć quicksort(smaller) + [pivot] + quicksort(greater)
```
</b>
</details>

<a name="box"></a>
## Sortowanie kubełkowe [⬆️](#)
<details><summary>Rozwiń</summary>

Założenia: sortujemy liczby (całkowite lub rzeczywiste), najlepiej nieujemne i w miarę równomiernie rozłożone w przedziale [min, max]. Przedział [min, max] dzielimy na n równych części (kubełków), każdą liczbę wrzucamy do odpowiedniego kubełka, sortujemy kubełki (np. przez wstawianie) i sklejamy je po kolei. Dzięki odejmowaniu minimum kod działa także dla liczb ujemnych.

```python
# Not in place - zwraca nową, posortowaną listę

def insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]
        j = i
        while j > 0 and A[j - 1] > liczba:
            A[j] = A[j - 1]
            j -= 1
        A[j] = liczba


def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr[:]
    mini, maks = min(arr), max(arr)  # liczone raz, przed pętlą
    if mini == maks:  # wszystkie elementy są równe
        return arr[:]

    buckets = [[] for _ in range(n)]
    szerokosc = (maks - mini) / n  # zakres wartości jednego kubełka

    for i in range(n):
        j = int((arr[i] - mini) / szerokosc)
        if j >= n:  # maksimum trafia do ostatniego kubełka
            j = n - 1
        buckets[j].append(arr[i])

    output = []
    for z in range(n):
        insertion_sort(buckets[z])
        output += buckets[z]
    return output
```
<b>

```
arr[1..n] - tablica liczb
n - długość tablicy
min(), max() - najmniejszy i największy element tablicy
int() - część całkowita liczby

def bucket_sort(arr):
	Jeżeli n <= 1
		Zwróć arr
	mini <- min(arr)
	maks <- max(arr)
	Jeżeli mini == maks
		Zwróć arr
	kubelki[1..n] <- n pustych list
	szerokosc <- (maks - mini) / n
	Dla i = 1, 2, ... n
		j <- int((arr[i] - mini) / szerokosc) + 1
		Jeżeli j > n
			j <- n
		Dodaj arr[i] na koniec kubelki[j]
	wynik <- []
	Dla j = 1, 2, ... n
		Posortuj kubelki[j] (np. przez wstawianie)
		Dopisz kubelki[j] na koniec wynik
	Zwróć wynik
```
</b>
</details>

<a name="fast_power"></a>
## Szybkie podnoszenie do potęgi [⬆️](#)
<details><summary>Rozwiń</summary>

Zamiast mnożyć a przez siebie n razy (n mnożeń), korzystamy z tego, że a^n = (a^(n div 2))^2 dla parzystego n oraz a^n = a * a^(n - 1) dla nieparzystego n. Wystarczy wtedy ok. 2 * log2(n) mnożeń.

### Szybkie potęgowanie a^n (iteracyjnie, na bitach wykładnika)
```python
#Iterated version

def fast_power(a, n):  # a^n, n >= 0
    wynik = 1
    while n > 0:
        if n % 2 == 1:  # ostatni bit wykładnika to 1
            wynik *= a
        a *= a  # a, a^2, a^4, a^8, ...
        n //= 2
    return wynik
```
<b>

```
a - podstawa
n - wykładnik (n >= 0)
mod - reszta z dzielenia
div - dzielenie całkowite

def fast_power(a, n):
	wynik <- 1
	Dopóki n > 0
		Jeżeli n mod 2 == 1
			wynik <- wynik * a
		a <- a * a
		n <- n div 2
	Zwróć wynik
```
</b>

### Szybkie potęgowanie modularne (szybko znajduje wartość base ^ power mod m, domyślnie m = 1000000007)
```python
#Iterated version

def fast_power_mod(base, power, m=1000000007):
    result = 1 % m
    base %= m
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % m
        power //= 2
        base = (base * base) % m
    return result
```
<b>

```
base - podstawa
power - wykładnik (power >= 0)
m - moduł
mod - reszta z dzielenia
div - dzielenie całkowite

def fast_power_mod(base, power, m):
	result <- 1
	base <- base mod m
	Dopóki power > 0
		Jeżeli power mod 2 == 1
			result <- (result * base) mod m
		power <- power div 2
		base <- (base * base) mod m
	Zwróć result mod m
```
</b>

### Szybkie potęgowanie a^n - wersja rekurencyjna (bez modulo, działa dla dowolnie dużych wyników).
```python
#Recursive version

def fast_pow(a, n):  # a^n, n >= 0 (przyjmujemy 0^0 = 1, tak jak pow w Pythonie)
    if n == 0:
        return 1
    # jeżeli wykładnik jest nieparzysty, to zmniejsz o jeden, by stał się parzysty,
    # a następnie oblicz potęgę a do parzystego wykładnika i pomnóż to przez a,
    # aby dostać a * a^parzysty_wykładnik.
    # na przykład: a^5 = a^4 * a
    if n % 2 == 1:
        return fast_pow(a, n - 1) * a
    # dla parzystego wykładnika szukamy potęgę z wykładnikiem o połowę mniejszym.
    # robiąc to, można dojść do a^2, co potem się składa na a^4 itd...
    # np. a^4 = a^2 * a^2.
    # kiedy n == 2, to funkcja szuka a^1, bo 2 div 2 == 1.
    # kiedy n == 1, to funkcja szuka a^0 * a, bo 1 jest liczbą nieparzystą, więc trafia do drugiego warunku.
    p = fast_pow(a, n // 2)
    return p * p
```
<b>

```
a - podstawa
n - wykładnik (n >= 0)
mod - reszta z dzielenia
div - dzielenie całkowite

def fast_pow(a, n):
	Jeżeli n == 0
		Zwróć 1
	Jeżeli n mod 2 == 1
		Zwróć fast_pow(a, n - 1) * a
	p <- fast_pow(a, n div 2)
	Zwróć p * p
```
</b>
</details>

<a name="bisekcja"></a>
## Wyznaczanie miejsc zerowych funkcji metodą połowienia - bisekcja [⬆️](#)
<details><summary>Rozwiń</summary>

Funkcja f musi być ciągła w przedziale [a, b] i przyjmować na jego końcach wartości o przeciwnych znakach (f(a) * f(b) < 0). Wtedy w przedziale jest miejsce zerowe, a my w każdym kroku zostawiamy tę połowę przedziału, na której końcach znaki wciąż są przeciwne.

```python
def f(x):
    return -4 * x + 2


# bisection(od,do)
def bisection(a, b, precyzja=0.0001):
    if f(a) * f(b) >= 0:  # brak gwarancji miejsca zerowego w [a, b]
        return None
    c = a
    while b - a >= precyzja:
        c = (a + b) / 2
        if f(c) == 0.0:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c
```
<b>

```
f(x) - badana funkcja, ciągła w przedziale [a, b]
precyzja - dokładność wyniku

def f(x):
	Zwróć -4 * x + 2

def bisection(a, b, precyzja):
	Jeżeli f(a) * f(b) >= 0
		Zwróć "brak gwarancji miejsca zerowego"
	c <- a
	Dopóki b - a >= precyzja
		c <- (a + b) / 2
		Jeżeli f(c) == 0
			Zwróć c
		Jeżeli f(c) * f(a) < 0
			b <- c
		W innym wypadku
			a <- c
	Zwróć c
```
</b>
</details>

<a name="heron"></a>
## Obliczanie pierwiastka kwadratowego metodą Herona (Newtona) [⬆️](#)
<details><summary>Rozwiń</summary>

Szukamy kwadratu o polu x. Zaczynamy od prostokąta o bokach a = x i b = 1 (pole x). W każdym kroku nowy bok a to średnia arytmetyczna boków, a drugi bok b = x / a (pole się nie zmienia). Prostokąt coraz bardziej przypomina kwadrat, a jego bok zbliża się do pierwiastka z x.

```python
def heron(x, precyzja=0.000001):  # pierwiastek kwadratowy z x >= 0
    if x == 0:
        return 0
    a = x
    b = 1
    while abs(a - b) > precyzja:
        a = (a + b) / 2
        b = x / a
    return a


print(heron(2))  # 1.41421356...
```
<b>

```
x - liczba, z której liczymy pierwiastek (x > 0)
precyzja - dokładność wyniku
|a - b| - wartość bezwzględna różnicy

def heron(x, precyzja):
	a <- x
	b <- 1
	Dopóki |a - b| > precyzja
		a <- (a + b) / 2
		b <- x / a
	Zwróć a
```
</b>
</details>

<a name="horner"></a>
## Obliczanie wartości wielomianu za pomocą schematu Hornera [⬆️](#)
<details><summary>Rozwiń</summary>

Wielomian w(x) = a_n * x^n + ... + a_1 * x + a_0 zapisujemy jako w(x) = (...((a_n * x + a_(n-1)) * x + a_(n-2)) * x + ...) * x + a_0. Wystarczy wtedy n mnożeń i n dodawań (bez liczenia potęg). Współczynniki podajemy od najwyższej potęgi, np. 2x^3 - 6x^2 + 2x - 1 -> [2, -6, 2, -1].

```python
#Iterated version

def horner(wsp, x):  # wsp = [a_n, a_(n-1), ..., a_1, a_0]
    wynik = 0
    for i in range(len(wsp)):
        wynik = wynik * x + wsp[i]
    return wynik


print(horner([2, -6, 2, -1], 3))  # 2*27 - 6*9 + 2*3 - 1 = 5
```
<b>

```
wsp[0..n] - współczynniki wielomianu, od najwyższej potęgi
x - argument

def horner(wsp, x):
	wynik <- 0
	Dla i = 0, 1, ... n
		wynik <- wynik * x + wsp[i]
	Zwróć wynik
```
</b>

```python
#Recursive version - wywołanie: horner_rek(wsp, x, len(wsp) - 1)

def horner_rek(wsp, x, n):  # wartość wielomianu zbudowanego ze współczynników wsp[0..n]
    if n == 0:
        return wsp[0]
    return horner_rek(wsp, x, n - 1) * x + wsp[n]
```
<b>

```
wsp[0..n] - współczynniki wielomianu, od najwyższej potęgi
x - argument

def horner_rek(wsp, x, n):
	Jeżeli n == 0
		Zwróć wsp[0]
	W innym wypadku
		Zwróć horner_rek(wsp, x, n - 1) * x + wsp[n]
```
</b>

### Zastosowanie: zamiana liczby z systemu o podstawie b na dziesiętny
Cyfry liczby to współczynniki wielomianu, a podstawa b to argument, np. 1011 (2) = 1 * 2^3 + 0 * 2^2 + 1 * 2 + 1 = ((1 * 2 + 0) * 2 + 1) * 2 + 1 = 11.

```python
def na_dziesietny(liczba, b):  # liczba jako napis, np. na_dziesietny("1F", 16) == 31
    wynik = 0
    for znak in liczba:
        if "0" <= znak <= "9":
            cyfra = ord(znak) - ord("0")
        else:
            cyfra = ord(znak.upper()) - ord("A") + 10  # A = 10, B = 11, ...
        wynik = wynik * b + cyfra
    return wynik
```
<b>

```
liczba[1..n] - napis z cyframi liczby w systemie o podstawie b
wartosc(c) - wartość cyfry c (0..9, A = 10, B = 11, ...)

def na_dziesietny(liczba, b):
	wynik <- 0
	Dla i = 1, 2, ... n
		wynik <- wynik * b + wartosc(liczba[i])
	Zwróć wynik
```
</b>
</details>

<a name="pole"></a>
## Obliczanie pola obszarów zamkniętych [⬆️](#)
<details><summary>Rozwiń</summary>

Liczymy przybliżone pole obszaru ograniczonego wykresem funkcji f (f(x) >= 0), osią OX i prostymi x = a, x = b. Przedział [a, b] dzielimy na n części o szerokości h = (b - a) / n i sumujemy pola prostokątów (wysokość f w lewym końcu części) albo trapezów (podstawy f w obu końcach części). Przykład: f(x) = x^2 na [0, 1], dokładne pole to 1/3.

```python
def f(x):
    return x * x


def prostokaty(a, b, n):  # n - liczba prostokątów
    h = (b - a) / n
    pole = 0
    for i in range(n):
        pole += f(a + i * h) * h
    return pole


def trapezy(a, b, n):  # n - liczba trapezów
    h = (b - a) / n
    pole = 0
    for i in range(n):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        pole += (f(x1) + f(x2)) / 2 * h
    return pole


print(prostokaty(0, 1, 1000))  # ok. 0.33283
print(trapezy(0, 1, 1000))     # ok. 0.3333335
```
<b>

```
f(x) - funkcja nieujemna w przedziale [a, b]
n - liczba części, na które dzielimy przedział

def prostokaty(a, b, n):
	h <- (b - a) / n
	pole <- 0
	Dla i = 0, 1, ... n - 1
		pole <- pole + f(a + i * h) * h
	Zwróć pole

def trapezy(a, b, n):
	h <- (b - a) / n
	pole <- 0
	Dla i = 0, 1, ... n - 1
		x1 <- a + i * h
		x2 <- a + (i + 1) * h
		pole <- pole + (f(x1) + f(x2)) / 2 * h
	Zwróć pole
```
</b>
</details>

<a name="palindrom"></a>
## Sprawdzanie, czy dany ciąg znaków tworzy palindrom [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#With list and slices

def is_palindrom(string):
    lista = list(string)
    if lista == lista[::-1]:
        return True
    return False
```

```python
#With 2 strings

def is_palindrom(string):
    wynik = ""
    for i in string[::-1]:
        wynik += i
    if wynik == string:
        return True
    return False
```

```python
# Recursive version

def isPalindrom(string):
    if len(string) <= 1:  # pusty napis i napis jednoznakowy są palindromami
        return True
    if len(string) == 2:
        if string[0] == string[1]:
            return True
        return False
    return isPalindrom(string[1:-1]) if string[0] == string[-1] else False

# This code is contributed by Pixel
```
<b>

```
n - długość napisu
string[2..n-1] - napis bez pierwszego i ostatniego znaku

def isPalindrom(string):
	Jeżeli n <= 1
		Zwróć Prawdę
	Jeżeli string[1] != string[n]
		Zwróć Fałsz
	W innym wypadku
		Zwróć isPalindrom(string[2..n-1])
```
</b>

```python
#Iterated version (dwa wskaźniki: od początku i od końca)

def is_palindrom(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True
```
<b>

```
n - długość napisu
string[1..n] - sprawdzany napis

def is_palindrom(string):
	i <- 1
	j <- n
	Dopóki i < j
		Jeżeli string[i] != string[j]
			Zwróć Fałsz
		i <- i + 1
		j <- j - 1
	Zwróć Prawdę
```
</b>
</details>

<a name="anagram"></a>
## Sprawdzanie, czy dany ciąg znaków tworzy anagram [⬆️](#)
<details><summary>Rozwiń</summary>

Dwa napisy są anagramami, jeżeli składają się z tych samych znaków, występujących tyle samo razy (np. "kebab" i "babek").

```python
#With sorting

def is_anagram(string,string2):
    if sorted(string) == sorted(string2):
        return True
    return False
```

```python
#With own sorting

def sort_1(string):
    string = list(string)
    for i in range(len(string)):
        for j in range(len(string) - i - 1):
            if string[j] > string[j + 1]:
                string[j], string[j + 1] = string[j + 1], string[j]
    return "".join(string)


def is_anagram(string, pattern):
    if len(string) != len(pattern):
        return False

    string = sort_1(string)
    pattern = sort_1(pattern)
    for i in range(len(string)):
        if string[i] != pattern[i]:
            return False
    return True
```
<b>

```
n - długość napisów
dł() - długość napisu
sort_1() - sortuje znaki napisu (np. bąbelkowo)

def is_anagram(string, pattern):
	Jeżeli dł(string) != dł(pattern)
		Zwróć Fałsz
	string <- sort_1(string)
	pattern <- sort_1(pattern)
	Dla i = 1, 2, ... n
		Jeżeli string[i] != pattern[i]
			Zwróć Fałsz
	Zwróć Prawdę
```
</b>

```python
#Counting version (zliczanie wystąpień znaków w słowniku)

def is_anagram(string, pattern):
    if len(string) != len(pattern):
        return False

    licznik = {}
    for znak in string:
        licznik[znak] = licznik.get(znak, 0) + 1

    for znak in pattern:
        if licznik.get(znak, 0) == 0:  # znaku brak albo występuje za dużo razy
            return False
        licznik[znak] -= 1
    return True
```
<b>

```
n - długość napisów
dł() - długość napisu
licznik[z] - ile razy znak z wystąpił (na początku 0 dla każdego znaku)

def is_anagram(string, pattern):
	Jeżeli dł(string) != dł(pattern)
		Zwróć Fałsz
	Dla i = 1, 2, ... n
		licznik[string[i]] <- licznik[string[i]] + 1
	Dla i = 1, 2, ... n
		Jeżeli licznik[pattern[i]] == 0
			Zwróć Fałsz
		licznik[pattern[i]] <- licznik[pattern[i]] - 1
	Zwróć Prawdę
```
</b>
</details>

<a name="alfa"></a>
## Porządkowanie alfabetyczne [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#Sortowanie liter bąbelkowo

slowo = "niezdammatury"


def bubble_sort(tab):
    tab = list(tab)
    for i in range(len(tab)):
        for j in range(len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]
    return "".join(tab)


print(bubble_sort(slowo))
```
<b>

```
tab[1..n] - litery napisu
litery porównujemy według ich kodów (kolejność w alfabecie)

Dla i = 1, 2, ... n
	Dla j = 1, 2, ... n – i
		Jeżeli tab[j] > tab[j + 1]
			Zamień tab[j] z tab[j + 1]
```
</b>

```python
#Porządek leksykograficzny słów (porównywanie napisów znak po znaku)

def mniejsze(s1, s2):  # czy s1 jest w słowniku przed s2
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] != s2[i]:
            return s1[i] < s2[i]  # decyduje pierwszy różniący się znak
        i += 1
    return len(s1) < len(s2)  # jedno słowo jest początkiem drugiego, np. "kot" < "kotek"


def sortuj_slowa(slowa):  # sortowanie bąbelkowe listy słów
    slowa = slowa[:]
    for i in range(len(slowa)):
        for j in range(len(slowa) - i - 1):
            if mniejsze(slowa[j + 1], slowa[j]):
                slowa[j], slowa[j + 1] = slowa[j + 1], slowa[j]
    return slowa


print(sortuj_slowa(["kotek", "ala", "kot", "ma"]))  # ['ala', 'kot', 'kotek', 'ma']
```
<b>

```
dł() - długość napisu

def mniejsze(s1, s2):
	i <- 1
	Dopóki i <= dł(s1) oraz i <= dł(s2)
		Jeżeli s1[i] != s2[i]
			Zwróć s1[i] < s2[i]
		i <- i + 1
	Zwróć dł(s1) < dł(s2)
```
</b>
</details>

<a name="pattern"></a>
## Wyszukiwanie wzorca w tekście [⬆️](#)
<details><summary>Rozwiń</summary>

Algorytm naiwny: przykładamy wzorzec do każdej pozycji tekstu, od której jeszcze się mieści (i = 0 .. len(tekst) - len(pattern)), i porównujemy znak po znaku.

```py
def find_pattern(tekst, pattern):  # indeks pierwszego wystąpienia wzorca albo -1
    for i in range(len(tekst) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and tekst[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i
    return -1


def is_pattern(tekst, pattern):
    return find_pattern(tekst, pattern) != -1


def find_all(tekst, pattern):  # lista wszystkich pozycji wystąpień (także nachodzących na siebie)
    pozycje = []
    for i in range(len(tekst) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and tekst[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            pozycje.append(i)
    return pozycje


print(find_pattern("abrakadabra", "abra"))  # 0
print(find_all("abrakadabra", "abra"))      # [0, 7]
```

<b>

```
tekst[1..n] - przeszukiwany tekst
pattern[1..m] - szukany wzorzec

def find_pattern(tekst, pattern):
	Dla i = 1, 2, ... n - m + 1
		j <- 1
		Dopóki j <= m oraz tekst[i + j - 1] == pattern[j]
			j <- j + 1
		Jeżeli j == m + 1
			Zwróć i
	Zwróć -1
```
</b>

</details>

<a name="onp"></a>
## Obliczanie wartości wyrażenia w odwrotnej notacji polskiej (ONP) [⬆️](#)
<details><summary>Rozwiń</summary>

W ONP operator stoi za argumentami, np. (3 + 4) * 2 zapisujemy jako 3 4 + 2 *. Nawiasy nie są potrzebne. Wyrażenie czytamy od lewej: liczbę wkładamy na stos, a operator zdejmuje ze stosu dwie liczby, wykonuje działanie i wkłada wynik na stos. Na końcu na stosie zostaje wynik.

```python
def onp(wyrazenie):  # elementy oddzielone spacjami, np. "3 4 + 2 *"
    stos = []
    for element in wyrazenie.split():
        if element in ["+", "-", "*", "/"]:
            b = stos.pop()  # najpierw zdejmujemy PRAWY argument
            a = stos.pop()
            if element == "+":
                stos.append(a + b)
            elif element == "-":
                stos.append(a - b)
            elif element == "*":
                stos.append(a * b)
            else:
                stos.append(a / b)
        else:
            stos.append(float(element))
    return stos.pop()


print(onp("3 4 + 2 *"))          # 14.0
print(onp("5 1 2 + 4 * + 3 -"))  # 14.0
```
<b>

```
wyrazenie[1..n] - kolejne elementy wyrażenia (liczby i operatory)
stos - na początku pusty

def onp(wyrazenie):
	Dla i = 1, 2, ... n
		Jeżeli wyrazenie[i] jest operatorem
			b <- zdejmij ze stosu
			a <- zdejmij ze stosu
			Połóż na stos wynik działania a wyrazenie[i] b
		W innym wypadku
			Połóż na stos liczbę wyrazenie[i]
	Zwróć zdejmij ze stosu
```
</b>
</details>

<a name="len"></a>
## Kompresja danych [⬆️](#)

### Kod prefiksowy (prefix free)
<details><summary>Rozwiń</summary>

Kody znaków o zmiennej długości są w wymaganiach (przykłady: kod prefiksowy poniżej, kod Huffmana, alfabet Morse’a). Częste znaki dostają krótkie kody, a rzadkie - dłuższe.

Kod jest nazywany "prefix (free) code", jeżeli w systemie nie ma kodu słowa, który byłby prefixem (początkiem) innego kodu słowa. Dzięki temu ciąg bitów da się odkodować jednoznacznie, bez żadnych separatorów.

Załóżmy, że mamy plik z 100,000 znakami, jedyne znaki jakie występują w pliku to: a,b,c,d,e,f i chcemy zmniejszyć rozmiar tego pliku kompresją, gdzie każdy kod znaku ma różną długość.

|                         |   a   |   b   |   c   |   d   |   e   |   f   |
| ----------------------: | :---: | :---: | :---: | :---: | :---: | :---: |
|  Częstość (w tysiącach) |  45   |  13   |  12   |  16   |   9   |   5   |
|    Kod o stałej długości |  000  |  001  |  010  |  011  |  100  |  101  |
| Kod o zmiennej długości |   0   |  101  |  100  |  111  | 1101  | 1100  |

Przy kodzie o stałej długości plik zajmie 100,000 * 3 = 300,000 bitów, a przy kodzie o zmiennej długości (45 * 1 + 13 * 3 + 12 * 3 + 16 * 3 + 9 * 4 + 5 * 4) * 1000 = 224,000 bitów.

```python
#Iterated version

# kod prefiksowy: żaden kod nie jest początkiem innego
cipher = {'00': ' ', '010': 'a', '011': 'm', '100': 'n', '101': 'i', '110': 'e', '1110': 'z', '1111': 'd'}

text = "1001011100011101111010011"


def decrypt(cipher, text):  # zwraca None, jeżeli text jest niepoprawny
    res = ""
    bufor = ""
    for bit in text:
        bufor += bit
        if bufor in cipher:  # bufor jest pełnym kodem znaku
            res += cipher[bufor]
            bufor = ""
    if bufor != "":  # zostały bity, które nie tworzą żadnego kodu
        return None
    return res


to_code = "zdam"


def encrypt(cipher, text):  # zwraca None, jeżeli w text jest znak spoza słownika
    res = ""
    for char in text:
        if char in cipher.values():
            for k, v in cipher.items():
                if v == char:
                    res += k
        else:
            return None
    return res


print(decrypt(cipher, text))     # nie zdam
print(encrypt(cipher, to_code))  # 11101111010011
```
<b>

```
cipher - słownik: kod -> znak (kod prefiksowy)
text[1..n] - ciąg bitów

def decrypt(cipher, text):
	res <- ""
	bufor <- ""
	Dla i = 1, 2, ... n
		bufor <- bufor + text[i]
		Jeżeli bufor jest kluczem w cipher
			res <- res + cipher[bufor]
			bufor <- ""
	Jeżeli bufor != ""
		Zwróć "błędny ciąg bitów"
	Zwróć res

def encrypt(cipher, text):
	res <- ""
	Dla i = 1, 2, ... dł(text)
		Znajdź kod k, dla którego cipher[k] == text[i]
		res <- res + k
	Zwróć res
```
</b>
</details>

<a name="huffman"></a>
## Kod Huffmana [⬆️](#)
<details><summary>Rozwiń</summary>

Kod Huffmana to optymalny kod prefiksowy: daje najkrótszy zakodowany tekst spośród kodów, w których każdy znak ma stały ciąg bitów. Budowa drzewa: każdy znak to liść o wadze równej liczbie jego wystąpień. Dopóki mamy więcej niż jedno drzewo, łączymy dwa drzewa o najmniejszych wagach w jedno (waga = suma wag). Kod znaku to ścieżka od korzenia do liścia: krok w lewo = 0, w prawo = 1. Do wybierania najlżejszych drzew używamy kolejki priorytetowej (moduł heapq).

```python
import heapq


def huffman(tekst):  # zwraca słownik: znak -> kod
    if tekst == "":
        return {}
    czestosc = {}
    for znak in tekst:
        czestosc[znak] = czestosc.get(znak, 0) + 1

    # element kolejki: (waga, numer, drzewo); numer rozstrzyga remisy wag
    # drzewo to znak (liść) albo para (lewe poddrzewo, prawe poddrzewo)
    kolejka = []
    numer = 0
    for znak in czestosc:
        heapq.heappush(kolejka, (czestosc[znak], numer, znak))
        numer += 1

    if len(kolejka) == 1:  # tylko jeden rodzaj znaku
        return {kolejka[0][2]: "0"}

    while len(kolejka) > 1:
        waga1, _, lewe = heapq.heappop(kolejka)   # dwa najlżejsze drzewa
        waga2, _, prawe = heapq.heappop(kolejka)
        heapq.heappush(kolejka, (waga1 + waga2, numer, (lewe, prawe)))
        numer += 1

    kody = {}
    przypisz_kody(kolejka[0][2], "", kody)
    return kody


def przypisz_kody(wezel, kod, kody):
    if isinstance(wezel, str):  # liść - znak
        kody[wezel] = kod
    else:
        przypisz_kody(wezel[0], kod + "0", kody)
        przypisz_kody(wezel[1], kod + "1", kody)


def koduj(tekst, kody):
    wynik = ""
    for znak in tekst:
        wynik += kody[znak]
    return wynik


def dekoduj(bity, kody):
    odwrotne = {}
    for znak in kody:
        odwrotne[kody[znak]] = znak
    wynik = ""
    bufor = ""
    for bit in bity:
        bufor += bit
        if bufor in odwrotne:
            wynik += odwrotne[bufor]
            bufor = ""
    return wynik


tekst = "abrakadabra"
kody = huffman(tekst)
zakodowany = koduj(tekst, kody)
print(kody)
print(zakodowany, len(zakodowany), "bitów zamiast", 8 * len(tekst))
print(dekoduj(zakodowany, kody))
```
<b>

```
Q - kolejka priorytetowa drzew (na początku drzewo o najmniejszej wadze)
czestosc[z] - liczba wystąpień znaku z w tekście

def huffman(tekst):
	Dla każdego znaku z w tekście
		czestosc[z] <- czestosc[z] + 1
	Dla każdego różnego znaku z
		Wstaw do Q liść z o wadze czestosc[z]
	Dopóki w Q jest więcej niż jedno drzewo
		x <- usuń z Q drzewo o najmniejszej wadze
		y <- usuń z Q drzewo o najmniejszej wadze
		Wstaw do Q nowy węzeł o dzieciach x, y i wadze waga(x) + waga(y)
	korzen <- jedyne drzewo w Q
	przypisz_kody(korzen, "")

def przypisz_kody(wezel, kod):
	Jeżeli wezel jest liściem ze znakiem z
		kody[z] <- kod
	W innym wypadku
		przypisz_kody(lewe dziecko wezel, kod + "0")
		przypisz_kody(prawe dziecko wezel, kod + "1")
```
</b>
</details>

<a name="morse"></a>
## Alfabet Morse’a [⬆️](#)
<details><summary>Rozwiń</summary>

W zakodowanym tekście litery oddzielamy jedną spacją, a wyrazy znakiem " / ".

<details><summary>Python</summary>

```python
# słownik kodujący: znak -> kod Morse'a
morseEncode = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}
# słownik dekodujący: kod Morse'a -> znak (odwrócony słownik kodujący)
morseDecode = {val: key for key, val in morseEncode.items()}

SEP = ' / '  # separator wyrazów


def morseCode(string, decode=False):
    if not decode:  # kodowanie
        wyrazy = []
        for wyraz in string.lower().split():
            litery = []
            for char in wyraz:
                litery.append(morseEncode.get(char, '*'))  # '*' dla nieznanych znaków
            wyrazy.append(' '.join(litery))
        return SEP.join(wyrazy)
    else:  # dekodowanie
        wyrazy = []
        for wyraz in string.split(SEP):
            litery = ''
            for kod in wyraz.split():
                litery += morseDecode.get(kod, '*')  # '*' dla nieznanych kodów
            wyrazy.append(litery)
        return ' '.join(wyrazy)


# test
string = "Keep learning"
coded = morseCode(string)
print("Coded:", coded)
decoded = morseCode(coded, decode=True)
print("Decoded:", decoded)
```
</details>
<details><summary>C++</summary>

```cpp
#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

// litery oddzielamy jedną spacją, a wyrazy znakiem "/" (otoczonym spacjami)
map<char, string> kodTab{
    {'a', ".-"}, {'b', "-..."}, {'c', "-.-."}, {'d', "-.."},
    {'e', "."}, {'f', "..-."}, {'g', "--."}, {'h', "...."},
    {'i', ".."}, {'j', ".---"}, {'k', "-.-"}, {'l', ".-.."},
    {'m', "--"}, {'n', "-."}, {'o', "---"}, {'p', ".--."},
    {'q', "--.-"}, {'r', ".-."}, {'s', "..."}, {'t', "-"},
    {'u', "..-"}, {'v', "...-"}, {'w', ".--"}, {'x', "-..-"},
    {'y', "-.--"}, {'z', "--.."}, {'1', ".----"}, {'2', "..---"},
    {'3', "...--"}, {'4', "....-"}, {'5', "....."}, {'6', "-...."},
    {'7', "--..."}, {'8', "---.."}, {'9', "----."}, {'0', "-----"}
};

string koduj(const string& tekst) {
    stringstream ss(tekst);
    string wyraz, wynik = "";
    while (ss >> wyraz) {                // kolejne wyrazy (bez spacji)
        if (wynik != "") wynik += " / ";
        for (int i = 0; i < (int)wyraz.length(); i++) {
            char c = (char)tolower((unsigned char)wyraz[i]);
            if (i > 0) wynik += " ";
            if (kodTab.count(c)) wynik += kodTab[c];
            else wynik += "*";           // nieznany znak
        }
    }
    return wynik;
}

string dekoduj(const string& kod) {
    map<string, char> dekTab;            // odwrócona tablica: kod -> znak
    for (const auto& para : kodTab) dekTab[para.second] = para.first;

    stringstream ss(kod);
    string token, wynik = "";
    while (ss >> token) {                // kolejne kody liter albo "/"
        if (token == "/") wynik += ' ';
        else if (dekTab.count(token)) wynik += dekTab[token];
        else wynik += '*';               // nieznany kod
    }
    return wynik;
}

int main() {
    string zakodowane = koduj("Keep learning");
    cout << "encoded: " << zakodowane << endl;
    cout << "decoded: " << dekoduj(zakodowane) << endl;
    return 0;
}
```
</details>
</details>

<a name="przes"></a>
## Transpozycyjny [⬆️](#)
<details><summary>Rozwiń</summary>

Szyfry przestawieniowe dokonują przestawienia znaków w tekście. Tekst zaszyfrowany jest permutacją tekstu jawnego, tzn. zawiera wszystkie znaki tekstu jawnego, jednak ustawione w innej kolejności. Operacja taka nosi nazwę transpozycji.

### Zamiana sąsiednich znaków
Zamieniamy miejscami znaki na pozycjach i oraz i + 1 dla i = 0, jump, 2 * jump, ... Dla jump >= 2 pary się nie nakładają, więc ta sama funkcja (z tym samym jump) służy do szyfrowania i odszyfrowania.

```python
tekst = "aMtruaz  nifromtayik ot inct rdungeo"  # jump = 3 to decrypt


def przes(tekst, jump):  # jump >= 2
    tekst = list(tekst)
    for i in range(0, len(tekst) - 1, jump):
        tekst[i], tekst[i + 1] = tekst[i + 1], tekst[i]
    return "".join(tekst)


print(przes(tekst, 3))  # Matura z informatyki to nic trudnego
```
<b>

```
tekst[0..n-1] - szyfrowany tekst
jump - odstęp między początkami zamienianych par (jump >= 2)

def przes(tekst, jump):
	i <- 0
	Dopóki i < n - 1
		t <- tekst[i]
		tekst[i] <- tekst[i + 1]
		tekst[i + 1] <- t
		i <- i + jump
	Zwróć tekst
```
</b>

### Szyfr kolumnowy
Tekst wpisujemy wierszami do tabeli o k kolumnach, a odczytujemy kolumnami, np. dla k = 3 "ALA MA KOTA" -> "A  TLMKAAAO".

```python
def szyfruj_kolumnowo(tekst, k):  # k - liczba kolumn
    wynik = ""
    for kolumna in range(k):
        for i in range(kolumna, len(tekst), k):  # znaki z jednej kolumny
            wynik += tekst[i]
    return wynik


def deszyfruj_kolumnowo(szyfr, k):
    tekst = [""] * len(szyfr)
    pozycja = 0
    for kolumna in range(k):  # wpisujemy znaki z powrotem w tej samej kolejności
        for i in range(kolumna, len(szyfr), k):
            tekst[i] = szyfr[pozycja]
            pozycja += 1
    return "".join(tekst)


print(szyfruj_kolumnowo("ALA MA KOTA", 3))    # A  TLMKAAAO
print(deszyfruj_kolumnowo("A  TLMKAAAO", 3))  # ALA MA KOTA
```
<b>

```
tekst[0..n-1] - szyfrowany tekst
k - liczba kolumn

def szyfruj_kolumnowo(tekst, k):
	wynik <- ""
	Dla kolumna = 0, 1, ... k - 1
		i <- kolumna
		Dopóki i < n
			wynik <- wynik + tekst[i]
			i <- i + k
	Zwróć wynik

def deszyfruj_kolumnowo(szyfr, k):
	pozycja <- 0
	Dla kolumna = 0, 1, ... k - 1
		i <- kolumna
		Dopóki i < n
			tekst[i] <- szyfr[pozycja]
			pozycja <- pozycja + 1
			i <- i + k
	Zwróć tekst
```
</b>
</details>

<a name="atbash"></a>
## Szyfr AtBash [⬆️](#)
<details><summary>Rozwiń</summary>

Jest to monoalfabetyczny szyfr podstawieniowy, ograniczony. Zasada jego działania polega na podstawieniu zamiast danej litery, litery leżącej po drugiej stronie alfabetu w takiej samej odległości. Np. zamiast litery A powinniśmy podstawić literę Z, za literę C wstawiamy literę X. Ta sama funkcja szyfruje i odszyfrowuje.

```python
txt = "Nie zdam maturki elo"


def atbash(txt):
    txt = list(txt)
    for i in range(len(txt)):
        if "A" <= txt[i] <= "Z":  # wielkie litery
            txt[i] = chr(ord("Z") - (ord(txt[i]) - ord("A")))
        elif "a" <= txt[i] <= "z":  # małe litery
            txt[i] = chr(ord("z") - (ord(txt[i]) - ord("a")))
        # pozostałe znaki (spacje, cyfry, polskie litery) zostają bez zmian

    return "".join(txt)


print(atbash(txt))  # Mrv awzn nzgfipr vol
```
<b>

```
txt[1..n] - szyfrowany tekst
ord() - kod znaku
chr() - znak o podanym kodzie

def atbash(txt):
	Dla i = 1, 2, ... n
		Jeżeli "A" <= txt[i] <= "Z"
			txt[i] <- chr(ord("Z") - (ord(txt[i]) - ord("A")))
		W innym wypadku Jeżeli "a" <= txt[i] <= "z"
			txt[i] <- chr(ord("z") - (ord(txt[i]) - ord("a")))
	Zwróć txt
```
</b>
</details>

<a name="cezar"></a>
## Szyfr Cezara [⬆️](#)
<details><summary>Rozwiń</summary>

<details><summary>Python</summary>

Jest to rodzaj szyfru podstawieniowego, w którym każda litera tekstu jawnego (niezaszyfrowanego) zastępowana jest inną, oddaloną od niej o stałą liczbę pozycji w alfabecie. <br>

Jeżeli przesunięcie będzie równe 13, uzyskamy szyfr ROT13.
```python
def koduj(wiadomosc, klucz):
    wynik = ""
    wiadomosc = wiadomosc.upper().strip().replace(" ", "")
    for i in wiadomosc:
        if "A" <= i <= "Z":
            wynik += chr((ord(i) + klucz - 65) % 26 + 65)  # 65 = ord("A")
        else:
            wynik += i  # znaki inne niż litery A-Z zostają bez zmian
    return wynik


def dekoduj(wiadomosc, klucz):
    klucz *= -1
    return koduj(wiadomosc, klucz)


print(koduj("Ala ma kota", 3))  # DODPDNRWD
print(dekoduj("DODPDNRWD", 3))   # ALAMAKOTA
```
<b>

```
wiadomosc[1..n] - ciąg wielkich liter alfabetu angielskiego, bez spacji i znaków specjalnych
ord() - pokazuje kod znaku w unicode
chr() - pokazuje znak kodu unicode
mod - reszta z dzielenia (zawsze nieujemna)
n - długość ciągu znaków
klucz - liczba całkowita (przy deszyfrowaniu używamy -klucz)

koduj(wiadomosc, klucz):
	wynik <- ""
	Dla i = 1, 2, 3 ... n
		wynik <- wynik + chr((ord(wiadomosc[i]) + klucz - 65) mod 26 + 65)
	Zwróć wynik
```
</b>
</details>
<details><summary>C++</summary>

```cpp
#include <iostream>
#include <string>

using namespace std;

// klucz może być ujemny (deszyfrowanie), znaki inne niż litery zostają bez zmian
string cezar(string wiadomosc, int klucz) {
    string wynik = "";

    for (char i : wiadomosc) {
        if (i >= 'A' && i <= 'Z') wynik += (char)(((i - 'A' + klucz) % 26 + 26) % 26 + 'A');
        else if (i >= 'a' && i <= 'z') wynik += (char)(((i - 'a' + klucz) % 26 + 26) % 26 + 'a');
        else wynik += i;
    }

    return wynik;
}

int main() {
    string szyfr = cezar("Ala ma kota", 3);
    cout << szyfr << endl;              // Dod pd nrwd
    cout << cezar(szyfr, -3) << endl;   // Ala ma kota
    return 0;
}
```
</details>
</details>

<a name="vigenere"></a>
## Szyfr Vigenère’a [⬆️](#)
<details><summary>Rozwiń</summary>

Szyfr podstawieniowy wieloalfabetowy - to szyfr Cezara, w którym przesunięcie zmienia się co literę. Kolejne litery klucza (powtarzanego w kółko) mówią, o ile przesunąć kolejne litery tekstu: A = 0, B = 1, ..., Z = 25. Przy odszyfrowaniu przesuwamy w drugą stronę.

```python
def vigenere(tekst, klucz, deszyfruj=False):  # tekst i klucz: wielkie litery A-Z
    wynik = ""
    j = 0  # pozycja w kluczu
    for znak in tekst:
        if "A" <= znak <= "Z":
            przesuniecie = ord(klucz[j % len(klucz)]) - ord("A")
            if deszyfruj:
                przesuniecie = -przesuniecie
            wynik += chr((ord(znak) - ord("A") + przesuniecie) % 26 + ord("A"))
            j += 1
        else:
            wynik += znak  # inne znaki bez zmian (nie zużywają litery klucza)
    return wynik


szyfr = vigenere("ATTACKATDAWN", "LEMON")
print(szyfr)                                    # LXFOPVEFRNHR
print(vigenere(szyfr, "LEMON", deszyfruj=True))  # ATTACKATDAWN
```
<b>

```
tekst[1..n] - wielkie litery A-Z
klucz[1..k] - wielkie litery A-Z
ord() - kod znaku
chr() - znak o podanym kodzie
mod - reszta z dzielenia (zawsze nieujemna)

def vigenere(tekst, klucz, deszyfruj):
	wynik <- ""
	Dla i = 1, 2, ... n
		przesuniecie <- ord(klucz[(i - 1) mod k + 1]) - ord("A")
		Jeżeli deszyfruj
			przesuniecie <- -przesuniecie
		wynik <- wynik + chr((ord(tekst[i]) - ord("A") + przesuniecie) mod 26 + ord("A"))
	Zwróć wynik
```
</b>
</details>

<a name="rsa"></a>
## RSA + rozszerzony algorytm Euklidesa [⬆️](#)
<details><summary>Rozwiń</summary>

### Rozszerzony algorytm Euklidesa
Oprócz d = nwd(a, b) znajduje liczby całkowite x, y, takie że a * x + b * y = d. Gdy nwd(e, m) = 1, to x mod m jest odwrotnością e modulo m, czyli (e * x) mod m = 1 - tego potrzebujemy w RSA.

```python
#Recursive version

def rozszerzony_nwd(a, b):  # zwraca (d, x, y), gdzie d = nwd(a, b) = a * x + b * y
    if b == 0:
        return a, 1, 0
    d, x1, y1 = rozszerzony_nwd(b, a % b)
    return d, y1, x1 - (a // b) * y1


def odwrotnosc_mod(e, m):  # liczba d taka, że (e * d) mod m == 1, albo None
    d, x, y = rozszerzony_nwd(e, m)
    if d != 1:
        return None  # odwrotność istnieje tylko, gdy nwd(e, m) == 1
    return x % m


print(rozszerzony_nwd(240, 46))  # (2, -9, 47), bo 240 * (-9) + 46 * 47 = 2
print(odwrotnosc_mod(17, 3120))  # 2753
```
<b>

```
a, b - liczby całkowite nieujemne
mod - reszta z dzielenia
div - dzielenie całkowite

def rozszerzony_nwd(a, b):
	Jeżeli b == 0
		Zwróć (a, 1, 0)
	(d, x1, y1) <- rozszerzony_nwd(b, a mod b)
	Zwróć (d, y1, x1 - (a div b) * y1)

def odwrotnosc_mod(e, m):
	(d, x, y) <- rozszerzony_nwd(e, m)
	Jeżeli d != 1
		Zwróć "brak odwrotności"
	Zwróć x mod m
```
</b>

### RSA
Szyfr z kluczem jawnym (asymetryczny): klucz publiczny (e, n) służy do szyfrowania, a klucz prywatny (d, n) do odszyfrowania.
1. Wybieramy dwie różne liczby pierwsze p i q, liczymy n = p * q oraz phi = (p - 1) * (q - 1).
2. Wybieramy e względnie pierwsze z phi (nwd(e, phi) = 1).
3. Liczymy d - odwrotność e modulo phi, czyli (e * d) mod phi = 1.
4. Szyfrowanie liczby m (0 <= m < n): c = m^e mod n. Odszyfrowanie: m = c^d mod n.

```python
def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def rozszerzony_nwd(a, b):  # zwraca (d, x, y), gdzie d = nwd(a, b) = a * x + b * y
    if b == 0:
        return a, 1, 0
    d, x1, y1 = rozszerzony_nwd(b, a % b)
    return d, y1, x1 - (a // b) * y1


def generuj_klucze(p, q, e=None):  # p, q - różne liczby pierwsze
    n = p * q
    phi = (p - 1) * (q - 1)
    if e is None:  # najmniejsze e >= 3 względnie pierwsze z phi
        e = 3
        while nwd(e, phi) != 1:
            e += 2
    d = rozszerzony_nwd(e, phi)[1] % phi  # albo: d = pow(e, -1, phi) (Python 3.8+)
    return (e, n), (d, n)  # (klucz publiczny, klucz prywatny)


def szyfruj(m, klucz_publiczny):  # m - liczba, 0 <= m < n
    e, n = klucz_publiczny
    return pow(m, e, n)  # szybkie potęgowanie modularne


def deszyfruj(c, klucz_prywatny):
    d, n = klucz_prywatny
    return pow(c, d, n)


publiczny, prywatny = generuj_klucze(61, 53, 17)
print(publiczny, prywatny)  # (17, 3233) (2753, 3233)
c = szyfruj(65, publiczny)
print(c, deszyfruj(c, prywatny))  # 2790 65

# szyfrowanie tekstu - każdy znak osobno jako liczba (kod znaku < n)
zaszyfrowane = [szyfruj(ord(znak), publiczny) for znak in "MATURA"]
print("".join(chr(deszyfruj(c, prywatny)) for c in zaszyfrowane))  # MATURA
```
<b>

```
p, q - różne liczby pierwsze
nwd() - największy wspólny dzielnik
odwrotnosc_mod() - odwrotność modulo (rozszerzony algorytm Euklidesa)
mod - reszta z dzielenia

def generuj_klucze(p, q):
	n <- p * q
	phi <- (p - 1) * (q - 1)
	e <- 3
	Dopóki nwd(e, phi) != 1
		e <- e + 2
	d <- odwrotnosc_mod(e, phi)
	Zwróć (e, n), (d, n)

def szyfruj(m, e, n):
	Zwróć m^e mod n          (szybkie potęgowanie modularne)

def deszyfruj(c, d, n):
	Zwróć c^d mod n
```
</b>
</details>

<a name="trojkat"></a>
## Sprawdzanie warunku trójkąta [⬆️](#)
<details><summary>Rozwiń</summary>

Z odcinków o długościach a, b, c da się zbudować trójkąt wtedy i tylko wtedy, gdy wszystkie długości są dodatnie, a suma każdych dwóch jest większa od trzeciej.

```python
def czy_trojkat(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a
```
<b>

```
a, b, c - długości odcinków

def czy_trojkat(a, b, c):
	Jeżeli a <= 0 lub b <= 0 lub c <= 0
		Zwróć Fałsz
	Jeżeli a + b > c oraz a + c > b oraz b + c > a
		Zwróć Prawdę
	W innym wypadku
		Zwróć Fałsz
```
</b>
</details>

<a name="punkt_prosta"></a>
## Badanie położenia punktów względem prostej [⬆️](#)
<details><summary>Rozwiń</summary>

Punkty zapisujemy jako pary (x, y). Położenie punktu C względem prostej przechodzącej przez A i B mówi znak wyznacznika (iloczynu wektorowego wektorów AB i AC):

det(A, B, C) = (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)

det > 0 - C leży po lewej stronie prostej (patrząc z A w stronę B), det < 0 - po prawej, det = 0 - C leży na prostej AB. Dwa punkty C i D leżą po tej samej stronie prostej AB, gdy det(A, B, C) i det(A, B, D) mają ten sam znak.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def polozenie(A, B, C):  # położenie punktu C względem prostej AB
    w = wyznacznik(A, B, C)
    if w > 0:
        return "po lewej"
    if w < 0:
        return "po prawej"
    return "na prostej"


def ta_sama_strona(A, B, C, D):  # czy C i D leżą po tej samej stronie prostej AB
    return wyznacznik(A, B, C) * wyznacznik(A, B, D) > 0


print(polozenie((0, 0), (2, 2), (0, 5)))  # po lewej
```
<b>

```
A = (xA, yA), B = (xB, yB) - punkty wyznaczające prostą
C = (xC, yC) - badany punkt

def wyznacznik(A, B, C):
	Zwróć (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)

def polozenie(A, B, C):
	w <- wyznacznik(A, B, C)
	Jeżeli w > 0
		Zwróć "po lewej"
	Jeżeli w < 0
		Zwróć "po prawej"
	Zwróć "na prostej"
```
</b>
</details>

<a name="punkt_odcinek"></a>
## Badanie przynależności punktu do odcinka [⬆️](#)
<details><summary>Rozwiń</summary>

Punkt C należy do odcinka AB, gdy leży na prostej AB (wyznacznik równy 0) i jego współrzędne mieszczą się między współrzędnymi końców odcinka.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def na_odcinku(A, B, C):  # czy punkt C należy do odcinka AB
    if wyznacznik(A, B, C) != 0:
        return False
    return (min(A[0], B[0]) <= C[0] <= max(A[0], B[0])
            and min(A[1], B[1]) <= C[1] <= max(A[1], B[1]))


print(na_odcinku((0, 0), (4, 4), (2, 2)))  # True
print(na_odcinku((0, 0), (4, 4), (5, 5)))  # False
```
<b>

```
A = (xA, yA), B = (xB, yB) - końce odcinka
C = (xC, yC) - badany punkt

def na_odcinku(A, B, C):
	Jeżeli wyznacznik(A, B, C) != 0
		Zwróć Fałsz
	Jeżeli min(xA, xB) <= xC <= max(xA, xB) oraz min(yA, yB) <= yC <= max(yA, yB)
		Zwróć Prawdę
	W innym wypadku
		Zwróć Fałsz
```
</b>
</details>

<a name="odcinki"></a>
## Przecinanie się odcinków [⬆️](#)
<details><summary>Rozwiń</summary>

Odcinki AB i CD przecinają się, gdy końce C i D leżą po przeciwnych stronach prostej AB, a jednocześnie końce A i B leżą po przeciwnych stronach prostej CD. Osobno sprawdzamy przypadki szczególne, gdy koniec jednego odcinka leży na drugim odcinku.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def na_odcinku(A, B, C):  # czy punkt C należy do odcinka AB
    if wyznacznik(A, B, C) != 0:
        return False
    return (min(A[0], B[0]) <= C[0] <= max(A[0], B[0])
            and min(A[1], B[1]) <= C[1] <= max(A[1], B[1]))


def przecinaja_sie(A, B, C, D):  # czy odcinki AB i CD mają punkt wspólny
    w1 = wyznacznik(A, B, C)
    w2 = wyznacznik(A, B, D)
    w3 = wyznacznik(C, D, A)
    w4 = wyznacznik(C, D, B)
    if w1 * w2 < 0 and w3 * w4 < 0:  # przypadek ogólny
        return True
    # przypadki szczególne: koniec jednego odcinka leży na drugim
    if na_odcinku(A, B, C) or na_odcinku(A, B, D) or na_odcinku(C, D, A) or na_odcinku(C, D, B):
        return True
    return False


print(przecinaja_sie((0, 0), (4, 4), (0, 4), (4, 0)))  # True
print(przecinaja_sie((0, 0), (1, 1), (2, 2), (3, 3)))  # False
```
<b>

```
A, B - końce pierwszego odcinka
C, D - końce drugiego odcinka

def przecinaja_sie(A, B, C, D):
	w1 <- wyznacznik(A, B, C)
	w2 <- wyznacznik(A, B, D)
	w3 <- wyznacznik(C, D, A)
	w4 <- wyznacznik(C, D, B)
	Jeżeli w1 * w2 < 0 oraz w3 * w4 < 0
		Zwróć Prawdę
	Jeżeli na_odcinku(A, B, C) lub na_odcinku(A, B, D) lub na_odcinku(C, D, A) lub na_odcinku(C, D, B)
		Zwróć Prawdę
	Zwróć Fałsz
```
</b>
</details>

<a name="punkt_wielokat"></a>
## Przynależność punktu do obszaru (wielokąta) [⬆️](#)
<details><summary>Rozwiń</summary>

Metoda półprostej (ray casting): z punktu P prowadzimy poziomą półprostą w prawo i liczymy, ile boków wielokąta przecina. Nieparzysta liczba przecięć - punkt leży wewnątrz, parzysta - na zewnątrz. Działa także dla wielokątów wklęsłych. Punkt leżący na brzegu traktujemy jako należący do obszaru.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def na_odcinku(A, B, C):  # czy punkt C należy do odcinka AB
    if wyznacznik(A, B, C) != 0:
        return False
    return (min(A[0], B[0]) <= C[0] <= max(A[0], B[0])
            and min(A[1], B[1]) <= C[1] <= max(A[1], B[1]))


def w_wielokacie(P, wielokat):  # wielokat - lista kolejnych wierzchołków
    x, y = P
    n = len(wielokat)
    wewnatrz = False
    for i in range(n):
        A = wielokat[i]
        B = wielokat[(i + 1) % n]  # ostatni wierzchołek łączy się z pierwszym
        if na_odcinku(A, B, P):
            return True  # punkt na brzegu
        if (A[1] > y) != (B[1] > y):  # bok przecina poziomą prostą y = P.y
            x_przeciecia = A[0] + (y - A[1]) * (B[0] - A[0]) / (B[1] - A[1])
            if x_przeciecia > x:  # przecięcie leży na prawo od P
                wewnatrz = not wewnatrz
    return wewnatrz


kwadrat = [(0, 0), (4, 0), (4, 4), (0, 4)]
print(w_wielokacie((2, 2), kwadrat))  # True
print(w_wielokacie((5, 2), kwadrat))  # False
```
<b>

```
P = (x, y) - badany punkt
W[0..n-1] - kolejne wierzchołki wielokąta

def w_wielokacie(P, W):
	wewnatrz <- Fałsz
	Dla i = 0, 1, ... n - 1
		A <- W[i]
		B <- W[(i + 1) mod n]
		Jeżeli na_odcinku(A, B, P)
			Zwróć Prawdę
		Jeżeli (yA > y) != (yB > y)
			x_przeciecia <- xA + (y - yA) * (xB - xA) / (yB - yA)
			Jeżeli x_przeciecia > x
				wewnatrz <- nie wewnatrz
	Zwróć wewnatrz
```
</b>
</details>

<a name="koch"></a>
## Krzywa Kocha [⬆️](#)
<details><summary>Rozwiń</summary>

Krzywa Kocha stopnia 0 to odcinek. Krzywą stopnia k otrzymujemy, dzieląc odcinek na 3 równe części i zastępując środkową częścią dwoma bokami trójkąta równobocznego - każdy z 4 nowych odcinków rysujemy jako krzywą stopnia k - 1. Trzy krzywe Kocha narysowane na bokach trójkąta równobocznego tworzą płatek Kocha.

```python
import turtle


def koch(dlugosc, stopien):
    if stopien == 0:
        turtle.forward(dlugosc)
        return
    dlugosc /= 3
    koch(dlugosc, stopien - 1)
    turtle.left(60)
    koch(dlugosc, stopien - 1)
    turtle.right(120)
    koch(dlugosc, stopien - 1)
    turtle.left(60)
    koch(dlugosc, stopien - 1)


turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
koch(400, 3)
# płatek Kocha: for _ in range(3): koch(400, 3); turtle.right(120)
turtle.done()
```
<b>

```
dlugosc - długość odcinka
stopien - stopień krzywej

def koch(dlugosc, stopien):
	Jeżeli stopien == 0
		Narysuj odcinek o długości dlugosc
		Zakończ
	koch(dlugosc / 3, stopien - 1)
	Obróć w lewo o 60 stopni
	koch(dlugosc / 3, stopien - 1)
	Obróć w prawo o 120 stopni
	koch(dlugosc / 3, stopien - 1)
	Obróć w lewo o 60 stopni
	koch(dlugosc / 3, stopien - 1)
```
</b>
</details>

<a name="pitagoras"></a>
## Drzewo Pitagorasa [⬆️](#)
<details><summary>Rozwiń</summary>

Rysujemy kwadrat, a na jego górnym boku trójkąt prostokątny równoramienny. Na przyprostokątnych tego trójkąta budujemy (rekurencyjnie) dwa mniejsze drzewa, każde z kwadratem o boku bok * √2 / 2. Funkcja zaczyna i kończy rysowanie w tym samym miejscu (lewy dolny róg kwadratu) i z tym samym kierunkiem żółwia - dzięki temu wywołania rekurencyjne nie psują sobie położenia.

```python
import turtle


def drzewo(bok, stopien):  # żółw stoi w lewym dolnym rogu kwadratu i patrzy "w górę" kwadratu
    if stopien == 0:
        return
    for _ in range(4):  # kwadrat rysowany w prawo od żółwia
        turtle.forward(bok)
        turtle.right(90)
    nowy_bok = bok * 2 ** 0.5 / 2
    turtle.forward(bok)              # lewy górny róg kwadratu
    turtle.left(45)
    drzewo(nowy_bok, stopien - 1)    # lewa gałąź
    turtle.right(90)
    turtle.forward(nowy_bok)         # wierzchołek trójkąta
    drzewo(nowy_bok, stopien - 1)    # prawa gałąź
    turtle.back(nowy_bok)            # powrót do punktu startu
    turtle.left(45)
    turtle.back(bok)


turtle.speed(0)
turtle.penup()
turtle.goto(-50, -250)
turtle.pendown()
turtle.left(90)  # żółw patrzy w górę
drzewo(100, 8)
turtle.done()
```
<b>

```
bok - długość boku kwadratu
stopien - liczba poziomów drzewa

def drzewo(bok, stopien):
	Jeżeli stopien == 0
		Zakończ
	Narysuj kwadrat o boku bok
	nowy_bok <- bok * pierwiastek(2) / 2
	Idź naprzód o bok
	Obróć w lewo o 45 stopni
	drzewo(nowy_bok, stopien - 1)
	Obróć w prawo o 90 stopni
	Idź naprzód o nowy_bok
	drzewo(nowy_bok, stopien - 1)
	Cofnij się o nowy_bok
	Obróć w lewo o 45 stopni
	Cofnij się o bok
```
</b>
</details>

[py]: https://img.shields.io/badge/Python-%E2%9C%94-green?style=flat-square&logo=python
[notpy]: https://img.shields.io/badge/Python-%E2%9C%98-red?style=flat-square&logo=python

[java]: https://img.shields.io/badge/Java-%E2%9C%94-green?style=flat-square&logo=Java&logoColor=yellow
[nojava]: https://img.shields.io/badge/Java-%E2%9C%98-red?style=flat-square&logo=Java&logoColor=yellow

[c++]: https://img.shields.io/badge/C++-%E2%9C%94-green?style=flat-square&logo=c%2B%2B&logoColor=blue
[noc++]: https://img.shields.io/badge/C++-%E2%9C%98-red?style=flat-square&logo=c%2B%2B&logoColor=blue 
