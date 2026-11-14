<h1 align="center">Matura 2019 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md) --- [PLIKI](https://github.com/wernexnrs/MATURA-INFORMATYKA/tree/master/dzialy/zadania_arkusze/2019_czerwiec)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

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
> Podaj najmniejszą i największą możliwą liczbę wywołań funkcji `Rek` (wliczając pierwsze) po wywołaniu `Rek(2019, 6, 14)` dla `n = 17` i pewnej rosnącej tablicy `T[1..17]` różnych liczb całkowitych.

```py
# Liczba wywołań Rek zależy tylko od tego, w którą połowę przedziału p..k pójdzie rekurencja.
# Sprawdzamy obie możliwości w każdym kroku i wybieramy najmniejszą / największą liczbę wywołań.
def wywolania(p, k, wybierz):
    if p < k:
        s = (p + k) // 2
        return 1 + wybierz(wywolania(p, s, wybierz), wywolania(s + 1, k, wybierz))
    return 1


print("najmniejsza:", wywolania(6, 14, min))
print("największa:", wywolania(6, 14, max))
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
    std::println("najmniejsza: {}", wywolania(6, 14, mniejsza));
    std::println("największa: {}", wywolania(6, 14, wieksza));
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
        System.out.println("najmniejsza: " + wywolania(6, 14, Math::min));
        System.out.println("największa: " + wywolania(6, 14, Math::max));
    }
}
```

**Odpowiedź:** najmniejsza liczba wywołań 4, największa 5

## 1.2

> **Treść zadania:** Funkcja `Rek(x, p, k)` jak w zadaniu 1.1 (rekurencyjne wyszukiwanie binarne `x` w rosnącej tablicy `T`).
>
> Dla `n = 11`, tablicy `T = [1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38]` i pierwszego wywołania `Rek(37, 1, 11)` podaj wartości parametrów `(x, p, k)` w kolejnych wywołaniach funkcji.

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


print("wynik:", Rek(37, 1, 11))
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
    int wynik = Rek(37, 1, 11);
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
        int wynik = Rek(37, 1, 11);
        System.out.println("wynik: " + wynik);
    }
}
```

**Odpowiedź:** Rek(37,7,11), Rek(37,10,11), Rek(37,11,11) (1.3: złożoność logarytmiczna)

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2 (szyfr kolumnowy). Tabela ma `k` wierszy (`k` — klucz). Znaki tekstu wpisujemy do kolejnych kolumn, zaczynając od lewego górnego rogu: w kolumnach nieparzystych z góry na dół, w parzystych z dołu do góry. Wolne miejsca w ostatniej kolumnie wypełniamy znakiem `_` (spacja). Szyfrogram to kolejne wiersze odczytane od góry, każdy od lewej do prawej.
>
> Przykład: dla `k = 3` i tekstu `MATURA_Z_INFORMATYKI` powstają wiersze `MA_FOYK`, `ARZNRTI`, `TU_IMA_`, więc szyfrogram to `MA_FOYKARZNRTITU_IMA_`.
>
> - 2.1 — 40-znakowy cytat Juliusza Cezara zaszyfrowano kluczem 10, otrzymując `NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P`. Rozszyfruj go.
> - 2.2 — napisz algorytm deszyfrujący: dane to klucz `k > 0`, długość `n` (wielokrotność `k`) i szyfrogram `S[1..n]`; wynikiem jest tekst odszyfrowany `T[1..n]`.

```py
def deszyfruj(k, S):
    n = len(S)
    kolumny = n // k
    # tabela k wierszy na kolumny - szyfrogram to kolejne wiersze tabeli
    tabela = [S[w * kolumny:(w + 1) * kolumny] for w in range(k)]
    T = ""
    for kol in range(kolumny):
        if kol % 2 == 0:  # kolumny nieparzyste (numerując od 1) czytamy z góry na dół
            for w in range(k):
                T += tabela[w][kol]
        else:  # kolumny parzyste - z dołu do góry
            for w in range(k - 1, -1, -1):
                T += tabela[w][kol]
    return T


print(deszyfruj(3, "MA_FOYKARZNRTITU_IMA_"))
print(deszyfruj(10, "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"))
```

```cpp
// C++23
#include <print>
#include <string>
#include <vector>

std::string deszyfruj(int k, const std::string& S) {
    int n = S.size();
    int kolumny = n / k;
    // tabela k wierszy na kolumny - szyfrogram to kolejne wiersze tabeli
    std::vector<std::string> tabela;
    for (int w = 0; w < k; w++)
        tabela.push_back(S.substr(w * kolumny, kolumny));
    std::string T = "";
    for (int kol = 0; kol < kolumny; kol++) {
        if (kol % 2 == 0) {  // kolumny nieparzyste (numerując od 1) czytamy z góry na dół
            for (int w = 0; w < k; w++)
                T += tabela[w][kol];
        } else {  // kolumny parzyste - z dołu do góry
            for (int w = k - 1; w >= 0; w--)
                T += tabela[w][kol];
        }
    }
    return T;
}

