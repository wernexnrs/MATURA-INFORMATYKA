<h1 align="center">Matura próbna 2021 — marzec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

Test diagnostyczny CKE – marzec 2021.

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

> **Treść zadania:** W turnieju pucharowym bierze udział n = 2^k drużyn o numerach 0…n−1; turniej trwa k rund. W 1. rundzie w meczu nr i grają drużyny 2(i−1) i 2(i−1)+1, a w kolejnych rundach w meczu nr i grają zwycięzcy meczów 2i−1 i 2i z poprzedniej rundy. Numer rundy, w której mogą się spotkać drużyny x i y, wynika z ich k-bitowych zapisów binarnych.
>
> - **1.1** — Uzupełnij tabelę: podaj numer rundy dla k=4, x=3, y=7 oraz k=5, x=16, y=30. (Przykłady: k=3, x=2, y=6 → 3; k=4, x=0, y=3 → 2.)
> - **1.2** — Napisz algorytm, który dla k ≥ 1 i różnych x, y z przedziału [0, 2^k − 1] wyznacza numer rundy, w której drużyny mogą się spotkać. Bez funkcji wbudowanych (w szczególności potęgowania).

```py
def runda(k, x, y):
    # drużyny spotkają się w rundzie r, gdy ich numery różnią się tylko na r ostatnich bitach,
    # więc dzielimy oba numery przez 2 (usuwamy ostatni bit), aż staną się równe
    r = 0
    while x != y:
        r += 1
        x //= 2
        y //= 2
    return r


for k, x, y in [(3, 2, 6), (4, 0, 3), (4, 3, 7), (5, 16, 30)]:
    print(k, x, y, runda(k, x, y))
```
```cpp
// C++23
#include <print>

int runda(int k, int x, int y) {
    // drużyny spotkają się w rundzie r, gdy ich numery różnią się tylko na r ostatnich bitach,
    // więc dzielimy oba numery przez 2 (usuwamy ostatni bit), aż staną się równe
    (void)k;  // k (liczba rund) nie jest potrzebne w obliczeniach
    int r = 0;
    while (x != y) {
        r++;
        x /= 2;
        y /= 2;
    }
    return r;
}

int main() {
    int dane[4][3] = {{3, 2, 6}, {4, 0, 3}, {4, 3, 7}, {5, 16, 30}};
    for (auto& [k, x, y] : dane)
        std::println("{} {} {} {}", k, x, y, runda(k, x, y));
}
```
```java
// Java 25
public class Zadanie {
    static int runda(int k, int x, int y) {
        // drużyny spotkają się w rundzie r, gdy ich numery różnią się tylko na r ostatnich bitach,
        // więc dzielimy oba numery przez 2 (usuwamy ostatni bit), aż staną się równe
        int r = 0;
        while (x != y) {
            r++;
            x /= 2;
            y /= 2;
        }
        return r;
    }

    public static void main(String[] args) throws Exception {
        int[][] dane = {{3, 2, 6}, {4, 0, 3}, {4, 3, 7}, {5, 16, 30}};
        for (var d : dane)
            System.out.println(d[0] + " " + d[1] + " " + d[2] + " " + runda(d[0], d[1], d[2]));
    }
}
```

**Odpowiedź:** 1.1: (3, 2, 6) → 3, (4, 0, 3) → 2, (4, 3, 7) → 3, (5, 16, 30) → 4; 1.2: algorytm w kodzie

## 2.1 i 2.2

> **Treść zadania:** Przeanalizuj funkcję Algo(n) dla dodatniej liczby całkowitej n (div — dzielenie całkowite):
>
> ```
> Algo(n)
>     jeżeli n ≤ 2 to wynikiem jest 1
>     p ← 1; k ← n
>     dopóki k − p > 1 wykonuj
>         s ← (p + k) div 2
>         jeżeli s * s ≤ n to p ← s
>         w przeciwnym przypadku k ← s
>     wynikiem jest p
> ```
>
> - **2.1** — Podaj wynik Algo(n) dla wartości n z tabeli arkusza (np. Algo(5) = 2).
> - **2.2** — Podaj, ile razy wykonuje się instrukcja `s ← (p + k) div 2` dla wartości n z tabeli (np. dla n = 5 — 2 razy).

