<h1 align="center">Matura 2017 — maj, poziom rozszerzony (stara formuła)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/informatyka/MIN-R1_1P-172.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/informatyka/MIN-R2_1P-172.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/informatyka/Dane_PR2.zip) --- [ODPOWIEDZI](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/zasady_oceniania/MIN-R1-S.pdf)

## 1.1 i 1.2

> **Treść zadania:** Zadanie 1. Sortowanie. Dane: liczby całkowite dodatnie `n`, `k` oraz ciąg `T[1..n]` liczb z zakresu `[1..k]`. Wynik: tablica `W[1..n]` — elementy `T` uporządkowane niemalejąco. Algorytm:
>
> ```
> dla i=1..k: Liczba_wystapien[i] ← 0
> dla i=1..n: Liczba_wystapien[T[i]] ← Liczba_wystapien[T[i]] + 1
> p ← 1
> dla j=1..k:
>     dla i=1..Liczba_wystapien[j]:
>         W[p] ← j; p ← p+1
> ```
>
> - 1.1 — Podaj końcową zawartość tablicy `Liczba_wystapien[1..k]` dla danych: `n=10, k=5, T=[1,2,3,4,5,1,2,3,4,4]`; `n=5, k=10, T=[1,3,3,5,10]`; `n=5, k=5, T=[5,5,5,5,5]`; `n=10, k=4, T=[1,2,3,1,2,3,1,1,2,3]`.
> - 1.2 — Rangą elementu `T[i]` nazywamy liczbę elementów ciągu mniejszych od `T[i]` (np. dla `T=[1,2,3,4,5,1,4,3,2,5]` ranga `T[8]=3` wynosi 4). Korzystając z gotowej tablicy `Liczba_wystapien`, uzupełnij algorytm `r ← 0; dla j=1..___: r ← r + Liczba_wystapien[j]` tak, by `r` było rangą `T[i]`.

```py
def sortowanie(T, k):
    liczba_wystapien = [0] * (k + 1)       # indeksy 1..k
    for x in T:
        liczba_wystapien[x] += 1
    W = []
    for j in range(1, k + 1):
        for i in range(liczba_wystapien[j]):
            W.append(j)
    return liczba_wystapien[1:], W


def ranga(T, k, i):
    # i - numer elementu liczony od 1, jak w tresci zadania
    liczba_wystapien = [0] + sortowanie(T, k)[0]
    r = 0
    for j in range(1, T[i - 1]):           # j = 1 .. T[i]-1
        r += liczba_wystapien[j]
    return r


dane = [(5, [1, 2, 3, 4, 5, 1, 2, 3, 4, 4]), (10, [1, 3, 3, 5, 10]), (5, [5, 5, 5, 5, 5]), (4, [1, 2, 3, 1, 2, 3, 1, 1, 2, 3])]
for k, T in dane:
    print(sortowanie(T, k)[0])

T = [1, 2, 3, 4, 5, 1, 4, 3, 2, 5]
print(ranga(T, 5, 8), ranga(T, 5, 10), ranga(T, 5, 6))
```

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

// zwraca (liczba_wystapien[1..k], posortowany ciąg W)
std::pair<std::vector<int>, std::vector<int>> sortowanie(const std::vector<int>& T, int k) {
    std::vector<int> liczba_wystapien(k + 1, 0);  // indeksy 1..k
    for (int x : T)
        liczba_wystapien[x]++;
    std::vector<int> W;
    for (int j = 1; j <= k; j++)
        for (int i = 0; i < liczba_wystapien[j]; i++)
            W.push_back(j);
    return {std::vector<int>(liczba_wystapien.begin() + 1, liczba_wystapien.end()), W};
}

int ranga(const std::vector<int>& T, int k, int i) {
    // i - numer elementu liczony od 1, jak w tresci zadania
    std::vector<int> liczba_wystapien = {0};
    for (int x : sortowanie(T, k).first)
        liczba_wystapien.push_back(x);
    int r = 0;
    for (int j = 1; j < T[i - 1]; j++)  // j = 1 .. T[i]-1
        r += liczba_wystapien[j];
    return r;
}

