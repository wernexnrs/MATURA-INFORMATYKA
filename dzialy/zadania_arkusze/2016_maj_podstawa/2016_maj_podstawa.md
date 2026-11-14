<h1 align="center">Matura 2016 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa-odpowiedzi.pdf)

## 1.1

> **Treść zadania:** Kompresja. Algorytm zastępuje każdą grupę kolejnych jednakowych znaków jednym wystąpieniem tego znaku poprzedzonym liczbą jego kolejnych wystąpień (liczba ta nie przekracza 9, więc zajmuje jeden znak). Np. tekst `FFFYYYYYYYYYFFFHAAAAA` (21 znaków) po kompresji to `3F9Y3F1H5A` (10 znaków).
>
> Skompresuj tym algorytmem tekst `***##!!*` i podaj rozmiar tekstu (w znakach) przed kompresją i po niej.

```py
def kompresuj(tekst):
    wynik = ""
    i = 0
    while i < len(tekst):
        j = i
        while j < len(tekst) and tekst[j] == tekst[i]:
            j += 1
        wynik += str(j - i) + tekst[i]
        i = j
    return wynik


skompresowany = kompresuj("***##!!*")
print(skompresowany, len("***##!!*"), len(skompresowany))
```

```cpp
// C++23
#include <iostream>
#include <string>

std::string kompresuj(const std::string& tekst) {
    std::string wynik = "";
    size_t i = 0;
    while (i < tekst.size()) {
        size_t j = i;
        while (j < tekst.size() && tekst[j] == tekst[i])
            j++;
        wynik += std::to_string(j - i) + tekst[i];
        i = j;
    }
    return wynik;
}

int main() {
    std::string tekst = "***##!!*";
    std::string skompresowany = kompresuj(tekst);
    std::cout << skompresowany << ' ' << tekst.size() << ' ' << skompresowany.size() << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static String kompresuj(String tekst) {
        var wynik = new StringBuilder();
        int i = 0;
        while (i < tekst.length()) {
            int j = i;
            while (j < tekst.length() && tekst.charAt(j) == tekst.charAt(i))
                j++;
            wynik.append(j - i).append(tekst.charAt(i));
            i = j;
        }
        return wynik.toString();
    }

    public static void main(String[] args) {
        String tekst = "***##!!*";
        String skompresowany = kompresuj(tekst);
        System.out.println(skompresowany + " " + tekst.length() + " " + skompresowany.length());
    }
}
```
**Odpowiedź:** 3\*2#2!1\*, rozmiar przed kompresją 8, po kompresji 8; 1.2: co najmniej 3 kolejne znaki; 1.3: bezstratna

## 1.4

> **Treść zadania:** Kompresja: każda grupa kolejnych jednakowych znaków (co najwyżej 9) jest zapisywana jako liczba wystąpień i ten znak, np. `FFFYYYYYYYYYFFFHAAAAA` → `3F9Y3F1H5A`. Zapisz (lista kroków, schemat blokowy, pseudokod lub język programowania) algorytm obliczający rozmiar skompresowanego tekstu.
>
> Specyfikacja:
> - Dane: `n` — dodatnia liczba całkowita, długość tekstu; `T[1..n]` — tablica z tekstem, T[i] to i-ty znak.
> - Wynik: `b` — rozmiar skompresowanego tekstu T.

```py
def rozmiar_po_kompresji(n, T):
    r = 1  # liczba grup takich samych znaków
    for i in range(1, n):
        if T[i] != T[i - 1]:
            r += 1
    return 2 * r


tekst = "FFFYYYYYYYYYFFFHAAAAA"
print(rozmiar_po_kompresji(len(tekst), tekst))
```

```cpp
// C++23
#include <iostream>
#include <string>

int rozmiar_po_kompresji(int n, const std::string& T) {
    int r = 1;  // liczba grup takich samych znaków
    for (int i = 1; i < n; i++)
        if (T[i] != T[i - 1])
            r++;
    return 2 * r;
}

int main() {
    std::string tekst = "FFFYYYYYYYYYFFFHAAAAA";
    std::cout << rozmiar_po_kompresji(tekst.size(), tekst) << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static int rozmiarPoKompresji(int n, String T) {
        int r = 1;  // liczba grup takich samych znaków
        for (int i = 1; i < n; i++)
            if (T.charAt(i) != T.charAt(i - 1))
                r++;
        return 2 * r;
    }

    public static void main(String[] args) {
        String tekst = "FFFYYYYYYYYYFFFHAAAAA";
        System.out.println(rozmiarPoKompresji(tekst.length(), tekst));
    }
}
```
**Odpowiedź:** dla przykładu z treści – 10