```py
def Algo(n):
    ile_s = 0  # liczba wykonań instrukcji s <- (p + k) div 2
    if n <= 2:
        return 1, ile_s
    p = 1
    k = n
    while k - p > 1:
        s = (p + k) // 2
        ile_s += 1
        if s * s <= n:
            p = s
        else:
            k = s
    return p, ile_s


# 2.1
for n in [5, 35, 1025]:
    print(n, Algo(n)[0])
# 2.2
for n in [5, 2, 63, 1024]:
    print(n, Algo(n)[1])
```
```cpp
// C++23
#include <print>
#include <utility>

// zwraca parę: (wynik, liczba wykonań instrukcji s <- (p + k) div 2)
std::pair<int, int> Algo(int n) {
    int ile_s = 0;
    if (n <= 2) return {1, ile_s};
    int p = 1;
    int k = n;
    while (k - p > 1) {
        int s = (p + k) / 2;
        ile_s++;
        if (s * s <= n)
            p = s;
        else
            k = s;
    }
    return {p, ile_s};
}

int main() {
    // 2.1
    for (int n : {5, 35, 1025}) std::println("{} {}", n, Algo(n).first);
    // 2.2
    for (int n : {5, 2, 63, 1024}) std::println("{} {}", n, Algo(n).second);
}
```
```java
// Java 25
public class Zadanie {
    // zwraca tablicę: {wynik, liczba wykonań instrukcji s <- (p + k) div 2}
    static int[] Algo(int n) {
        int ileS = 0;
        if (n <= 2) return new int[] {1, ileS};
        int p = 1;
        int k = n;
        while (k - p > 1) {
            int s = (p + k) / 2;
            ileS++;
            if (s * s <= n)
                p = s;
            else
                k = s;
        }
        return new int[] {p, ileS};
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        for (int n : new int[] {5, 35, 1025}) System.out.println(n + " " + Algo(n)[0]);
        // 2.2
        for (int n : new int[] {5, 2, 63, 1024}) System.out.println(n + " " + Algo(n)[1]);
    }
}
```

**Odpowiedź:** 2.1: Algo(5) = 2, Algo(35) = 5, Algo(1025) = 32; 2.2: 5 → 2, 2 → 0, 63 → 6, 1024 → 10

## 4.1

> **Treść zadania:** Plik `galerie.txt` zawiera 50 wierszy, każdy opisuje planowaną galerię handlową: kod kraju, nazwę miasta (nazwy się nie powtarzają) i 70 par liczb — długość i szerokość (w metrach) prostokątnych lokali; brakujące lokale uzupełniono zerami. Plik `galerie_przyklad.txt` (10 wierszy) służy do testów.
>
> Dla każdego kraju podaj liczbę miast, w których powstaną galerie. Wynik zapisz w `wynik4_1.txt` (w wierszu: kod kraju i liczba miast).

```py
miasta = {}  # kod kraju -> liczba miast

with open("galerie.txt") as file:
    for line in file:
        kod_kraju = line.split()[0]
        miasta[kod_kraju] = miasta.get(kod_kraju, 0) + 1

with open("wynik4_1.txt", "w") as wynik:
    for kod_kraju, ile in miasta.items():
        print(kod_kraju, ile)
        wynik.write(f"{kod_kraju} {ile}\n")
```
```cpp
// C++23
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::map<std::string, int> miasta;  // kod kraju -> liczba miast
    std::vector<std::string> kolejnosc; // kody krajów w kolejności pojawienia się w pliku

    std::ifstream plik("galerie.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        std::istringstream ss(linia);
        std::string kod_kraju;
        if (!(ss >> kod_kraju)) continue;
        if (miasta[kod_kraju] == 0) kolejnosc.push_back(kod_kraju);
        miasta[kod_kraju]++;
    }

    std::ofstream wynik("wynik4_1.txt");
    for (auto& kod_kraju : kolejnosc) {
        std::println("{} {}", kod_kraju, miasta[kod_kraju]);
        wynik << kod_kraju << " " << miasta[kod_kraju] << "\n";
    }
}
```
```java
// Java 25
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var miasta = new LinkedHashMap<String, Integer>();  // kod kraju -> liczba miast (w kolejności z pliku)

        for (var linia : Files.readAllLines(Path.of("galerie.txt"))) {
            if (linia.isBlank()) continue;
            String kodKraju = linia.trim().split("\\s+")[0];
            miasta.merge(kodKraju, 1, Integer::sum);
        }

        try (var wynik = new PrintWriter("wynik4_1.txt")) {
            for (var e : miasta.entrySet()) {
                System.out.println(e.getKey() + " " + e.getValue());
                wynik.print(e.getKey() + " " + e.getValue() + "\n");
            }
        }
    }
}
```