int main() {
    std::vector<std::pair<int, std::vector<int>>> dane = {
        {5, {1, 2, 3, 4, 5, 1, 2, 3, 4, 4}}, {10, {1, 3, 3, 5, 10}}, {5, {5, 5, 5, 5, 5}}, {4, {1, 2, 3, 1, 2, 3, 1, 1, 2, 3}}};
    for (auto& [k, T] : dane)
        std::println("{}", sortowanie(T, k).first);

    std::vector<int> T = {1, 2, 3, 4, 5, 1, 4, 3, 2, 5};
    std::println("{} {} {}", ranga(T, 5, 8), ranga(T, 5, 10), ranga(T, 5, 6));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    // zwraca liczba_wystapien[1..k] (posortowany ciąg W budujemy tak jak w treści)
    static List<Integer> sortowanie(int[] T, int k) {
        int[] liczbaWystapien = new int[k + 1];  // indeksy 1..k
        for (int x : T)
            liczbaWystapien[x]++;
        List<Integer> W = new ArrayList<>();
        for (int j = 1; j <= k; j++)
            for (int i = 0; i < liczbaWystapien[j]; i++)
                W.add(j);
        List<Integer> wynik = new ArrayList<>();
        for (int j = 1; j <= k; j++)
            wynik.add(liczbaWystapien[j]);
        return wynik;
    }

    static int ranga(int[] T, int k, int i) {
        // i - numer elementu liczony od 1, jak w tresci zadania
        List<Integer> liczbaWystapien = new ArrayList<>(List.of(0));
        liczbaWystapien.addAll(sortowanie(T, k));
        int r = 0;
        for (int j = 1; j < T[i - 1]; j++)  // j = 1 .. T[i]-1
            r += liczbaWystapien.get(j);
        return r;
    }

    public static void main(String[] args) {
        int[] ki = {5, 10, 5, 4};
        int[][] ciagi = {{1, 2, 3, 4, 5, 1, 2, 3, 4, 4}, {1, 3, 3, 5, 10}, {5, 5, 5, 5, 5}, {1, 2, 3, 1, 2, 3, 1, 1, 2, 3}};
        for (int d = 0; d < ki.length; d++)
            System.out.println(sortowanie(ciagi[d], ki[d]));

        int[] T = {1, 2, 3, 4, 5, 1, 4, 3, 2, 5};
        System.out.println(ranga(T, 5, 8) + " " + ranga(T, 5, 10) + " " + ranga(T, 5, 6));
    }
}
```

**Odpowiedź:** 1.1: [2, 2, 2, 3, 1], [1, 0, 2, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 5], [4, 3, 3, 0]; 1.2: `dla j = 1..T[i] - 1`

## 1.3

> **Treść zadania:** Teraz elementy tablicy `T[1..n]` mogą być dowolnymi dodatnimi liczbami całkowitymi. Algorytm LicznikiMod:
>
> ```
> dla i=1..k: Liczba_wystapien[i] ← 0
> dla i=1..n:
>     m ← 1 + (T[i] mod k)
>     Liczba_wystapien[m] ← Liczba_wystapien[m] + 1
> w ← Liczba_wystapien[1]
> ```
>
> Podaj końcową zawartość tablicy `Liczba_wystapien[1..k]` dla `n=10`, `T=[1,2,3,4,5,1,2,3,4,4]` i `k` = 2, 3, 4, 5. Uzupełnij też specyfikację: co oznacza wynik `w`?

```py
def liczniki_mod(T, k):
    liczba_wystapien = [0] * (k + 1)
    for x in T:
        m = 1 + x % k
        liczba_wystapien[m] += 1
    w = liczba_wystapien[1]                # liczba elementow podzielnych przez k
    return liczba_wystapien[1:], w


T = [1, 2, 3, 4, 5, 1, 2, 3, 4, 4]
for k in [2, 3, 4, 5]:
    print(k, *liczniki_mod(T, k))
```

```cpp
// C++23
#include <print>
#include <vector>

