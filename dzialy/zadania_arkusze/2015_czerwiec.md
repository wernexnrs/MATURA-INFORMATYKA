<h1 align="center">Matura 2015 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1

> **Treść zadania:** Zadanie 1. Kod uzupełnień do dwóch (U2). W `n`-bitowym kodzie U2 zapis `(a[n−1] … a1 a0)` oznacza liczbę `−a[n−1]·2^(n−1) + a[n−2]·2^(n−2) + … + a1·2 + a0`, czyli najstarszy bit ma wagę ujemną; zakres to `[−2^(n−1), 2^(n−1) − 1]` (dla `n = 8`: od −128 do 127). Przykłady: `(01110101) = 117`, `(10101110) = −82`.
>
> Zapisz w 8-bitowym kodzie U2 liczby `93` i `−42` oraz wynik dodawania `(00101011)U2 + (10011011)U2` (też w 8-bitowym U2).

```py
def na_u2(liczba, n=8):
    # dla liczby ujemnej zapisujemy 2^n + liczba (bit znaku ma wagę -2^(n-1))
    if liczba < 0:
        liczba += 2 ** n
    return bin(liczba)[2:].zfill(n)


def z_u2(zapis):
    n = len(zapis)
    return -int(zapis[0]) * 2 ** (n - 1) + int(zapis[1:], 2)


print(na_u2(93), na_u2(-42))
print(na_u2(z_u2("00101011") + z_u2("10011011")))
```

```cpp
// C++23
#include <format>
#include <print>
#include <string>

std::string na_u2(int liczba, int n = 8) {
    // dla liczby ujemnej zapisujemy 2^n + liczba (bit znaku ma wagę -2^(n-1))
    if (liczba < 0) liczba += 1 << n;
    return std::format("{:0{}b}", liczba, n);  // zapis binarny uzupełniony zerami do n znaków
}

int z_u2(const std::string& zapis) {
    int n = zapis.size();
    return -(zapis[0] - '0') * (1 << (n - 1)) + std::stoi(zapis.substr(1), nullptr, 2);
}

int main() {
    std::println("{} {}", na_u2(93), na_u2(-42));
    std::println("{}", na_u2(z_u2("00101011") + z_u2("10011011")));
}
```

```java
// Java 25
public class Zadanie {
    static String naU2(int liczba, int n) {
        // dla liczby ujemnej zapisujemy 2^n + liczba (bit znaku ma wagę -2^(n-1))
        if (liczba < 0) liczba += 1 << n;
        String bin = Integer.toBinaryString(liczba);
        return "0".repeat(n - bin.length()) + bin;  // uzupełniamy zerami do n znaków
    }

    static String naU2(int liczba) {
        return naU2(liczba, 8);
    }

    static int zU2(String zapis) {
        int n = zapis.length();
        return -(zapis.charAt(0) - '0') * (1 << (n - 1)) + Integer.parseInt(zapis.substring(1), 2);
    }

    public static void main(String[] args) throws Exception {
        System.out.println(naU2(93) + " " + naU2(-42));
        System.out.println(naU2(zU2("00101011") + zU2("10011011")));
    }
}
```
**Odpowiedź:** 93 = (01011101)U2, -42 = (11010110)U2, suma = (11000110)U2

## 1.2

> **Treść zadania:** Kod U2 jak w zadaniu 1.1. Algorytm wyznacza zapis liczby przeciwnej `−x` dla `x` danego w `n`-bitowym U2 (`x ≠ 0`, `x ≠ −2^(n−1)`):
> ```
> i ← 0
> dopóki a[i] = 0: b[i] ← 0; i ← i + 1
> b[i] ← a[i]; i ← i + 1
> dopóki i < n: b[i] ← not(a[i]); i ← i + 1
> ```
>
> - podaj wynik algorytmu dla `n = 16` i `x = (1111001001110000)U2`,
> - podaj przykład 16-bitowej liczby U2, dla której pętla w kroku 2 nie wykona się ani razu,
> - podaj przykład 16-bitowej liczby U2, dla której pętla w kroku 5 wykona operację `not` dokładnie 7 razy.