**Odpowiedź:** GB 5, D 15, E 6, I 6, F 2, RO 1, A 1, H 1, BG 1, CZ 1, B 1, S 1, HR 1, NL 2, LV 1, GR 1, LT 1, FIN 1, DK 1, IRL 1

## 4.2

> **Treść zadania:** Dane z pliku `galerie.txt` (kraj, miasto, 70 par wymiarów lokali; zera oznaczają brak lokalu).
>
> - **a)** Dla każdej galerii oblicz łączną powierzchnię (sumę powierzchni lokali) i liczbę lokali; zapisz w `wynik4_2a.txt` wiersze: miasto, powierzchnia, liczba lokali.
> - **b)** Podaj miasto z galerią o największej i miasto z galerią o najmniejszej powierzchni całkowitej (każde jest jedno) wraz z tymi powierzchniami; zapisz w `wynik4_2b.txt`.

```py
galerie = []  # (miasto, powierzchnia, liczba lokali)

with open("galerie.txt") as file:
    for line in file:
        dane = line.split()
        miasto = dane[1]
        liczby = [int(x) for x in dane[2:]]
        powierzchnia = 0
        lokale = 0
        for i in range(0, len(liczby), 2):
            if liczby[i] != 0:  # zera uzupełniają wiersz do 70 par
                powierzchnia += liczby[i] * liczby[i + 1]
                lokale += 1
        galerie.append((miasto, powierzchnia, lokale))

# a)
with open("wynik4_2a.txt", "w") as wynik:
    for miasto, powierzchnia, lokale in galerie:
        print(miasto, powierzchnia, lokale)
        wynik.write(f"{miasto} {powierzchnia} {lokale}\n")

# b)
najwieksza = max(galerie, key=lambda g: g[1])
najmniejsza = min(galerie, key=lambda g: g[1])
with open("wynik4_2b.txt", "w") as wynik:
    for miasto, powierzchnia, lokale in [najwieksza, najmniejsza]:
        print(miasto, powierzchnia)
        wynik.write(f"{miasto} {powierzchnia}\n")
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

struct Galeria {
    std::string miasto;
    int powierzchnia;
    int lokale;
};

int main() {
    std::vector<Galeria> galerie;

    std::ifstream plik("galerie.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        std::istringstream ss(linia);
        std::string kod_kraju, miasto;
        if (!(ss >> kod_kraju >> miasto)) continue;
        int powierzchnia = 0;
        int lokale = 0;
        int a, b;
        while (ss >> a >> b) {
            if (a != 0) {  // zera uzupełniają wiersz do 70 par
                powierzchnia += a * b;
                lokale++;
            }
        }
        galerie.push_back({miasto, powierzchnia, lokale});
    }

    // a)
    std::ofstream wynik_a("wynik4_2a.txt");
    for (auto& [miasto, powierzchnia, lokale] : galerie) {
        std::println("{} {} {}", miasto, powierzchnia, lokale);
        wynik_a << miasto << " " << powierzchnia << " " << lokale << "\n";
    }

    // b) max_element / min_element zwracają pierwszy największy / najmniejszy element
    auto po_powierzchni = [](const Galeria& x, const Galeria& y) { return x.powierzchnia < y.powierzchnia; };
    Galeria najwieksza = *std::max_element(galerie.begin(), galerie.end(), po_powierzchni);
    Galeria najmniejsza = *std::min_element(galerie.begin(), galerie.end(), po_powierzchni);
    std::ofstream wynik_b("wynik4_2b.txt");
    for (auto& g : {najwieksza, najmniejsza}) {
        std::println("{} {}", g.miasto, g.powierzchnia);
        wynik_b << g.miasto << " " << g.powierzchnia << "\n";
    }
}
```
```java
// Java 25
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    record Galeria(String miasto, int powierzchnia, int lokale) {}

    public static void main(String[] args) throws Exception {
        var galerie = new ArrayList<Galeria>();

        for (var linia : Files.readAllLines(Path.of("galerie.txt"))) {
            if (linia.isBlank()) continue;
            var dane = linia.trim().split("\\s+");
            String miasto = dane[1];
            int powierzchnia = 0;
            int lokale = 0;
            for (int i = 2; i + 1 < dane.length; i += 2) {
                int a = Integer.parseInt(dane[i]);
                int b = Integer.parseInt(dane[i + 1]);
                if (a != 0) {  // zera uzupełniają wiersz do 70 par
                    powierzchnia += a * b;
                    lokale++;
                }
            }
            galerie.add(new Galeria(miasto, powierzchnia, lokale));
        }

        // a)
        try (var wynik = new PrintWriter("wynik4_2a.txt")) {
            for (var g : galerie) {
                System.out.println(g.miasto() + " " + g.powierzchnia() + " " + g.lokale());
                wynik.print(g.miasto() + " " + g.powierzchnia() + " " + g.lokale() + "\n");
            }
        }

        // b) przy remisie zostaje pierwsza galeria (jak max/min w Pythonie)
        Galeria najwieksza = galerie.get(0), najmniejsza = galerie.get(0);
        for (var g : galerie) {
            if (g.powierzchnia() > najwieksza.powierzchnia()) najwieksza = g;
            if (g.powierzchnia() < najmniejsza.powierzchnia()) najmniejsza = g;
        }
        try (var wynik = new PrintWriter("wynik4_2b.txt")) {
            for (var g : List.of(najwieksza, najmniejsza)) {
                System.out.println(g.miasto() + " " + g.powierzchnia());
                wynik.print(g.miasto() + " " + g.powierzchnia() + "\n");
            }
        }
    }
}
```