int main() {
    std::vector<int> T = {1, 2, 3, 4, 5, 1, 2, 3, 4, 4};
    for (int k : {2, 3, 4, 5}) {
        std::vector<int> liczba_wystapien(k + 1, 0);
        for (int x : T) {
            int m = 1 + x % k;
            liczba_wystapien[m]++;
        }
        int w = liczba_wystapien[1];  // liczba elementow podzielnych przez k
        std::vector<int> liczniki(liczba_wystapien.begin() + 1, liczba_wystapien.end());
        std::println("{} {} {}", k, liczniki, w);
    }
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    public static void main(String[] args) {
        int[] T = {1, 2, 3, 4, 5, 1, 2, 3, 4, 4};
        for (int k : new int[]{2, 3, 4, 5}) {
            int[] liczbaWystapien = new int[k + 1];
            for (int x : T) {
                int m = 1 + x % k;
                liczbaWystapien[m]++;
            }
            int w = liczbaWystapien[1];  // liczba elementow podzielnych przez k
            List<Integer> liczniki = new ArrayList<>();
            for (int j = 1; j <= k; j++)
                liczniki.add(liczbaWystapien[j]);
            System.out.println(k + " " + liczniki + " " + w);
        }
    }
}
```

**Odpowiedź:** k=3: [2, 5, 3], k=4: [3, 3, 2, 2], k=5: [1, 2, 2, 2, 3]; w — liczba elementów ciągu T[1..n] podzielnych przez k

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2. Ciąg Pentanacciego: `p0=0, p1=1, p2=1, p3=2, p4=4`, a dla `n ≥ 5`: `pn = p(n-1) + p(n-2) + p(n-3) + p(n-4) + p(n-5)`.
>
> - 2.1 — Podaj `pn` dla `n` = 7 i 9 (dla `n=5` jest to 8).
> - 2.2 — Uzupełnij luki w algorytmie obliczającym `w = pn` dla nieujemnego `n`, który przechowuje tylko 5 ostatnich wyrazów w tablicy `tab[0..4]`:
>
> ```
> tab[0..4] ← 0, 1, 1, 2, 4
> i ← 5
> dopóki i ≤ ... wykonuj
>     temp ← tab[0]+tab[1]+tab[2]+tab[3]+tab[4]
>     tab[... mod 5] ← temp
>     i ← i+1
> ```

```py
def pentanacci(n):
    tab = [0, 1, 1, 2, 4]
    i = 5
    while i <= n:
        temp = tab[0] + tab[1] + tab[2] + tab[3] + tab[4]
        tab[i % 5] = temp
        i += 1
    return tab[n % 5]


for n in [5, 7, 9]:
    print(n, pentanacci(n))
```

```cpp
// C++23
#include <print>

long long pentanacci(int n) {
    long long tab[5] = {0, 1, 1, 2, 4};
    int i = 5;
    while (i <= n) {
        long long temp = tab[0] + tab[1] + tab[2] + tab[3] + tab[4];
        tab[i % 5] = temp;
        i++;
    }
    return tab[n % 5];
}

int main() {
    for (int n : {5, 7, 9})
        std::println("{} {}", n, pentanacci(n));
}
```

```java
// Java 25
public class Zadanie {
    static long pentanacci(int n) {
        long[] tab = {0, 1, 1, 2, 4};
        int i = 5;
        while (i <= n) {
            long temp = tab[0] + tab[1] + tab[2] + tab[3] + tab[4];
            tab[i % 5] = temp;
            i++;
        }
        return tab[n % 5];
    }

    public static void main(String[] args) {
        for (int n : new int[]{5, 7, 9})
            System.out.println(n + " " + pentanacci(n));
    }
}
```

**Odpowiedź:** p7 = 31, p9 = 120; luki: `i ≤ n`, `tab[i mod 5]`, `w ← tab[n mod 5]`

## 2.3

> **Treść zadania:** Dla ciągu Pentanacciego (`p0..p4 = 0, 1, 1, 2, 4`, `pn` = suma pięciu poprzednich wyrazów) rozważamy ciąg `rn = pn mod 2`: `r0..r4 = 0, 1, 1, 0, 0`, `rn = (r(n-1)+...+r(n-5)) mod 2`. Liczba `pn` jest parzysta wtedy i tylko wtedy, gdy `rn = 0`, a ciąg `rn` jest okresowy z okresem 6 (zależy tylko od `n mod 6`). Zapisz algorytm o jak najmniejszej złożoności, który dla nieujemnego `n` zwraca `w = 0`, gdy `pn` jest parzysta, i `w = 1`, gdy nieparzysta.

```py
def parzystosc(n):
    k = n % 6
    if k == 1 or k == 2:
        return 1
    return 0


