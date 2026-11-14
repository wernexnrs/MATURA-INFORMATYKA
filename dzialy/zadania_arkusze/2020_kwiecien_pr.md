<h1 align="center">Matura próbna 2020 — kwiecień</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona-odpowiedzi.pdf)

## 1.1

> **Treść zadania:** Zadanie 1 (rekurencja). Dana jest dodatnia liczba całkowita `n` i rosnąco uporządkowana tablica różnych liczb całkowitych `T[1..n]`. Funkcja rekurencyjna (parametry całkowite, `1 ≤ p ≤ k ≤ n`, div — dzielenie całkowite):
>
> ```
> Rek(x, p, k)
>     jeżeli p < k
>         s ← (p + k) div 2
>         jeżeli T[s] ≥ x
>             wynikiem jest Rek(x, p, s)
>         w przeciwnym razie
>             wynikiem jest Rek(x, s + 1, k)
>     w przeciwnym razie
>         jeżeli T[p] = x
>             wynikiem jest p
>         w przeciwnym razie
>             wynikiem jest −1
> ```
>
> Podaj najmniejszą i największą możliwą liczbę wywołań funkcji `Rek` (wliczając pierwsze) po wywołaniu `Rek(2020, 5, 14)` dla `n = 17` i pewnej rosnącej tablicy `T[1..17]` różnych liczb całkowitych.

```py
# Liczba wywołań Rek zależy tylko od tego, w którą połowę przedziału p..k pójdzie rekurencja.
# Sprawdzamy obie możliwości w każdym kroku i wybieramy najmniejszą / największą liczbę wywołań.
def wywolania(p, k, wybierz):
    if p < k:
        s = (p + k) // 2
        return 1 + wybierz(wywolania(p, s, wybierz), wywolania(s + 1, k, wybierz))
    return 1


print("najmniejsza:", wywolania(5, 14, min))
print("największa:", wywolania(5, 14, max))
```

```cpp
// C++23
#include <algorithm>
#include <functional>
#include <print>

// Liczba wywołań Rek zależy tylko od tego, w którą połowę przedziału p..k pójdzie rekurencja.
// Sprawdzamy obie możliwości w każdym kroku i wybieramy najmniejszą / największą liczbę wywołań.
int wywolania(int p, int k, const std::function<int(int, int)>& wybierz) {
    if (p < k) {
        int s = (p + k) / 2;
        return 1 + wybierz(wywolania(p, s, wybierz), wywolania(s + 1, k, wybierz));
    }
    return 1;
}

int main() {
    auto mniejsza = [](int a, int b) { return std::min(a, b); };
    auto wieksza = [](int a, int b) { return std::max(a, b); };
    std::println("najmniejsza: {}", wywolania(5, 14, mniejsza));
    std::println("największa: {}", wywolania(5, 14, wieksza));
}
```

```java
// Java 25
import java.util.function.IntBinaryOperator;

public class Zadanie {
    // Liczba wywołań Rek zależy tylko od tego, w którą połowę przedziału p..k pójdzie rekurencja.
    // Sprawdzamy obie możliwości w każdym kroku i wybieramy najmniejszą / największą liczbę wywołań.
    static int wywolania(int p, int k, IntBinaryOperator wybierz) {
        if (p < k) {
            int s = (p + k) / 2;
            return 1 + wybierz.applyAsInt(wywolania(p, s, wybierz), wywolania(s + 1, k, wybierz));
        }
        return 1;
    }

    public static void main(String[] args) throws Exception {
        System.out.println("najmniejsza: " + wywolania(5, 14, Math::min));
        System.out.println("największa: " + wywolania(5, 14, Math::max));
    }
}
```

**Odpowiedź:** najmniejsza liczba wywołań 4, największa 5

## 1.2

> **Treść zadania:** Funkcja `Rek(x, p, k)` jak w zadaniu 1.1 (rekurencyjne wyszukiwanie binarne `x` w rosnącej tablicy `T`).
>
> Dla `n = 11`, tablicy `T = [1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38]` i pierwszego wywołania `Rek(7, 1, 11)` podaj wartości parametrów `(x, p, k)` w kolejnych wywołaniach funkcji.