```py
def przeciwna(a):
    # a - napis an-1 ... a1 a0, indeks i liczony od prawej (a0 to ostatni znak)
    n = len(a)
    b = ["0"] * n
    i = 0
    while a[n - 1 - i] == "0":       # krok 2
        b[n - 1 - i] = "0"
        i += 1
    b[n - 1 - i] = a[n - 1 - i]      # krok 3
    i += 1                           # krok 4
    while i < n:                     # krok 5
        if a[n - 1 - i] == "0":
            b[n - 1 - i] = "1"
        else:
            b[n - 1 - i] = "0"
        i += 1
    return "".join(b)


print(przeciwna("1111001001110000"))
# pętla z kroku 2 nie wykona się, gdy a0 = 1, np.:
print(przeciwna("0000000000000001"))
# 7 negacji w kroku 5: ostatnia jedynka na pozycji 8, czyli xxxxxxx100000000, np.:
print(przeciwna("0000000100000000"))
```

```cpp
// C++23
#include <print>
#include <string>

std::string przeciwna(const std::string& a) {
    // a - napis an-1 ... a1 a0, indeks i liczony od prawej (a0 to ostatni znak)
    int n = a.size();
    std::string b(n, '0');
    int i = 0;
    while (a[n - 1 - i] == '0') {  // krok 2
        b[n - 1 - i] = '0';
        i++;
    }
    b[n - 1 - i] = a[n - 1 - i];  // krok 3
    i++;                          // krok 4
    while (i < n) {               // krok 5
        if (a[n - 1 - i] == '0') b[n - 1 - i] = '1';
        else b[n - 1 - i] = '0';
        i++;
    }
    return b;
}

int main() {
    std::println("{}", przeciwna("1111001001110000"));
    // pętla z kroku 2 nie wykona się, gdy a0 = 1, np.:
    std::println("{}", przeciwna("0000000000000001"));
    // 7 negacji w kroku 5: ostatnia jedynka na pozycji 8, czyli xxxxxxx100000000, np.:
    std::println("{}", przeciwna("0000000100000000"));
}
```

```java
// Java 25
public class Zadanie {
    static String przeciwna(String a) {
        // a - napis an-1 ... a1 a0, indeks i liczony od prawej (a0 to ostatni znak)
        int n = a.length();
        char[] b = "0".repeat(n).toCharArray();
        int i = 0;
        while (a.charAt(n - 1 - i) == '0') {  // krok 2
            b[n - 1 - i] = '0';
            i++;
        }
        b[n - 1 - i] = a.charAt(n - 1 - i);  // krok 3
        i++;                                 // krok 4
        while (i < n) {                      // krok 5
            if (a.charAt(n - 1 - i) == '0') b[n - 1 - i] = '1';
            else b[n - 1 - i] = '0';
            i++;
        }
        return new String(b);
    }

    public static void main(String[] args) throws Exception {
        System.out.println(przeciwna("1111001001110000"));
        // pętla z kroku 2 nie wykona się, gdy a0 = 1, np.:
        System.out.println(przeciwna("0000000000000001"));
        // 7 negacji w kroku 5: ostatnia jedynka na pozycji 8, czyli xxxxxxx100000000, np.:
        System.out.println(przeciwna("0000000100000000"));
    }
}
```
**Odpowiedź:** 0000110110010000; brak obrotów pętli z kroku 2: dowolna liczba postaci xxxxxxxxxxxxxxx1; 7 negacji: xxxxxxx100000000

## 2.1

> **Treść zadania:** Zadanie 2. Triady. Trzy liczby dodatnie `a`, `b`, `c` tworzą triadę, jeśli istnieje trójkąt o bokach `a`, `b`, `c`.
>
> Uzupełnij warunki: dla `a ≤ b` liczby tworzą triadę wtedy i tylko wtedy, gdy `b − a < …` oraz `b + a > …`. Następnie podaj, które wartości `c` ze zbioru `C = {2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24}` tworzą triadę z `a = 5` i `b = 15`, oraz ile ich jest.

```py
a, b = 5, 15
C = [2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24]

# dla a <= b: a, b, c tworzą triadę <=> b - a < c < b + a
triady = []
for c in C:
    if b - a < c < b + a:
        triady.append(c)

print(triady)
print(len(triady))
```

