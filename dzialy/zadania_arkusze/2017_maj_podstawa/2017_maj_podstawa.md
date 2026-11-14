<h1 align="center">Matura 2017 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa-odpowiedzi.pdf)

## 1.1

> **Treść zadania:** Zadanie 1. Szyfrowanie. Dane: długość tekstu `d > 1`, tekst jawny `s[1..d]` oraz liczby całkowite dodatnie `k < d` i `n < d`. Wynik: zaszyfrowany tekst `szyfr[1..d]`. Algorytm (`↔` oznacza zamianę znaków miejscami):
>
> ```
> od j=1 do d: szyfr[j] ← s[j]
> i ← 1
> dopóki i ≤ d − k
>     szyfr[i] ↔ szyfr[i+k]
>     i ← i+n
> ```
>
> Podaj szyfr dla danych: `ataknadranem` (d=12, k=4, n=2), `maturazinformatyki` (d=18, k=3, n=5), `stokrotka` (d=9, k=1, n=2).

```py
def szyfruj(s, k, n):
    d = len(s)
    szyfr = list(s)
    i = 1  # numeracja od 1 jak w treści
    while i <= d - k:
        szyfr[i - 1], szyfr[i + k - 1] = szyfr[i + k - 1], szyfr[i - 1]
        i = i + n
    return "".join(szyfr)


print(szyfruj("ataknadranem", 4, 2))
print(szyfruj("maturazinformatyki", 3, 5))
print(szyfruj("stokrotka", 1, 2))
```

```cpp
// C++23
#include <print>
#include <string>
#include <utility>

std::string szyfruj(std::string s, int k, int n) {
    int d = s.size();
    std::string szyfr = s;
    int i = 1;  // numeracja od 1 jak w treści
    while (i <= d - k) {
        std::swap(szyfr[i - 1], szyfr[i + k - 1]);
        i = i + n;
    }
    return szyfr;
}

int main() {
    std::println("{}", szyfruj("ataknadranem", 4, 2));
    std::println("{}", szyfruj("maturazinformatyki", 3, 5));
    std::println("{}", szyfruj("stokrotka", 1, 2));
}
```

```java
// Java 25
public class Zadanie {
    static String szyfruj(String s, int k, int n) {
        int d = s.length();
        char[] szyfr = s.toCharArray();
        int i = 1;  // numeracja od 1 jak w treści
        while (i <= d - k) {
            char pom = szyfr[i - 1];
            szyfr[i - 1] = szyfr[i + k - 1];
            szyfr[i + k - 1] = pom;
            i = i + n;
        }
        return new String(szyfr);
    }

    public static void main(String[] args) {
        System.out.println(szyfruj("ataknadranem", 4, 2));
        System.out.println(szyfruj("maturazinformatyki", 3, 5));
        System.out.println(szyfruj("stokrotka", 1, 2));
    }
}
```
**Odpowiedź:** ntdkaaeranam, uatmrnziafarmotyki, tskoorkta

## 1.2 i 1.3

> **Treść zadania:** Dotyczy algorytmu szyfrującego z zadania 1 (kopiuje `s` do `szyfr`, a potem dla `i = 1, 1+n, 1+2n, …` dopóki `i ≤ d−k` zamienia `szyfr[i] ↔ szyfr[i+k]`).
>
> - 1.2 — Odszyfruj tekst `eiindaezotinwezssyktpo` (d=22, k=2, n=2).
> - 1.3 — Uzupełnij algorytm deszyfrujący (dane: `d`, `szyfr[1..d]`, `k`, `n`; wynik: tekst jawny `s[1..d]`); wolno używać operacji arytmetycznych, zamiany `↔` i własnych funkcji:
>
> ```
> od j=1 do d: s[j] ← szyfr[j]
> i ← 1
> dopóki ..........
>     i ← i+n
> dopóki i ≥ 1
>     s[i] ↔ s[i+k]
>     ..........
> ```