**Odpowiedź:** a) Londyn 3628 58, Berlin 3777 59, Madryt 2217 34, Rzym 3678 51, … , Duisburg 3948 61; b) Essen 4760, Wilno 1620

## 4.3

> **Treść zadania:** Dane z pliku `galerie.txt`. Dwa lokale są tego samego rodzaju, gdy mają równą powierzchnię.
>
> Podaj miasto z galerią o największej liczbie różnych rodzajów lokali oraz miasto z galerią o najmniejszej takiej liczbie (każde jest jedno), wraz z tymi liczbami. Wynik zapisz w `wynik4_3.txt` (dwa wiersze: miasto i liczba rodzajów).

```py
rodzaje = []  # (miasto, liczba różnych rodzajów lokali)

with open("galerie.txt") as file:
    for line in file:
        dane = line.split()
        miasto = dane[1]
        liczby = [int(x) for x in dane[2:]]
        powierzchnie = set()
        for i in range(0, len(liczby), 2):
            if liczby[i] != 0:
                powierzchnie.add(liczby[i] * liczby[i + 1])
        rodzaje.append((miasto, len(powierzchnie)))

najwiecej = max(rodzaje, key=lambda r: r[1])
najmniej = min(rodzaje, key=lambda r: r[1])

with open("wynik4_3.txt", "w") as wynik:
    for miasto, ile in [najwiecej, najmniej]:
        print(miasto, ile)
        wynik.write(f"{miasto} {ile}\n")
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::vector<std::pair<std::string, int>> rodzaje;  // (miasto, liczba różnych rodzajów lokali)

    std::ifstream plik("galerie.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        std::istringstream ss(linia);
        std::string kod_kraju, miasto;
        if (!(ss >> kod_kraju >> miasto)) continue;
        std::set<int> powierzchnie;
        int a, b;
        while (ss >> a >> b)
            if (a != 0) powierzchnie.insert(a * b);
        rodzaje.push_back({miasto, (int)powierzchnie.size()});
    }

    auto po_liczbie = [](const auto& x, const auto& y) { return x.second < y.second; };
    auto najwiecej = *std::max_element(rodzaje.begin(), rodzaje.end(), po_liczbie);
    auto najmniej = *std::min_element(rodzaje.begin(), rodzaje.end(), po_liczbie);

    std::ofstream wynik("wynik4_3.txt");
    for (auto& [miasto, ile] : {najwiecej, najmniej}) {
        std::println("{} {}", miasto, ile);
        wynik << miasto << " " << ile << "\n";
    }
}
```
```java
// Java 25
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    record Rodzaje(String miasto, int ile) {}

    public static void main(String[] args) throws Exception {
        var rodzaje = new ArrayList<Rodzaje>();  // (miasto, liczba różnych rodzajów lokali)

        for (var linia : Files.readAllLines(Path.of("galerie.txt"))) {
            if (linia.isBlank()) continue;
            var dane = linia.trim().split("\\s+");
            var powierzchnie = new HashSet<Integer>();
            for (int i = 2; i + 1 < dane.length; i += 2) {
                int a = Integer.parseInt(dane[i]);
                int b = Integer.parseInt(dane[i + 1]);
                if (a != 0) powierzchnie.add(a * b);
            }
            rodzaje.add(new Rodzaje(dane[1], powierzchnie.size()));
        }

        // przy remisie zostaje pierwsze miasto (jak max/min w Pythonie)
        Rodzaje najwiecej = rodzaje.get(0), najmniej = rodzaje.get(0);
        for (var r : rodzaje) {
            if (r.ile() > najwiecej.ile()) najwiecej = r;
            if (r.ile() < najmniej.ile()) najmniej = r;
        }

        try (var wynik = new PrintWriter("wynik4_3.txt")) {
            for (var r : List.of(najwiecej, najmniej)) {
                System.out.println(r.miasto() + " " + r.ile());
                wynik.print(r.miasto() + " " + r.ile() + "\n");
            }
        }
    }
}
```

