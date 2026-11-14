<h1 align="center">Matura 2012 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

> **Treść zadania:** Funkcja rekurencyjna Fib oblicza k-ty wyraz ciągu Fibonacciego (k — liczba naturalna większa od zera):
>
> ```
> Fib(k):
> 1. jeżeli k = 1 lub k = 2, to wynikiem jest 1
> 2. jeżeli k > 2, to wynikiem jest Fib(k − 1) + Fib(k − 2)
> ```
>
> Np. Fib(4) = Fib(3) + Fib(2) = Fib(2) + Fib(1) + Fib(2) = 3.
>
> - 1a — Uzupełnij tabelę wartości Fib(k) (m.in. dla k = 8 i k = 11).
> - 1b — Wywołanie Fib(k) dla k > 2 powoduje dwa wywołania z mniejszymi argumentami, co można przedstawić jako drzewo wywołań (w arkuszu podano drzewo dla k = 5, w węzłach są argumenty). Narysuj drzewo wywołań dla Fib(6).

```py
poziomy = []


def fib(k, poziom=0):
    # zapamiętujemy argumenty wywołań na kolejnych poziomach drzewa
    if len(poziomy) <= poziom:
        poziomy.append([])
    poziomy[poziom].append(k)
    if k == 1 or k == 2:
        return 1
    return fib(k - 1, poziom + 1) + fib(k - 2, poziom + 1)


print("Fib(8) =", fib(8))
print("Fib(11) =", fib(11))

poziomy.clear()
fib(6)
for poziom in poziomy:  # drzewo wywołań dla Fib(6), poziom po poziomie
    print(*poziom)
```

```cpp
// C++23
#include <print>
#include <vector>

std::vector<std::vector<int>> poziomy;

int fib(int k, int poziom = 0) {
    // zapamiętujemy argumenty wywołań na kolejnych poziomach drzewa
    if (static_cast<int>(poziomy.size()) <= poziom) {
        poziomy.push_back({});
    }
    poziomy[poziom].push_back(k);
    if (k == 1 || k == 2) {
        return 1;
    }
    return fib(k - 1, poziom + 1) + fib(k - 2, poziom + 1);
}

int main() {
    std::println("Fib(8) = {}", fib(8));
    std::println("Fib(11) = {}", fib(11));

    poziomy.clear();
    fib(6);
    for (const auto& poziom : poziomy) { // drzewo wywołań dla Fib(6), poziom po poziomie
        for (size_t i = 0; i < poziom.size(); i++) {
            std::print("{}{}", i > 0 ? " " : "", poziom[i]);
        }
        std::println();
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static List<List<Integer>> poziomy = new ArrayList<>();

    static int fib(int k, int poziom) {
        // zapamiętujemy argumenty wywołań na kolejnych poziomach drzewa
        if (poziomy.size() <= poziom) {
            poziomy.add(new ArrayList<>());
        }
        poziomy.get(poziom).add(k);
        if (k == 1 || k == 2) {
            return 1;
        }
        return fib(k - 1, poziom + 1) + fib(k - 2, poziom + 1);
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Fib(8) = " + fib(8, 0));
        System.out.println("Fib(11) = " + fib(11, 0));

        poziomy.clear();
        fib(6, 0);
        for (List<Integer> poziom : poziomy) { // drzewo wywołań dla Fib(6), poziom po poziomie
            var napisy = new ArrayList<String>();
            for (int k : poziom) {
                napisy.add(String.valueOf(k));
            }
            System.out.println(String.join(" ", napisy));
        }
    }
}
```
**Odpowiedź:** a) Fib(8) = 21, Fib(11) = 89; b) drzewo: 6 / 5 4 / 4 3 3 2 / 3 2 2 1 2 1 / 2 1

## 1c

