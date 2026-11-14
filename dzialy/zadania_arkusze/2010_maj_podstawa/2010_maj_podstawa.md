<h1 align="center">Matura 2010 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a

> **Treść zadania:** Poniższy algorytm szyfruje słowo s szyfrem przestawieniowym, a wynik zapisuje w zmiennej w (`''` — słowo puste, `s[j]` — j-ty znak słowa numerowany od 1, `•` — sklejanie):
>
> ```
> 1. i ← 1, w ← '', k ← 2
> 2. dopóki i ≤ k wykonuj
>        j ← i
>        dopóki j ≤ długość(s) wykonuj
>            w ← w • s[j]
>            j ← j + k
>        i ← i + 1
> ```
>
> - 1a — Podaj wynik działania algorytmu dla słów ARKA i MOTOR.
> - 1b — Kluczem szyfrującym nazywamy wartość potrzebną przy szyfrowaniu i deszyfrowaniu, której zmiana zmienia wynik szyfrowania. Która ze zmiennych i, j, k przechowuje klucz?

```py
def szyfruj(s, k):
    w = ""
    i = 0
    while i < k:
        j = i
        while j < len(s):
            w = w + s[j]
            j = j + k
        i = i + 1
    return w


print(szyfruj("ARKA", 2), szyfruj("MOTOR", 2))
```

```cpp
// C++23
#include <print>
#include <string>

std::string szyfruj(const std::string& s, int k) {
    std::string w = "";
    int i = 0;
    while (i < k) {
        int j = i;
        while (j < static_cast<int>(s.size())) {
            w = w + s[j];
            j = j + k;
        }
        i = i + 1;
    }
    return w;
}

int main() {
    std::println("{} {}", szyfruj("ARKA", 2), szyfruj("MOTOR", 2));
}
```

```java
// Java 25
public class Zadanie {
    static String szyfruj(String s, int k) {
        String w = "";
        int i = 0;
        while (i < k) {
            int j = i;
            while (j < s.length()) {
                w = w + s.charAt(j);
                j = j + k;
            }
            i = i + 1;
        }
        return w;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(szyfruj("ARKA", 2) + " " + szyfruj("MOTOR", 2));
    }
}
```
**Odpowiedź:** AKRA, MTROO (kluczem jest k)

## 1c

> **Treść zadania:** Zapisz algorytm innego szyfru: słowo s dzielimy na pary kolejnych znaków i w każdej parze zamieniamy znaki miejscami; przy nieparzystej długości ostatni znak zostaje bez zmian. Wynik zapisz w zmiennej w.
>
> Przykłady: MOTOR → MO TO R → OM OT R → `OMOTR`; MATURA → MA TU RA → `AMUTAR`.

```py
def szyfruj_pary(s):
    w = ""
    i = 0
    while i + 1 < len(s):
        w = w + s[i + 1] + s[i]
        i = i + 2
    if i < len(s):  # nieparzysta długość - ostatni znak bez zmian
        w = w + s[i]
    return w


print(szyfruj_pary("MOTOR"), szyfruj_pary("MATURA"))
```

```cpp
// C++23
#include <print>
#include <string>

std::string szyfruj_pary(const std::string& s) {
    std::string w = "";
    size_t i = 0;
    while (i + 1 < s.size()) {
        w = w + s[i + 1] + s[i];
        i = i + 2;
    }
    if (i < s.size()) { // nieparzysta długość - ostatni znak bez zmian
        w = w + s[i];
    }
    return w;
}

int main() {
    std::println("{} {}", szyfruj_pary("MOTOR"), szyfruj_pary("MATURA"));
}
```

```java
// Java 25
public class Zadanie {
    static String szyfrujPary(String s) {
        String w = "";
        int i = 0;
        while (i + 1 < s.length()) {
            w = w + s.charAt(i + 1) + s.charAt(i);
            i = i + 2;
        }
        if (i < s.length()) { // nieparzysta długość - ostatni znak bez zmian
            w = w + s.charAt(i);
        }
        return w;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(szyfrujPary("MOTOR") + " " + szyfrujPary("MATURA"));
    }
}
```
**Odpowiedź:** OMOTR, AMUTAR