## 2.1 i 2.3

> **Treść zadania:** Zapis liczb. Każdą liczbę naturalną n można zapisać jako sumę jej cyfr i iloczynu pewnego naturalnego współczynnika k oraz liczby 9, np. 19 = 1 + 9 + (1 · 9), 123 = 1 + 2 + 3 + (13 · 9).
> - 2.1 — Podaj rozkład i współczynnik k dla liczb 42, 375 i 913 (dla 11: 1 + 1 + (1 · 9), k = 1).
> - 2.3 — Zapisz algorytm, który dla danej liczby naturalnej n oblicza współczynnik k z jej rozkładu. Można używać tylko dodawania, odejmowania, mnożenia, dzielenia całkowitego i reszty z dzielenia oraz funkcji `suma_cyfr(n)` zwracającej sumę cyfr n.

```py
def suma_cyfr(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


def wspolczynnik(n):
    return (n - suma_cyfr(n)) // 9


for n in [11, 42, 375, 913]:
    print(n, "=", suma_cyfr(n), "+", wspolczynnik(n), "* 9", "  k =", wspolczynnik(n))
```

```cpp
// C++23
#include <iostream>

int suma_cyfr(int n) {
    int s = 0;
    while (n > 0) {
        s = s + n % 10;
        n = n / 10;
    }
    return s;
}

int wspolczynnik(int n) {
    return (n - suma_cyfr(n)) / 9;
}

int main() {
    for (int n : {11, 42, 375, 913})
        std::cout << n << " = " << suma_cyfr(n) << " + " << wspolczynnik(n) << " * 9   k = " << wspolczynnik(n) << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static int sumaCyfr(int n) {
        int s = 0;
        while (n > 0) {
            s = s + n % 10;
            n = n / 10;
        }
        return s;
    }

    static int wspolczynnik(int n) {
        return (n - sumaCyfr(n)) / 9;
    }

    public static void main(String[] args) {
        for (int n : new int[] {11, 42, 375, 913})
            System.out.println(n + " = " + sumaCyfr(n) + " + " + wspolczynnik(n) + " * 9   k = " + wspolczynnik(n));
    }
}
```
**Odpowiedź:** 42 → k = 4; 375 → k = 40; 913 → k = 100 (2.2 – funkcja `suma_cyfr`)

## 4.1

> **Treść zadania:** Plik `demografia.txt` zawiera dane o urodzeniach, zgonach i ruchu naturalnym ludności w Polsce w 2009 roku w podziale na powiaty. Kolumny: powiat, województwo, ludność ogółem, współczynnik urodzeń, współczynnik zgonów, saldo migracji (pierwszy wiersz to nagłówek; np. `augustowski podlaskie 58763 10,4 10,5 -1,1`). Odpowiedzi zapisz w pliku `wyniki_4.txt`, poprzedzając je numerem zadania.
>
> Podaj liczbę powiatów województwa mazowieckiego, w których saldo migracji było ujemne.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
count = 0

with open("demografia.txt") as file:
    next(file)  # pomijamy nagłówek
    for line in file:
        dane = line.strip().split("\t")
        saldo = float(dane[5].replace(",", "."))
        if dane[1] == "mazowieckie" and saldo < 0:
            count += 1

print(count)
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz po tabulatorach (bez końcowego \r)
std::vector<std::string> podziel(std::string line) {
    if (!line.empty() && line.back() == '\r') line.pop_back();
    std::vector<std::string> dane;
    std::stringstream ss(line);
    std::string pole;
    while (std::getline(ss, pole, '\t')) dane.push_back(pole);
    return dane;
}

double liczba(std::string s) {  // "10,4" -> 10.4
    for (char& c : s)
        if (c == ',') c = '.';
    return std::stod(s);
}

