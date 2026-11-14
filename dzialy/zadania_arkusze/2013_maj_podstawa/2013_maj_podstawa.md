<h1 align="center">Matura 2013 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a

> **Treść zadania:** Zadanie 1. Obliczanie wartości wielomianu. Dla liczb rzeczywistych `a0, a1, a2, a3, a4` i `x` obliczamy `W(x) = a0·x⁴ + a1·x³ + a2·x² + a3·x + a4`. Sposób 1 liczy każdą potęgę osobno, sposób 2 korzysta ze schematu Hornera: `W(x) = x·(x·(x·(x·a0 + a1) + a2) + a3) + a4`.
>
> Algorytm (sposób 1):
> ```
> W ← 0, i ← 0
> dopóki i <= 4 wykonuj:
>     sk ← a[i], j ← 4 - i
>     dopóki j > 0 wykonuj: sk ← sk*x; j ← j - 1
>     W ← W + sk, i ← i + 1
> ```
>
> Podaj, ile mnożeń i ile dodawań liczb rzeczywistych wykonuje ten algorytm (bez operacji na zmiennych sterujących `i`, `j`).

```py
def sposob1(a, x):
    mnozenia = 0
    dodawania = 0
    W = 0
    i = 0
    while i <= 4:
        sk = a[i]
        j = 4 - i
        while j > 0:
            sk = sk * x
            mnozenia += 1
            j = j - 1
        W = W + sk
        dodawania += 1
        i = i + 1
    return W, mnozenia, dodawania


print(sposob1([1, 2, 3, 4, 5], 2))
```

```cpp
// C++23
#include <print>
#include <vector>

struct Wynik {
    int W, mnozenia, dodawania;
};

Wynik sposob1(const std::vector<int>& a, int x) {
    int mnozenia = 0, dodawania = 0;
    int W = 0;
    int i = 0;
    while (i <= 4) {
        int sk = a[i];
        int j = 4 - i;
        while (j > 0) {
            sk = sk * x;
            mnozenia++;
            j = j - 1;
        }
        W = W + sk;
        dodawania++;
        i = i + 1;
    }
    return {W, mnozenia, dodawania};
}

int main() {
    Wynik w = sposob1({1, 2, 3, 4, 5}, 2);
    std::println("({}, {}, {})", w.W, w.mnozenia, w.dodawania);
}
```

```java
// Java 25
public class Zadanie {
    record Wynik(int W, int mnozenia, int dodawania) {}

    static Wynik sposob1(int[] a, int x) {
        int mnozenia = 0, dodawania = 0;
        int W = 0;
        int i = 0;
        while (i <= 4) {
            int sk = a[i];
            int j = 4 - i;
            while (j > 0) {
                sk = sk * x;
                mnozenia++;
                j = j - 1;
            }
            W = W + sk;
            dodawania++;
            i = i + 1;
        }
        return new Wynik(W, mnozenia, dodawania);
    }

    public static void main(String[] args) throws Exception {
        var w = sposob1(new int[]{1, 2, 3, 4, 5}, 2);
        System.out.println("(" + w.W() + ", " + w.mnozenia() + ", " + w.dodawania() + ")");
    }
}
```
**Odpowiedź:** liczba mnożeń – 10, liczba dodawań – 5

## 1b

> **Treść zadania:** Wielomian stopnia czwartego jak w zadaniu 1a. Uzupełnij algorytm realizujący sposób 2 (schemat Hornera):
> ```
> W ← a0, i ← 0
> dopóki i < 4 wykonuj:
>     i ← ……
>     W ← ……
> ```
>
> Podaj też, ile mnożeń i ile dodawań liczb rzeczywistych wykonuje Twój algorytm (bez operacji na zmiennej `i`).

```py
def sposob2(a, x):  # schemat Hornera
    mnozenia = 0
    dodawania = 0
    W = a[0]
    i = 0
    while i < 4:
        i = i + 1
        W = W * x + a[i]
        mnozenia += 1
        dodawania += 1
    return W, mnozenia, dodawania


print(sposob2([1, 2, 3, 4, 5], 2))
```