```py
def odszyfruj(szyfr, k, n):
    d = len(szyfr)
    s = list(szyfr)
    i = 1
    while i <= d - k - n:  # szukamy ostatniej zamiany wykonanej przy szyfrowaniu
        i = i + n
    while i >= 1:  # wykonujemy zamiany w odwrotnej kolejności
        s[i - 1], s[i + k - 1] = s[i + k - 1], s[i - 1]
        i = i - n
    return "".join(s)


print(odszyfruj("eiindaezotinwezssyktpo", 2, 2))
```

```cpp
// C++23
#include <print>
#include <string>
#include <utility>

std::string odszyfruj(std::string szyfr, int k, int n) {
    int d = szyfr.size();
    std::string s = szyfr;
    int i = 1;
    while (i <= d - k - n)  // szukamy ostatniej zamiany wykonanej przy szyfrowaniu
        i = i + n;
    while (i >= 1) {  // wykonujemy zamiany w odwrotnej kolejności
        std::swap(s[i - 1], s[i + k - 1]);
        i = i - n;
    }
    return s;
}

int main() {
    std::println("{}", odszyfruj("eiindaezotinwezssyktpo", 2, 2));
}
```

```java
// Java 25
public class Zadanie {
    static String odszyfruj(String szyfr, int k, int n) {
        int d = szyfr.length();
        char[] s = szyfr.toCharArray();
        int i = 1;
        while (i <= d - k - n)  // szukamy ostatniej zamiany wykonanej przy szyfrowaniu
            i = i + n;
        while (i >= 1) {  // wykonujemy zamiany w odwrotnej kolejności
            char pom = s[i - 1];
            s[i - 1] = s[i + k - 1];
            s[i + k - 1] = pom;
            i = i - n;
        }
        return new String(s);
    }

    public static void main(String[] args) {
        System.out.println(odszyfruj("eiindaezotinwezssyktpo", 2, 2));
    }
}
```
**Odpowiedź:** pieniadzetoniewszystko; luki: dopóki i ≤ d − k − n, i ← i − n

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2. Liczby pierwsze. Parą liczb bliźniaczych nazywamy dwie liczby pierwsze różniące się o 2 (np. 11 i 13; para 13 i 15 nie jest bliźniacza, bo 15 jest złożona).
>
> - 2.1 — Dla `a` = 31, 41, 49 uzupełnij tabelę: czy `a` jest pierwsza, czy `a+2` jest pierwsza, czy `a−2` jest pierwsza i czy `a` należy do pary liczb bliźniaczych (np. dla 17: tak, 19 — tak, 15 — nie, odpowiedź TAK).
> - 2.2 — Zapisz algorytm, który dla liczby całkowitej `a ≥ 3` wypisuje `TAK`, jeśli `a` należy do pary liczb bliźniaczych, a `NIE` w przeciwnym razie. Wolno używać tylko podstawowych operacji arytmetycznych (w tym dzielenia całkowitego i reszty), operacji logicznych i własnych funkcji.

```py
def pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True


def blizniacze(a):
    if pierwsza(a) and (pierwsza(a - 2) or pierwsza(a + 2)):
        return "TAK"
    return "NIE"


for a in [17, 5, 31, 41, 49]:
    print(a, pierwsza(a), pierwsza(a + 2), pierwsza(a - 2), blizniacze(a))
```

```cpp
// C++23
#include <print>
#include <string>

bool pierwsza(int x) {
    if (x < 2)
        return false;
    int i = 2;
    while (i * i <= x) {
        if (x % i == 0)
            return false;
        i = i + 1;
    }
    return true;
}

std::string blizniacze(int a) {
    if (pierwsza(a) && (pierwsza(a - 2) || pierwsza(a + 2)))
        return "TAK";
    return "NIE";
}

// wartość logiczna zapisana jak w Pythonie
std::string py(bool b) {
    return b ? "True" : "False";
}

int main() {
    for (int a : {17, 5, 31, 41, 49})
        std::println("{} {} {} {} {}", a, py(pierwsza(a)), py(pierwsza(a + 2)), py(pierwsza(a - 2)), blizniacze(a));
}
```