```cpp
// C++23
#include <print>
#include <vector>

int main() {
    int a = 5, b = 15;
    std::vector<int> C = {2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24};

    // dla a <= b: a, b, c tworzą triadę <=> b - a < c < b + a
    std::vector<int> triady;
    for (int c : C) {
        if (b - a < c && c < b + a) triady.push_back(c);
    }

    std::println("{}", triady);
    std::println("{}", triady.size());
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int a = 5, b = 15;
        var C = List.of(2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24);

        // dla a <= b: a, b, c tworzą triadę <=> b - a < c < b + a
        var triady = new ArrayList<Integer>();
        for (int c : C) {
            if (b - a < c && c < b + a) triady.add(c);
        }

        System.out.println(triady);
        System.out.println(triady.size());
    }
}
```
**Odpowiedź:** b - a < c, b + a > c; 6 wartości: 11, 13, 14, 15, 17, 19

## 2.2

> **Treść zadania:** Triady jak w zadaniu 2.1. Zapisz algorytm, który dla ciągu `c1, c2, …, cn` (`n ≥ 2`, liczby dodatnie, bez powtórzeń, nieposortowane, przy czym `c1 < c2`) poda liczbę wszystkich triad postaci `c1, c2, ck`, gdzie `1 ≤ k ≤ n` (`k` może być równe 1 lub 2).

```py
def ile_triad(c):
    # c[0] < c[1]; c1, c2, ck tworzą triadę <=> c2 - c1 < ck < c2 + c1
    minimum = c[1] - c[0]
    maksimum = c[1] + c[0]
    licznik = 0
    for ck in c:
        if minimum < ck < maksimum:
            licznik += 1
    return licznik


print(ile_triad([5, 15, 2, 3, 6, 9, 10, 11, 13, 14, 17, 19, 20, 23, 24]))
```

```cpp
// C++23
#include <print>
#include <vector>

int ile_triad(const std::vector<int>& c) {
    // c[0] < c[1]; c1, c2, ck tworzą triadę <=> c2 - c1 < ck < c2 + c1
    int minimum = c[1] - c[0];
    int maksimum = c[1] + c[0];
    int licznik = 0;
    for (int ck : c) {
        if (minimum < ck && ck < maksimum) licznik++;
    }
    return licznik;
}

int main() {
    std::println("{}", ile_triad({5, 15, 2, 3, 6, 9, 10, 11, 13, 14, 17, 19, 20, 23, 24}));
}
```

```java
// Java 25
public class Zadanie {
    static int ileTriad(int[] c) {
        // c[0] < c[1]; c1, c2, ck tworzą triadę <=> c2 - c1 < ck < c2 + c1
        int minimum = c[1] - c[0];
        int maksimum = c[1] + c[0];
        int licznik = 0;
        for (int ck : c) {
            if (minimum < ck && ck < maksimum) licznik++;
        }
        return licznik;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(ileTriad(new int[]{5, 15, 2, 3, 6, 9, 10, 11, 13, 14, 17, 19, 20, 23, 24}));
    }
}
```
**Odpowiedź:** liczba elementów ck spełniających c2 - c1 < ck < c2 + c1 (dla przykładu z 2.1: 6)

## 4.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 4. Elektrociepłownia. W pliku `piastek.txt` każdy wiersz opisuje dostawę z jednego dnia sezonu grzewczego: trzy liczby rozdzielone tabulatorem — tony kostki, orzecha i miału (dzień bez dostawy to trzy zera). Ceny za tonę: kostka 685 zł, orzech 620 zł, miał 380 zł. Sezon trwa od 15.10.2014 do 15.04.2015; przed pierwszą dostawą w magazynie jest po 80 t każdego rodzaju. Dostawy przychodzą rano, potem ustala się, czym palić danego dnia (tylko jednym rodzajem): kostką, jeśli jest jej co najmniej 200 t (zużycie 200 t/dobę); w przeciwnym razie orzechem, jeśli jest go co najmniej 260 t (1,3 × 200); w przeciwnym razie miałem, jeśli jest go co najmniej 320 t (1,6 × 200); jeśli brakuje każdego — tylko podtrzymuje się ogień (pomijalne zużycie). Podpowiedź: w sezonie zużyto 9280 t miału. Odpowiedzi zapisz w pliku `wynik4.txt`, poprzedzając każdą numerem zadania.
>
> Dla każdego miesiąca od października do kwietnia podaj, ile ton każdego rodzaju węgla dostarczono. (W zadaniu 4.2 do tych danych tworzy się czytelny wykres kolumnowy z tytułem, legendą i opisem osi.)