```cpp
// C++23
#include <print>
#include <vector>

struct Wynik {
    int W, mnozenia, dodawania;
};

Wynik sposob2(const std::vector<int>& a, int x) {  // schemat Hornera
    int mnozenia = 0, dodawania = 0;
    int W = a[0];
    int i = 0;
    while (i < 4) {
        i = i + 1;
        W = W * x + a[i];
        mnozenia++;
        dodawania++;
    }
    return {W, mnozenia, dodawania};
}

int main() {
    Wynik w = sposob2({1, 2, 3, 4, 5}, 2);
    std::println("({}, {}, {})", w.W, w.mnozenia, w.dodawania);
}
```

```java
// Java 25
public class Zadanie {
    record Wynik(int W, int mnozenia, int dodawania) {}

    static Wynik sposob2(int[] a, int x) {  // schemat Hornera
        int mnozenia = 0, dodawania = 0;
        int W = a[0];
        int i = 0;
        while (i < 4) {
            i = i + 1;
            W = W * x + a[i];
            mnozenia++;
            dodawania++;
        }
        return new Wynik(W, mnozenia, dodawania);
    }

    public static void main(String[] args) throws Exception {
        var w = sposob2(new int[]{1, 2, 3, 4, 5}, 2);
        System.out.println("(" + w.W() + ", " + w.mnozenia() + ", " + w.dodawania() + ")");
    }
}
```
**Odpowiedź:** a) i ← i + 1; b) W ← W * x + a[i]; liczba mnożeń – 4, liczba dodawań – 4

## 2a i 2c

> **Treść zadania:** Zadanie 2. Algorytm. Dla liczby całkowitej `N > 1`:
> ```
> d ← 2
> dopóki N ≥ d wykonuj:
>     jeżeli N mod d = 0 to: wypisz d; N ← N div d
>     w przeciwnym razie d ← d + 1
> ```
>
> - 2a — podaj liczby wypisane przez algorytm dla `N = 36`, `N = 120` i `N = 675`.
> - 2c — podaj, ile liczb zostanie wypisanych dla `N = 2100`.
>
> (W podpunkcie 2b należało wskazać, że algorytm wypisuje czynniki pierwsze liczby `N`.)

```py
def algorytm(N):
    wypisane = []
    d = 2
    while N >= d:
        if N % d == 0:
            wypisane.append(d)
            N = N // d
        else:
            d = d + 1
    return wypisane


for N in [36, 120, 675]:
    print(N, algorytm(N))

print(len(algorytm(2 ** 100)))
```

```cpp
// C++23
#include <print>
#include <vector>

// 2^100 nie mieści się w long long, więc używamy 128-bitowej liczby bez znaku
// (rozszerzenie kompilatora GCC/Clang)
using duza = unsigned __int128;

std::vector<long long> algorytm(duza N) {
    std::vector<long long> wypisane;
    duza d = 2;
    while (N >= d) {
        if (N % d == 0) {
            wypisane.push_back((long long)d);
            N = N / d;
        } else {
            d = d + 1;
        }
    }
    return wypisane;
}

int main() {
    for (int N : {36, 120, 675}) {
        std::println("{} {}", N, algorytm(N));
    }
    std::println("{}", algorytm(duza(1) << 100).size());
}
```

```java
// Java 25
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    // 2^100 nie mieści się w long, więc liczymy na BigInteger
    static List<BigInteger> algorytm(BigInteger N) {
        var wypisane = new ArrayList<BigInteger>();
        var d = BigInteger.TWO;
        while (N.compareTo(d) >= 0) {
            if (N.mod(d).signum() == 0) {
                wypisane.add(d);
                N = N.divide(d);
            } else {
                d = d.add(BigInteger.ONE);
            }
        }
        return wypisane;
    }

    public static void main(String[] args) throws Exception {
        for (int N : new int[]{36, 120, 675}) {
            System.out.println(N + " " + algorytm(BigInteger.valueOf(N)));
        }
        System.out.println(algorytm(BigInteger.TWO.pow(100)).size());
    }
}
```
**Odpowiedź:** a) 36 → 2, 2, 3, 3; 120 → 2, 2, 2, 3, 5; 675 → 3, 3, 3, 5, 5; b) czynniki pierwsze liczby N; c) dla N = 2<sup>100</sup> zostanie wypisanych 100 liczb