```py
T = [1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38]


def Rek(x, p, k):
    print(f"Rek({x},{p},{k})")
    if p < k:
        s = (p + k) // 2
        if T[s - 1] >= x:  # tablica w treści jest numerowana od 1
            return Rek(x, p, s)
        else:
            return Rek(x, s + 1, k)
    else:
        if T[p - 1] == x:
            return p
        return -1


print("wynik:", Rek(7, 1, 11))
```

```cpp
// C++23
#include <print>
#include <vector>

const std::vector<int> T = {1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38};

int Rek(int x, int p, int k) {
    std::println("Rek({},{},{})", x, p, k);
    if (p < k) {
        int s = (p + k) / 2;
        if (T[s - 1] >= x)  // tablica w treści jest numerowana od 1
            return Rek(x, p, s);
        else
            return Rek(x, s + 1, k);
    } else {
        if (T[p - 1] == x)
            return p;
        return -1;
    }
}

int main() {
    int wynik = Rek(7, 1, 11);
    std::println("wynik: {}", wynik);
}
```

```java
// Java 25
public class Zadanie {
    static final int[] T = {1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38};

    static int Rek(int x, int p, int k) {
        System.out.println("Rek(" + x + "," + p + "," + k + ")");
        if (p < k) {
            int s = (p + k) / 2;
            if (T[s - 1] >= x)  // tablica w treści jest numerowana od 1
                return Rek(x, p, s);
            else
                return Rek(x, s + 1, k);
        } else {
            if (T[p - 1] == x)
                return p;
            return -1;
        }
    }

    public static void main(String[] args) throws Exception {
        int wynik = Rek(7, 1, 11);
        System.out.println("wynik: " + wynik);
    }
}
```

**Odpowiedź:** Rek(7,1,6), Rek(7,1,3), Rek(7,3,3) (1.3: D. logarytmiczna)

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2 (moda). Moda (dominanta) zestawu danych to element występujący w nim najczęściej; zestaw może mieć kilka mód (np. 2, 3, -4, 2, 3, -5, 2, 3 ma mody 2 i 3). Jeśli wszystkie elementy występują jednakowo często, zestaw nie ma mody (np. 4, 4, 2, 3, 2, 3).
>
> - 2.1 — podaj, ile najwyżej różnych mód może mieć zestaw 10 elementów, i podaj przykład 10-elementowego zestawu z dokładnie trzema modami.
> - 2.2 — napisz algorytm, który dla `n > 2` i tablicy `T[1..n]` liczb całkowitych mającej dokładnie jedną modę wyznaczy tę modę `m`. Wolno używać tylko operacji arytmetycznych (w tym div i mod), odwołań do elementów tablicy, porównań, instrukcji sterujących, przypisań i własnych funkcji.

```py
def moda(n, T):
    najwiecej = 0
    for i in range(n):
        ile = 0
        for j in range(n):
            if T[j] == T[i]:
                ile += 1
        if ile > najwiecej:
            najwiecej = ile
            m = T[i]
    return m


print(moda(9, [2, 3, 4, 2, 3, 5, 2, 100, 67]))
# 2.1 - przykład 10-elementowego zestawu z trzema modami (maksymalnie mód może być 4)
print([1, 1, 1, 2, 2, 2, 3, 3, 3, 4])
```

```cpp
// C++23
#include <print>
#include <vector>

int moda(int n, const std::vector<int>& T) {
    int najwiecej = 0;
    int m = 0;
    for (int i = 0; i < n; i++) {
        int ile = 0;
        for (int j = 0; j < n; j++)
            if (T[j] == T[i])
                ile++;
        if (ile > najwiecej) {
            najwiecej = ile;
            m = T[i];
        }
    }
    return m;
}

int main() {
    std::println("{}", moda(9, {2, 3, 4, 2, 3, 5, 2, 100, 67}));
    // 2.1 - przykład 10-elementowego zestawu z trzema modami (maksymalnie mód może być 4)
    std::println("{}", std::vector<int>{1, 1, 1, 2, 2, 2, 3, 3, 3, 4});
}
```

```java
// Java 25
import java.util.Arrays;

public class Zadanie {
    static int moda(int n, int[] T) {
        int najwiecej = 0;
        int m = 0;
        for (int i = 0; i < n; i++) {
            int ile = 0;
            for (int j = 0; j < n; j++)
                if (T[j] == T[i])
                    ile++;
            if (ile > najwiecej) {
                najwiecej = ile;
                m = T[i];
            }
        }
        return m;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(moda(9, new int[]{2, 3, 4, 2, 3, 5, 2, 100, 67}));
        // 2.1 - przykład 10-elementowego zestawu z trzema modami (maksymalnie mód może być 4)
        System.out.println(Arrays.toString(new int[]{1, 1, 1, 2, 2, 2, 3, 3, 3, 4}));
    }
}
```