int main() {
    std::println("{}", deszyfruj(3, "MA_FOYKARZNRTITU_IMA_"));
    std::println("{}", deszyfruj(10, "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"));
}
```

```java
// Java 25
public class Zadanie {
    static String deszyfruj(int k, String S) {
        int n = S.length();
        int kolumny = n / k;
        // tabela k wierszy na kolumny - szyfrogram to kolejne wiersze tabeli
        String[] tabela = new String[k];
        for (int w = 0; w < k; w++)
            tabela[w] = S.substring(w * kolumny, (w + 1) * kolumny);
        var T = new StringBuilder();
        for (int kol = 0; kol < kolumny; kol++) {
            if (kol % 2 == 0) {  // kolumny nieparzyste (numerując od 1) czytamy z góry na dół
                for (int w = 0; w < k; w++)
                    T.append(tabela[w].charAt(kol));
            } else {  // kolumny parzyste - z dołu do góry
                for (int w = k - 1; w >= 0; w--)
                    T.append(tabela[w].charAt(kol));
            }
        }
        return T.toString();
    }

    public static void main(String[] args) throws Exception {
        System.out.println(deszyfruj(3, "MA_FOYKARZNRTITU_IMA_"));
        System.out.println(deszyfruj(10, "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"));
    }
}
```

**Odpowiedź:** NAUCZYCIELEM_WSZYSTKIEGO_JEST_PRAKTYKA

## 4.1

> **Treść zadania:** Zadanie 4 (wybrane liczby). Plik `liczby.txt` zawiera 300 liczb całkowitych z zakresu [1, 100 000], a plik `pierwsze.txt` — 200 liczb pierwszych z zakresu [10, 1 300 000], po jednej w wierszu (dane przykładowe: `liczby_przyklad.txt`, `pierwsze_przyklad.txt`, po 50 liczb). Liczba pierwsza to liczba naturalna większa od 1 o dokładnie dwóch dzielnikach.
>
> Wypisz, w kolejności z pliku, te liczby z `liczby.txt`, które są pierwsze i należą do przedziału [100, 5000]. Wynik zapisz w pliku `wyniki4_1.txt`.
>
> Dla danych przykładowych: 103, 163, 173, 701, 1033, 2137, 3529, 4933, 977, 2143.

```py
def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open("liczby.txt") as file:
    for line in file:
        liczba = int(line)
        if 100 <= liczba <= 5000 and czy_pierwsza(liczba):
            print(liczba)
```

```cpp
// C++23
#include <fstream>
#include <print>

bool czy_pierwsza(long long x) {
    if (x < 2)
        return false;
    long long i = 2;
    while (i * i <= x) {
        if (x % i == 0)
            return false;
        i++;
    }
    return true;
}

