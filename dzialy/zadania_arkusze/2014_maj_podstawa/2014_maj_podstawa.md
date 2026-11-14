<h1 align="center">Matura 2014 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

> **Treść zadania:** Zadanie 1. Doskonała inaczej. Algorytm wypisuje wszystkie dzielniki liczby naturalnej `n > 1` mniejsze od `n`:
> ```
> d ← 1
> dopóki d < n wykonuj:
>     jeżeli n mod d = 0, to wypisz d
>     d ← d + 1
> ```
>
> - 1a — podaj wynik algorytmu dla `n = 35`, `56` i `81` (dla `n = 6` wynik to `1 2 3`).
> - 1b — zmień warunek pętli tak, aby instrukcja `d ← d + 1` wykonywała się nie więcej niż `n/2` razy (algorytm nadal ma wypisywać te same dzielniki).

```py
def dzielniki(n):
    wynik = []
    d = 1
    while d <= n // 2:  # 1b: wystarczy sprawdzać do n div 2
        if n % d == 0:
            wynik.append(d)
        d = d + 1
    return wynik


for n in [6, 35, 56, 81]:
    print(n, *dzielniki(n))
```

```cpp
// C++23
#include <print>
#include <vector>

std::vector<int> dzielniki(int n) {
    std::vector<int> wynik;
    int d = 1;
    while (d <= n / 2) {  // 1b: wystarczy sprawdzać do n div 2
        if (n % d == 0) wynik.push_back(d);
        d = d + 1;
    }
    return wynik;
}

int main() {
    for (int n : {6, 35, 56, 81}) {
        std::print("{}", n);
        for (int d : dzielniki(n)) std::print(" {}", d);
        std::println();
    }
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    static List<Integer> dzielniki(int n) {
        var wynik = new ArrayList<Integer>();
        int d = 1;
        while (d <= n / 2) {  // 1b: wystarczy sprawdzać do n div 2
            if (n % d == 0) wynik.add(d);
            d = d + 1;
        }
        return wynik;
    }

    public static void main(String[] args) throws Exception {
        for (int n : new int[]{6, 35, 56, 81}) {
            var linia = new StringBuilder(Integer.toString(n));
            for (int d : dzielniki(n)) linia.append(" ").append(d);
            System.out.println(linia);
        }
    }
}
```
**Odpowiedź:** a) 35 → 1 5 7; 56 → 1 2 4 7 8 14 28; 81 → 1 3 9 27; b) d ≤ n div 2

## 1c

> **Treść zadania:** Dzielniki liczby jak w zadaniu 1. Liczba doskonała II rzędu to liczba naturalna `n`, równa iloczynowi wszystkich swoich dzielników mniejszych od niej (np. `6 = 1·2·3`). Zapisz algorytm, który dla liczby naturalnej `n > 1` wypisze `TAK`, jeśli jest ona liczbą doskonałą II rzędu, a w przeciwnym razie `NIE`.

```py
def doskonala_II_rzedu(n):
    iloczyn = 1
    d = 1
    while d <= n // 2:
        if n % d == 0:
            iloczyn = iloczyn * d
        d = d + 1
    if iloczyn == n:
        return "TAK"
    return "NIE"


for n in [6, 8, 10, 12, 16]:
    print(n, doskonala_II_rzedu(n))
```

```cpp
// C++23
#include <print>
#include <string>

std::string doskonala_II_rzedu(int n) {
    long long iloczyn = 1;
    int d = 1;
    while (d <= n / 2) {
        if (n % d == 0) iloczyn = iloczyn * d;
        d = d + 1;
    }
    if (iloczyn == n) return "TAK";
    return "NIE";
}

int main() {
    for (int n : {6, 8, 10, 12, 16}) {
        std::println("{} {}", n, doskonala_II_rzedu(n));
    }
}
```

```java
// Java 25
public class Zadanie {
    static String doskonalaIIRzedu(int n) {
        long iloczyn = 1;
        int d = 1;
        while (d <= n / 2) {
            if (n % d == 0) iloczyn = iloczyn * d;
            d = d + 1;
        }
        if (iloczyn == n) return "TAK";
        return "NIE";
    }

    public static void main(String[] args) throws Exception {
        for (int n : new int[]{6, 8, 10, 12, 16}) {
            System.out.println(n + " " + doskonalaIIRzedu(n));
        }
    }
}
```
**Odpowiedź:** np. 6 → TAK, 8 → TAK, 10 → TAK, 12 → NIE, 16 → NIE