## 2a i 2b

> **Treść zadania:** Rozkład liczby całkowitej większej od 1 na czynniki pierwsze to zapisanie jej jako iloczynu liczb pierwszych (liczba pierwsza ma rozkład złożony tylko z niej samej), np. 24 = 2 · 2 · 2 · 3, 20 = 2 · 2 · 5, 19 = 19.
>
> - 2a — Podaj rozkład na czynniki pierwsze liczb 63, 184 i 277.
> - 2b — Zapisz algorytm, który dla liczby całkowitej n > 1 wypisuje wszystkie czynniki pierwsze jej rozkładu (z powtórzeniami), np. dla n = 24 wynik to 2, 2, 2, 3, a dla n = 19 — 19.

```py
def czynniki_pierwsze(n):
    czynniki = []
    dzielnik = 2
    while n > 1:
        while n % dzielnik == 0:
            czynniki.append(dzielnik)
            n = n // dzielnik
        dzielnik = dzielnik + 1
    return czynniki


for n in [63, 184, 277]:
    print(n, czynniki_pierwsze(n))
```

```cpp
// C++23
#include <print>
#include <vector>

std::vector<int> czynniki_pierwsze(int n) {
    std::vector<int> czynniki;
    int dzielnik = 2;
    while (n > 1) {
        while (n % dzielnik == 0) {
            czynniki.push_back(dzielnik);
            n = n / dzielnik;
        }
        dzielnik = dzielnik + 1;
    }
    return czynniki;
}

int main() {
    for (int n : {63, 184, 277}) {
        std::println("{} {}", n, czynniki_pierwsze(n)); // wektor wypisuje się jako [3, 3, 7]
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static List<Integer> czynnikiPierwsze(int n) {
        var czynniki = new ArrayList<Integer>();
        int dzielnik = 2;
        while (n > 1) {
            while (n % dzielnik == 0) {
                czynniki.add(dzielnik);
                n = n / dzielnik;
            }
            dzielnik = dzielnik + 1;
        }
        return czynniki;
    }

    public static void main(String[] args) throws Exception {
        for (int n : new int[]{63, 184, 277}) {
            System.out.println(n + " " + czynnikiPierwsze(n)); // lista wypisuje się jako [3, 3, 7]
        }
    }
}
```
**Odpowiedź:** 63 = 3·3·7; 184 = 2·2·2·23; 277 = 277

## 4

> **Treść zadania:** W pliku `dane.txt` znajduje się 1000 słów (każde w osobnym wierszu) o długości od 2 do 25 znaków, złożonych z wielkich liter A–J. Palindrom to słowo, które czytane od lewej i od prawej jest takie samo (np. ABBA; JANA nie jest palindromem).
>
> Napisz program, który wypisze wszystkie palindromy z pliku, po jednym w wierszu, w kolejności występowania w pliku. Wyniki zapisz w pliku `zadanie4.txt`.

```py
with open("dane.txt") as file:
    with open("zadanie4.txt", "w") as wynik:
        for line in file:
            slowo = line.strip()
            if slowo == slowo[::-1]:
                print(slowo)
                wynik.write(slowo + "\n")
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("dane.txt");
    std::ofstream wynik("zadanie4.txt");
    std::string slowo;
    while (plik >> slowo) {
        std::string odwrocone(slowo.rbegin(), slowo.rend());
        if (slowo == odwrocone) {
            std::println("{}", slowo);
            wynik << slowo << "\n";
        }
    }
}
```