# sprawdzenie z algorytmem z 2.2 (funkcja pentanacci)
def pentanacci(n):
    tab = [0, 1, 1, 2, 4]
    for i in range(5, n + 1):
        tab[i % 5] = sum(tab)
    return tab[n % 5]


print(all(parzystosc(n) == pentanacci(n) % 2 for n in range(100)))
```

```cpp
// C++23
#include <print>

int parzystosc(int n) {
    int k = n % 6;
    if (k == 1 || k == 2)
        return 1;
    return 0;
}

// sprawdzenie z algorytmem z 2.2 (funkcja pentanacci)
// dla n bliskich 100 wyrazy nie mieszczą się w 64 bitach; unsigned long long liczy modulo 2^64,
// co nie zmienia parzystości - a tylko ją tu sprawdzamy
unsigned long long pentanacci(int n) {
    unsigned long long tab[5] = {0, 1, 1, 2, 4};
    for (int i = 5; i <= n; i++)
        tab[i % 5] = tab[0] + tab[1] + tab[2] + tab[3] + tab[4];
    return tab[n % 5];
}

int main() {
    bool wszystkie = true;
    for (int n = 0; n < 100; n++)
        if (parzystosc(n) != (int)(pentanacci(n) % 2))
            wszystkie = false;
    std::println("{}", wszystkie ? "True" : "False");
}
```

```java
// Java 25
public class Zadanie {
    static int parzystosc(int n) {
        int k = n % 6;
        if (k == 1 || k == 2)
            return 1;
        return 0;
    }

    // sprawdzenie z algorytmem z 2.2 (funkcja pentanacci)
    // dla n bliskich 100 wyrazy nie mieszczą się w long; przepełnienie liczy modulo 2^64,
    // co nie zmienia parzystości - a tylko ją tu sprawdzamy (Math.floorMod daje 0 lub 1)
    static long pentanacci(int n) {
        long[] tab = {0, 1, 1, 2, 4};
        for (int i = 5; i <= n; i++)
            tab[i % 5] = tab[0] + tab[1] + tab[2] + tab[3] + tab[4];
        return tab[n % 5];
    }

    public static void main(String[] args) {
        boolean wszystkie = true;
        for (int n = 0; n < 100; n++)
            if (parzystosc(n) != Math.floorMod(pentanacci(n), 2))
                wszystkie = false;
        System.out.println(wszystkie ? "True" : "False");
    }
}
```

**Odpowiedź:** k ← n mod 6; jeżeli k = 1 lub k = 2, to w ← 1, w przeciwnym razie w ← 0

## 4.1

> **Treść zadania:** Zadanie 4. Ciągi binarne. Plik `binarne.txt` zawiera 500 napisów złożonych z zer i jedynek (każdy w osobnym wierszu), a długość każdego napisu jest podzielna przez 4. Odpowiedzi zapisz w pliku `zadanie4.txt`, poprzedzając każdą numerem zadania.
>
> Napis jest dwucykliczny, jeśli składa się z dwóch powtórzeń tego samego napisu (np. `10001000` = `1000`+`1000`; `00011000` i `10001001` nie są dwucykliczne). Podaj liczbę napisów dwucyklicznych w pliku, najdłuższy z nich oraz jego długość.

```py
licznik = 0
najdluzszy = ""

with open("binarne.txt") as file:
    for line in file:
        napis = line.strip()
        polowa = len(napis) // 2
        if napis[:polowa] == napis[polowa:]:
            licznik += 1
            if len(napis) > len(najdluzszy):
                najdluzszy = napis