```py
from datetime import date, timedelta

miesiace = {}  # (rok, miesiąc) -> [kostka, orzech, miał]
dzien = date(2014, 10, 15)

with open("piastek.txt") as file:
    for line in file:
        if not line.strip():
            continue
        dostawa = list(map(int, line.split()))
        klucz = (dzien.year, dzien.month)
        if klucz not in miesiace:
            miesiace[klucz] = [0, 0, 0]
        for i in range(3):
            miesiace[klucz][i] += dostawa[i]
        dzien += timedelta(days=1)

for (rok, miesiac), tony in miesiace.items():
    print(rok, miesiac, *tony)
```

```cpp
// C++23
#include <array>
#include <chrono>
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std::chrono;

int main() {
    std::map<std::pair<int, unsigned>, std::array<int, 3>> miesiace;  // (rok, miesiąc) -> [kostka, orzech, miał]
    std::vector<std::pair<int, unsigned>> kolejnosc;  // kolejność dodawania miesięcy
    sys_days dzien = 2014y / October / 15;

    std::ifstream plik("piastek.txt");
    std::string line;
    while (std::getline(plik, line)) {
        std::stringstream ss(line);
        std::array<int, 3> dostawa;
        if (!(ss >> dostawa[0] >> dostawa[1] >> dostawa[2])) continue;  // pusty wiersz
        year_month_day data{dzien};
        std::pair<int, unsigned> klucz = {int(data.year()), unsigned(data.month())};
        if (!miesiace.contains(klucz)) {
            miesiace[klucz] = {0, 0, 0};
            kolejnosc.push_back(klucz);
        }
        for (int i = 0; i < 3; i++) miesiace[klucz][i] += dostawa[i];
        dzien += days{1};
    }

    for (auto klucz : kolejnosc) {
        auto tony = miesiace[klucz];
        std::println("{} {} {} {} {}", klucz.first, klucz.second, tony[0], tony[1], tony[2]);
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.time.YearMonth;
import java.util.LinkedHashMap;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // (rok, miesiąc) -> [kostka, orzech, miał]; LinkedHashMap pamięta kolejność dodawania
        var miesiace = new LinkedHashMap<YearMonth, int[]>();
        var dzien = LocalDate.of(2014, 10, 15);

        for (String line : Files.readAllLines(Path.of("piastek.txt"))) {
            if (line.isBlank()) continue;
            String[] pola = line.strip().split("\\s+");
            var klucz = YearMonth.from(dzien);
            int[] tony = miesiace.computeIfAbsent(klucz, k -> new int[3]);
            for (int i = 0; i < 3; i++) tony[i] += Integer.parseInt(pola[i]);
            dzien = dzien.plusDays(1);
        }

        for (var wpis : miesiace.entrySet()) {
            int[] tony = wpis.getValue();
            System.out.println(wpis.getKey().getYear() + " " + wpis.getKey().getMonthValue() + " " + tony[0] + " "
                    + tony[1] + " " + tony[2]);
        }
    }
}
```
**Odpowiedź:** (kostka, orzech, miał) 10: 1742 1658 915, 11: 2756 2884 1750, 12: 2696 2749 1586, 1: 2990 2870 1646, 2: 2579 2651 1252, 3: 3332 3026 1360, 4: 1365 966 706

## 4.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dostawy z pliku `piastek.txt` i ceny węgla jak w zadaniu 4.1. Podaj łączną kwotę, jaką elektrociepłownia zapłaci za węgiel z Kopalni Piastek.

```py
ceny = [685, 620, 380]  # kostka, orzech, miał [zł/t]
koszt = 0

with open("piastek.txt") as file:
    for line in file:
        dostawa = list(map(int, line.split()))
        for i in range(len(dostawa)):
            koszt += dostawa[i] * ceny[i]

print(koszt)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>

int main() {
    int ceny[] = {685, 620, 380};  // kostka, orzech, miał [zł/t]
    long long koszt = 0;

    std::ifstream plik("piastek.txt");
    std::string line;
    while (std::getline(plik, line)) {
        std::stringstream ss(line);
        int ilosc;
        int i = 0;
        while (ss >> ilosc) {
            koszt += (long long)ilosc * ceny[i];
            i++;
        }
    }
    std::println("{}", koszt);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int[] ceny = {685, 620, 380};  // kostka, orzech, miał [zł/t]
        long koszt = 0;

        for (String line : Files.readAllLines(Path.of("piastek.txt"))) {
            if (line.isBlank()) continue;
            String[] dostawa = line.strip().split("\\s+");
            for (int i = 0; i < dostawa.length; i++) {
                koszt += (long) Integer.parseInt(dostawa[i]) * ceny[i];
            }
        }
        System.out.println(koszt);
    }
}
```
**Odpowiedź:** 25 880 280 zł