> **Treść zadania:** Ciąg Fibonacciego można liczyć iteracyjnie, pamiętając dwa ostatnie wyrazy. Zdefiniujmy nowy ciąg: pierwszy i drugi wyraz są równe 1; dla k > 2 parzystego k-ty wyraz jest sumą trzech wyrazów go poprzedzających; dla k > 2 nieparzystego k-ty wyraz jest równy wyrazowi o numerze k − 1. Początkowe wyrazy (k = 1..8): 1, 1, 1, 3, 3, 7, 7, 17.
>
> Zapisz iteracyjny algorytm, który dla danego k > 0 wyznacza k-ty wyraz tego ciągu.

```py
def wyraz(k):
    a = [0, 1, 1]  # a[1] = a[2] = 1, a[0] nieużywane
    for i in range(3, k + 1):
        if i % 2 == 0:
            a.append(a[i - 1] + a[i - 2] + a[i - 3])
        else:
            a.append(a[i - 1])
    return a[k]


for k in range(1, 9):
    print(k, wyraz(k))
```

```cpp
// C++23
#include <print>
#include <vector>

int wyraz(int k) {
    std::vector<int> a = {0, 1, 1}; // a[1] = a[2] = 1, a[0] nieużywane
    for (int i = 3; i <= k; i++) {
        if (i % 2 == 0) {
            a.push_back(a[i - 1] + a[i - 2] + a[i - 3]);
        } else {
            a.push_back(a[i - 1]);
        }
    }
    return a[k];
}

int main() {
    for (int k = 1; k < 9; k++) {
        std::println("{} {}", k, wyraz(k));
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static int wyraz(int k) {
        var a = new ArrayList<Integer>(List.of(0, 1, 1)); // a[1] = a[2] = 1, a[0] nieużywane
        for (int i = 3; i <= k; i++) {
            if (i % 2 == 0) {
                a.add(a.get(i - 1) + a.get(i - 2) + a.get(i - 3));
            } else {
                a.add(a.get(i - 1));
            }
        }
        return a.get(k);
    }

    public static void main(String[] args) throws Exception {
        for (int k = 1; k < 9; k++) {
            System.out.println(k + " " + wyraz(k));
        }
    }
}
```
**Odpowiedź:** 1, 1, 1, 3, 3, 7, 7, 17 (zgodnie z tabelą w treści)

## 2a

> **Treść zadania:** W sejfie jest n diamentów o różnych cenach d₁, …, dₙ, znanych tylko jubilerowi. Jubiler wykonuje jedynie operację porównania: `większe(i, j)` jest prawdą, gdy dᵢ > dⱼ, a fałszem, gdy dᵢ < dⱼ. Dany jest algorytm:
>
> ```
> 1. j ← 0
> 2. i ← 1
> 3. dopóki i < n
>        jeżeli większe(i, i + 1), to j ← j + 1
>        i ← i + 1
> 4. wypisz j
> ```
>
> Podaj wynik algorytmu dla n = 4 i ciągów cen: (5, 2, 1, 6), (2, 5, 1, 2), (1, 2, 3, 4), (4, 3, 2, 1) (pierwszy wynik, 2, podano w arkuszu).

```py
def algorytm(d):
    n = len(d)
    j = 0
    i = 1
    while i < n:
        if d[i - 1] > d[i]:  # większe(i, i+1), numeracja od 1
            j = j + 1
        i = i + 1
    return j


for d in [[5, 2, 1, 6], [2, 5, 1, 2], [1, 2, 3, 4], [4, 3, 2, 1]]:
    print(d, algorytm(d))
```