print(licznik, najdluzszy, len(najdluzszy))
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    int licznik = 0;
    std::string najdluzszy = "";

    std::ifstream plik("binarne.txt");
    std::string napis;
    while (plik >> napis) {
        int polowa = napis.size() / 2;
        if (napis.substr(0, polowa) == napis.substr(polowa)) {
            licznik++;
            if (napis.size() > najdluzszy.size())
                najdluzszy = napis;
        }
    }

    std::println("{} {} {}", licznik, najdluzszy, najdluzszy.size());
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        String najdluzszy = "";

        for (String linia : Files.readAllLines(Path.of("binarne.txt"))) {
            String napis = linia.strip();
            int polowa = napis.length() / 2;
            if (napis.substring(0, polowa).equals(napis.substring(polowa))) {
                licznik++;
                if (napis.length() > najdluzszy.length())
                    najdluzszy = napis;
            }
        }

        System.out.println(licznik + " " + najdluzszy + " " + najdluzszy.length());
    }
}
```

**Odpowiedź:** 18; 00100101100011100010010110001110; 32

## 4.2

> **Treść zadania:** Napisy z pliku `binarne.txt` (500 napisów 0/1 o długościach podzielnych przez 4) traktujemy jako zapis BCD: każdy 4-znakowy segment koduje binarnie jedną cyfrę dziesiętną. Napis jest niepoprawny, jeśli któryś segment ma wartość większą niż 9 (np. `10010111` = 97 jest poprawny, a `11010000` i `1110` nie). Podaj liczbę niepoprawnych napisów oraz najmniejszą długość niepoprawnego napisu. Wynik dopisz do `zadanie4.txt`.

```py
licznik = 0
najkrotszy = None

with open("binarne.txt") as file:
    for line in file:
        napis = line.strip()
        poprawny = True
        for i in range(0, len(napis), 4):
            if int(napis[i:i + 4], 2) > 9:
                poprawny = False
        if not poprawny:
            licznik += 1
            if najkrotszy is None or len(napis) < najkrotszy:
                najkrotszy = len(napis)

print(licznik, najkrotszy)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    int licznik = 0;
    int najkrotszy = -1;  // -1 oznacza "jeszcze brak" (None w Pythonie)

    std::ifstream plik("binarne.txt");
    std::string napis;
    while (plik >> napis) {
        bool poprawny = true;
        for (size_t i = 0; i < napis.size(); i += 4)
            if (std::stoi(napis.substr(i, 4), nullptr, 2) > 9)
                poprawny = false;
        if (!poprawny) {
            licznik++;
            if (najkrotszy == -1 || (int)napis.size() < najkrotszy)
                najkrotszy = napis.size();
        }
    }

    std::println("{} {}", licznik, najkrotszy);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        Integer najkrotszy = null;

        for (String linia : Files.readAllLines(Path.of("binarne.txt"))) {
            String napis = linia.strip();
            boolean poprawny = true;
            for (int i = 0; i < napis.length(); i += 4)
                if (Integer.parseInt(napis.substring(i, Math.min(i + 4, napis.length())), 2) > 9)
                    poprawny = false;
            if (!poprawny) {
                licznik++;
                if (najkrotszy == null || napis.length() < najkrotszy)
                    najkrotszy = napis.length();
            }
        }

        System.out.println(licznik + " " + najkrotszy);
    }
}
```

**Odpowiedź:** 359; 4

## 4.3

> **Treść zadania:** Napisy z pliku `binarne.txt` traktujemy jako liczby naturalne w zwykłym zapisie binarnym, pomijając liczby większe niż 65 535. Znajdź największą z pozostałych liczb i podaj ją w zapisie binarnym oraz dziesiętnym. Wynik dopisz do `zadanie4.txt`.
>
> Przykład: dla napisów `1111000011110000`, `11110000111100001000`, `10100110` drugi jest pomijany, a odpowiedzią jest `1111000011110000, 61680`.

```py
maks = 0

with open("binarne.txt") as file:
    for line in file:
        liczba = int(line.strip(), 2)
        if liczba <= 65535 and liczba > maks:
            maks = liczba