```java
// Java 25
public class Zadanie {
    static boolean pierwsza(int x) {
        if (x < 2)
            return false;
        int i = 2;
        while (i * i <= x) {
            if (x % i == 0)
                return false;
            i = i + 1;
        }
        return true;
    }

    static String blizniacze(int a) {
        if (pierwsza(a) && (pierwsza(a - 2) || pierwsza(a + 2)))
            return "TAK";
        return "NIE";
    }

    // wartość logiczna zapisana jak w Pythonie
    static String py(boolean b) {
        return b ? "True" : "False";
    }

    public static void main(String[] args) {
        for (int a : new int[]{17, 5, 31, 41, 49})
            System.out.println(a + " " + py(pierwsza(a)) + " " + py(pierwsza(a + 2)) + " "
                    + py(pierwsza(a - 2)) + " " + blizniacze(a));
    }
}
```
**Odpowiedź:** 31 → TAK (29), 41 → TAK (43), 49 → NIE

## 4.1

> **Treść zadania:** Zadanie 4. Trójki liczb. Plik `liczby.txt` zawiera 1000 wierszy, w każdym trzy liczby całkowite z przedziału [1, 32 767] oddzielone spacjami. Odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając je numerami zadań.
>
> Podaj, w ilu wierszach liczby są uporządkowane rosnąco. Przykład: dla wierszy `4587 9351 28950`, `15010 28342 31848`, `30172 7492 6768`, `29120 21664 32328` odpowiedzią jest 2.

```py
count = 0

with open("liczby.txt") as file:
    for line in file:
        a, b, c = map(int, line.split())
        if a < b < c:
            count += 1

print(count)
```

```cpp
// C++23
#include <fstream>
#include <print>

int main() {
    int count = 0;

    std::ifstream plik("liczby.txt");
    long long a, b, c;
    while (plik >> a >> b >> c)
        if (a < b && b < c)
            count++;

    std::println("{}", count);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int count = 0;

        for (String linia : Files.readAllLines(Path.of("liczby.txt"))) {
            String[] pola = linia.trim().split("\\s+");
            long a = Long.parseLong(pola[0]), b = Long.parseLong(pola[1]), c = Long.parseLong(pola[2]);
            if (a < b && b < c)
                count++;
        }

        System.out.println(count);
    }
}
```
**Odpowiedź:** 139

## 4.2

> **Treść zadania:** Dla każdego wiersza pliku `liczby.txt` (1000 trójek liczb z [1, 32 767]) wyznacz NWD trzech zapisanych w nim liczb i podaj sumę tych NWD. Przykład: dla wierszy `3 6 9`, `34 10 4`, `36 20 28`, `16 40 56` wynik to 3+2+4+8 = 17. Wynik zapisz w `wyniki4.txt`.

```py
def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


suma = 0

with open("liczby.txt") as file:
    for line in file:
        a, b, c = map(int, line.split())
        suma += nwd(nwd(a, b), c)

print(suma)
```

```cpp
// C++23
#include <fstream>
#include <print>

long long nwd(long long a, long long b) {
    while (b > 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    long long suma = 0;

    std::ifstream plik("liczby.txt");
    long long a, b, c;
    while (plik >> a >> b >> c)
        suma += nwd(nwd(a, b), c);

    std::println("{}", suma);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static long nwd(long a, long b) {
        while (b > 0) {
            long r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public static void main(String[] args) throws Exception {
        long suma = 0;

        for (String linia : Files.readAllLines(Path.of("liczby.txt"))) {
            String[] pola = linia.trim().split("\\s+");
            long a = Long.parseLong(pola[0]), b = Long.parseLong(pola[1]), c = Long.parseLong(pola[2]);
            suma += nwd(nwd(a, b), c);
        }

        System.out.println(suma);
    }
}
```
**Odpowiedź:** 1404