int main() {
    int count = 0;
    std::ifstream plik("demografia.txt");
    std::string line;
    std::getline(plik, line);  // pomijamy nagłówek
    while (std::getline(plik, line)) {
        auto dane = podziel(line);
        double saldo = liczba(dane[5]);
        if (dane[1] == "mazowieckie" && saldo < 0)
            count++;
    }
    std::cout << count << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int count = 0;
        var linie = Files.readAllLines(Path.of("demografia.txt"));
        for (var line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            var dane = line.strip().split("\t");
            double saldo = Double.parseDouble(dane[5].replace(",", "."));
            if (dane[1].equals("mazowieckie") && saldo < 0)
                count++;
        }
        System.out.println(count);
    }
}
```
**Odpowiedź:** 24

## 4.2

> **Treść zadania:** Dane z pliku `demografia.txt` (powiat, województwo, ludność, współczynnik urodzeń, współczynnik zgonów, saldo migracji). Współczynnik przyrostu naturalnego to różnica współczynnika urodzeń i współczynnika zgonów. Utwórz zestawienie 10 powiatów o największym współczynniku przyrostu naturalnego (nazwa powiatu i współczynnik), uporządkowane alfabetycznie.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
powiaty = []

with open("demografia.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        urodzenia = float(dane[3].replace(",", "."))
        zgony = float(dane[4].replace(",", "."))
        powiaty.append((round(urodzenia - zgony, 1), dane[0]))

powiaty.sort(reverse=True)
for przyrost, powiat in sorted(powiaty[:10], key=lambda x: x[1]):
    print(powiat, przyrost)
```

```cpp
// C++23
#include <algorithm>
#include <format>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

std::vector<std::string> podziel(std::string line) {  // dzieli wiersz po tabulatorach
    if (!line.empty() && line.back() == '\r') line.pop_back();
    std::vector<std::string> dane;
    std::stringstream ss(line);
    std::string pole;
    while (std::getline(ss, pole, '\t')) dane.push_back(pole);
    return dane;
}

double liczba(std::string s) {  // "10,4" -> 10.4
    for (char& c : s)
        if (c == ',') c = '.';
    return std::stod(s);
}

int main() {
    std::vector<std::pair<double, std::string>> powiaty;  // (przyrost, powiat)

    std::ifstream plik("demografia.txt");
    std::string line;
    std::getline(plik, line);
    while (std::getline(plik, line)) {
        auto dane = podziel(line);
        double urodzenia = liczba(dane[3]);
        double zgony = liczba(dane[4]);
        // zaokrąglenie do 1 miejsca jak round(x, 1) w Pythonie: zapis "{:.1f}" i z powrotem na liczbę
        double przyrost = std::stod(std::format("{:.1f}", urodzenia - zgony));
        powiaty.push_back({przyrost, dane[0]});
    }

    std::ranges::sort(powiaty, std::greater{});  // malejąco, jak sort(reverse=True)
    std::vector<std::pair<double, std::string>> najlepsze(powiaty.begin(), powiaty.begin() + 10);
    std::ranges::stable_sort(najlepsze, {}, &std::pair<double, std::string>::second);
    for (const auto& [przyrost, powiat] : najlepsze)
        std::cout << powiat << ' ' << std::format("{:.1f}", przyrost) << '\n';
}
```

```java
// Java 25
import java.math.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    record Powiat(double przyrost, String nazwa) {}

    public static void main(String[] args) throws Exception {
        var powiaty = new ArrayList<Powiat>();
        var linie = Files.readAllLines(Path.of("demografia.txt"));
        for (var line : linie.subList(1, linie.size())) {
            var dane = line.strip().split("\t");
            double urodzenia = Double.parseDouble(dane[3].replace(",", "."));
            double zgony = Double.parseDouble(dane[4].replace(",", "."));
            // zaokrąglenie do 1 miejsca dokładnie jak round(x, 1) w Pythonie
            double przyrost = new BigDecimal(urodzenia - zgony).setScale(1, RoundingMode.HALF_EVEN).doubleValue();
            powiaty.add(new Powiat(przyrost, dane[0]));
        }

        // malejąco po (przyrost, nazwa), jak sort(reverse=True) na krotkach
        powiaty.sort(Comparator.comparingDouble(Powiat::przyrost).thenComparing(Powiat::nazwa).reversed());
        var najlepsze = new ArrayList<>(powiaty.subList(0, 10));
        najlepsze.sort(Comparator.comparing(Powiat::nazwa));
        for (var p : najlepsze)
            System.out.println(p.nazwa() + " " + p.przyrost());
    }
}
```
**Odpowiedź:** bytowski 5,7; gdanski 6,0; kartuski 8,7; koscierski 7,2; limanowski 6,4; m Zory 5,7; nowosadecki 6,1; poznanski 6,0; pszczynski 5,5; wejherowski 7,2