```cpp
// C++23
#include <print>
#include <vector>

int algorytm(const std::vector<int>& d) {
    int n = static_cast<int>(d.size());
    int j = 0;
    int i = 1;
    while (i < n) {
        if (d[i - 1] > d[i]) { // większe(i, i+1), numeracja od 1
            j = j + 1;
        }
        i = i + 1;
    }
    return j;
}

int main() {
    std::vector<std::vector<int>> dane = {{5, 2, 1, 6}, {2, 5, 1, 2}, {1, 2, 3, 4}, {4, 3, 2, 1}};
    for (const auto& d : dane) {
        std::println("{} {}", d, algorytm(d));
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static int algorytm(List<Integer> d) {
        int n = d.size();
        int j = 0;
        int i = 1;
        while (i < n) {
            if (d.get(i - 1) > d.get(i)) { // większe(i, i+1), numeracja od 1
                j = j + 1;
            }
            i = i + 1;
        }
        return j;
    }

    public static void main(String[] args) throws Exception {
        var dane = List.of(List.of(5, 2, 1, 6), List.of(2, 5, 1, 2), List.of(1, 2, 3, 4), List.of(4, 3, 2, 1));
        for (List<Integer> d : dane) {
            System.out.println(d + " " + algorytm(d));
        }
    }
}
```
**Odpowiedź:** 2 (podane), 1, 0, 3

## 2b

> **Treść zadania:** Diamenty i operacja `większe(i, j)` jak w 2a.
>
> Zapisz algorytm, który dla n > 0 diamentów o różnych cenach znajduje numer i diamentu o najwyższej cenie, korzystając wyłącznie z operacji `większe`. Podaj, ile porównań wykonuje Twój algorytm dla n = 1000.

```py
def najdrozszy(d):
    porownania = 0
    i = 1
    for k in range(2, len(d) + 1):
        porownania += 1
        if d[k - 1] > d[i - 1]:  # większe(k, i)
            i = k
    return i, porownania


print(najdrozszy([5, 2, 1, 6]))
print(najdrozszy(list(range(1000)))[1])
```

```cpp
// C++23
#include <numeric>
#include <print>
#include <utility>
#include <vector>

std::pair<int, int> najdrozszy(const std::vector<int>& d) {
    int porownania = 0;
    int i = 1;
    for (int k = 2; k <= static_cast<int>(d.size()); k++) {
        porownania += 1;
        if (d[k - 1] > d[i - 1]) { // większe(k, i)
            i = k;
        }
    }
    return {i, porownania};
}

int main() {
    std::println("{}", najdrozszy({5, 2, 1, 6})); // para wypisuje się jako (4, 3)
    std::vector<int> d(1000);
    std::iota(d.begin(), d.end(), 0); // 0, 1, ..., 999
    std::println("{}", najdrozszy(d).second);
}
```

```java
// Java 25
public class Zadanie {
    // zwraca parę (indeks najdroższego, liczba porównań)
    static int[] najdrozszy(int[] d) {
        int porownania = 0;
        int i = 1;
        for (int k = 2; k <= d.length; k++) {
            porownania += 1;
            if (d[k - 1] > d[i - 1]) { // większe(k, i)
                i = k;
            }
        }
        return new int[]{i, porownania};
    }

    public static void main(String[] args) throws Exception {
        int[] wynik = najdrozszy(new int[]{5, 2, 1, 6});
        System.out.println("(" + wynik[0] + ", " + wynik[1] + ")");
        int[] d = new int[1000];
        for (int i = 0; i < 1000; i++) {
            d[i] = i;
        }
        System.out.println(najdrozszy(d)[1]);
    }
}
```
**Odpowiedź:** dla n = 1000 algorytm wykonuje 999 porównań

## 4a

> **Treść zadania:** W pliku `cyfry.txt` znajduje się 1000 liczb naturalnych mniejszych niż 10⁹, każda w osobnym wierszu. Odpowiedzi zapisz w pliku `zadanie4.txt`, poprzedzając je oznaczeniem podpunktu.
>
> Ile liczb w pliku jest parzystych?

```py
parzyste = 0

with open("cyfry.txt") as file:
    for line in file:
        if int(line) % 2 == 0:
            parzyste += 1

print(parzyste)
```