print(bin(maks)[2:], maks)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    long long maks = 0;

    std::ifstream plik("binarne.txt");
    std::string napis;
    while (plik >> napis) {
        // napisy mają do 80 cyfr - nie zmieszczą się w long long, więc najpierw
        // usuwamy zera wiodące: liczba <= 65535 ma najwyżej 16 cyfr dwójkowych
        size_t pierwsza_jedynka = napis.find('1');
        if (pierwsza_jedynka == std::string::npos)
            continue;  // same zera - liczba 0 nie zmieni maksimum
        std::string bez_zer = napis.substr(pierwsza_jedynka);
        if (bez_zer.size() > 16)
            continue;
        long long liczba = std::stoll(bez_zer, nullptr, 2);
        if (liczba <= 65535 && liczba > maks)
            maks = liczba;
    }

    // zapis dwójkowy liczby maks (bez zer wiodących, jak bin(maks)[2:])
    std::string dwojkowo = "";
    long long x = maks;
    do {
        dwojkowo = char('0' + x % 2) + dwojkowo;
        x /= 2;
    } while (x > 0);
    std::println("{} {}", dwojkowo, maks);
}
```

```java
// Java 25
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // napisy mają do 80 cyfr - nie zmieszczą się w long, dlatego BigInteger
        BigInteger maks = BigInteger.ZERO;
        BigInteger granica = BigInteger.valueOf(65535);

        for (String linia : Files.readAllLines(Path.of("binarne.txt"))) {
            BigInteger liczba = new BigInteger(linia.strip(), 2);
            if (liczba.compareTo(granica) <= 0 && liczba.compareTo(maks) > 0)
                maks = liczba;
        }

        System.out.println(maks.toString(2) + " " + maks);
    }
}
```

**Odpowiedź:** 1101011001100101, 54885

## 5.1, 5.2 i 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 5. Ogrzewanie. Sezon grzewczy trwa od 15.09.2015 do 31.03.2016. Rano 15.09.2015 pan Binarny ma 550 kg drewna; jedno ogrzewanie drewnem zużywa 26 kg. Dom jest ogrzewany dwa razy dziennie:
> - w dni robocze (pn–pt) rano gazem;
> - w soboty i niedziele rano drewnem, jeśli jest co najmniej 26 kg drewna, w przeciwnym razie gazem;
> - codziennie wieczorem drewnem, jeśli jest co najmniej 26 kg drewna, w przeciwnym razie gazem.
>
> W każdy piątek rano sprawdzany jest zapas: jeśli jest mniejszy niż 100 kg, tego dnia przed wieczornym ogrzewaniem dostarczane jest 300 kg drewna. Odpowiedzi zapisz w pliku `zadanie5.txt`, poprzedzając je numerami zadań.
>
> - 5.1 — Podaj datę i porę dnia (rano/wieczór), kiedy po raz pierwszy po ogrzewaniu zapas drewna był niższy niż 100 kg.
> - 5.2 — Podaj, ile razy w sezonie dostarczono drewno oraz ile razy wieczorem dom ogrzewano drewnem, a ile gazem.
> - 5.4 — Podaj minimalną masę drewna dostarczanego w piątki (przy zapasie < 100 kg; dostawa to zawsze co najmniej 300 kg), przy której przez cały sezon dom zawsze da się ogrzać drewnem, gdy przewiduje to harmonogram.

```py
from datetime import date, timedelta


def sezon(dostawa):
    dzien = date(2015, 9, 15)
    drewno = 550
    pierwszy_raz = None
    dostawy = 0
    wieczory_drewno = 0
    wieczory_gaz = 0
    ogrzewania_gazem_zamiast_drewnem = 0
    while dzien <= date(2016, 3, 31):
        dzien_tygodnia = dzien.weekday()    # 0 - poniedzialek, 4 - piatek, 5 i 6 - weekend
        if dzien_tygodnia == 4 and drewno < 100:
            drewno += dostawa
            dostawy += 1
        # rano - w weekend drewno (jesli jest), w dni robocze gaz
        if dzien_tygodnia >= 5:
            if drewno >= 26:
                drewno -= 26
            else:
                ogrzewania_gazem_zamiast_drewnem += 1
            if drewno < 100 and pierwszy_raz is None:
                pierwszy_raz = (dzien, "rano")
        # wieczor - zawsze drewno (jesli jest)
        if drewno >= 26:
            drewno -= 26
            wieczory_drewno += 1
        else:
            wieczory_gaz += 1
            ogrzewania_gazem_zamiast_drewnem += 1
        if drewno < 100 and pierwszy_raz is None:
            pierwszy_raz = (dzien, "wieczor")
        dzien += timedelta(days=1)
    return pierwszy_raz, dostawy, wieczory_drewno, wieczory_gaz, ogrzewania_gazem_zamiast_drewnem