**Odpowiedź:** 2.1: maksymalnie 4 mody, np. 1 1 1 2 2 2 3 3 3 4; 2.2: algorytm w kodzie (dla przykładu z treści moda = 2)

## 4.1

> **Treść zadania:** Zadanie 4 (luki w ciągu). Luka to wartość bezwzględna różnicy dwóch kolejnych elementów ciągu (np. ciąg 5, 2, 7, 10 ma luki 3, 5, 3). Plik `dane4.txt` zawiera ciąg 1000 dodatnich liczb całkowitych nie większych od 2·10⁹. Odpowiedzi zapisz w pliku `zadanie4.txt`, poprzedzając każdą numerem zadania.
>
> Podaj wartość największej i najmniejszej luki w ciągu.

```py
with open("dane4.txt") as file:
    liczby = [int(line) for line in file]

luki = []
for i in range(1, len(liczby)):
    luki.append(abs(liczby[i] - liczby[i - 1]))

print(min(luki))
print(max(luki))
```

```cpp
// C++23
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <print>
#include <vector>

int main() {
    std::ifstream plik("dane4.txt");
    std::vector<long long> liczby;
    long long x;
    while (plik >> x)
        liczby.push_back(x);

    std::vector<long long> luki;
    for (size_t i = 1; i < liczby.size(); i++)
        luki.push_back(std::llabs(liczby[i] - liczby[i - 1]));

    std::println("{}", std::ranges::min(luki));
    std::println("{}", std::ranges::max(luki));
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<Long>();
        for (String line : Files.readAllLines(Path.of("dane4.txt")))
            if (!line.isBlank())
                liczby.add(Long.parseLong(line.trim()));

        var luki = new ArrayList<Long>();
        for (int i = 1; i < liczby.size(); i++)
            luki.add(Math.abs(liczby.get(i) - liczby.get(i - 1)));

        System.out.println(Collections.min(luki));
        System.out.println(Collections.max(luki));
    }
}
```

**Odpowiedź:** najmniejsza 1, największa 1056392131

## 4.2

> **Treść zadania:** Dane z pliku `dane4.txt` (ciąg 1000 liczb; luka = |różnica kolejnych elementów|).
>
> Fragment ciągu jest regularny, jeśli wszystkie jego luki są równe. Znajdź najdłuższy fragment regularny (jest jeden taki) i podaj jego długość oraz pierwszą i ostatnią liczbę.
>
> Przykład: w ciągu 4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3 najdłuższe fragmenty regularne mają długość 4: `4, 1, 4, 7` oraz `11, 12, 13, 14`.

```py
with open("dane4.txt") as file:
    liczby = [int(line) for line in file]

najdluzszy = 2
dlugosc = 2  # każde dwa kolejne elementy tworzą fragment regularny
poczatek, koniec = liczby[0], liczby[1]

for i in range(2, len(liczby)):
    if abs(liczby[i] - liczby[i - 1]) == abs(liczby[i - 1] - liczby[i - 2]):
        dlugosc += 1
    else:
        dlugosc = 2
    if dlugosc > najdluzszy:
        najdluzszy = dlugosc
        poczatek = liczby[i - dlugosc + 1]
        koniec = liczby[i]

print(najdluzszy, poczatek, koniec)
```