```cpp
// C++23
#include <fstream>
#include <print>

int main() {
    int parzyste = 0;
    std::ifstream plik("cyfry.txt");
    long long liczba;
    while (plik >> liczba) {
        if (liczba % 2 == 0) {
            parzyste += 1;
        }
    }
    std::println("{}", parzyste);
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int parzyste = 0;
        for (String linia : Files.readAllLines(Path.of("cyfry.txt"))) {
            if (Long.parseLong(linia.strip()) % 2 == 0) {
                parzyste += 1;
            }
        }
        System.out.println(parzyste);
    }
}
```
**Odpowiedź:** 495

## 4b

> **Treść zadania:** Dane z pliku `cyfry.txt` (1000 liczb naturalnych < 10⁹).
>
> Podaj liczbę o największej sumie cyfr oraz liczbę o najmniejszej sumie cyfr (każda jest jedyna). Przykład: dla 121324, 66562, 675100, 1187010 odpowiedzią jest 66562 (suma 25) oraz 121324 (suma 13).

```py
def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma


najwieksza = ""
najmniejsza = ""

with open("cyfry.txt") as file:
    for line in file:
        liczba = line.strip()
        if najwieksza == "" or suma_cyfr(liczba) > suma_cyfr(najwieksza):
            najwieksza = liczba
        if najmniejsza == "" or suma_cyfr(liczba) < suma_cyfr(najmniejsza):
            najmniejsza = liczba

print("największa suma cyfr:", najwieksza)
print("najmniejsza suma cyfr:", najmniejsza)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int suma_cyfr(const std::string& liczba) {
    int suma = 0;
    for (char cyfra : liczba) {
        suma += cyfra - '0';
    }
    return suma;
}

int main() {
    std::string najwieksza = "";
    std::string najmniejsza = "";
    std::ifstream plik("cyfry.txt");
    std::string liczba;
    while (plik >> liczba) {
        if (najwieksza == "" || suma_cyfr(liczba) > suma_cyfr(najwieksza)) {
            najwieksza = liczba;
        }
        if (najmniejsza == "" || suma_cyfr(liczba) < suma_cyfr(najmniejsza)) {
            najmniejsza = liczba;
        }
    }
    std::println("największa suma cyfr: {}", najwieksza);
    std::println("najmniejsza suma cyfr: {}", najmniejsza);
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    static int sumaCyfr(String liczba) {
        int suma = 0;
        for (char cyfra : liczba.toCharArray()) {
            suma += cyfra - '0';
        }
        return suma;
    }

    public static void main(String[] args) throws Exception {
        String najwieksza = "";
        String najmniejsza = "";
        for (String linia : Files.readAllLines(Path.of("cyfry.txt"))) {
            String liczba = linia.strip();
            if (najwieksza.isEmpty() || sumaCyfr(liczba) > sumaCyfr(najwieksza)) {
                najwieksza = liczba;
            }
            if (najmniejsza.isEmpty() || sumaCyfr(liczba) < sumaCyfr(najmniejsza)) {
                najmniejsza = liczba;
            }
        }
        System.out.println("największa suma cyfr: " + najwieksza);
        System.out.println("najmniejsza suma cyfr: " + najmniejsza);
    }
}
```
**Odpowiedź:** największa suma cyfr: 187869866, najmniejsza suma cyfr: 10010

## 4c

> **Treść zadania:** Dane z pliku `cyfry.txt` (1000 liczb naturalnych < 10⁹).
>
> Wypisz wszystkie liczby, których cyfry tworzą ciąg ściśle rosnący (np. 123579 tak; 1232 i 34556 nie).