## 4.4, 4.5 i 4.6

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Symulacja pracy elektrociepłowni (dane z `piastek.txt`, zasady wyboru paliwa) jak w zadaniu 4.1.
>
> - 4.4 — podaj, w ilu dniach palono odpowiednio kostką, orzechem i miałem.
> - 4.5 — podaj datę, kiedy po raz pierwszy palono miałem.
> - 4.6 — podaj, przez ile dni z powodu zbyt małych zapasów jedynie podtrzymywano ogień.

```py
from datetime import date, timedelta

dostawy = []
with open("piastek.txt") as file:
    for line in file:
        if line.strip():
            dostawy.append(list(map(int, line.split())))

spalanie = [200, 260, 320]      # dzienne zużycie: 200, 1,3 * 200, 1,6 * 200

magazyn = [80, 80, 80]
dni_palenia = [0, 0, 0]
podtrzymanie = 0
pierwszy_mial = None
dzien = date(2014, 10, 15)

for dostawa in dostawy:
    for i in range(3):
        magazyn[i] += dostawa[i]

    spalono = False
    for i in range(3):          # najpierw kostka, potem orzech, na końcu miał
        if magazyn[i] >= spalanie[i]:
            magazyn[i] -= spalanie[i]
            dni_palenia[i] += 1
            if i == 2 and pierwszy_mial is None:
                pierwszy_mial = dzien
            spalono = True
            break
    if not spalono:
        podtrzymanie += 1

    dzien += timedelta(days=1)

print("4.4", *dni_palenia)
print("4.5", pierwszy_mial)
print("4.6", podtrzymanie)
```

```cpp
// C++23
#include <array>
#include <chrono>
#include <fstream>
#include <optional>
#include <print>
#include <sstream>
#include <string>
#include <vector>
using namespace std::chrono;

int main() {
    std::vector<std::array<int, 3>> dostawy;
    std::ifstream plik("piastek.txt");
    std::string line;
    while (std::getline(plik, line)) {
        std::stringstream ss(line);
        std::array<int, 3> d;
        if (ss >> d[0] >> d[1] >> d[2]) dostawy.push_back(d);
    }

    int spalanie[] = {200, 260, 320};  // dzienne zużycie: 200, 1,3 * 200, 1,6 * 200

    int magazyn[] = {80, 80, 80};
    int dni_palenia[] = {0, 0, 0};
    int podtrzymanie = 0;
    std::optional<sys_days> pierwszy_mial;
    sys_days dzien = 2014y / October / 15;

    for (const auto& dostawa : dostawy) {
        for (int i = 0; i < 3; i++) magazyn[i] += dostawa[i];

        bool spalono = false;
        for (int i = 0; i < 3; i++) {  // najpierw kostka, potem orzech, na końcu miał
            if (magazyn[i] >= spalanie[i]) {
                magazyn[i] -= spalanie[i];
                dni_palenia[i]++;
                if (i == 2 && !pierwszy_mial) pierwszy_mial = dzien;
                spalono = true;
                break;
            }
        }
        if (!spalono) podtrzymanie++;

        dzien += days{1};
    }

    std::println("4.4 {} {} {}", dni_palenia[0], dni_palenia[1], dni_palenia[2]);
    if (pierwszy_mial) std::println("4.5 {}", year_month_day{*pierwszy_mial});
    else std::println("4.5 None");
    std::println("4.6 {}", podtrzymanie);
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
        var dostawy = new ArrayList<int[]>();
        for (String line : Files.readAllLines(Path.of("piastek.txt"))) {
            if (line.isBlank()) continue;
            String[] pola = line.strip().split("\\s+");
            dostawy.add(new int[]{Integer.parseInt(pola[0]), Integer.parseInt(pola[1]), Integer.parseInt(pola[2])});
        }

        int[] spalanie = {200, 260, 320};  // dzienne zużycie: 200, 1,3 * 200, 1,6 * 200

        int[] magazyn = {80, 80, 80};
        int[] dniPalenia = {0, 0, 0};
        int podtrzymanie = 0;
        LocalDate pierwszyMial = null;
        var dzien = LocalDate.of(2014, 10, 15);

        for (int[] dostawa : dostawy) {
            for (int i = 0; i < 3; i++) magazyn[i] += dostawa[i];

            boolean spalono = false;
            for (int i = 0; i < 3; i++) {  // najpierw kostka, potem orzech, na końcu miał
                if (magazyn[i] >= spalanie[i]) {
                    magazyn[i] -= spalanie[i];
                    dniPalenia[i]++;
                    if (i == 2 && pierwszyMial == null) pierwszyMial = dzien;
                    spalono = true;
                    break;
                }
            }
            if (!spalono) podtrzymanie++;

            dzien = dzien.plusDays(1);
        }

        System.out.println("4.4 " + dniPalenia[0] + " " + dniPalenia[1] + " " + dniPalenia[2]);
        System.out.println("4.5 " + (pierwszyMial == null ? "None" : pierwszyMial));
        System.out.println("4.6 " + podtrzymanie);
    }
}
```
**Odpowiedź:** 4.4: kostka 87, orzech 64, miał 29 dni; 4.5: 2014-10-18; 4.6: 3 dni