```cpp
// C++23
#include <cstdlib>
#include <fstream>
#include <print>
#include <vector>

int main() {
    std::ifstream plik("dane4.txt");
    std::vector<long long> liczby;
    long long x;
    while (plik >> x)
        liczby.push_back(x);

    int najdluzszy = 2;
    int dlugosc = 2;  // każde dwa kolejne elementy tworzą fragment regularny
    long long poczatek = liczby[0], koniec = liczby[1];

    for (size_t i = 2; i < liczby.size(); i++) {
        if (std::llabs(liczby[i] - liczby[i - 1]) == std::llabs(liczby[i - 1] - liczby[i - 2]))
            dlugosc++;
        else
            dlugosc = 2;
        if (dlugosc > najdluzszy) {
            najdluzszy = dlugosc;
            poczatek = liczby[i - dlugosc + 1];
            koniec = liczby[i];
        }
    }

    std::println("{} {} {}", najdluzszy, poczatek, koniec);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<Long>();
        for (String line : Files.readAllLines(Path.of("dane4.txt")))
            if (!line.isBlank())
                liczby.add(Long.parseLong(line.trim()));

        int najdluzszy = 2;
        int dlugosc = 2;  // każde dwa kolejne elementy tworzą fragment regularny
        long poczatek = liczby.get(0), koniec = liczby.get(1);

        for (int i = 2; i < liczby.size(); i++) {
            if (Math.abs(liczby.get(i) - liczby.get(i - 1)) == Math.abs(liczby.get(i - 1) - liczby.get(i - 2)))
                dlugosc++;
            else
                dlugosc = 2;
            if (dlugosc > najdluzszy) {
                najdluzszy = dlugosc;
                poczatek = liczby.get(i - dlugosc + 1);
                koniec = liczby.get(i);
            }
        }

        System.out.println(najdluzszy + " " + poczatek + " " + koniec);
    }
}
```

**Odpowiedź:** długość 17, początek 193134524, koniec 223545714

## 4.3

> **Treść zadania:** Dane z pliku `dane4.txt` (ciąg 1000 liczb; luka = |różnica kolejnych elementów|).
>
> Krotność luki to liczba jej wystąpień, a najczęstsza luka to luka o największej krotności. Podaj krotność najczęstszej luki oraz wartości wszystkich najczęstszych luk.
>
> Przykład: dla ciągu 4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3 największa krotność to 4 i mają ją luki 7 i 3.

```py
with open("dane4.txt") as file:
    liczby = [int(line) for line in file]

krotnosc = {}
for i in range(1, len(liczby)):
    luka = abs(liczby[i] - liczby[i - 1])
    krotnosc[luka] = krotnosc.get(luka, 0) + 1

najwiecej = max(krotnosc.values())
print(najwiecej)
for luka in krotnosc:
    if krotnosc[luka] == najwiecej:
        print(luka)
```

```cpp
// C++23
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <print>
#include <unordered_map>
#include <vector>

int main() {
    std::ifstream plik("dane4.txt");
    std::vector<long long> liczby;
    long long x;
    while (plik >> x)
        liczby.push_back(x);

    std::unordered_map<long long, int> krotnosc;
    std::vector<long long> kolejnosc;  // luki w kolejności pojawienia się (jak słownik w Pythonie)
    for (size_t i = 1; i < liczby.size(); i++) {
        long long luka = std::llabs(liczby[i] - liczby[i - 1]);
        if (!krotnosc.contains(luka))
            kolejnosc.push_back(luka);
        krotnosc[luka]++;
    }

    int najwiecej = 0;
    for (const auto& [luka, ile] : krotnosc)
        najwiecej = std::max(najwiecej, ile);
    std::println("{}", najwiecej);
    for (long long luka : kolejnosc)
        if (krotnosc[luka] == najwiecej)
            std::println("{}", luka);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<Long>();
        for (String line : Files.readAllLines(Path.of("dane4.txt")))
            if (!line.isBlank())
                liczby.add(Long.parseLong(line.trim()));

        var krotnosc = new LinkedHashMap<Long, Integer>();  // pamięta kolejność dodawania, jak słownik w Pythonie
        for (int i = 1; i < liczby.size(); i++) {
            long luka = Math.abs(liczby.get(i) - liczby.get(i - 1));
            krotnosc.merge(luka, 1, Integer::sum);
        }

        int najwiecej = Collections.max(krotnosc.values());
        System.out.println(najwiecej);
        for (var e : krotnosc.entrySet())
            if (e.getValue() == najwiecej)
                System.out.println(e.getKey());
    }
}
```