```py
with open("cyfry.txt") as file:
    for line in file:
        liczba = line.strip()
        rosnace = True
        for i in range(1, len(liczba)):
            if liczba[i] <= liczba[i - 1]:
                rosnace = False
        if rosnace:
            print(liczba)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("cyfry.txt");
    std::string liczba;
    while (plik >> liczba) {
        bool rosnace = true;
        for (size_t i = 1; i < liczba.size(); i++) {
            if (liczba[i] <= liczba[i - 1]) {
                rosnace = false;
            }
        }
        if (rosnace) {
            std::println("{}", liczba);
        }
    }
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        for (String linia : Files.readAllLines(Path.of("cyfry.txt"))) {
            String liczba = linia.strip();
            boolean rosnace = true;
            for (int i = 1; i < liczba.length(); i++) {
                if (liczba.charAt(i) <= liczba.charAt(i - 1)) {
                    rosnace = false;
                }
            }
            if (rosnace) {
                System.out.println(liczba);
            }
        }
    }
}
```
**Odpowiedź:** 2389, 23567, 123456789, 3468

## 5a i 5b

> **Treść zadania:** Plik `gielda.txt` ma 400 wierszy; w każdym są trzy liczby całkowite — zmiany cen akcji firm A, B i C w kolejnych dniach. Przed pierwszym dniem każda akcja kosztowała 200 zł (np. wiersze `0 12 -7`, `1 -3 4` dają ceny 200/212/193, potem 201/209/197). Odpowiedzi (poza wykresem z c) zapisz w pliku `zadanie5.txt`, poprzedzając je literą podpunktu.
>
> - 5a — Wyznacz końcową (po 400 dniach) cenę akcji każdej z firm.
> - 5b — Podaj najwyższą i najniższą cenę akcji każdej z firm w ciągu tych 400 dni.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
cena = [200, 200, 200]
najwyzsza = [200, 200, 200]
najnizsza = [10 ** 9, 10 ** 9, 10 ** 9]

with open("gielda.txt") as file:
    for line in file:
        zmiany = list(map(int, line.split()))
        for i in range(3):
            cena[i] += zmiany[i]
            najwyzsza[i] = max(najwyzsza[i], cena[i])
            najnizsza[i] = min(najnizsza[i], cena[i])

print("a)", "A:", cena[0], "B:", cena[1], "C:", cena[2])
print("b) max:", najwyzsza, "min:", najnizsza)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <vector>