## 2d

> **Treść zadania:** Algorytm rozkładu na czynniki jak w zadaniu 2. Zapisz algorytm, który dla liczby całkowitej `N > 1` wypisze jej rozkład na czynniki pierwsze w postaci par `a, b`, gdzie `a` — czynnik pierwszy, `b` — liczba jego wystąpień w rozkładzie.
>
> Przykład: dla `225 = 3·3·5·5` wypisujemy pary `3, 2` i `5, 2`; dla `784` — pary `2, 4` i `7, 2`.

```py
def czynniki_pary(N):
    a = 2
    b = 0
    while N >= a:
        if N % a == 0:
            b = b + 1
            N = N // a
        else:
            if b > 0:
                print(a, b)
            a = a + 1
            b = 0
    print(a, b)


czynniki_pary(225)
czynniki_pary(784)
```

```cpp
// C++23
#include <print>

void czynniki_pary(int N) {
    int a = 2;
    int b = 0;
    while (N >= a) {
        if (N % a == 0) {
            b = b + 1;
            N = N / a;
        } else {
            if (b > 0) std::println("{} {}", a, b);
            a = a + 1;
            b = 0;
        }
    }
    std::println("{} {}", a, b);
}

int main() {
    czynniki_pary(225);
    czynniki_pary(784);
}
```

```java
// Java 25
public class Zadanie {
    static void czynnikiPary(int N) {
        int a = 2;
        int b = 0;
        while (N >= a) {
            if (N % a == 0) {
                b = b + 1;
                N = N / a;
            } else {
                if (b > 0) System.out.println(a + " " + b);
                a = a + 1;
                b = 0;
            }
        }
        System.out.println(a + " " + b);
    }

    public static void main(String[] args) throws Exception {
        czynnikiPary(225);
        czynnikiPary(784);
    }
}
```
**Odpowiedź:** 225 → (3, 2), (5, 2); 784 → (2, 4), (7, 2)

## 4a

> **Treść zadania:** Zadanie 4. Napisy. W pliku `napisy.txt` znajduje się 1000 napisów o długości od 2 do 16 znaków, każdy w osobnym wierszu, złożonych wyłącznie ze znaków `0` i `1`. Odpowiedzi zapisz w pliku `zadanie4.txt`, poprzedzając każdą literą podpunktu.
>
> Podaj, ile napisów ma parzystą długość.

```py
parzyste = 0

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        if len(napis) % 2 == 0:
            parzyste += 1

print(parzyste)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("napisy.txt");
    int parzyste = 0;
    std::string napis;
    while (plik >> napis) {
        if (napis.size() % 2 == 0) parzyste++;
    }
    std::println("{}", parzyste);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int parzyste = 0;
        for (String line : Files.readAllLines(Path.of("napisy.txt"))) {
            String napis = line.strip();
            if (napis.length() % 2 == 0) parzyste++;
        }
        System.out.println(parzyste);
    }
}
```
**Odpowiedź:** 504

## 4b

> **Treść zadania:** Napisy zero-jedynkowe z pliku `napisy.txt` jak w zadaniu 4a. Podaj, ile napisów zawiera tyle samo zer co jedynek.

```py
count = 0

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        if napis.count("0") == napis.count("1"):
            count += 1

print(count)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("napisy.txt");
    int count = 0;
    std::string napis;
    while (plik >> napis) {
        if (std::ranges::count(napis, '0') == std::ranges::count(napis, '1')) count++;
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
        for (String line : Files.readAllLines(Path.of("napisy.txt"))) {
            String napis = line.strip();
            long zera = napis.chars().filter(c -> c == '0').count();
            long jedynki = napis.chars().filter(c -> c == '1').count();
            if (zera == jedynki) count++;
        }
        System.out.println(count);
    }
}
```
**Odpowiedź:** 110

## 4c