## 4.3

> **Treść zadania:** Dla każdego wiersza pliku `liczby.txt` oblicz sumę cyfr wszystkich trzech liczb. Podaj:
> - liczbę wierszy, w których ta suma wynosi 35;
> - największą sumę cyfr w wierszu oraz liczbę wierszy, w których ona występuje.
>
> Przykład: dla wierszy `45 9151 2800`, `2882 15040 2800`, `30172 2592 1102`, `29121 23564 320`, `3 243 765` suma 35 występuje w dwóch wierszach, a maksymalna suma 40 — także w dwóch. Wynik zapisz w `wyniki4.txt`.

```py
sumy_cyfr = []

with open("liczby.txt") as file:
    for line in file:
        suma = 0
        for znak in line.strip():
            if znak != " ":
                suma += int(znak)
        sumy_cyfr.append(suma)

najwieksza = max(sumy_cyfr)
print(sumy_cyfr.count(35), najwieksza, sumy_cyfr.count(najwieksza))
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <vector>

int main() {
    std::vector<int> sumy_cyfr;

    std::ifstream plik("liczby.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        int suma = 0;
        for (char znak : linia)
            if (znak >= '0' && znak <= '9')  // pomijamy spacje i \r
                suma += znak - '0';
        sumy_cyfr.push_back(suma);
    }

    int najwieksza = *std::max_element(sumy_cyfr.begin(), sumy_cyfr.end());
    std::println("{} {} {}", std::ranges::count(sumy_cyfr, 35), najwieksza, std::ranges::count(sumy_cyfr, najwieksza));
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        List<Integer> sumyCyfr = new ArrayList<>();

        for (String linia : Files.readAllLines(Path.of("liczby.txt"))) {
            int suma = 0;
            for (char znak : linia.strip().toCharArray())
                if (znak != ' ')
                    suma += znak - '0';
            sumyCyfr.add(suma);
        }

        int najwieksza = Collections.max(sumyCyfr);
        System.out.println(Collections.frequency(sumyCyfr, 35) + " " + najwieksza + " "
                + Collections.frequency(sumyCyfr, najwieksza));
    }
}
```
**Odpowiedź:** 4 wiersze z sumą 35; największa suma cyfr 88, wystąpiła 2 razy

## 5.1

> **Treść zadania:** Zadanie 5. Kemping. Ośrodek ma domki 2-, 3-, 4-, 5- i 6-osobowe. Plik `wynajem.txt` (pola rozdzielone tabulatorami, pierwszy wiersz nagłówkowy) zawiera historię wynajmu z 2014 r.: data przyjazdu, data wyjazdu (format `RRRR-MM-DD`), koszt energii, koszt wody, typ domku (liczba osób). Odpowiedzi zapisz w pliku `wyniki5.txt` (poza wykresem z 5.4), poprzedzając je numerami zadań.
>
> Podaj, domki którego typu były wynajmowane najwięcej razy.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
wynajmy = {}

with open("wynajem.txt") as file:
    next(file)  # pomijamy nagłówek
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        wynajmy[typ] = wynajmy.get(typ, 0) + 1

print(max(wynajmy, key=wynajmy.get))
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