**Odpowiedź:** Berlin 35, Kolonia 18

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Plik `telefony.txt` (2148 wierszy) opisuje połączenia firmy z lipca 2017: numer, data, godzina rozpoczęcia i zakończenia (`gg:mm:ss`), oddzielone spacjami. Numery 7-cyfrowe to stacjonarne, 8-cyfrowe — komórkowe, 10-cyfrowe i dłuższe — zagraniczne. Odpowiedzi zapisz w `wyniki5.txt`, poprzedzając je numerem zadania.
>
> Podaj trzy numery, pod które wykonano najwięcej połączeń, oraz liczby tych połączeń.

```py
polaczenia = {}

with open("telefony.txt") as file:
    file.readline()  # nagłówek
    for line in file:
        numer = line.split()[0]
        polaczenia[numer] = polaczenia.get(numer, 0) + 1

for numer, ile in sorted(polaczenia.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(numer, ile)
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <map>
#include <print>
#include <string>
#include <vector>

int main() {
    std::map<std::string, int> polaczenia;
    std::vector<std::string> numery;  // numery w kolejności pierwszego wystąpienia

    std::ifstream plik("telefony.txt");
    std::string naglowek;
    std::getline(plik, naglowek);  // nagłówek
    std::string numer, data, poczatek, koniec;
    while (plik >> numer >> data >> poczatek >> koniec) {
        if (polaczenia[numer] == 0) numery.push_back(numer);
        polaczenia[numer]++;
    }

    // stable_sort zachowuje kolejność numerów o tej samej liczbie połączeń (jak sorted w Pythonie)
    std::stable_sort(numery.begin(), numery.end(),
                     [&](const std::string& a, const std::string& b) { return polaczenia[a] > polaczenia[b]; });
    for (int i = 0; i < 3 && i < (int)numery.size(); i++)
        std::println("{} {}", numery[i], polaczenia[numery[i]]);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var polaczenia = new LinkedHashMap<String, Integer>();

        var linie = Files.readAllLines(Path.of("telefony.txt"));
        for (var linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            if (linia.isBlank()) continue;
            String numer = linia.trim().split("\\s+")[0];
            polaczenia.merge(numer, 1, Integer::sum);
        }

        // sortowanie w Javie jest stabilne - remisy zostają w kolejności z pliku (jak w Pythonie)
        var numery = new ArrayList<>(polaczenia.keySet());
        numery.sort((a, b) -> polaczenia.get(b) - polaczenia.get(a));
        for (var numer : numery.subList(0, Math.min(3, numery.size())))
            System.out.println(numer + " " + polaczenia.get(numer));
    }
}
```