> **Treść zadania:** Napisy zero-jedynkowe z pliku `napisy.txt` jak w zadaniu 4a. Podaj, ile napisów składa się z samych zer, oraz ile — z samych jedynek.

```py
zera = 0
jedynki = 0

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        if napis.count("0") == len(napis):
            zera += 1
        if napis.count("1") == len(napis):
            jedynki += 1

print("same zera:", zera, "same jedynki:", jedynki)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("napisy.txt");
    int zera = 0, jedynki = 0;
    std::string napis;
    while (plik >> napis) {
        long long dlugosc = napis.size();
        if (std::ranges::count(napis, '0') == dlugosc) zera++;
        if (std::ranges::count(napis, '1') == dlugosc) jedynki++;
    }
    std::println("same zera: {} same jedynki: {}", zera, jedynki);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int zera = 0, jedynki = 0;
        for (String line : Files.readAllLines(Path.of("napisy.txt"))) {
            String napis = line.strip();
            if (napis.chars().filter(c -> c == '0').count() == napis.length()) zera++;
            if (napis.chars().filter(c -> c == '1').count() == napis.length()) jedynki++;
        }
        System.out.println("same zera: " + zera + " same jedynki: " + jedynki);
    }
}
```
**Odpowiedź:** same zera – 32, same jedynki – 50

## 4d

> **Treść zadania:** Napisy zero-jedynkowe z pliku `napisy.txt` jak w zadaniu 4a. Dla każdej długości `k = 2, 3, …, 16` podaj, ile napisów w pliku ma długość `k`.

```py
dlugosci = [0] * 17

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        dlugosci[len(napis)] += 1

for k in range(2, 17):
    print(k, dlugosci[k])
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>
#include <vector>

int main() {
    std::ifstream plik("napisy.txt");
    std::vector<int> dlugosci(17, 0);
    std::string napis;
    while (plik >> napis) {
        dlugosci[napis.size()]++;
    }
    for (int k = 2; k < 17; k++) {
        std::println("{} {}", k, dlugosci[k]);
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int[] dlugosci = new int[17];
        for (String line : Files.readAllLines(Path.of("napisy.txt"))) {
            String napis = line.strip();
            dlugosci[napis.length()]++;
        }
        for (int k = 2; k < 17; k++) {
            System.out.println(k + " " + dlugosci[k]);
        }
    }
}
```
**Odpowiedź:** 2: 43, 3: 38, 4: 37, 5: 57, 6: 53, 7: 68, 8: 78, 9: 103, 10: 83, 11: 90, 12: 86, 13: 81, 14: 68, 15: 59, 16: 56

## 6a

> **Treść zadania:** Zadanie 6. Fundusze. W pliku `historia.txt` są ceny jednostek uczestnictwa 12 funduszy inwestycyjnych (A–L) w kolejnych dniach roboczych 2008 roku. Każdy wiersz zawiera datę i 12 liczb z dwoma miejscami po przecinku, rozdzielonych średnikami, np. `2008-01-02;50,90;51,62;…;50,23`. Odpowiedzi zapisz w pliku `zadanie6.txt`, poprzedzając każdą literą podpunktu.
>
> Dla każdego funduszu podaj średnią cenę jednostki z całego roku, zaokrągloną do dwóch miejsc po przecinku.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
fundusze = "ABCDEFGHIJKL"
sumy = [0] * 12
dni = 0

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split(";")
        ceny = list(map(float, dane[1:]))
        for i in range(12):
            sumy[i] += ceny[i]
        dni += 1

for i in range(12):
    print(fundusze[i], round(sumy[i] / dni, 2))
```

```cpp
// C++23
#include <format>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// liczba rzeczywista wypisana tak jak w Pythonie (np. 38.3, 38.0)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find('.') == std::string::npos) s += ".0";
    return s;
}

// round(x, 2) z Pythona: zaokrąglenie do 2 miejsc po przecinku
double zaokraglij2(double x) {
    return std::stod(std::format("{:.2f}", x));
}