int main() {
    // typ -> liczba wynajmów; wektor zachowuje kolejność pierwszego wystąpienia (jak dict w Pythonie)
    std::vector<std::pair<std::string, int>> wynajmy;

    std::ifstream plik("wynajem.txt");
    std::string linia;
    std::getline(plik, linia);  // pomijamy nagłówek
    while (std::getline(plik, linia)) {
        std::istringstream ss(linia);
        std::string przyjazd, wyjazd, energia, woda, typ;
        ss >> przyjazd >> wyjazd >> energia >> woda >> typ;
        bool znaleziony = false;
        for (auto& [t, ile] : wynajmy)
            if (t == typ) {
                ile++;
                znaleziony = true;
            }
        if (!znaleziony)
            wynajmy.push_back({typ, 1});
    }

    // pierwszy typ z największą liczbą wynajmów, jak max(..., key=...) w Pythonie
    auto najlepszy = wynajmy[0];
    for (auto& para : wynajmy)
        if (para.second > najlepszy.second)
            najlepszy = para;
    std::println("{}", najlepszy.first);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // typ -> liczba wynajmów; LinkedHashMap zachowuje kolejność wstawiania (jak dict w Pythonie)
        Map<String, Integer> wynajmy = new LinkedHashMap<>();

        List<String> linie = Files.readAllLines(Path.of("wynajem.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            wynajmy.merge(pola[4], 1, Integer::sum);
        }

        // pierwszy typ z największą liczbą wynajmów, jak max(..., key=...) w Pythonie
        String najlepszy = null;
        for (String typ : wynajmy.keySet())
            if (najlepszy == null || wynajmy.get(typ) > wynajmy.get(najlepszy))
                najlepszy = typ;
        System.out.println(najlepszy);
    }
}
```
**Odpowiedź:** domki 2-osobowe

## 5.2

> **Treść zadania:** Na podstawie pliku `wynajem.txt` oblicz dla każdego typu domku łączną liczbę dób wynajmu (liczba dób = data wyjazdu − data przyjazdu). Przykład: dla wynajmów 02.01–11.01 (typ 5), 02.01–23.01 (typ 6), 02.01–14.01 (typ 6), 02.01–22.01 (typ 5) domki typu 5 wynajęto na 29 dób, a typu 6 — na 33 doby. Wynik zapisz w `wyniki5.txt`.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
from datetime import date

doby = {}

with open("wynajem.txt") as file:
    next(file)
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        liczba_dob = (date.fromisoformat(wyjazd) - date.fromisoformat(przyjazd)).days
        doby[typ] = doby.get(typ, 0) + liczba_dob

for typ in sorted(doby):
    print(typ, doby[typ])
```

```cpp
// C++23
#include <chrono>
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>

using namespace std::chrono;

// "rrrr-mm-dd" -> dzień kalendarzowy, na którym można liczyć różnice
sys_days na_date(const std::string& tekst) {
    int r = std::stoi(tekst.substr(0, 4));
    unsigned m = std::stoi(tekst.substr(5, 2)), d = std::stoi(tekst.substr(8, 2));
    return year(r) / month(m) / day(d);
}

int main() {
    std::map<std::string, long long> doby;  // std::map - typy posortowane

    std::ifstream plik("wynajem.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        std::istringstream ss(linia);
        std::string przyjazd, wyjazd, energia, woda, typ;
        ss >> przyjazd >> wyjazd >> energia >> woda >> typ;
        long long liczba_dob = (na_date(wyjazd) - na_date(przyjazd)).count();
        doby[typ] += liczba_dob;
    }

    for (auto& [typ, suma] : doby)
        std::println("{} {}", typ, suma);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        Map<String, Long> doby = new TreeMap<>();  // TreeMap - typy posortowane

        List<String> linie = Files.readAllLines(Path.of("wynajem.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            long liczbaDob = ChronoUnit.DAYS.between(LocalDate.parse(pola[0]), LocalDate.parse(pola[1]));
            doby.merge(pola[4], liczbaDob, Long::sum);
        }

        for (var wpis : doby.entrySet())
            System.out.println(wpis.getKey() + " " + wpis.getValue());
    }
}
```
**Odpowiedź:** 2 – 2985, 3 – 2816, 4 – 2944, 5 – 2997, 6 – 3244

## 5.3