pierwszy_raz, dostawy, wieczory_drewno, wieczory_gaz, _ = sezon(300)
print("5.1", pierwszy_raz[0], pierwszy_raz[1])
print("5.2", dostawy, wieczory_drewno, wieczory_gaz)

masa = 300
while sezon(masa)[4] > 0:
    masa += 1
print("5.4", masa)
```

```cpp
// C++23
#include <chrono>
#include <print>
#include <string>

using namespace std::chrono;

struct Sezon {
    sys_days pierwszy_raz_dzien;
    std::string pierwszy_raz_pora;  // "" - jeszcze nie było (None w Pythonie)
    int dostawy, wieczory_drewno, wieczory_gaz, ogrzewania_gazem_zamiast_drewnem;
};

Sezon sezon(int dostawa) {
    sys_days dzien = year(2015) / September / 15;
    sys_days koniec = year(2016) / March / 31;
    int drewno = 550;
    Sezon s{};
    while (dzien <= koniec) {
        int dzien_tygodnia = weekday(dzien).iso_encoding() - 1;  // 0 - poniedzialek, 4 - piatek, 5 i 6 - weekend
        if (dzien_tygodnia == 4 && drewno < 100) {
            drewno += dostawa;
            s.dostawy++;
        }
        // rano - w weekend drewno (jesli jest), w dni robocze gaz
        if (dzien_tygodnia >= 5) {
            if (drewno >= 26)
                drewno -= 26;
            else
                s.ogrzewania_gazem_zamiast_drewnem++;
            if (drewno < 100 && s.pierwszy_raz_pora.empty()) {
                s.pierwszy_raz_dzien = dzien;
                s.pierwszy_raz_pora = "rano";
            }
        }
        // wieczor - zawsze drewno (jesli jest)
        if (drewno >= 26) {
            drewno -= 26;
            s.wieczory_drewno++;
        } else {
            s.wieczory_gaz++;
            s.ogrzewania_gazem_zamiast_drewnem++;
        }
        if (drewno < 100 && s.pierwszy_raz_pora.empty()) {
            s.pierwszy_raz_dzien = dzien;
            s.pierwszy_raz_pora = "wieczor";
        }
        dzien += days(1);
    }
    return s;
}

int main() {
    Sezon s = sezon(300);
    std::println("5.1 {} {}", year_month_day(s.pierwszy_raz_dzien), s.pierwszy_raz_pora);
    std::println("5.2 {} {} {}", s.dostawy, s.wieczory_drewno, s.wieczory_gaz);

    int masa = 300;
    while (sezon(masa).ogrzewania_gazem_zamiast_drewnem > 0)
        masa++;
    std::println("5.4 {}", masa);
}
```

```java
// Java 25
import java.time.LocalDate;

public class Zadanie {
    record Sezon(LocalDate pierwszyRazDzien, String pierwszyRazPora, int dostawy,
                 int wieczoryDrewno, int wieczoryGaz, int ogrzewaniaGazemZamiastDrewnem) {}

    static Sezon sezon(int dostawa) {
        LocalDate dzien = LocalDate.of(2015, 9, 15);
        int drewno = 550;
        LocalDate pierwszyRazDzien = null;
        String pierwszyRazPora = null;
        int dostawy = 0;
        int wieczoryDrewno = 0;
        int wieczoryGaz = 0;
        int ogrzewaniaGazemZamiastDrewnem = 0;
        while (!dzien.isAfter(LocalDate.of(2016, 3, 31))) {
            int dzienTygodnia = dzien.getDayOfWeek().getValue() - 1;  // 0 - poniedzialek, 4 - piatek, 5 i 6 - weekend
            if (dzienTygodnia == 4 && drewno < 100) {
                drewno += dostawa;
                dostawy++;
            }
            // rano - w weekend drewno (jesli jest), w dni robocze gaz
            if (dzienTygodnia >= 5) {
                if (drewno >= 26)
                    drewno -= 26;
                else
                    ogrzewaniaGazemZamiastDrewnem++;
                if (drewno < 100 && pierwszyRazPora == null) {
                    pierwszyRazDzien = dzien;
                    pierwszyRazPora = "rano";
                }
            }
            // wieczor - zawsze drewno (jesli jest)
            if (drewno >= 26) {
                drewno -= 26;
                wieczoryDrewno++;
            } else {
                wieczoryGaz++;
                ogrzewaniaGazemZamiastDrewnem++;
            }
            if (drewno < 100 && pierwszyRazPora == null) {
                pierwszyRazDzien = dzien;
                pierwszyRazPora = "wieczor";
            }
            dzien = dzien.plusDays(1);
        }
        return new Sezon(pierwszyRazDzien, pierwszyRazPora, dostawy, wieczoryDrewno, wieczoryGaz,
                ogrzewaniaGazemZamiastDrewnem);
    }