int main() {
    std::string fundusze = "ABCDEFGHIJKL";
    std::vector<double> sumy(12, 0.0);
    int dni = 0;

    std::ifstream plik("historia.txt");
    std::string line;
    while (std::getline(plik, line)) {
        for (char& c : line) {
            if (c == ',') c = '.';  // przecinek dziesiętny -> kropka
        }
        std::stringstream ss(line);
        std::string data, cena;
        std::getline(ss, data, ';');
        for (int i = 0; i < 12; i++) {
            std::getline(ss, cena, ';');
            sumy[i] += std::stod(cena);
        }
        dni++;
    }

    for (int i = 0; i < 12; i++) {
        std::println("{} {}", fundusze[i], jak_python(zaokraglij2(sumy[i] / dni)));
    }
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    // round(x, 2) z Pythona: zaokrąglenie do 2 miejsc po przecinku
    static double zaokraglij2(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).doubleValue();
    }

    public static void main(String[] args) throws Exception {
        String fundusze = "ABCDEFGHIJKL";
        double[] sumy = new double[12];
        int dni = 0;

        for (String line : Files.readAllLines(Path.of("historia.txt"))) {
            String[] dane = line.strip().replace(",", ".").split(";");
            for (int i = 0; i < 12; i++) {
                sumy[i] += Double.parseDouble(dane[i + 1]);
            }
            dni++;
        }

        for (int i = 0; i < 12; i++) {
            System.out.println(fundusze.charAt(i) + " " + zaokraglij2(sumy[i] / dni));
        }
    }
}
```
**Odpowiedź:** A 36,54; B 37,14; C 38,30; D 39,00; E 39,28; F 39,56; G 33,40; H 33,44; I 33,49; J 38,34; K 38,42; L 38,49

## 6b

> **Treść zadania:** Ceny 12 funduszy z pliku `historia.txt` jak w zadaniu 6a. Podaj liczbę dni, w których ceny jednostek wszystkich funduszy były wyższe niż 33 zł.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
count = 0

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split(";")
        ceny = list(map(float, dane[1:]))
        if min(ceny) > 33:
            count += 1

print(count)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

int main() {
    int count = 0;
    std::ifstream plik("historia.txt");
    std::string line;
    while (std::getline(plik, line)) {
        for (char& c : line) {
            if (c == ',') c = '.';  // przecinek dziesiętny -> kropka
        }
        std::stringstream ss(line);
        std::string data, cena;
        std::getline(ss, data, ';');
        std::vector<double> ceny;
        while (std::getline(ss, cena, ';')) ceny.push_back(std::stod(cena));
        if (std::ranges::min(ceny) > 33) count++;
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
        for (String line : Files.readAllLines(Path.of("historia.txt"))) {
            String[] dane = line.strip().replace(",", ".").split(";");
            double najmniejsza = Double.MAX_VALUE;
            for (int i = 1; i < dane.length; i++) {
                najmniejsza = Math.min(najmniejsza, Double.parseDouble(dane[i]));
            }
            if (najmniejsza > 33) count++;
        }
        System.out.println(count);
    }
}
```
**Odpowiedź:** 158

## 6c

> **Treść zadania:** Ceny 12 funduszy z pliku `historia.txt` jak w zadaniu 6a. Podaj cenę, która w całym roku (we wszystkich funduszach) wystąpiła najczęściej, oraz liczbę jej wystąpień.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
wystapienia = {}

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().split(";")
        for cena in dane[1:]:
            wystapienia[cena] = wystapienia.get(cena, 0) + 1