## 4.3

> **Treść zadania:** Dane z pliku `demografia.txt` (powiat, województwo, ludność ogółem, …). Podaj nazwy czterech województw o największej liczbie ludności oraz liczbę ludności każdego z nich.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
ludnosc = {}

with open("demografia.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        ludnosc[dane[1]] = ludnosc.get(dane[1], 0) + int(dane[2])

wojewodztwa = sorted(ludnosc, key=ludnosc.get, reverse=True)
for wojewodztwo in wojewodztwa[:4]:
    print(wojewodztwo, ludnosc[wojewodztwo])
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> podziel(std::string line) {  // dzieli wiersz po tabulatorach
    if (!line.empty() && line.back() == '\r') line.pop_back();
    std::vector<std::string> dane;
    std::stringstream ss(line);
    std::string pole;
    while (std::getline(ss, pole, '\t')) dane.push_back(pole);
    return dane;
}

int main() {
    std::map<std::string, long long> ludnosc;
    std::vector<std::string> wojewodztwa;  // kolejność pierwszego pojawienia się (jak klucze słownika w Pythonie)

    std::ifstream plik("demografia.txt");
    std::string line;
    std::getline(plik, line);
    while (std::getline(plik, line)) {
        auto dane = podziel(line);
        if (!ludnosc.contains(dane[1])) wojewodztwa.push_back(dane[1]);
        ludnosc[dane[1]] += std::stoll(dane[2]);
    }

    std::ranges::stable_sort(wojewodztwa, [&](const std::string& a, const std::string& b) {
        return ludnosc[a] > ludnosc[b];
    });
    for (int i = 0; i < 4; i++)
        std::cout << wojewodztwa[i] << ' ' << ludnosc[wojewodztwa[i]] << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var ludnosc = new LinkedHashMap<String, Long>();  // zachowuje kolejność, jak słownik w Pythonie
        var linie = Files.readAllLines(Path.of("demografia.txt"));
        for (var line : linie.subList(1, linie.size())) {
            var dane = line.strip().split("\t");
            ludnosc.merge(dane[1], Long.parseLong(dane[2]), Long::sum);
        }

        var wojewodztwa = new ArrayList<>(ludnosc.keySet());
        wojewodztwa.sort(Comparator.comparing((String w) -> ludnosc.get(w)).reversed());
        for (var wojewodztwo : wojewodztwa.subList(0, 4))
            System.out.println(wojewodztwo + " " + ludnosc.get(wojewodztwo));
    }
}
```
**Odpowiedź:** mazowieckie 5222167, slaskie 4640725, wielkopolskie 3408281, malopolskie 3298270

## 4.4

> **Treść zadania:** Dane z pliku `demografia.txt`. Współczynnik urodzeń to liczba urodzeń na 1000 mieszkańców: wsp_urodzen = liczba_urodzen / ludnosc_ogolem · 1000. Dla województwa opolskiego wykonaj alfabetycznie posortowane zestawienie powiatów wraz z liczbą urodzeń w 2009 roku w każdym z nich (obliczoną z ludności i współczynnika urodzeń, zaokrągloną w dół do liczby całkowitej). Na jego podstawie utwórz poprawnie opisany wykres kolumnowy.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
urodzenia = []

with open("demografia.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        if dane[1] == "opolskie":
            # współczynnik w dziesiątych częściach (np. 10,4 -> 104), żeby liczyć na liczbach całkowitych
            wsp = round(float(dane[3].replace(",", ".")) * 10)
            urodzenia.append((dane[0], int(dane[2]) * wsp // 10000))

for powiat, liczba in sorted(urodzenia):
    print(powiat, liczba)
```