> **Treść zadania:** Opłata za wynajem to czynsz plus koszt mediów (energia i woda), przy czym czynsz = 10 zł · liczba osób (typ domku) · liczba dób. Np. domek 5-osobowy na 9 dób z energią 39,35 zł i wodą 1,04 zł kosztuje 450 + 39,35 + 1,04 = 490,39 zł. Na podstawie `wynajem.txt` utwórz zestawienie łącznych opłat dla każdego typu domku, posortowane nierosnąco według kwoty. Wynik zapisz w `wyniki5.txt`.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
from datetime import date

oplaty = {}

with open("wynajem.txt") as file:
    next(file)
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        liczba_dob = (date.fromisoformat(wyjazd) - date.fromisoformat(przyjazd)).days
        czynsz = 10 * int(typ) * liczba_dob
        oplata = czynsz + float(energia.replace(",", ".")) + float(woda.replace(",", "."))
        oplaty[typ] = oplaty.get(typ, 0) + oplata

for typ in sorted(oplaty, key=oplaty.get, reverse=True):
    print(typ, round(oplaty[typ], 2))
```

```cpp
// C++23
#include <algorithm>
#include <chrono>
#include <format>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std::chrono;

// "rrrr-mm-dd" -> dzień kalendarzowy, na którym można liczyć różnice
sys_days na_date(const std::string& tekst) {
    int r = std::stoi(tekst.substr(0, 4));
    unsigned m = std::stoi(tekst.substr(5, 2)), d = std::stoi(tekst.substr(8, 2));
    return year(r) / month(m) / day(d);
}

// "39,35" -> 39.35
double na_liczbe(std::string tekst) {
    std::replace(tekst.begin(), tekst.end(), ',', '.');
    return std::stod(tekst);
}

// zaokraglenie do 2 miejsc jak round(x, 2) w Pythonie
double zaokraglij(double x) {
    return std::stod(std::format("{:.2f}", x));
}

// liczba zmiennoprzecinkowa wypisana tak jak w Pythonie (np. 61401.0, 196335.25)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find_first_of(".e") == std::string::npos)
        s += ".0";
    return s;
}