int main() {
    std::vector<int> cena = {200, 200, 200};
    std::vector<int> najwyzsza = {200, 200, 200};
    std::vector<int> najnizsza = {1000000000, 1000000000, 1000000000};

    std::ifstream plik("gielda.txt");
    int zmiany[3];
    while (plik >> zmiany[0] >> zmiany[1] >> zmiany[2]) {
        for (int i = 0; i < 3; i++) {
            cena[i] += zmiany[i];
            najwyzsza[i] = std::max(najwyzsza[i], cena[i]);
            najnizsza[i] = std::min(najnizsza[i], cena[i]);
        }
    }

    std::println("a) A: {} B: {} C: {}", cena[0], cena[1], cena[2]);
    std::println("b) max: {} min: {}", najwyzsza, najnizsza);
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int[] cena = {200, 200, 200};
        int[] najwyzsza = {200, 200, 200};
        int[] najnizsza = {1000000000, 1000000000, 1000000000};

        for (String linia : Files.readAllLines(Path.of("gielda.txt"))) {
            String[] zmiany = linia.strip().split("\\s+");
            for (int i = 0; i < 3; i++) {
                cena[i] += Integer.parseInt(zmiany[i]);
                najwyzsza[i] = Math.max(najwyzsza[i], cena[i]);
                najnizsza[i] = Math.min(najnizsza[i], cena[i]);
            }
        }

        System.out.println("a) A: " + cena[0] + " B: " + cena[1] + " C: " + cena[2]);
        System.out.println("b) max: " + Arrays.toString(najwyzsza) + " min: " + Arrays.toString(najnizsza));
    }
}
```
**Odpowiedź:** a) A – 221, B – 117, C – 198; b) max: A 264, B 210, C 223; min: A 167, B 62, C 97

## 5d

> **Treść zadania:** Dane z pliku `gielda.txt` (dzienne zmiany cen akcji A, B, C; start 200 zł).
>
> Krach giełdowy to dzień, w którym spadła cena akcji każdej z trzech firm, a suma spadków przekracza 20 zł (np. 233/166/164 → 230/150/160: spadki 3 + 16 + 4 > 20). Podaj liczbę krachów oraz ceny akcji wszystkich firm w dniu ostatniego krachu.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
cena = [200, 200, 200]
krachy = 0
ostatni = []

with open("gielda.txt") as file:
    for line in file:
        zmiany = list(map(int, line.split()))
        for i in range(3):
            cena[i] += zmiany[i]
        if zmiany[0] < 0 and zmiany[1] < 0 and zmiany[2] < 0 and -sum(zmiany) > 20:
            krachy += 1
            ostatni = cena[:]

print(krachy, ostatni)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <vector>

int main() {
    std::vector<int> cena = {200, 200, 200};
    int krachy = 0;
    std::vector<int> ostatni;

    std::ifstream plik("gielda.txt");
    int zmiany[3];
    while (plik >> zmiany[0] >> zmiany[1] >> zmiany[2]) {
        for (int i = 0; i < 3; i++) {
            cena[i] += zmiany[i];
        }
        int suma = zmiany[0] + zmiany[1] + zmiany[2];
        if (zmiany[0] < 0 && zmiany[1] < 0 && zmiany[2] < 0 && -suma > 20) {
            krachy += 1;
            ostatni = cena; // kopia wektora
        }
    }

    std::println("{} {}", krachy, ostatni);
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int[] cena = {200, 200, 200};
        int krachy = 0;
        int[] ostatni = {};

        for (String linia : Files.readAllLines(Path.of("gielda.txt"))) {
            int[] zmiany = Arrays.stream(linia.strip().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            for (int i = 0; i < 3; i++) {
                cena[i] += zmiany[i];
            }
            int suma = zmiany[0] + zmiany[1] + zmiany[2];
            if (zmiany[0] < 0 && zmiany[1] < 0 && zmiany[2] < 0 && -suma > 20) {
                krachy += 1;
                ostatni = cena.clone(); // kopia tablicy
            }
        }

        System.out.println(krachy + " " + Arrays.toString(ostatni));
    }
}
```
**Odpowiedź:** 6 krachów, ceny przy ostatnim krachu: A – 224, B – 163, C – 194

## 5e

> **Treść zadania:** Dane z pliku `gielda.txt` (dzienne zmiany cen akcji A, B, C; start 200 zł).
>
> Rekord firmy to cena akcji w dniu, w którym jest ona wyższa od wszystkich wcześniejszych cen tej firmy (przed pierwszym dniem rekord wynosi 200 zł). Podaj, ile razy w ciągu 400 dni zmieniał się rekord firmy A.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
cena = 200
rekord = 200
zmiany_rekordu = 0

with open("gielda.txt") as file:
    for line in file:
        cena += int(line.split()[0])
        if cena > rekord:
            rekord = cena
            zmiany_rekordu += 1

print(zmiany_rekordu)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    int cena = 200;
    int rekord = 200;
    int zmiany_rekordu = 0;

    std::ifstream plik("gielda.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        cena += std::stoi(linia); // stoi czyta pierwszą liczbę w wierszu (spółka A)
        if (cena > rekord) {
            rekord = cena;
            zmiany_rekordu += 1;
        }
    }

    std::println("{}", zmiany_rekordu);
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int cena = 200;
        int rekord = 200;
        int zmianyRekordu = 0;

        for (String linia : Files.readAllLines(Path.of("gielda.txt"))) {
            cena += Integer.parseInt(linia.strip().split("\\s+")[0]); // pierwsza liczba w wierszu (spółka A)
            if (cena > rekord) {
                rekord = cena;
                zmianyRekordu += 1;
            }
        }

        System.out.println(zmianyRekordu);
    }
}
```
**Odpowiedź:** 14 razy