## 2a i 2b

> **Treść zadania:** Zadanie 2. Min-Max. Dla parzystej dodatniej liczby `n` i tablicy `a[1..n]` liczb całkowitych:
> ```
> i ← 1
> dopóki i < n wykonuj:
>     jeżeli a[i] > a[i+1], to zamień a[i] z a[i+1]
>     i ← i + 2
> ```
>
> - 2a — podaj zawartość tablicy po wykonaniu algorytmu dla `a = [45, 12, 7, 39, 20, 1]` (`n = 6`) oraz `a = [21, 1, 56, 90, 8, 8, 19, 47]` (`n = 8`).
> - 2b — wstaw jeden ze znaków `<`, `>`, `≤`, `≥` tak, by zdanie „dla każdego `i = 1, 3, …, n−1` mamy `a[i] _ a[i+1]`” poprawnie opisywało tablicę po wykonaniu algorytmu.

```py
def min_max_pary(a):
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        i = i + 2
    return a


print(min_max_pary([45, 12, 7, 39, 20, 1]))
print(min_max_pary([21, 1, 56, 90, 8, 8, 19, 47]))
```

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

std::vector<int> min_max_pary(std::vector<int> a) {
    int n = a.size();
    int i = 0;
    while (i < n - 1) {
        if (a[i] > a[i + 1]) std::swap(a[i], a[i + 1]);
        i = i + 2;
    }
    return a;
}

int main() {
    std::println("{}", min_max_pary({45, 12, 7, 39, 20, 1}));
    std::println("{}", min_max_pary({21, 1, 56, 90, 8, 8, 19, 47}));
}
```

```java
// Java 25
import java.util.Arrays;

public class Zadanie {
    static int[] minMaxPary(int[] a) {
        int n = a.length;
        int i = 0;
        while (i < n - 1) {
            if (a[i] > a[i + 1]) {
                int pom = a[i];
                a[i] = a[i + 1];
                a[i + 1] = pom;
            }
            i = i + 2;
        }
        return a;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(Arrays.toString(minMaxPary(new int[]{45, 12, 7, 39, 20, 1})));
        System.out.println(Arrays.toString(minMaxPary(new int[]{21, 1, 56, 90, 8, 8, 19, 47})));
    }
}
```
**Odpowiedź:** a) [12, 45, 7, 39, 1, 20], [1, 21, 56, 90, 8, 8, 19, 47]; b) a[i] ≤ a[i+1]

## 2c

> **Treść zadania:** Algorytm porządkujący pary jak w zadaniu 2. Uzupełnij luki w algorytmie znajdującym minimum i maksimum tablicy `a[1..n]` (`n` parzyste), wykorzystując to, że z każdej pary tylko mniejszy element może być kandydatem na minimum, a tylko większy — na maksimum:
> ```
> (kroki 1–2 jak wyżej: porządkowanie par)
> min ← ……; max ← ……
> i ← 3
> dopóki …… wykonuj:
>     jeżeli ……, to min ← ……
>     jeżeli ……, to max ← ……
>     i ← i + 2
> ```

```py
def min_max(a):
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        i = i + 2
    mini = a[0]
    maks = a[1]
    i = 2
    while i < n - 1:
        if a[i] < mini:
            mini = a[i]
        if a[i + 1] > maks:
            maks = a[i + 1]
        i = i + 2
    return mini, maks


print(min_max([45, 12, 7, 39, 20, 1]))
print(min_max([21, 1, 56, 90, 8, 8, 19, 47]))
```

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

std::pair<int, int> min_max(std::vector<int> a) {
    int n = a.size();
    int i = 0;
    while (i < n - 1) {
        if (a[i] > a[i + 1]) std::swap(a[i], a[i + 1]);
        i = i + 2;
    }
    int mini = a[0];
    int maks = a[1];
    i = 2;
    while (i < n - 1) {
        if (a[i] < mini) mini = a[i];
        if (a[i + 1] > maks) maks = a[i + 1];
        i = i + 2;
    }
    return {mini, maks};
}

int main() {
    auto [mini1, maks1] = min_max({45, 12, 7, 39, 20, 1});
    std::println("({}, {})", mini1, maks1);
    auto [mini2, maks2] = min_max({21, 1, 56, 90, 8, 8, 19, 47});
    std::println("({}, {})", mini2, maks2);
}
```