int main() {
    // typ -> suma opłat; wektor zachowuje kolejność pierwszego wystąpienia (jak dict w Pythonie)
    std::vector<std::pair<std::string, double>> oplaty;

    std::ifstream plik("wynajem.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        std::istringstream ss(linia);
        std::string przyjazd, wyjazd, energia, woda, typ;
        ss >> przyjazd >> wyjazd >> energia >> woda >> typ;
        long long liczba_dob = (na_date(wyjazd) - na_date(przyjazd)).count();
        long long czynsz = 10 * std::stoll(typ) * liczba_dob;
        double oplata = czynsz + na_liczbe(energia) + na_liczbe(woda);
        auto it = std::ranges::find_if(oplaty, [&](const auto& p) { return p.first == typ; });
        if (it == oplaty.end())
            oplaty.push_back({typ, oplata});
        else
            it->second += oplata;
    }

    // stable_sort - malejąco po opłatach, remisy w kolejności wstawiania (jak sorted w Pythonie)
    std::stable_sort(oplaty.begin(), oplaty.end(),
                     [](const auto& a, const auto& b) { return a.second > b.second; });
    for (auto& [typ, suma] : oplaty)
        std::println("{} {}", typ, jak_python(zaokraglij(suma)));
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Zadanie {
    // zaokraglenie do 2 miejsc jak round(x, 2) w Pythonie
    static double zaokraglij(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).doubleValue();
    }

    public static void main(String[] args) throws Exception {
        // typ -> suma opłat; LinkedHashMap zachowuje kolejność wstawiania (jak dict w Pythonie)
        Map<String, Double> oplaty = new LinkedHashMap<>();

        List<String> linie = Files.readAllLines(Path.of("wynajem.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            long liczbaDob = ChronoUnit.DAYS.between(LocalDate.parse(pola[0]), LocalDate.parse(pola[1]));
            long czynsz = 10 * Long.parseLong(pola[4]) * liczbaDob;
            double oplata = czynsz + Double.parseDouble(pola[2].replace(",", "."))
                    + Double.parseDouble(pola[3].replace(",", "."));
            oplaty.merge(pola[4], oplata, Double::sum);
        }

        // sortowanie listy jest stabilne - malejąco po opłatach, remisy w kolejności wstawiania
        List<String> typy = new ArrayList<>(oplaty.keySet());
        typy.sort((a, b) -> Double.compare(oplaty.get(b), oplaty.get(a)));
        for (String typ : typy)
            System.out.println(typ + " " + zaokraglij(oplaty.get(typ)));
    }
}
```
**Odpowiedź:** 6 – 196 335,25 zł; 5 – 151 509,94 zł; 4 – 119 478,24 zł; 3 – 86 170,73 zł; 2 – 61 401,00 zł

## 5.4

> **Treść zadania:** Na podstawie `wynajem.txt` utwórz zestawienie łącznych kosztów mediów (energia + woda) w poszczególnych miesiącach, przypisując każdy wynajem do miesiąca daty przyjazdu. Sporządź czytelnie opisany wykres kolumnowy tego zestawienia.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
media = [0] * 13

with open("wynajem.txt") as file:
    next(file)
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        miesiac = int(przyjazd[5:7])
        media[miesiac] += float(energia.replace(",", ".")) + float(woda.replace(",", "."))

for miesiac in range(1, 13):
    print(miesiac, round(media[miesiac], 2))
```

```cpp
// C++23
#include <algorithm>
#include <format>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// "39,35" -> 39.35
double na_liczbe(std::string tekst) {
    std::replace(tekst.begin(), tekst.end(), ',', '.');
    return std::stod(tekst);
}

// zaokraglenie do 2 miejsc jak round(x, 2) w Pythonie
double zaokraglij(double x) {
    return std::stod(std::format("{:.2f}", x));
}

// liczba zmiennoprzecinkowa wypisana tak jak w Pythonie (np. 628.6, 1078.32)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find_first_of(".e") == std::string::npos)
        s += ".0";
    return s;
}

int main() {
    std::vector<double> media(13, 0.0);

    std::ifstream plik("wynajem.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        std::istringstream ss(linia);
        std::string przyjazd, wyjazd, energia, woda, typ;
        ss >> przyjazd >> wyjazd >> energia >> woda >> typ;
        int miesiac = std::stoi(przyjazd.substr(5, 2));
        media[miesiac] += na_liczbe(energia) + na_liczbe(woda);
    }

    for (int miesiac = 1; miesiac <= 12; miesiac++)
        std::println("{} {}", miesiac, jak_python(zaokraglij(media[miesiac])));
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Zadanie {
    // zaokraglenie do 2 miejsc jak round(x, 2) w Pythonie
    static double zaokraglij(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).doubleValue();
    }

    public static void main(String[] args) throws Exception {
        double[] media = new double[13];

        List<String> linie = Files.readAllLines(Path.of("wynajem.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            int miesiac = Integer.parseInt(pola[0].substring(5, 7));
            media[miesiac] += Double.parseDouble(pola[2].replace(",", "."))
                    + Double.parseDouble(pola[3].replace(",", "."));
        }

        for (int miesiac = 1; miesiac <= 12; miesiac++)
            System.out.println(miesiac + " " + zaokraglij(media[miesiac]));
    }
}
```
**Odpowiedź:** 1: 1078,32; 2: 611,15; 3: 565,22; 4: 322,96; 5: 299,66; 6: 568,59; 7: 628,60; 8: 531,33; 9: 1045,12; 10: 813,25; 11: 1107,80; 12: 893,16 (wykres kolumnowy wykonuje się w arkuszu kalkulacyjnym)