## 6.1

> **Treść zadania:** Zadanie 6. Kody kreskowe. W Standard Code 25 napis składa się z: znaku START `11011010`, kodów kolejnych cyfr liczby (tabela w pliku `cyfra_kodkreskowy.txt`, np. `0 → 10101110111010`, `1 → 11101010101110`), kodu cyfry kontrolnej i znaku STOP `11010110`. Cyfrę kontrolną liczymy tak: numerujemy pozycje od cyfry jedności (pozycja 0); sumujemy cyfry z pozycji parzystych i z nieparzystych; potrojoną pierwszą sumę dodajemy do drugiej; wynik bierzemy mod 10, odejmujemy od 10 i znów bierzemy mod 10. Przykład: dla `764321`: `(1+3+6)·3 + (2+4+7) = 43`, `(10 − 3) mod 10 = 7`. W pliku `kody.txt` jest 500 liczb sześciocyfrowych, po jednej w wierszu; wyniki zapisuj w wierszach odpowiadających kolejnym liczbom.
>
> Do pliku `kody1.txt` zapisz dla każdej liczby dwie liczby oddzielone spacją: sumę cyfr z pozycji parzystych i sumę cyfr z pozycji nieparzystych.

```py
def sumy(liczba):
    # pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    parzyste = nieparzyste = 0
    for pozycja, cyfra in enumerate(reversed(liczba)):
        if pozycja % 2 == 0:
            parzyste += int(cyfra)
        else:
            nieparzyste += int(cyfra)
    return parzyste, nieparzyste


with open("kody.txt") as file, open("kody1.txt", "w") as wynik:
    for line in file:
        parzyste, nieparzyste = sumy(line.strip())
        wynik.write(f"{parzyste} {nieparzyste}\n")
```

```cpp
// C++23
#include <fstream>
#include <string>
#include <utility>

std::pair<int, int> sumy(const std::string& liczba) {
    // pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    int parzyste = 0, nieparzyste = 0;
    int n = liczba.size();
    for (int pozycja = 0; pozycja < n; pozycja++) {
        int cyfra = liczba[n - 1 - pozycja] - '0';
        if (pozycja % 2 == 0) parzyste += cyfra;
        else nieparzyste += cyfra;
    }
    return {parzyste, nieparzyste};
}

int main() {
    std::ifstream plik("kody.txt");
    std::ofstream wynik("kody1.txt");
    std::string liczba;
    while (plik >> liczba) {
        auto [parzyste, nieparzyste] = sumy(liczba);
        wynik << parzyste << " " << nieparzyste << "\n";
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static int[] sumy(String liczba) {
        // pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
        int parzyste = 0, nieparzyste = 0;
        int n = liczba.length();
        for (int pozycja = 0; pozycja < n; pozycja++) {
            int cyfra = liczba.charAt(n - 1 - pozycja) - '0';
            if (pozycja % 2 == 0) parzyste += cyfra;
            else nieparzyste += cyfra;
        }
        return new int[]{parzyste, nieparzyste};
    }

    public static void main(String[] args) throws Exception {
        try (var wynik = new PrintWriter("kody1.txt")) {
            for (String line : Files.readAllLines(Path.of("kody.txt"))) {
                int[] s = sumy(line.strip());
                wynik.print(s[0] + " " + s[1] + "\n");
            }
        }
    }
}
```
**Odpowiedź:** plik kody1.txt (pierwsze wiersze: 10 13, 11 17, 17 16, …)