najczestsza = max(wystapienia, key=wystapienia.get)
print(najczestsza, wystapienia[najczestsza])
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
    std::map<std::string, int> wystapienia;
    std::vector<std::string> kolejnosc;  // kolejność pierwszego wystąpienia (jak w słowniku Pythona)

    std::ifstream plik("historia.txt");
    std::string line;
    while (std::getline(plik, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        std::stringstream ss(line);
        std::string data, cena;
        std::getline(ss, data, ';');
        while (std::getline(ss, cena, ';')) {
            if (!wystapienia.contains(cena)) kolejnosc.push_back(cena);
            wystapienia[cena]++;
        }
    }

    std::string najczestsza = kolejnosc[0];
    for (const auto& cena : kolejnosc) {
        if (wystapienia[cena] > wystapienia[najczestsza]) najczestsza = cena;
    }
    std::println("{} {}", najczestsza, wystapienia[najczestsza]);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.LinkedHashMap;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // LinkedHashMap pamięta kolejność dodawania (jak słownik w Pythonie)
        var wystapienia = new LinkedHashMap<String, Integer>();
        for (String line : Files.readAllLines(Path.of("historia.txt"))) {
            String[] dane = line.strip().split(";");
            for (int i = 1; i < dane.length; i++) {
                wystapienia.merge(dane[i], 1, Integer::sum);
            }
        }

        String najczestsza = null;
        for (String cena : wystapienia.keySet()) {
            if (najczestsza == null || wystapienia.get(cena) > wystapienia.get(najczestsza)) najczestsza = cena;
        }
        System.out.println(najczestsza + " " + wystapienia.get(najczestsza));
    }
}
```
**Odpowiedź:** 42,98 – wystąpiła 8 razy

## 6d

> **Treść zadania:** Ceny 12 funduszy z pliku `historia.txt` jak w zadaniu 6a. Dla każdego funduszu podaj najniższą i najwyższą cenę jednostki w 2008 roku i sporządź czytelnie opisany wykres liniowy tego zestawienia.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
fundusze = "ABCDEFGHIJKL"
najnizsza = [10 ** 9] * 12
najwyzsza = [0] * 12

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split(";")
        ceny = list(map(float, dane[1:]))
        for i in range(12):
            najnizsza[i] = min(najnizsza[i], ceny[i])
            najwyzsza[i] = max(najwyzsza[i], ceny[i])

for i in range(12):
    print(fundusze[i], najnizsza[i], najwyzsza[i])
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

// liczba rzeczywista wypisana tak jak w Pythonie (np. 50.9, 50.0)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find('.') == std::string::npos) s += ".0";
    return s;
}

int main() {
    std::string fundusze = "ABCDEFGHIJKL";
    std::vector<double> najnizsza(12, 1e9);
    std::vector<double> najwyzsza(12, 0.0);

    std::ifstream plik("historia.txt");
    std::string line;
    while (std::getline(plik, line)) {
        for (char& c : line) {
            if (c == ',') c = '.';  // przecinek dziesiętny -> kropka
        }
        std::stringstream ss(line);
        std::string data, cena;
        std::getline(ss, data, ';');
        for (int i = 0; i < 12; i++) {
            std::getline(ss, cena, ';');
            double c = std::stod(cena);
            najnizsza[i] = std::min(najnizsza[i], c);
            najwyzsza[i] = std::max(najwyzsza[i], c);
        }
    }

    for (int i = 0; i < 12; i++) {
        std::println("{} {} {}", fundusze[i], jak_python(najnizsza[i]), jak_python(najwyzsza[i]));
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        String fundusze = "ABCDEFGHIJKL";
        double[] najnizsza = new double[12];
        double[] najwyzsza = new double[12];
        Arrays.fill(najnizsza, 1e9);

        for (String line : Files.readAllLines(Path.of("historia.txt"))) {
            String[] dane = line.strip().replace(",", ".").split(";");
            for (int i = 0; i < 12; i++) {
                double c = Double.parseDouble(dane[i + 1]);
                najnizsza[i] = Math.min(najnizsza[i], c);
                najwyzsza[i] = Math.max(najwyzsza[i], c);
            }
        }

        for (int i = 0; i < 12; i++) {
            System.out.println(fundusze.charAt(i) + " " + najnizsza[i] + " " + najwyzsza[i]);
        }
    }
}
```
**Odpowiedź:** (min, max) A 20,82 50,90; B 21,21 51,62; C 21,92 53,12; D 18,76 58,66; E 18,94 58,96; F 19,12 59,26; G 16,04 48,15; H 16,08 48,17; I 16,12 48,19; J 20,33 50,23; K 20,41 50,23; L 20,50 50,23 (wykres liniowy wykonuje się w arkuszu kalkulacyjnym)