```cpp
// C++23
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

std::vector<std::string> podziel(std::string line) {  // dzieli wiersz po tabulatorach
    if (!line.empty() && line.back() == '\r') line.pop_back();
    std::vector<std::string> dane;
    std::stringstream ss(line);
    std::string pole;
    while (std::getline(ss, pole, '\t')) dane.push_back(pole);
    return dane;
}

double liczba(std::string s) {  // "10,4" -> 10.4
    for (char& c : s)
        if (c == ',') c = '.';
    return std::stod(s);
}

int main() {
    std::vector<std::pair<std::string, long long>> urodzenia;

    std::ifstream plik("demografia.txt");
    std::string line;
    std::getline(plik, line);
    while (std::getline(plik, line)) {
        auto dane = podziel(line);
        if (dane[1] == "opolskie") {
            // współczynnik w dziesiątych częściach (np. 10,4 -> 104), żeby liczyć na liczbach całkowitych
            // (std::nearbyint zaokrągla jak round() w Pythonie)
            long long wsp = static_cast<long long>(std::nearbyint(liczba(dane[3]) * 10));
            urodzenia.push_back({dane[0], std::stoll(dane[2]) * wsp / 10000});
        }
    }

    std::ranges::sort(urodzenia);
    for (const auto& [powiat, ile] : urodzenia)
        std::cout << powiat << ' ' << ile << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    record Powiat(String nazwa, long urodzenia) {}

    public static void main(String[] args) throws Exception {
        var urodzenia = new ArrayList<Powiat>();
        var linie = Files.readAllLines(Path.of("demografia.txt"));
        for (var line : linie.subList(1, linie.size())) {
            var dane = line.strip().split("\t");
            if (dane[1].equals("opolskie")) {
                // współczynnik w dziesiątych częściach (np. 10,4 -> 104), żeby liczyć na liczbach całkowitych
                // (Math.rint zaokrągla jak round() w Pythonie)
                long wsp = (long) Math.rint(Double.parseDouble(dane[3].replace(",", ".")) * 10);
                urodzenia.add(new Powiat(dane[0], Long.parseLong(dane[2]) * wsp / 10000));
            }
        }

        urodzenia.sort(Comparator.comparing(Powiat::nazwa).thenComparingLong(Powiat::urodzenia));
        for (var p : urodzenia)
            System.out.println(p.nazwa() + " " + p.urodzenia());
    }
}
```
**Odpowiedź:** brzeski 995, glubczycki 459, kedzierzynsko-kozielski 812, kluczborski 591, krapkowicki 561, m Opole 1182, namyslowski 473, nyski 1337, oleski 584, opolski 1093, prudnicki 528, strzelecki 657 (wykres kolumnowy wykonuje się w arkuszu kalkulacyjnym)

## 6.1

> **Treść zadania:** Liczba pierwsza to liczba naturalna większa od 1, mająca dokładnie dwa dzielniki naturalne: 1 i samą siebie. W pliku `dane_6.txt` jest 2000 liczb całkowitych z zakresu ⟨0, 30000⟩, każda w osobnym wierszu. Odpowiedzi zapisz w pliku `wyniki_6.txt`, poprzedzając je numerem zadania.
>
> Podaj, ile liczb z pliku to liczby pierwsze.

W arkuszu plik nazywa się `dane_6.txt`, w paczce z danymi CKE – `dane4.txt`.

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


count = 0

with open("dane4.txt") as file:
    for line in file:
        if czy_pierwsza(int(line)):
            count += 1

print(count)
```

```cpp
// C++23
#include <fstream>
#include <iostream>

bool czy_pierwsza(int x) {
    if (x < 2)
        return false;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0)
            return false;
    return true;
}