**Odpowiedź:** 4546455 – 8, 3505978 – 7, 4657345 – 6

## 5.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `telefony.txt` (numer, data, początek, koniec połączenia).
>
> Utwórz zestawienie liczby połączeń do telefonów stacjonarnych i osobno komórkowych w poszczególnych dniach. Na jego podstawie wykonaj czytelny wykres kolumnowy (tytuł, opisy osi, legenda).

```py
stacjonarne = {}
komorkowe = {}

with open("telefony.txt") as file:
    file.readline()
    for line in file:
        numer, data, poczatek, koniec = line.split()
        if data not in stacjonarne:
            stacjonarne[data] = 0
            komorkowe[data] = 0
        if len(numer) == 7:
            stacjonarne[data] += 1
        elif len(numer) == 8:
            komorkowe[data] += 1

for data in stacjonarne:  # dni są w pliku w kolejności chronologicznej
    print(data, komorkowe[data], stacjonarne[data])
# na podstawie zestawienia należy jeszcze wykonać wykres kolumnowy
```
```cpp
// C++23
#include <fstream>
#include <map>
#include <print>
#include <string>
#include <vector>

int main() {
    std::map<std::string, int> stacjonarne;
    std::map<std::string, int> komorkowe;
    std::vector<std::string> dni;  // dni w kolejności z pliku

    std::ifstream plik("telefony.txt");
    std::string naglowek;
    std::getline(plik, naglowek);
    std::string numer, data, poczatek, koniec;
    while (plik >> numer >> data >> poczatek >> koniec) {
        if (!stacjonarne.contains(data)) {
            stacjonarne[data] = 0;
            komorkowe[data] = 0;
            dni.push_back(data);
        }
        if (numer.size() == 7)
            stacjonarne[data]++;
        else if (numer.size() == 8)
            komorkowe[data]++;
    }

    for (auto& data : dni)  // dni są w pliku w kolejności chronologicznej
        std::println("{} {} {}", data, komorkowe[data], stacjonarne[data]);
    // na podstawie zestawienia należy jeszcze wykonać wykres kolumnowy
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var stacjonarne = new LinkedHashMap<String, Integer>();  // pamięta kolejność dni z pliku
        var komorkowe = new HashMap<String, Integer>();

        var linie = Files.readAllLines(Path.of("telefony.txt"));
        for (var linia : linie.subList(1, linie.size())) {
            if (linia.isBlank()) continue;
            var dane = linia.trim().split("\\s+");
            String numer = dane[0], data = dane[1];
            if (!stacjonarne.containsKey(data)) {
                stacjonarne.put(data, 0);
                komorkowe.put(data, 0);
            }
            if (numer.length() == 7)
                stacjonarne.merge(data, 1, Integer::sum);
            else if (numer.length() == 8)
                komorkowe.merge(data, 1, Integer::sum);
        }

        for (var data : stacjonarne.keySet())  // dni są w pliku w kolejności chronologicznej
            System.out.println(data + " " + komorkowe.get(data) + " " + stacjonarne.get(data));
        // na podstawie zestawienia należy jeszcze wykonać wykres kolumnowy
    }
}
```

**Odpowiedź:** 3-07-2017: komórkowe 27, stacjonarne 67; 4-07-2017: 23, 68; 5-07-2017: 24, 79; … ; 31-07-2017: 23, 82 (łącznie 512 i 1524) (+ wykres kolumnowy)

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `telefony.txt`.
>
> Podaj liczbę połączeń do numerów stacjonarnych zaczynających się od `12` oraz łączny czas ich trwania zaokrąglony w górę do pełnych minut.