## 6.2

> **Treść zadania:** Liczby z pliku `kody.txt` i zasady Standard Code 25 jak w zadaniu 6.1. Do pliku `kody2.txt` zapisz dla każdej liczby jej cyfrę kontrolną, a po spacji — kod kreskowy tej cyfry.

```py
kody = {}
with open("cyfra_kodkreskowy.txt") as file:
    next(file)
    for line in file:
        cyfra, kod = line.split()
        kody[cyfra] = kod


def sumy(liczba):
    # pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    parzyste = nieparzyste = 0
    for pozycja, cyfra in enumerate(reversed(liczba)):
        if pozycja % 2 == 0:
            parzyste += int(cyfra)
        else:
            nieparzyste += int(cyfra)
    return parzyste, nieparzyste


def cyfra_kontrolna(liczba):
    parzyste, nieparzyste = sumy(liczba)
    return str((10 - (3 * parzyste + nieparzyste) % 10) % 10)


with open("kody.txt") as file, open("kody2.txt", "w") as wynik:
    for line in file:
        k = cyfra_kontrolna(line.strip())
        wynik.write(f"{k} {kody[k]}\n")
```

```cpp
// C++23
#include <fstream>
#include <map>
#include <string>
#include <utility>

std::map<std::string, std::string> kody;

std::pair<int, int> sumy(const std::string& liczba) {
    // pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    int parzyste = 0, nieparzyste = 0;
    int n = liczba.size();
    for (int pozycja = 0; pozycja < n; pozycja++) {
        int cyfra = liczba[n - 1 - pozycja] - '0';
        if (pozycja % 2 == 0) parzyste += cyfra;
        else nieparzyste += cyfra;
    }
    return {parzyste, nieparzyste};
}

std::string cyfra_kontrolna(const std::string& liczba) {
    auto [parzyste, nieparzyste] = sumy(liczba);
    return std::to_string((10 - (3 * parzyste + nieparzyste) % 10) % 10);
}

int main() {
    std::ifstream tabela("cyfra_kodkreskowy.txt");
    std::string naglowek, cyfra, kod;
    std::getline(tabela, naglowek);  // pomijamy nagłówek
    while (tabela >> cyfra >> kod) kody[cyfra] = kod;

    std::ifstream plik("kody.txt");
    std::ofstream wynik("kody2.txt");
    std::string liczba;
    while (plik >> liczba) {
        std::string k = cyfra_kontrolna(liczba);
        wynik << k << " " << kody[k] << "\n";
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;

public class Zadanie {
    static Map<String, String> kody = new HashMap<>();

    static int[] sumy(String liczba) {
        // pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
        int parzyste = 0, nieparzyste = 0;
        int n = liczba.length();
        for (int pozycja = 0; pozycja < n; pozycja++) {
            int cyfra = liczba.charAt(n - 1 - pozycja) - '0';
            if (pozycja % 2 == 0) parzyste += cyfra;
            else nieparzyste += cyfra;
        }
        return new int[]{parzyste, nieparzyste};
    }

    static String cyfraKontrolna(String liczba) {
        int[] s = sumy(liczba);
        return Integer.toString((10 - (3 * s[0] + s[1]) % 10) % 10);
    }

    public static void main(String[] args) throws Exception {
        var tabela = Files.readAllLines(Path.of("cyfra_kodkreskowy.txt"));
        for (String line : tabela.subList(1, tabela.size())) {  // pomijamy nagłówek
            String[] pola = line.strip().split("\\s+");
            kody.put(pola[0], pola[1]);
        }

        try (var wynik = new PrintWriter("kody2.txt")) {
            for (String line : Files.readAllLines(Path.of("kody.txt"))) {
                String k = cyfraKontrolna(line.strip());
                wynik.print(k + " " + kody.get(k) + "\n");
            }
        }
    }
}
```
**Odpowiedź:** plik kody2.txt (pierwsze wiersze: 7 10101011101110, 0 10101110111010, 3 11101110101010, …)

## 6.3

> **Treść zadania:** Liczby z pliku `kody.txt` i zasady Standard Code 25 jak w zadaniu 6.1. Do pliku `kody3.txt` zapisz dla każdej liczby jej pełny kod w Standard Code 25 (START, kody cyfr, kod cyfry kontrolnej, STOP) jako jeden ciąg zer i jedynek bez spacji. Każdy plik wynikowy ma mieć 500 wierszy.