int main() {
    int count = 0;
    std::ifstream plik("dane4.txt");
    int liczba;
    while (plik >> liczba)
        if (czy_pierwsza(liczba))
            count++;
    std::cout << count << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    static boolean czyPierwsza(int x) {
        if (x < 2)
            return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0)
                return false;
        return true;
    }

    public static void main(String[] args) throws Exception {
        int count = 0;
        for (var line : Files.readAllLines(Path.of("dane4.txt")))
            if (czyPierwsza(Integer.parseInt(line.strip())))
                count++;
        System.out.println(count);
    }
}
```
**Odpowiedź:** 236

## 6.2

> **Treść zadania:** Plik `dane_6.txt` zawiera 2000 liczb całkowitych z zakresu ⟨0, 30000⟩. Podaj największą i najmniejszą liczbę pierwszą występującą w pliku. Odpowiedź zapisz w `wyniki_6.txt`.

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


pierwsze = []

with open("dane4.txt") as file:
    for line in file:
        liczba = int(line)
        if czy_pierwsza(liczba):
            pierwsze.append(liczba)

print("max =", max(pierwsze), "min =", min(pierwsze))
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

bool czy_pierwsza(int x) {
    if (x < 2)
        return false;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0)
            return false;
    return true;
}

int main() {
    std::vector<int> pierwsze;
    std::ifstream plik("dane4.txt");
    int liczba;
    while (plik >> liczba)
        if (czy_pierwsza(liczba))
            pierwsze.push_back(liczba);

    std::cout << "max = " << std::ranges::max(pierwsze) << " min = " << std::ranges::min(pierwsze) << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static boolean czyPierwsza(int x) {
        if (x < 2)
            return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0)
                return false;
        return true;
    }

    public static void main(String[] args) throws Exception {
        var pierwsze = new ArrayList<Integer>();
        for (var line : Files.readAllLines(Path.of("dane4.txt"))) {
            int liczba = Integer.parseInt(line.strip());
            if (czyPierwsza(liczba))
                pierwsze.add(liczba);
        }
        System.out.println("max = " + Collections.max(pierwsze) + " min = " + Collections.min(pierwsze));
    }
}
```
**Odpowiedź:** max = 29881, min = 73

## 6.3

> **Treść zadania:** Plik `dane_6.txt` zawiera 2000 liczb całkowitych z zakresu ⟨0, 30000⟩. Liczby bliźniacze to dwie liczby pierwsze różniące się o 2, np. (3, 5), (5, 3), (11, 13), (19, 17). Zbadaj kolejne pary sąsiednich liczb w pliku (pierwsza i druga, druga i trzecia, …, przedostatnia i ostatnia). Podaj liczbę par liczb bliźniaczych i wypisz wszystkie te pary, każdą w osobnym wierszu. Odpowiedź zapisz w `wyniki_6.txt`.
>
> Przykład: dla liczb 11698, 13234, 1999, 1997, 16444, 15173, 5927 odpowiedzią jest 1 oraz para 1999 i 1997.

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


liczby = []

with open("dane4.txt") as file:
    for line in file:
        liczby.append(int(line))

pary = []
for i in range(1, len(liczby)):
    a = liczby[i - 1]
    b = liczby[i]
    if abs(a - b) == 2 and czy_pierwsza(a) and czy_pierwsza(b):
        pary.append((a, b))

print(len(pary))
for a, b in pary:
    print(a, b)
```

```cpp
// C++23
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <utility>
#include <vector>

bool czy_pierwsza(int x) {
    if (x < 2)
        return false;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0)
            return false;
    return true;
}

int main() {
    std::vector<int> liczby;
    std::ifstream plik("dane4.txt");
    int liczba;
    while (plik >> liczba)
        liczby.push_back(liczba);

    std::vector<std::pair<int, int>> pary;
    for (size_t i = 1; i < liczby.size(); i++) {
        int a = liczby[i - 1];
        int b = liczby[i];
        if (std::abs(a - b) == 2 && czy_pierwsza(a) && czy_pierwsza(b))
            pary.push_back({a, b});
    }

    std::cout << pary.size() << '\n';
    for (auto [a, b] : pary)
        std::cout << a << ' ' << b << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static boolean czyPierwsza(int x) {
        if (x < 2)
            return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0)
                return false;
        return true;
    }

    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<Integer>();
        for (var line : Files.readAllLines(Path.of("dane4.txt")))
            liczby.add(Integer.parseInt(line.strip()));

        var pary = new ArrayList<int[]>();
        for (int i = 1; i < liczby.size(); i++) {
            int a = liczby.get(i - 1);
            int b = liczby.get(i);
            if (Math.abs(a - b) == 2 && czyPierwsza(a) && czyPierwsza(b))
                pary.add(new int[] {a, b});
        }

        System.out.println(pary.size());
        for (var p : pary)
            System.out.println(p[0] + " " + p[1]);
    }
}
```
**Odpowiedź:** 4 pary: 1999 1997, 1721 1723, 1481 1483, 809 811