```java
// Java 25
public class Zadanie {
    static int[] minMax(int[] a) {
        int n = a.length;
        int i = 0;
        while (i < n - 1) {
            if (a[i] > a[i + 1]) {
                int pom = a[i];
                a[i] = a[i + 1];
                a[i + 1] = pom;
            }
            i = i + 2;
        }
        int mini = a[0];
        int maks = a[1];
        i = 2;
        while (i < n - 1) {
            if (a[i] < mini) mini = a[i];
            if (a[i + 1] > maks) maks = a[i + 1];
            i = i + 2;
        }
        return new int[]{mini, maks};
    }

    public static void main(String[] args) throws Exception {
        int[] w1 = minMax(new int[]{45, 12, 7, 39, 20, 1});
        System.out.println("(" + w1[0] + ", " + w1[1] + ")");
        int[] w2 = minMax(new int[]{21, 1, 56, 90, 8, 8, 19, 47});
        System.out.println("(" + w2[0] + ", " + w2[1] + ")");
    }
}
```
**Odpowiedź:** min ← a[1], max ← a[2], dopóki i < n: jeżeli a[i] < min, to min ← a[i]; jeżeli a[i+1] > max, to max ← a[i+1]

## 4a

> **Treść zadania:** Zadanie 4. Działki. W pliku `DZIALKI.TXT` jest 5000 wierszy (po wierszu nagłówkowym) z danymi działek rozdzielonymi średnikami: numer, powierzchnia w m², rodzaj, typ ulgi, np. `517/12;1259,19;R;B`. Stawki podatku za m²: rolna `R` — 0,65 zł, budowlana `B` — 0,77 zł, siedliskowa `S` — 0,21 zł, leśna `L` — 0,04 zł, rekreacyjna `X` — 0,43 zł. Ulgi: `A` — 20%, `B` — 50%, `C` — 90%, `D` — 0%. Podatek (powierzchnia × stawka) zaokrągla się do grosza, a kwotę po odjęciu ulgi — ponownie do grosza (np. dla `517/12` podatek 818,47 zł, po uldze 409,24 zł). Odpowiedzi zapisz w kolejnych wierszach pliku `ZADANIE4.TXT`, poprzedzając każdą literą podpunktu.
>
> Podaj powierzchnię i rodzaj najmniejszej działki oraz powierzchnię i rodzaj największej działki.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
dzialki = []

with open("DZIALKI.TXT") as file:
    next(file)  # pomijamy nagłówek
    for line in file:
        numer, powierzchnia, rodzaj, ulga = line.strip().split(";")
        dzialki.append((float(powierzchnia.replace(",", ".")), rodzaj))

print("min:", min(dzialki))
print("max:", max(dzialki))
```

```cpp
// C++23
#include <algorithm>
#include <format>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

// liczba rzeczywista wypisana tak jak w Pythonie (np. 500.18, 1500.0)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find('.') == std::string::npos) s += ".0";
    return s;
}