```py
kody = {}
with open("cyfra_kodkreskowy.txt") as file:
    next(file)
    for line in file:
        cyfra, kod = line.split()
        kody[cyfra] = kod


def sumy(liczba):
    # pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    parzyste = nieparzyste = 0
    for pozycja, cyfra in enumerate(reversed(liczba)):
        if pozycja % 2 == 0:
            parzyste += int(cyfra)
        else:
            nieparzyste += int(cyfra)
    return parzyste, nieparzyste


def cyfra_kontrolna(liczba):
    parzyste, nieparzyste = sumy(liczba)
    return str((10 - (3 * parzyste + nieparzyste) % 10) % 10)


with open("kody.txt") as file, open("kody3.txt", "w") as wynik:
    for line in file:
        liczba = line.strip()
        kod = "11011010"                                   # START
        for cyfra in liczba:
            kod += kody[cyfra]
        kod += kody[cyfra_kontrolna(liczba)] + "11010110"  # cyfra kontrolna i STOP
        wynik.write(kod + "\n")
```

```cpp
// C++23
#include <fstream>
#include <map>
#include <string>
#include <utility>

std::map<char, std::string> kody;

std::pair<int, int> sumy(const std::string& liczba) {
    // pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    int parzyste = 0, nieparzyste = 0;
    int n = liczba.size();
    for (int pozycja = 0; pozycja < n; pozycja++) {
        int cyfra = liczba[n - 1 - pozycja] - '0';
        if (pozycja % 2 == 0) parzyste += cyfra;
        else nieparzyste += cyfra;
    }
    return {parzyste, nieparzyste};
}

char cyfra_kontrolna(const std::string& liczba) {
    auto [parzyste, nieparzyste] = sumy(liczba);
    return '0' + (10 - (3 * parzyste + nieparzyste) % 10) % 10;
}

int main() {
    std::ifstream tabela("cyfra_kodkreskowy.txt");
    std::string naglowek, cyfra, kod;
    std::getline(tabela, naglowek);  // pomijamy nagłówek
    while (tabela >> cyfra >> kod) kody[cyfra[0]] = kod;

    std::ifstream plik("kody.txt");
    std::ofstream wynik("kody3.txt");
    std::string liczba;
    while (plik >> liczba) {
        std::string kod_liczby = "11011010";  // START
        for (char c : liczba) kod_liczby += kody[c];
        kod_liczby += kody[cyfra_kontrolna(liczba)] + "11010110";  // cyfra kontrolna i STOP
        wynik << kod_liczby << "\n";
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;

public class Zadanie {
    static Map<String, String> kody = new HashMap<>();

    static int[] sumy(String liczba) {
        // pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
        int parzyste = 0, nieparzyste = 0;
        int n = liczba.length();
        for (int pozycja = 0; pozycja < n; pozycja++) {
            int cyfra = liczba.charAt(n - 1 - pozycja) - '0';
            if (pozycja % 2 == 0) parzyste += cyfra;
            else nieparzyste += cyfra;
        }
        return new int[]{parzyste, nieparzyste};
    }

    static String cyfraKontrolna(String liczba) {
        int[] s = sumy(liczba);
        return Integer.toString((10 - (3 * s[0] + s[1]) % 10) % 10);
    }

    public static void main(String[] args) throws Exception {
        var tabela = Files.readAllLines(Path.of("cyfra_kodkreskowy.txt"));
        for (String line : tabela.subList(1, tabela.size())) {  // pomijamy nagłówek
            String[] pola = line.strip().split("\\s+");
            kody.put(pola[0], pola[1]);
        }

        try (var wynik = new PrintWriter("kody3.txt")) {
            for (String line : Files.readAllLines(Path.of("kody.txt"))) {
                String liczba = line.strip();
                var kod = new StringBuilder("11011010");  // START
                for (char cyfra : liczba.toCharArray()) kod.append(kody.get(String.valueOf(cyfra)));
                kod.append(kody.get(cyfraKontrolna(liczba))).append("11010110");  // cyfra kontrolna i STOP
                wynik.print(kod + "\n");
            }
        }
    }
}
```
**Odpowiedź:** plik kody3.txt (pierwszy wiersz to kod liczby 764321, taki jak w przykładzie z treści zadania)