int main() {
    std::ifstream plik("liczby.txt");
    long long liczba;
    while (plik >> liczba)
        if (100 <= liczba && liczba <= 5000 && czy_pierwsza(liczba))
            std::println("{}", liczba);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static boolean czyPierwsza(long x) {
        if (x < 2)
            return false;
        long i = 2;
        while (i * i <= x) {
            if (x % i == 0)
                return false;
            i++;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        for (String line : Files.readAllLines(Path.of("liczby.txt"))) {
            if (line.isBlank())
                continue;
            long liczba = Long.parseLong(line.trim());
            if (100 <= liczba && liczba <= 5000 && czyPierwsza(liczba))
                System.out.println(liczba);
        }
    }
}
```

**Odpowiedź:** 563, 2087, 163, 2423, 3581, 911, 997, 113, 1049, 1511, 2467, 283, 3559, 521, 4201, 877, 1301, 2749, 4919, 1213, 2039, 4111, 3331, 401, 2221

## 4.2

> **Treść zadania:** Dane z pliku `pierwsze.txt` (200 liczb pierwszych).
>
> Wypisz, w kolejności z pliku, te liczby, które czytane od prawej do lewej również są liczbami pierwszymi (np. 17 → 71). Wynik zapisz w pliku `wyniki4_2.txt`.
>
> Dla danych przykładowych: 701, 709, 1033, 167, 1109, 1619, 1009, 179, 1499, 76001, 1601, 31873.

```py
def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open("pierwsze.txt") as file:
    for line in file:
        liczba = line.strip()
        if czy_pierwsza(int(liczba[::-1])):
            print(liczba)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

bool czy_pierwsza(long long x) {
    if (x < 2)
        return false;
    long long i = 2;
    while (i * i <= x) {
        if (x % i == 0)
            return false;
        i++;
    }
    return true;
}

int main() {
    std::ifstream plik("pierwsze.txt");
    std::string liczba;
    while (plik >> liczba) {
        std::string odwrocona(liczba.rbegin(), liczba.rend());
        if (czy_pierwsza(std::stoll(odwrocona)))
            std::println("{}", liczba);
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static boolean czyPierwsza(long x) {
        if (x < 2)
            return false;
        long i = 2;
        while (i * i <= x) {
            if (x % i == 0)
                return false;
            i++;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        for (String line : Files.readAllLines(Path.of("pierwsze.txt"))) {
            if (line.isBlank())
                continue;
            String liczba = line.strip();
            String odwrocona = new StringBuilder(liczba).reverse().toString();
            if (czyPierwsza(Long.parseLong(odwrocona)))
                System.out.println(liczba);
        }
    }
}
```

**Odpowiedź:** 51 liczb: 31, 37, 101, 1009, 1021, 113, 1499, 1213, 1217, 1229, 1231, 1237, 1487, 1223, 7027, … , 112111

## 4.3

> **Treść zadania:** Dane z pliku `pierwsze.txt` (200 liczb pierwszych).
>
> Niech `w(N)` oznacza sumę cyfr liczby `N`. Tworzymy ciąg `N1 = w(N)`, `N2 = w(N1)`, … aż do otrzymania liczby jednocyfrowej — jest ona wagą liczby `N` (np. waga 1109 to 2: 1109 → 11 → 2; waga 31699 to 1: 31699 → 28 → 10 → 1).
>
> Podaj, ile liczb z pliku ma wagę równą 1. Wynik zapisz w pliku `wyniki4_3.txt`.
>
> Dla danych przykładowych: 6.

```py
def waga(liczba):
    while liczba >= 10:
        suma = 0
        for cyfra in str(liczba):
            suma += int(cyfra)
        liczba = suma
    return liczba


ile = 0

with open("pierwsze.txt") as file:
    for line in file:
        if waga(int(line)) == 1:
            ile += 1

print(ile)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

long long waga(long long liczba) {
    while (liczba >= 10) {
        long long suma = 0;
        for (char cyfra : std::to_string(liczba))
            suma += cyfra - '0';
        liczba = suma;
    }
    return liczba;
}

int main() {
    int ile = 0;
    std::ifstream plik("pierwsze.txt");
    long long liczba;
    while (plik >> liczba)
        if (waga(liczba) == 1)
            ile++;
    std::println("{}", ile);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static long waga(long liczba) {
        while (liczba >= 10) {
            long suma = 0;
            for (char cyfra : String.valueOf(liczba).toCharArray())
                suma += cyfra - '0';
            liczba = suma;
        }
        return liczba;
    }

    public static void main(String[] args) throws Exception {
        int ile = 0;
        for (String line : Files.readAllLines(Path.of("pierwsze.txt")))
            if (!line.isBlank() && waga(Long.parseLong(line.trim())) == 1)
                ile++;
        System.out.println(ile);
    }
}
```

**Odpowiedź:** 27

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 5 (zbiornik wody). Ogród ma zbiornik na wodę o pojemności 25 000 litrów; 31 marca o 21:00 był pełny. Plik `pogoda.txt` zawiera (z wierszem nagłówkowym) średnią dobową temperaturę i opady dobowe w l/m² dla kolejnych dni od 1 kwietnia do 30 września 2015 r. Zasady:
> - temperatura i opady są mierzone od 20:00 dnia poprzedniego do 20:00 dnia bieżącego;
> - opady uzupełniają zbiornik o `700 · x` litrów (`x` — opady w l/m²), najwyżej do pełna;
> - w dni bezdeszczowe paruje `0,03% · T^1,5 · y` litrów (`T` — średnia temperatura, `y` — stan zbiornika o 21:00 dnia poprzedniego), zaokrąglone w górę;
> - ogród podlewa się o 20:00 w dni, gdy temperatura przekracza 15°C, a opady nie przekraczają 0,6 l/m²; zużywa się 12 000 l, a gdy temperatura przekracza 30°C — 24 000 l;
> - jeśli przed podlewaniem w zbiorniku brakuje wody, dolewa się go z wodociągu do pełna; podlewanie kończy się o 21:00.
>
> Wyniki zaokrąglaj w górę do pełnych litrów (kontrolnie: przez cały okres dolano 743 427 l). Odpowiedzi zapisz w pliku `wyniki5.txt`, poprzedzając je numerem zadania.
>
> Podaj datę, kiedy pierwszy raz trzeba było dolać wodę do zbiornika, oraz ilość dolanej wody.

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()  # nagłówek
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

## 5.2

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

## 5.3

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

**Odpowiedź:** kwiecień 0 l – 0 zł, maj 13172 l – 14 m3 – 164,36 zł, czerwiec 89444 l – 90 m3 – 1056,60 zł, lipiec 217938 l – 218 m3 – 2559,32 zł, sierpień 310099 l – 311 m3 – 3651,14 zł, wrzesień 112774 l – 113 m3 – 1326,62 zł

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `pogoda.txt` (temperatura średnia i opady, 1.04–30.09.2015).
>
> Podaj liczbę dni, w których:
> - temperatura nie przekraczała 15°C,
> - temperatura przekraczała 15°C, a opady nie przekraczały 0,6 l/m²,
> - temperatura przekraczała 15°C i opady przekraczały 0,6 l/m².

```py
chlodne = cieple_bez_deszczu = cieple_z_deszczem = 0

with open("pogoda.txt") as file:
    file.readline()
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