```java
// Java 25
import java.io.*;
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        try (var wynik = new PrintWriter(new FileWriter("zadanie4.txt"))) {
            for (String linia : Files.readAllLines(Path.of("dane.txt"))) {
                String slowo = linia.strip();
                String odwrocone = new StringBuilder(slowo).reverse().toString();
                if (slowo.equals(odwrocone)) {
                    System.out.println(slowo);
                    wynik.println(slowo);
                }
            }
        }
    }
}
```
**Odpowiedź:** CBJBC, AABBHHIHHBBAA, CCJGJCC, FDDFFFDDF, BCACHCACB, DFDCCDFD, DFFFD, AABBAA, … (42 palindromy)

## 5a i 5b

> **Treść zadania:** Producenci A i B sprzedają towar po 12,00 zł za sztukę z upustami (x — liczba sztuk, k — koszt):
>
> - Producent A: dla x ≤ 500: k = x · (1 − 0,15) · 12; dla x > 500: k = x · (1 − 0,25) · 12.
> - Producent B: dla x ≤ 300: k = x · (1 − 0,1) · 12; dla 300 < x ≤ 600: k = 300 · (1 − 0,1) · 12 + (x − 300) · (1 − 0,25) · 12; dla x > 600: k = x · (1 − 0,35) · 12.
>
> Towar pakowany jest po 10 sztuk, więc x to wielokrotność 10 z przedziału [10, 1000]. Odpowiedzi zapisz w pliku `zadanie5.txt`, poprzedzając je literą podpunktu.
>
> - 5a — W jakich przedziałach wartości x zakup u producenta A jest tańszy?
> - 5b — Przy jakiej liczbie sztuk koszt u obu producentów jest taki sam?

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
def koszt_a(x):  # koszt w groszach
    if x <= 500:
        return x * 85 * 12
    return x * 75 * 12


def koszt_b(x):
    if x <= 300:
        return x * 90 * 12
    if x <= 600:
        return 300 * 90 * 12 + (x - 300) * 75 * 12
    return x * 65 * 12


# a) przedziały, w których A jest tańszy
przedzialy = []
for x in range(10, 1001, 10):
    if koszt_a(x) < koszt_b(x):
        if przedzialy and przedzialy[-1][1] == x - 10:
            przedzialy[-1][1] = x
        else:
            przedzialy.append([x, x])
print("a)", przedzialy)

# b) ten sam koszt
for x in range(10, 1001, 10):
    if koszt_a(x) == koszt_b(x):
        print("b)", x)
```

```cpp
// C++23
#include <array>
#include <print>
#include <vector>

int koszt_a(int x) { // koszt w groszach
    if (x <= 500) {
        return x * 85 * 12;
    }
    return x * 75 * 12;
}

int koszt_b(int x) {
    if (x <= 300) {
        return x * 90 * 12;
    }
    if (x <= 600) {
        return 300 * 90 * 12 + (x - 300) * 75 * 12;
    }
    return x * 65 * 12;
}