**Odpowiedź:** krotność 31, luki 149 i 11

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 5 (zbiornik wody). Ogród ma zbiornik na wodę o pojemności 25 000 litrów; 31 marca o 21:00 był pełny. Plik `pogoda.txt` zawiera (z wierszem nagłówkowym, dane rozdzielone tabulatorem) średnią dobową temperaturę i opady dobowe w l/m² dla kolejnych dni od 1 kwietnia do 30 września 2015 r. Zasady:
> - temperatura i opady są mierzone od 20:00 dnia poprzedniego do 20:00 dnia bieżącego;
> - opady uzupełniają zbiornik o `700 · x` litrów (`x` — opady w l/m²), najwyżej do pełna;
> - w dni bezdeszczowe paruje `0,03% · T^1,5 · y` litrów (`T` — średnia temperatura, `y` — stan zbiornika o 21:00 dnia poprzedniego), zaokrąglone w górę;
> - ogród podlewa się o 20:00 w dni, gdy temperatura przekracza 15°C, a opady nie przekraczają 0,6 l/m²; zużywa się 12 000 l, a gdy temperatura przekracza 30°C — 24 000 l;
> - jeśli przed podlewaniem w zbiorniku brakuje wody, dolewa się go z wodociągu do pełna; podlewanie kończy się o 21:00.
>
> Wyniki zaokrąglaj w górę do pełnych litrów (kontrolnie: przez cały okres dolano 743 427 l). Odpowiedzi zapisz w pliku `wyniki5.txt`, poprzedzając je numerem zadania.
>
> Podaj liczbę dni, w których:
> - temperatura nie przekraczała 15°C,
> - temperatura przekraczała 15°C, a opady nie przekraczały 0,6 l/m²,
> - temperatura przekraczała 15°C i opady przekraczały 0,6 l/m².

```py
chlodne = cieple_bez_deszczu = cieple_z_deszczem = 0

with open("pogoda.txt") as file:
    file.readline()  # nagłówek
    for line in file:
        temperatura, opady = line.split()
        temperatura = float(temperatura.replace(",", "."))
        opady = float(opady.replace(",", "."))
        if temperatura <= 15:
            chlodne += 1
        elif opady <= 0.6:
            cieple_bez_deszczu += 1
        else:
            cieple_z_deszczem += 1

print(chlodne, cieple_bez_deszczu, cieple_z_deszczem)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>

// liczba z przecinkiem dziesiętnym, np. "12,5" -> 12.5
double na_liczbe(std::string tekst) {
    std::ranges::replace(tekst, ',', '.');
    return std::stod(tekst);
}

int main() {
    int chlodne = 0, cieple_bez_deszczu = 0, cieple_z_deszczem = 0;

    std::ifstream plik("pogoda.txt");
    std::string naglowek;
    std::getline(plik, naglowek);
    std::string t, o;
    while (plik >> t >> o) {
        double temperatura = na_liczbe(t);
        double opady = na_liczbe(o);
        if (temperatura <= 15)
            chlodne++;
        else if (opady <= 0.6)
            cieple_bez_deszczu++;
        else
            cieple_z_deszczem++;
    }

    std::println("{} {} {}", chlodne, cieple_bez_deszczu, cieple_z_deszczem);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int chlodne = 0, ciepleBezDeszczu = 0, ciepleZDeszczem = 0;

        var linie = Files.readAllLines(Path.of("pogoda.txt"));
        for (String line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            if (line.isBlank())
                continue;
            String[] czesci = line.trim().split("\\s+");
            double temperatura = Double.parseDouble(czesci[0].replace(",", "."));
            double opady = Double.parseDouble(czesci[1].replace(",", "."));
            if (temperatura <= 15)
                chlodne++;
            else if (opady <= 0.6)
                ciepleBezDeszczu++;
            else
                ciepleZDeszczem++;
        }

        System.out.println(chlodne + " " + ciepleBezDeszczu + " " + ciepleZDeszczem);
    }
}
```

**Odpowiedź:** 88 dni (temperatura ≤ 15°C), 73 dni (temperatura > 15°C i opady ≤ 0,6), 22 dni (temperatura > 15°C i opady > 0,6)

## 5.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `pogoda.txt` i zasady pracy zbiornika jak w zadaniu 5.1.
>
> Podaj datę, kiedy pierwszy raz trzeba było dolać wodę do zbiornika, oraz ilość dolanej wody.

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC  # 31 marca o 21:00 zbiornik był pełen
dzien = date(2015, 4, 1)
dolewki = []  # (data, ile litrów dolano)

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            dolewki.append((dzien, POJEMNOSC - stan))
            stan = POJEMNOSC
        stan -= potrzeba
    dzien += timedelta(days=1)

print(dolewki[0])
print("razem dolano:", sum(ile for d, ile in dolewki))
```

```cpp
// C++23
#include <algorithm>
#include <chrono>
#include <cmath>
#include <fstream>
#include <print>
#include <string>
#include <utility>
#include <vector>