    public static void main(String[] args) {
        Sezon s = sezon(300);
        System.out.println("5.1 " + s.pierwszyRazDzien() + " " + s.pierwszyRazPora());
        System.out.println("5.2 " + s.dostawy() + " " + s.wieczoryDrewno() + " " + s.wieczoryGaz());

        int masa = 300;
        while (sezon(masa).ogrzewaniaGazemZamiastDrewnem() > 0)
            masa++;
        System.out.println("5.4 " + masa);
    }
}
```

**Odpowiedź:** 5.1: 2015-09-28, wieczorem; 5.2: 18 dostaw, 167 wieczorów drewnem, 32 wieczory gazem; 5.4: 468 kg

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** W symulacji ogrzewania z zadania 5 (sezon 15.09.2015–31.03.2016, początkowo 550 kg drewna, 26 kg na ogrzewanie, dostawy 300 kg w piątki przy zapasie < 100 kg) przedstaw na wykresie liniowym masę drewna wieczorem (po wieczornym ogrzewaniu) we wszystkich dniach sezonu. Zadbaj o czytelność wykresu.

```py
from datetime import date, timedelta

# dane do wykresu liniowego: data, masa drewna po wieczornym ogrzewaniu
dzien = date(2015, 9, 15)
drewno = 550

with open("wykres_5_3.txt", "w") as wynik:
    while dzien <= date(2016, 3, 31):
        if dzien.weekday() == 4 and drewno < 100:
            drewno += 300
        if dzien.weekday() >= 5 and drewno >= 26:
            drewno -= 26
        if drewno >= 26:
            drewno -= 26
        wynik.write(f"{dzien};{drewno}\n")
        dzien += timedelta(days=1)
```

```cpp
// C++23
#include <chrono>
#include <fstream>
#include <print>

using namespace std::chrono;

int main() {
    // dane do wykresu liniowego: data, masa drewna po wieczornym ogrzewaniu
    sys_days dzien = year(2015) / September / 15;
    sys_days koniec = year(2016) / March / 31;
    int drewno = 550;

    std::ofstream wynik("wykres_5_3.txt");
    while (dzien <= koniec) {
        int dzien_tygodnia = weekday(dzien).iso_encoding() - 1;  // 0 - poniedzialek, 4 - piatek
        if (dzien_tygodnia == 4 && drewno < 100)
            drewno += 300;
        if (dzien_tygodnia >= 5 && drewno >= 26)
            drewno -= 26;
        if (drewno >= 26)
            drewno -= 26;
        std::println(wynik, "{};{}", year_month_day(dzien), drewno);
        dzien += days(1);
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.time.LocalDate;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // dane do wykresu liniowego: data, masa drewna po wieczornym ogrzewaniu
        LocalDate dzien = LocalDate.of(2015, 9, 15);
        int drewno = 550;

        try (var wynik = new PrintWriter("wykres_5_3.txt")) {
            while (!dzien.isAfter(LocalDate.of(2016, 3, 31))) {
                int dzienTygodnia = dzien.getDayOfWeek().getValue() - 1;  // 0 - poniedzialek, 4 - piatek
                if (dzienTygodnia == 4 && drewno < 100)
                    drewno += 300;
                if (dzienTygodnia >= 5 && drewno >= 26)
                    drewno -= 26;
                if (drewno >= 26)
                    drewno -= 26;
                wynik.println(dzien + ";" + drewno);
                dzien = dzien.plusDays(1);
            }
        }
    }
}
```

**Odpowiedź:** wykres liniowy (oś X — data, oś Y — masa drewna wieczorem) tworzymy z pliku `wykres_5_3.txt`