```py
import math


def sekundy(czas):
    g, m, s = czas.split(":")
    return int(g) * 3600 + int(m) * 60 + int(s)


ile = 0
czas = 0

with open("telefony.txt") as file:
    file.readline()
    for line in file:
        numer, data, poczatek, koniec = line.split()
        if len(numer) == 7 and numer.startswith("12"):
            ile += 1
            czas += sekundy(koniec) - sekundy(poczatek)

print(ile, math.ceil(czas / 60))
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int sekundy(const std::string& czas) {
    // czas w formacie gg:mm:ss
    int g = std::stoi(czas.substr(0, 2));
    int m = std::stoi(czas.substr(3, 2));
    int s = std::stoi(czas.substr(6, 2));
    return g * 3600 + m * 60 + s;
}

int main() {
    int ile = 0;
    int czas = 0;

    std::ifstream plik("telefony.txt");
    std::string naglowek;
    std::getline(plik, naglowek);
    std::string numer, data, poczatek, koniec;
    while (plik >> numer >> data >> poczatek >> koniec) {
        if (numer.size() == 7 && numer.starts_with("12")) {
            ile++;
            czas += sekundy(koniec) - sekundy(poczatek);
        }
    }

    std::println("{} {}", ile, (czas + 59) / 60);  // zaokrąglenie w górę do pełnych minut
}
```
```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    static int sekundy(String czas) {
        var gms = czas.split(":");
        return Integer.parseInt(gms[0]) * 3600 + Integer.parseInt(gms[1]) * 60 + Integer.parseInt(gms[2]);
    }

    public static void main(String[] args) throws Exception {
        int ile = 0;
        int czas = 0;

        var linie = Files.readAllLines(Path.of("telefony.txt"));
        for (var linia : linie.subList(1, linie.size())) {
            if (linia.isBlank()) continue;
            var dane = linia.trim().split("\\s+");
            String numer = dane[0], poczatek = dane[2], koniec = dane[3];
            if (numer.length() == 7 && numer.startsWith("12")) {
                ile++;
                czas += sekundy(koniec) - sekundy(poczatek);
            }
        }

        System.out.println(ile + " " + (czas + 59) / 60);  // zaokrąglenie w górę do pełnych minut
    }
}
```

**Odpowiedź:** 21 połączeń, 192 minuty

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `telefony.txt`. Zasady rachunku:
>
> - abonament 50 zł obejmuje pierwsze 800 minut połączeń krajowych (stacjonarne + komórkowe łącznie);
> - po wyczerpaniu limitu minuty rozlicza się w pakietach po 100: każdy rozpoczęty pakiet do stacjonarnych kosztuje 5 zł, do komórkowych 6 zł;
> - połączenia zagraniczne: 1 zł za każdą rozpoczętą minutę rozmowy (np. 2:02 → 3 zł).
>
> Podaj łączną kwotę rachunku oraz osobno: abonament i koszty połączeń stacjonarnych, komórkowych i zagranicznych.