int main() {
    // a) przedziały, w których A jest tańszy
    std::vector<std::array<int, 2>> przedzialy;
    for (int x = 10; x <= 1000; x += 10) {
        if (koszt_a(x) < koszt_b(x)) {
            if (!przedzialy.empty() && przedzialy.back()[1] == x - 10) {
                przedzialy.back()[1] = x;
            } else {
                przedzialy.push_back({x, x});
            }
        }
    }
    std::println("a) {}", przedzialy);

    // b) ten sam koszt
    for (int x = 10; x <= 1000; x += 10) {
        if (koszt_a(x) == koszt_b(x)) {
            std::println("b) {}", x);
        }
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static int kosztA(int x) { // koszt w groszach
        if (x <= 500) {
            return x * 85 * 12;
        }
        return x * 75 * 12;
    }

    static int kosztB(int x) {
        if (x <= 300) {
            return x * 90 * 12;
        }
        if (x <= 600) {
            return 300 * 90 * 12 + (x - 300) * 75 * 12;
        }
        return x * 65 * 12;
    }

    public static void main(String[] args) throws Exception {
        // a) przedziały, w których A jest tańszy
        var przedzialy = new ArrayList<List<Integer>>();
        for (int x = 10; x <= 1000; x += 10) {
            if (kosztA(x) < kosztB(x)) {
                if (!przedzialy.isEmpty() && przedzialy.getLast().get(1) == x - 10) {
                    przedzialy.getLast().set(1, x);
                } else {
                    przedzialy.add(new ArrayList<>(List.of(x, x)));
                }
            }
        }
        System.out.println("a) " + przedzialy);

        // b) ten sam koszt
        for (int x = 10; x <= 1000; x += 10) {
            if (kosztA(x) == kosztB(x)) {
                System.out.println("b) " + x);
            }
        }
    }
}
```
**Odpowiedź:** a) <10, 440> i <510, 600>; b) 450 sztuk

## 5c i 5d

> **Treść zadania:** Dane i reguły cenowe producentów A i B jak w 5a (x — wielokrotność 10 z przedziału [10, 1000]); odpowiedzi w pliku `zadanie5.txt`.
>
> - 5c — Jaka jest największa liczba sztuk, dla której koszt zakupu u A jest mniejszy niż koszt zakupu 500 sztuk u B?
> - 5d — Jaka jest największa liczba sztuk, dla której koszt zakupu u B jest mniejszy niż koszt zakupu 600 sztuk u A?

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
def koszt_a(x):  # koszt w groszach
    if x <= 500:
        return x * 85 * 12
    return x * 75 * 12


def koszt_b(x):
    if x <= 300:
        return x * 90 * 12
    if x <= 600:
        return 300 * 90 * 12 + (x - 300) * 75 * 12
    return x * 65 * 12


najwiecej_c = 0
najwiecej_d = 0
for x in range(10, 1001, 10):
    if koszt_a(x) < koszt_b(500):
        najwiecej_c = x
    if koszt_b(x) < koszt_a(600):
        najwiecej_d = x

print("c)", najwiecej_c)
print("d)", najwiecej_d)
```

```cpp
// C++23
#include <print>

int koszt_a(int x) { // koszt w groszach
    if (x <= 500) {
        return x * 85 * 12;
    }
    return x * 75 * 12;
}

int koszt_b(int x) {
    if (x <= 300) {
        return x * 90 * 12;
    }
    if (x <= 600) {
        return 300 * 90 * 12 + (x - 300) * 75 * 12;
    }
    return x * 65 * 12;
}

int main() {
    int najwiecej_c = 0;
    int najwiecej_d = 0;
    for (int x = 10; x <= 1000; x += 10) {
        if (koszt_a(x) < koszt_b(500)) {
            najwiecej_c = x;
        }
        if (koszt_b(x) < koszt_a(600)) {
            najwiecej_d = x;
        }
    }
    std::println("c) {}", najwiecej_c);
    std::println("d) {}", najwiecej_d);
}
```

```java
// Java 25
public class Zadanie {
    static int kosztA(int x) { // koszt w groszach
        if (x <= 500) {
            return x * 85 * 12;
        }
        return x * 75 * 12;
    }

    static int kosztB(int x) {
        if (x <= 300) {
            return x * 90 * 12;
        }
        if (x <= 600) {
            return 300 * 90 * 12 + (x - 300) * 75 * 12;
        }
        return x * 65 * 12;
    }

    public static void main(String[] args) throws Exception {
        int najwiecejC = 0;
        int najwiecejD = 0;
        for (int x = 10; x <= 1000; x += 10) {
            if (kosztA(x) < kosztB(500)) {
                najwiecejC = x;
            }
            if (kosztB(x) < kosztA(600)) {
                najwiecejD = x;
            }
        }
        System.out.println("c) " + najwiecejC);
        System.out.println("d) " + najwiecejD);
    }
}
```
**Odpowiedź:** c) 550 sztuk; d) 690 sztuk