int main() {
    std::vector<std::pair<double, std::string>> dzialki;  // (powierzchnia, rodzaj)

    std::ifstream plik("DZIALKI.TXT");
    std::string line;
    std::getline(plik, line);  // pomijamy nagłówek
    while (std::getline(plik, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        std::stringstream ss(line);
        std::string numer, powierzchnia, rodzaj, ulga;
        std::getline(ss, numer, ';');
        std::getline(ss, powierzchnia, ';');
        std::getline(ss, rodzaj, ';');
        std::getline(ss, ulga, ';');
        std::ranges::replace(powierzchnia, ',', '.');
        dzialki.push_back({std::stod(powierzchnia), rodzaj});
    }

    // pary porównują się jak krotki w Pythonie: najpierw powierzchnia, potem rodzaj
    auto najmniejsza = std::ranges::min(dzialki);
    auto najwieksza = std::ranges::max(dzialki);
    std::println("min: ({}, '{}')", jak_python(najmniejsza.first), najmniejsza.second);
    std::println("max: ({}, '{}')", jak_python(najwieksza.first), najwieksza.second);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    record Dzialka(double powierzchnia, String rodzaj) {}

    // porównanie jak krotek w Pythonie: najpierw powierzchnia, potem rodzaj
    static int porownaj(Dzialka a, Dzialka b) {
        int w = Double.compare(a.powierzchnia(), b.powierzchnia());
        return w != 0 ? w : a.rodzaj().compareTo(b.rodzaj());
    }

    public static void main(String[] args) throws Exception {
        var linie = Files.readAllLines(Path.of("DZIALKI.TXT"));
        Dzialka najmniejsza = null, najwieksza = null;
        for (String line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = line.strip().split(";");
            var d = new Dzialka(Double.parseDouble(pola[1].replace(",", ".")), pola[2]);
            if (najmniejsza == null || porownaj(d, najmniejsza) < 0) najmniejsza = d;
            if (najwieksza == null || porownaj(d, najwieksza) > 0) najwieksza = d;
        }
        System.out.println("min: (" + najmniejsza.powierzchnia() + ", '" + najmniejsza.rodzaj() + "')");
        System.out.println("max: (" + najwieksza.powierzchnia() + ", '" + najwieksza.rodzaj() + "')");
    }
}
```
**Odpowiedź:** min: 500,18 – siedliskowa (S); max: 1500 – rekreacyjna (X)

## 4b

> **Treść zadania:** Działki z pliku `DZIALKI.TXT` jak w zadaniu 4a. Dla każdego rodzaju działki podaj: rodzaj, liczbę działek tego rodzaju i ich średnią powierzchnię zaokrągloną do dwóch miejsc po przecinku.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
liczba = {}
suma = {}

with open("DZIALKI.TXT") as file:
    next(file)
    for line in file:
        numer, powierzchnia, rodzaj, ulga = line.strip().split(";")
        liczba[rodzaj] = liczba.get(rodzaj, 0) + 1
        suma[rodzaj] = suma.get(rodzaj, 0) + float(powierzchnia.replace(",", "."))

for rodzaj in "RBSLX":
    print(rodzaj, liczba[rodzaj], round(suma[rodzaj] / liczba[rodzaj], 2))
```

```cpp
// C++23
#include <algorithm>
#include <format>
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>

// liczba rzeczywista wypisana tak jak w Pythonie (np. 989.98, 990.0)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find('.') == std::string::npos) s += ".0";
    return s;
}

// round(x, 2) z Pythona
double zaokraglij2(double x) {
    return std::stod(std::format("{:.2f}", x));
}

int main() {
    std::map<char, int> liczba;
    std::map<char, double> suma;

    std::ifstream plik("DZIALKI.TXT");
    std::string line;
    std::getline(plik, line);  // pomijamy nagłówek
    while (std::getline(plik, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        std::stringstream ss(line);
        std::string numer, powierzchnia, rodzaj, ulga;
        std::getline(ss, numer, ';');
        std::getline(ss, powierzchnia, ';');
        std::getline(ss, rodzaj, ';');
        std::getline(ss, ulga, ';');
        std::ranges::replace(powierzchnia, ',', '.');
        liczba[rodzaj[0]]++;
        suma[rodzaj[0]] += std::stod(powierzchnia);
    }

    for (char rodzaj : std::string("RBSLX")) {
        std::println("{} {} {}", rodzaj, liczba[rodzaj], jak_python(zaokraglij2(suma[rodzaj] / liczba[rodzaj])));
    }
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;

public class Zadanie {
    // round(x, 2) z Pythona
    static double zaokraglij2(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).doubleValue();
    }

    public static void main(String[] args) throws Exception {
        var liczba = new HashMap<String, Integer>();
        var suma = new HashMap<String, Double>();

        var linie = Files.readAllLines(Path.of("DZIALKI.TXT"));
        for (String line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = line.strip().split(";");
            String rodzaj = pola[2];
            liczba.merge(rodzaj, 1, Integer::sum);
            suma.merge(rodzaj, Double.parseDouble(pola[1].replace(",", ".")), Double::sum);
        }

        for (String rodzaj : "RBSLX".split("")) {
            System.out.println(rodzaj + " " + liczba.get(rodzaj) + " " + zaokraglij2(suma.get(rodzaj) / liczba.get(rodzaj)));
        }
    }
}
```
**Odpowiedź:** R (rolna) 708 – 989,98; B (budowlana) 1775 – 999,59; S (siedliskowa) 964 – 986,12; L (leśna) 559 – 1016,75; X (rekreacyjna) 994 – 989,94

## 4c

> **Treść zadania:** Działki i zasady naliczania podatku z ulgami jak w zadaniu 4a. Podaj, ile działek ma podatek (po uwzględnieniu ulgi): do 100 zł włącznie, ponad 100 zł do 500 zł włącznie oraz ponad 500 zł. Sporządź czytelnie opisany wykres procentowy tego zestawienia.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
from decimal import Decimal, ROUND_HALF_UP

stawka = {"R": "0.65", "B": "0.77", "S": "0.21", "L": "0.04", "X": "0.43"}
procent_ulgi = {"A": 20, "B": 50, "C": 90, "D": 0}


def zaokraglij(x):  # zaokrąglenie do grosza jak w arkuszu kalkulacyjnym
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


do_100 = 0
do_500 = 0
ponad_500 = 0

with open("DZIALKI.TXT") as file:
    next(file)
    for line in file:
        numer, powierzchnia, rodzaj, ulga = line.strip().split(";")
        podatek = zaokraglij(Decimal(powierzchnia.replace(",", ".")) * Decimal(stawka[rodzaj]))
        podatek = zaokraglij(podatek * (100 - procent_ulgi[ulga]) / 100)
        if podatek <= 100:
            do_100 += 1
        elif podatek <= 500:
            do_500 += 1
        else:
            ponad_500 += 1

print(do_100, do_500, ponad_500)
```

```cpp
// C++23
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>

// Liczymy w groszach na liczbach całkowitych, żeby uniknąć błędów zaokrągleń
// (w Pythonie użyto Decimal). Kwota "1293,99" -> 129399 groszy.
long long na_grosze(const std::string& tekst) {
    size_t przecinek = tekst.find(',');
    if (przecinek == std::string::npos) return std::stoll(tekst) * 100;
    std::string ulamek = tekst.substr(przecinek + 1);
    while (ulamek.size() < 2) ulamek += "0";
    return std::stoll(tekst.substr(0, przecinek)) * 100 + std::stoll(ulamek);
}

// dzielenie liczby nieujemnej przez 100 z zaokrągleniem "połówki w górę" (jak w arkuszu)
long long zaokraglij(long long x) {
    return (x + 50) / 100;
}

int main() {
    std::map<char, long long> stawka = {{'R', 65}, {'B', 77}, {'S', 21}, {'L', 4}, {'X', 43}};  // w groszach
    std::map<char, int> procent_ulgi = {{'A', 20}, {'B', 50}, {'C', 90}, {'D', 0}};

    int do_100 = 0, do_500 = 0, ponad_500 = 0;

    std::ifstream plik("DZIALKI.TXT");
    std::string line;
    std::getline(plik, line);  // pomijamy nagłówek
    while (std::getline(plik, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        std::stringstream ss(line);
        std::string numer, powierzchnia, rodzaj, ulga;
        std::getline(ss, numer, ';');
        std::getline(ss, powierzchnia, ';');
        std::getline(ss, rodzaj, ';');
        std::getline(ss, ulga, ';');
        // setne części m^2 * grosze = 1/100 grosza -> zaokrąglamy do grosza
        long long podatek = zaokraglij(na_grosze(powierzchnia) * stawka[rodzaj[0]]);
        podatek = zaokraglij(podatek * (100 - procent_ulgi[ulga[0]]));
        if (podatek <= 100 * 100) do_100++;
        else if (podatek <= 500 * 100) do_500++;
        else ponad_500++;
    }

    std::println("{} {} {}", do_100, do_500, ponad_500);
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;

public class Zadanie {
    static final Map<String, String> STAWKA = Map.of("R", "0.65", "B", "0.77", "S", "0.21", "L", "0.04", "X", "0.43");
    static final Map<String, Integer> PROCENT_ULGI = Map.of("A", 20, "B", 50, "C", 90, "D", 0);

    static BigDecimal zaokraglij(BigDecimal x) {  // zaokrąglenie do grosza jak w arkuszu kalkulacyjnym
        return x.setScale(2, RoundingMode.HALF_UP);
    }

    public static void main(String[] args) throws Exception {
        int do100 = 0, do500 = 0, ponad500 = 0;
        var sto = new BigDecimal(100);
        var piecset = new BigDecimal(500);

        var linie = Files.readAllLines(Path.of("DZIALKI.TXT"));
        for (String line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = line.strip().split(";");
            String powierzchnia = pola[1], rodzaj = pola[2], ulga = pola[3];
            var podatek = zaokraglij(new BigDecimal(powierzchnia.replace(",", ".")).multiply(new BigDecimal(STAWKA.get(rodzaj))));
            podatek = zaokraglij(podatek.multiply(new BigDecimal(100 - PROCENT_ULGI.get(ulga))).divide(sto));
            if (podatek.compareTo(sto) <= 0) do100++;
            else if (podatek.compareTo(piecset) <= 0) do500++;
            else ponad500++;
        }

        System.out.println(do100 + " " + do500 + " " + ponad500);
    }
}
```
**Odpowiedź:** do 100 zł – 2096, ponad 100 zł do 500 zł – 2133, ponad 500 zł – 771 (wykres procentowy wykonuje się w arkuszu kalkulacyjnym)

## 5a

> **Treść zadania:** Zadanie 5. Pary liczb. W pliku `PARY_LICZB.TXT` jest 1000 wierszy, w każdym para liczb całkowitych dodatnich nie większych niż 30 000, rozdzielonych spacją. Odpowiedzi zapisz w pliku `ZADANIE5.TXT`, poprzedzając każdą literą podpunktu.
>
> Podaj, w ilu wierszach jedna z liczb jest wielokrotnością drugiej.

```py
count = 0

with open("PARY_LICZB.TXT") as file:
    for line in file:
        a, b = map(int, line.split())
        if a % b == 0 or b % a == 0:
            count += 1

print(count)
```

```cpp
// C++23
#include <fstream>
#include <print>

int main() {
    std::ifstream plik("PARY_LICZB.TXT");
    int count = 0;
    int a, b;
    while (plik >> a >> b) {
        if (a % b == 0 || b % a == 0) count++;
    }
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
        for (String line : Files.readAllLines(Path.of("PARY_LICZB.TXT"))) {
            String[] liczby = line.strip().split("\\s+");
            int a = Integer.parseInt(liczby[0]), b = Integer.parseInt(liczby[1]);
            if (a % b == 0 || b % a == 0) count++;
        }
        System.out.println(count);
    }
}
```
**Odpowiedź:** 10

## 5b

> **Treść zadania:** Pary liczb z pliku `PARY_LICZB.TXT` jak w zadaniu 5a. Podaj, w ilu wierszach liczby są względnie pierwsze (ich NWD wynosi 1).

```py
def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


count = 0

with open("PARY_LICZB.TXT") as file:
    for line in file:
        a, b = map(int, line.split())
        if nwd(a, b) == 1:
            count += 1

print(count)
```

```cpp
// C++23
#include <fstream>
#include <print>

int nwd(int a, int b) {
    while (b > 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    std::ifstream plik("PARY_LICZB.TXT");
    int count = 0;
    int a, b;
    while (plik >> a >> b) {
        if (nwd(a, b) == 1) count++;
    }
    std::println("{}", count);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static int nwd(int a, int b) {
        while (b > 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public static void main(String[] args) throws Exception {
        int count = 0;
        for (String line : Files.readAllLines(Path.of("PARY_LICZB.TXT"))) {
            String[] liczby = line.strip().split("\\s+");
            if (nwd(Integer.parseInt(liczby[0]), Integer.parseInt(liczby[1])) == 1) count++;
        }
        System.out.println(count);
    }
}
```
**Odpowiedź:** 584

## 5c

> **Treść zadania:** Pary liczb z pliku `PARY_LICZB.TXT` jak w zadaniu 5a. Podaj, w ilu wierszach suma cyfr pierwszej liczby jest równa sumie cyfr drugiej liczby.

```py
def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma


count = 0

with open("PARY_LICZB.TXT") as file:
    for line in file:
        a, b = line.split()
        if suma_cyfr(a) == suma_cyfr(b):
            count += 1

print(count)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int suma_cyfr(const std::string& liczba) {
    int suma = 0;
    for (char cyfra : liczba) suma += cyfra - '0';
    return suma;
}

int main() {
    std::ifstream plik("PARY_LICZB.TXT");
    int count = 0;
    std::string a, b;
    while (plik >> a >> b) {
        if (suma_cyfr(a) == suma_cyfr(b)) count++;
    }
    std::println("{}", count);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static int sumaCyfr(String liczba) {
        int suma = 0;
        for (char cyfra : liczba.toCharArray()) suma += cyfra - '0';
        return suma;
    }

    public static void main(String[] args) throws Exception {
        int count = 0;
        for (String line : Files.readAllLines(Path.of("PARY_LICZB.TXT"))) {
            String[] liczby = line.strip().split("\\s+");
            if (sumaCyfr(liczby[0]) == sumaCyfr(liczby[1])) count++;
        }
        System.out.println(count);
    }
}
```
**Odpowiedź:** 48