using namespace std::chrono;

// liczba z przecinkiem dziesiętnym, np. "12,5" -> 12.5
double na_liczbe(std::string tekst) {
    std::ranges::replace(tekst, ',', '.');
    return std::stod(tekst);
}

int main() {
    std::ifstream plik("pogoda.txt");
    std::string naglowek;
    std::getline(plik, naglowek);  // nagłówek
    std::vector<std::pair<double, double>> dane;
    std::string t, o;
    while (plik >> t >> o)
        dane.push_back({na_liczbe(t), na_liczbe(o)});

    const long long POJEMNOSC = 25000;
    long long stan = POJEMNOSC;  // 31 marca o 21:00 zbiornik był pełen
    sys_days dzien = year{2015} / 4 / 1;
    std::vector<std::pair<sys_days, long long>> dolewki;  // (data, ile litrów dolano)

    for (const auto& [temperatura, opady] : dane) {
        if (opady > 0)
            stan = std::min(POJEMNOSC, stan + (long long)std::ceil(700 * opady));
        else
            stan -= (long long)std::ceil(0.0003 * std::pow(temperatura, 1.5) * stan);
        if (temperatura > 15 && opady <= 0.6) {
            long long potrzeba = temperatura <= 30 ? 12000 : 24000;
            if (stan < potrzeba) {
                dolewki.push_back({dzien, POJEMNOSC - stan});
                stan = POJEMNOSC;
            }
            stan -= potrzeba;
        }
        dzien += days{1};
    }

    // wypisujemy tak jak Python: (datetime.date(2015, 5, 6), 13172)
    year_month_day pierwsza{dolewki[0].first};
    std::println("(datetime.date({}, {}, {}), {})", int(pierwsza.year()), unsigned(pierwsza.month()),
                 unsigned(pierwsza.day()), dolewki[0].second);
    long long razem = 0;
    for (const auto& [d, ile] : dolewki)
        razem += ile;
    std::println("razem dolano: {}", razem);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.util.ArrayList;

public class Zadanie {
    record Dolewka(LocalDate data, long ile) {}

    public static void main(String[] args) throws Exception {
        var linie = Files.readAllLines(Path.of("pogoda.txt"));
        var dane = new ArrayList<double[]>();
        for (String line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            if (line.isBlank())
                continue;
            String[] czesci = line.trim().split("\\s+");
            dane.add(new double[]{Double.parseDouble(czesci[0].replace(",", ".")),
                                  Double.parseDouble(czesci[1].replace(",", "."))});
        }

        final long POJEMNOSC = 25000;
        long stan = POJEMNOSC;  // 31 marca o 21:00 zbiornik był pełen
        var dzien = LocalDate.of(2015, 4, 1);
        var dolewki = new ArrayList<Dolewka>();  // (data, ile litrów dolano)

        for (double[] d : dane) {
            double temperatura = d[0], opady = d[1];
            if (opady > 0)
                stan = Math.min(POJEMNOSC, stan + (long) Math.ceil(700 * opady));
            else
                stan -= (long) Math.ceil(0.0003 * Math.pow(temperatura, 1.5) * stan);
            if (temperatura > 15 && opady <= 0.6) {
                long potrzeba = temperatura <= 30 ? 12000 : 24000;
                if (stan < potrzeba) {
                    dolewki.add(new Dolewka(dzien, POJEMNOSC - stan));
                    stan = POJEMNOSC;
                }
                stan -= potrzeba;
            }
            dzien = dzien.plusDays(1);
        }

        // wypisujemy tak jak Python: (datetime.date(2015, 5, 6), 13172)
        var pierwsza = dolewki.get(0);
        System.out.println("(datetime.date(" + pierwsza.data().getYear() + ", " + pierwsza.data().getMonthValue()
                + ", " + pierwsza.data().getDayOfMonth() + "), " + pierwsza.ile() + ")");
        long razem = 0;
        for (var d : dolewki)
            razem += d.ile();
        System.out.println("razem dolano: " + razem);
    }
}
```

**Odpowiedź:** 6 maja 2015 r., 13172 litrów (łącznie dolano 743 427 litrów)

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `pogoda.txt` i zasady pracy zbiornika jak w zadaniu 5.1.
>
> Wykonaj wykres liniowy ilości wody w zbiorniku od 1 kwietnia do 30 września 2015 r., przyjmując jako stan dnia wartość o 21:00 (po podlaniu). Wykres powinien mieć tytuł i opisy osi.

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC
dzien = date(2015, 4, 1)

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            stan = POJEMNOSC
        stan -= potrzeba
    print(dzien, stan)  # stan o 21:00 - dane do wykresu liniowego
    dzien += timedelta(days=1)
```

```cpp
// C++23
#include <algorithm>
#include <chrono>
#include <cmath>
#include <fstream>
#include <print>
#include <string>
#include <utility>
#include <vector>

using namespace std::chrono;

// liczba z przecinkiem dziesiętnym, np. "12,5" -> 12.5
double na_liczbe(std::string tekst) {
    std::ranges::replace(tekst, ',', '.');
    return std::stod(tekst);
}

int main() {
    std::ifstream plik("pogoda.txt");
    std::string naglowek;
    std::getline(plik, naglowek);
    std::vector<std::pair<double, double>> dane;
    std::string t, o;
    while (plik >> t >> o)
        dane.push_back({na_liczbe(t), na_liczbe(o)});

    const long long POJEMNOSC = 25000;
    long long stan = POJEMNOSC;
    sys_days dzien = year{2015} / 4 / 1;

    for (const auto& [temperatura, opady] : dane) {
        if (opady > 0)
            stan = std::min(POJEMNOSC, stan + (long long)std::ceil(700 * opady));
        else
            stan -= (long long)std::ceil(0.0003 * std::pow(temperatura, 1.5) * stan);
        if (temperatura > 15 && opady <= 0.6) {
            long long potrzeba = temperatura <= 30 ? 12000 : 24000;
            if (stan < potrzeba)
                stan = POJEMNOSC;
            stan -= potrzeba;
        }
        std::println("{} {}", year_month_day{dzien}, stan);  // stan o 21:00 - dane do wykresu liniowego
        dzien += days{1};
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.util.ArrayList;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var linie = Files.readAllLines(Path.of("pogoda.txt"));
        var dane = new ArrayList<double[]>();
        for (String line : linie.subList(1, linie.size())) {
            if (line.isBlank())
                continue;
            String[] czesci = line.trim().split("\\s+");
            dane.add(new double[]{Double.parseDouble(czesci[0].replace(",", ".")),
                                  Double.parseDouble(czesci[1].replace(",", "."))});
        }

        final long POJEMNOSC = 25000;
        long stan = POJEMNOSC;
        var dzien = LocalDate.of(2015, 4, 1);

        for (double[] d : dane) {
            double temperatura = d[0], opady = d[1];
            if (opady > 0)
                stan = Math.min(POJEMNOSC, stan + (long) Math.ceil(700 * opady));
            else
                stan -= (long) Math.ceil(0.0003 * Math.pow(temperatura, 1.5) * stan);
            if (temperatura > 15 && opady <= 0.6) {
                long potrzeba = temperatura <= 30 ? 12000 : 24000;
                if (stan < potrzeba)
                    stan = POJEMNOSC;
                stan -= potrzeba;
            }
            System.out.println(dzien + " " + stan);  // stan o 21:00 - dane do wykresu liniowego
            dzien = dzien.plusDays(1);
        }
    }
}
```

**Odpowiedź:** wykres liniowy stanu zbiornika o 21:00 w kolejnych dniach (od 2015-04-01 do 2015-09-30)

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `pogoda.txt` i zasady pracy zbiornika jak w zadaniu 5.1.
>
> Zestaw miesięczne (kwiecień–wrzesień 2015) koszty wody dolanej z wodociągu. 1 m³ (1000 l) kosztuje 11,74 zł; opłaty są miesięczne i naliczane za pełne m³ (zaokrąglenie w górę).

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC
dzien = date(2015, 4, 1)
dolano = {miesiac: 0 for miesiac in range(4, 10)}

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            dolano[dzien.month] += POJEMNOSC - stan
            stan = POJEMNOSC
        stan -= potrzeba
    dzien += timedelta(days=1)

for miesiac, litry in dolano.items():
    m3 = math.ceil(litry / 1000)
    print(miesiac, litry, m3, round(m3 * 11.74, 2))
```

```cpp
// C++23
#include <algorithm>
#include <chrono>
#include <cmath>
#include <format>
#include <fstream>
#include <map>
#include <print>
#include <string>
#include <utility>
#include <vector>

using namespace std::chrono;

// liczba z przecinkiem dziesiętnym, np. "12,5" -> 12.5
double na_liczbe(std::string tekst) {
    std::ranges::replace(tekst, ',', '.');
    return std::stod(tekst);
}

// round(x, 2) z Pythona: zaokrąglenie do 2 miejsc po przecinku
double zaokraglij(double x) {
    return std::stod(std::format("{:.2f}", x));
}

// liczba rzeczywista wypisana jak w Pythonie (np. 0.0 zamiast 0)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find_first_of(".en") == std::string::npos)
        s += ".0";
    return s;
}