```py
import math


def sekundy(czas):
    g, m, s = czas.split(":")
    return int(g) * 3600 + int(m) * 60 + int(s)


ABONAMENT = 50
LIMIT = 800 * 60  # w sekundach

wykorzystane = 0      # sekundy rozmów krajowych wliczone w abonament
stacjonarne = 0       # sekundy rozmów ponad limit
komorkowe = 0
zagraniczne_zl = 0

with open("telefony.txt") as file:
    file.readline()
    for line in file:  # połączenia są zapisane chronologicznie
        numer, data, poczatek, koniec = line.split()
        czas = sekundy(koniec) - sekundy(poczatek)
        if len(numer) >= 10:
            zagraniczne_zl += math.ceil(czas / 60)  # 1 zł za każdą rozpoczętą minutę
            continue
        z_abonamentu = min(czas, LIMIT - wykorzystane)
        wykorzystane += z_abonamentu
        if len(numer) == 7:
            stacjonarne += czas - z_abonamentu
        else:
            komorkowe += czas - z_abonamentu

# każdy rozpoczęty pakiet 100 minut
stacjonarne_zl = math.ceil(stacjonarne / 6000) * 5
komorkowe_zl = math.ceil(komorkowe / 6000) * 6

print("abonament", ABONAMENT)
print("stacjonarne", stacjonarne_zl)
print("komórkowe", komorkowe_zl)
print("zagraniczne", zagraniczne_zl)
print("suma", ABONAMENT + stacjonarne_zl + komorkowe_zl + zagraniczne_zl)
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>

int sekundy(const std::string& czas) {
    // czas w formacie gg:mm:ss
    int g = std::stoi(czas.substr(0, 2));
    int m = std::stoi(czas.substr(3, 2));
    int s = std::stoi(czas.substr(6, 2));
    return g * 3600 + m * 60 + s;
}

// dzielenie z zaokrągleniem w górę (dla liczb nieujemnych)
int sufit(int a, int b) { return (a + b - 1) / b; }

int main() {
    const int ABONAMENT = 50;
    const int LIMIT = 800 * 60;  // w sekundach

    int wykorzystane = 0;    // sekundy rozmów krajowych wliczone w abonament
    int stacjonarne = 0;     // sekundy rozmów ponad limit
    int komorkowe = 0;
    int zagraniczne_zl = 0;

    std::ifstream plik("telefony.txt");
    std::string naglowek;
    std::getline(plik, naglowek);
    std::string numer, data, poczatek, koniec;
    while (plik >> numer >> data >> poczatek >> koniec) {  // połączenia są zapisane chronologicznie
        int czas = sekundy(koniec) - sekundy(poczatek);
        if (numer.size() >= 10) {
            zagraniczne_zl += sufit(czas, 60);  // 1 zł za każdą rozpoczętą minutę
            continue;
        }
        int z_abonamentu = std::min(czas, LIMIT - wykorzystane);
        wykorzystane += z_abonamentu;
        if (numer.size() == 7)
            stacjonarne += czas - z_abonamentu;
        else
            komorkowe += czas - z_abonamentu;
    }

    // każdy rozpoczęty pakiet 100 minut
    int stacjonarne_zl = sufit(stacjonarne, 6000) * 5;
    int komorkowe_zl = sufit(komorkowe, 6000) * 6;

    std::println("abonament {}", ABONAMENT);
    std::println("stacjonarne {}", stacjonarne_zl);
    std::println("komórkowe {}", komorkowe_zl);
    std::println("zagraniczne {}", zagraniczne_zl);
    std::println("suma {}", ABONAMENT + stacjonarne_zl + komorkowe_zl + zagraniczne_zl);
}
```
```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    static int sekundy(String czas) {
        var gms = czas.split(":");
        return Integer.parseInt(gms[0]) * 3600 + Integer.parseInt(gms[1]) * 60 + Integer.parseInt(gms[2]);
    }

    // dzielenie z zaokrągleniem w górę (dla liczb nieujemnych)
    static int sufit(int a, int b) { return (a + b - 1) / b; }

    public static void main(String[] args) throws Exception {
        final int ABONAMENT = 50;
        final int LIMIT = 800 * 60;  // w sekundach

        int wykorzystane = 0;    // sekundy rozmów krajowych wliczone w abonament
        int stacjonarne = 0;     // sekundy rozmów ponad limit
        int komorkowe = 0;
        int zagraniczneZl = 0;

        var linie = Files.readAllLines(Path.of("telefony.txt"));
        for (var linia : linie.subList(1, linie.size())) {  // połączenia są zapisane chronologicznie
            if (linia.isBlank()) continue;
            var dane = linia.trim().split("\\s+");
            String numer = dane[0];
            int czas = sekundy(dane[3]) - sekundy(dane[2]);
            if (numer.length() >= 10) {
                zagraniczneZl += sufit(czas, 60);  // 1 zł za każdą rozpoczętą minutę
                continue;
            }
            int zAbonamentu = Math.min(czas, LIMIT - wykorzystane);
            wykorzystane += zAbonamentu;
            if (numer.length() == 7)
                stacjonarne += czas - zAbonamentu;
            else
                komorkowe += czas - zAbonamentu;
        }

        // każdy rozpoczęty pakiet 100 minut
        int stacjonarneZl = sufit(stacjonarne, 6000) * 5;
        int komorkoweZl = sufit(komorkowe, 6000) * 6;

        System.out.println("abonament " + ABONAMENT);
        System.out.println("stacjonarne " + stacjonarneZl);
        System.out.println("komórkowe " + komorkoweZl);
        System.out.println("zagraniczne " + zagraniczneZl);
        System.out.println("suma " + (ABONAMENT + stacjonarneZl + komorkoweZl + zagraniczneZl));
    }
}
```

**Odpowiedź:** abonament 50 zł, stacjonarne 610 zł, komórkowe 240 zł, zagraniczne 967 zł, razem 1867 zł