int main() {
    std::ifstream plik("pogoda.txt");
    std::string naglowek;
    std::getline(plik, naglowek);
    std::vector<std::pair<double, double>> dane;
    std::string t, o;
    while (plik >> t >> o)
        dane.push_back({na_liczbe(t), na_liczbe(o)});

    const long long POJEMNOSC = 25000;
    long long stan = POJEMNOSC;
    sys_days dzien = year{2015} / 4 / 1;
    std::map<unsigned, long long> dolano;
    for (unsigned miesiac = 4; miesiac < 10; miesiac++)
        dolano[miesiac] = 0;

    for (const auto& [temperatura, opady] : dane) {
        if (opady > 0)
            stan = std::min(POJEMNOSC, stan + (long long)std::ceil(700 * opady));
        else
            stan -= (long long)std::ceil(0.0003 * std::pow(temperatura, 1.5) * stan);
        if (temperatura > 15 && opady <= 0.6) {
            long long potrzeba = temperatura <= 30 ? 12000 : 24000;
            if (stan < potrzeba) {
                dolano[unsigned(year_month_day{dzien}.month())] += POJEMNOSC - stan;
                stan = POJEMNOSC;
            }
            stan -= potrzeba;
        }
        dzien += days{1};
    }

    for (const auto& [miesiac, litry] : dolano) {
        long long m3 = (long long)std::ceil(litry / 1000.0);
        std::println("{} {} {} {}", miesiac, litry, m3, jak_python(zaokraglij(m3 * 11.74)));
    }
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.TreeMap;

public class Zadanie {
    // round(x, 2) z Pythona: zaokrąglenie do 2 miejsc po przecinku
    static double zaokraglij(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).doubleValue();
    }

    public static void main(String[] args) throws Exception {
        var linie = Files.readAllLines(Path.of("pogoda.txt"));
        var dane = new ArrayList<double[]>();
        for (String line : linie.subList(1, linie.size())) {
            if (line.isBlank())
                continue;
            String[] czesci = line.trim().split("\\s+");
            dane.add(new double[]{Double.parseDouble(czesci[0].replace(",", ".")),
                                  Double.parseDouble(czesci[1].replace(",", "."))});
        }

        final long POJEMNOSC = 25000;
        long stan = POJEMNOSC;
        var dzien = LocalDate.of(2015, 4, 1);
        var dolano = new TreeMap<Integer, Long>();
        for (int miesiac = 4; miesiac < 10; miesiac++)
            dolano.put(miesiac, 0L);

        for (double[] d : dane) {
            double temperatura = d[0], opady = d[1];
            if (opady > 0)
                stan = Math.min(POJEMNOSC, stan + (long) Math.ceil(700 * opady));
            else
                stan -= (long) Math.ceil(0.0003 * Math.pow(temperatura, 1.5) * stan);
            if (temperatura > 15 && opady <= 0.6) {
                long potrzeba = temperatura <= 30 ? 12000 : 24000;
                if (stan < potrzeba) {
                    dolano.merge(dzien.getMonthValue(), POJEMNOSC - stan, Long::sum);
                    stan = POJEMNOSC;
                }
                stan -= potrzeba;
            }
            dzien = dzien.plusDays(1);
        }

        for (var e : dolano.entrySet()) {
            long litry = e.getValue();
            long m3 = (long) Math.ceil(litry / 1000.0);
            System.out.println(e.getKey() + " " + litry + " " + m3 + " " + zaokraglij(m3 * 11.74));
        }
    }
}
```

**Odpowiedź:** kwiecień 0 zł, maj 164,36 zł, czerwiec 1056,60 zł, lipiec 2559,32 zł, sierpień 3651,14 zł, wrzesień 1326,62 zł
