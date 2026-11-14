<h1 align="center">Matura 2011 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

> **Treść zadania:** Zegar nad wejściem do auli odlicza sekundy od początku wykładu i wyświetla ich liczbę w systemie dwójkowym, po jednej cyfrze na polu (przed startem świeci tylko skrajne prawe pole z zerem). Np. po 10 s widać 4 pola: `1010`, po 25 s — 5 pól: `11001`.
>
> - 1a — Na ilu polach zostanie wyświetlony czas najdłuższego wykładu, trwającego 240 minut (14 400 s)?
> - 1b — Ile minut trwał wykład, jeśli na koniec zegar pokazywał `1111110100100`? Podaj wynik dziesiętnie (pamiętaj o zamianie sekund na minuty).

```py
print(len(bin(14400)[2:]))  # liczba pól zegara
print(int("1111110100100", 2) // 60)  # liczba minut
```

```cpp
// C++23
#include <format>
#include <print>
#include <string>

int main() {
    std::println("{}", std::format("{:b}", 14400).size()); // liczba pól zegara
    std::println("{}", std::stoi("1111110100100", nullptr, 2) / 60); // liczba minut
}
```

```java
// Java 25
public class Zadanie {
    public static void main(String[] args) throws Exception {
        System.out.println(Integer.toBinaryString(14400).length()); // liczba pól zegara
        System.out.println(Integer.parseInt("1111110100100", 2) / 60); // liczba minut
    }
}
```
**Odpowiedź:** a) 14 pól; b) 135 minut

## 1c

> **Treść zadania:** Zegar dwójkowy z zadania 1a/1b.
>
> Zapisz algorytm, który dla czasu wykładu s (liczba całkowita dodatnia, w sekundach) obliczy l — liczbę jedynek wyświetlonych na zegarze na koniec wykładu. Uzupełnij też tabelę przykładów dla s = 3600 i s = 5400 (np. napis `111000010000` zawiera 4 jedynki).

```py
def liczba_jedynek(s):
    l = 0
    while s > 0:
        if s % 2 == 1:
            l += 1
        s = s // 2
    return l


print(liczba_jedynek(3600), liczba_jedynek(5400))
```

```cpp
// C++23
#include <print>

int liczba_jedynek(int s) {
    int l = 0;
    while (s > 0) {
        if (s % 2 == 1) {
            l += 1;
        }
        s = s / 2;
    }
    return l;
}

int main() {
    std::println("{} {}", liczba_jedynek(3600), liczba_jedynek(5400));
}
```

```java
// Java 25
public class Zadanie {
    static int liczbaJedynek(int s) {
        int l = 0;
        while (s > 0) {
            if (s % 2 == 1) {
                l += 1;
            }
            s = s / 2;
        }
        return l;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(liczbaJedynek(3600) + " " + liczbaJedynek(5400));
    }
}
```
**Odpowiedź:** dla 3600 → 4, dla 5400 → 5

## 2a

> **Treść zadania:** Algorytm dla liczby całkowitej n ≥ 2 wypisuje TAK lub NIE (`n mod i` — reszta z dzielenia n przez i):
>
> ```
> krok 1. i ← 2
> krok 2. jeśli i ≥ n, wypisz TAK i przejdź do kroku 5
> krok 3. jeśli (n mod i) = 0, wypisz NIE i przejdź do kroku 5
> krok 4. i ← i + 1 i przejdź do kroku 2
> krok 5. zakończ
> ```
>
> - 2a — Podaj komunikat wypisany dla n = 25, 37, 41, 49.
> - 2b — Oceń prawdziwość zdań: (1) warunek z kroku 3 wykona się dla każdego n dokładnie n razy; (2) wynikiem jest TAK, gdy n jest liczbą pierwszą; (3) wynikiem jest NIE, gdy n jest liczbą złożoną; (4) dla nieparzystego n algorytm nigdy się nie zakończy.

```py
def algorytm(n):
    i = 2
    while True:
        if i >= n:
            return "TAK"
        if n % i == 0:
            return "NIE"
        i += 1


for n in [25, 37, 41, 49]:
    print(n, algorytm(n))
```

```cpp
// C++23
#include <print>
#include <string>

std::string algorytm(int n) {
    int i = 2;
    while (true) {
        if (i >= n) {
            return "TAK";
        }
        if (n % i == 0) {
            return "NIE";
        }
        i += 1;
    }
}

int main() {
    for (int n : {25, 37, 41, 49}) {
        std::println("{} {}", n, algorytm(n));
    }
}
```

```java
// Java 25
public class Zadanie {
    static String algorytm(int n) {
        int i = 2;
        while (true) {
            if (i >= n) {
                return "TAK";
            }
            if (n % i == 0) {
                return "NIE";
            }
            i += 1;
        }
    }

    public static void main(String[] args) throws Exception {
        for (int n : new int[]{25, 37, 41, 49}) {
            System.out.println(n + " " + algorytm(n));
        }
    }
}
```
**Odpowiedź:** 25 NIE, 37 TAK, 41 TAK, 49 NIE; b) F, P, P, F

## 2c

> **Treść zadania:** Zapisz algorytm rozkładu liczby całkowitej n ≥ 2 na czynniki pierwsze — wynikiem jest ciąg liczb pierwszych, których iloczyn daje n.
>
> Przykłady: n = 42 → 2, 3, 7; n = 17 → 17; n = 36 → 2, 2, 3, 3.

```py
def rozklad(n):
    czynniki = []
    i = 2
    while n > 1:
        while n % i == 0:
            czynniki.append(i)
            n = n // i
        i += 1
    return czynniki


for n in [42, 17, 36]:
    print(n, rozklad(n))
```

```cpp
// C++23
#include <print>
#include <vector>

std::vector<int> rozklad(int n) {
    std::vector<int> czynniki;
    int i = 2;
    while (n > 1) {
        while (n % i == 0) {
            czynniki.push_back(i);
            n = n / i;
        }
        i += 1;
    }
    return czynniki;
}

int main() {
    for (int n : {42, 17, 36}) {
        std::println("{} {}", n, rozklad(n)); // wektor wypisuje się jako [2, 3, 7]
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static List<Integer> rozklad(int n) {
        var czynniki = new ArrayList<Integer>();
        int i = 2;
        while (n > 1) {
            while (n % i == 0) {
                czynniki.add(i);
                n = n / i;
            }
            i += 1;
        }
        return czynniki;
    }

    public static void main(String[] args) throws Exception {
        for (int n : new int[]{42, 17, 36}) {
            System.out.println(n + " " + rozklad(n)); // lista wypisuje się jako [2, 3, 7]
        }
    }
}
```
**Odpowiedź:** 42 → 2, 3, 7; 17 → 17; 36 → 2, 2, 3, 3

## 4a

> **Treść zadania:** W pliku `hasla.txt` zapisano 200 haseł, każde w osobnym wierszu; hasło składa się z małych liter alfabetu angielskiego i ma od 3 do 10 znaków.
>
> Podaj, ile haseł ma parzystą, a ile nieparzystą liczbę znaków. Odpowiedź zapisz w pliku `wynik4a.txt`.

```py
parzyste = 0
nieparzyste = 0

with open("hasla.txt") as file:
    for line in file:
        haslo = line.strip()
        if len(haslo) % 2 == 0:
            parzyste += 1
        else:
            nieparzyste += 1

print(parzyste, nieparzyste)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    int parzyste = 0;
    int nieparzyste = 0;
    std::ifstream plik("hasla.txt");
    std::string haslo;
    while (plik >> haslo) {
        if (haslo.size() % 2 == 0) {
            parzyste += 1;
        } else {
            nieparzyste += 1;
        }
    }
    std::println("{} {}", parzyste, nieparzyste);
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int parzyste = 0;
        int nieparzyste = 0;
        for (String linia : Files.readAllLines(Path.of("hasla.txt"))) {
            String haslo = linia.strip();
            if (haslo.length() % 2 == 0) {
                parzyste += 1;
            } else {
                nieparzyste += 1;
            }
        }
        System.out.println(parzyste + " " + nieparzyste);
    }
}
```
**Odpowiedź:** 105 haseł ma parzystą liczbę znaków, 95 nieparzystą

## 4b

> **Treść zadania:** Dane z pliku `hasla.txt` (200 haseł z małych liter).
>
> Wypisz hasła będące palindromami (czytane od lewej i od prawej brzmią tak samo, np. kajak), po jednym w wierszu, w kolejności z pliku. Wynik zapisz w pliku `wynik4b.txt`.

```py
with open("hasla.txt") as file:
    for line in file:
        haslo = line.strip()
        if haslo == haslo[::-1]:
            print(haslo)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("hasla.txt");
    std::string haslo;
    while (plik >> haslo) {
        std::string odwrocone(haslo.rbegin(), haslo.rend());
        if (haslo == odwrocone) {
            std::println("{}", haslo);
        }
    }
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        for (String linia : Files.readAllLines(Path.of("hasla.txt"))) {
            String haslo = linia.strip();
            if (haslo.equals(new StringBuilder(haslo).reverse().toString())) {
                System.out.println(haslo);
            }
        }
    }
}
```
**Odpowiedź:** dompmod, grafarg, kajak, komok, matam, mpoopm, mpouiuopm, oddo, omo, pokop, plkjjklp, pokkop, plolp

## 4c

> **Treść zadania:** Dane z pliku `hasla.txt` (200 haseł z małych liter).
>
> Wypisz hasła zawierające dwa sąsiednie znaki, których suma kodów ASCII wynosi 220 (np. `krzysio` zawiera „si”: 115 + 105 = 220; `cyrk` zawiera „cy”: 99 + 121 = 220), po jednym w wierszu, w kolejności z pliku. Wynik zapisz w pliku `wynik4c.txt`.

```py
with open("hasla.txt") as file:
    for line in file:
        haslo = line.strip()
        for i in range(1, len(haslo)):
            if ord(haslo[i - 1]) + ord(haslo[i]) == 220:
                print(haslo)
                break
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("hasla.txt");
    std::string haslo;
    while (plik >> haslo) {
        for (size_t i = 1; i < haslo.size(); i++) {
            if (haslo[i - 1] + haslo[i] == 220) { // suma kodów ASCII sąsiednich znaków
                std::println("{}", haslo);
                break;
            }
        }
    }
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        for (String linia : Files.readAllLines(Path.of("hasla.txt"))) {
            String haslo = linia.strip();
            for (int i = 1; i < haslo.length(); i++) {
                if (haslo.charAt(i - 1) + haslo.charAt(i) == 220) { // suma kodów ASCII sąsiednich znaków
                    System.out.println(haslo);
                    break;
                }
            }
        }
    }
}
```
**Odpowiedź:** amodda, damod, damodd, dompmod, edamo, edamod, isksad, iughd, … (54 hasła)

## 6a

> **Treść zadania:** W liceum przeprowadzono test z historii złożony z 25 pytań: pytania 1–5 dotyczą prehistorii, 6–10 starożytności, 11–15 średniowiecza, 16–20 historii nowożytnej, 21–25 historii najnowszej. Plik `test.txt` zawiera wyniki 126 uczniów: pierwszy wiersz to nagłówek (`Nr_ucznia` i numery pytań), a każdy kolejny — numer ucznia i 25 wartości 0/1 (1 — poprawna odpowiedź) oddzielonych spacjami. Odpowiedzi zapisz w pliku `wyniki6.txt`, poprzedzając je literą podpunktu.
>
> Podaj numery pytań, na które poprawnie odpowiedziało więcej niż 50% uczniów.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
uczniowie = []

with open("test.txt") as file:
    next(file)
    for line in file:
        uczniowie.append(list(map(int, line.split())))

for pytanie in range(1, 26):
    poprawne = 0
    for uczen in uczniowie:
        poprawne += uczen[pytanie]
    if poprawne > len(uczniowie) / 2:
        print(pytanie)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::vector<std::vector<int>> uczniowie;
    std::ifstream plik("test.txt");
    std::string linia;
    std::getline(plik, linia); // pomijamy wiersz nagłówka
    while (std::getline(plik, linia)) {
        std::istringstream strumien(linia);
        std::vector<int> odpowiedzi;
        int x;
        while (strumien >> x) {
            odpowiedzi.push_back(x);
        }
        uczniowie.push_back(odpowiedzi);
    }

    for (int pytanie = 1; pytanie < 26; pytanie++) {
        int poprawne = 0;
        for (const auto& uczen : uczniowie) {
            poprawne += uczen[pytanie];
        }
        if (poprawne > uczniowie.size() / 2.0) {
            std::println("{}", pytanie);
        }
    }
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var uczniowie = new ArrayList<int[]>();
        List<String> linie = Files.readAllLines(Path.of("test.txt"));
        for (String linia : linie.subList(1, linie.size())) { // pomijamy wiersz nagłówka
            uczniowie.add(Arrays.stream(linia.strip().split("\\s+")).mapToInt(Integer::parseInt).toArray());
        }

        for (int pytanie = 1; pytanie < 26; pytanie++) {
            int poprawne = 0;
            for (int[] uczen : uczniowie) {
                poprawne += uczen[pytanie];
            }
            if (poprawne > uczniowie.size() / 2.0) {
                System.out.println(pytanie);
            }
        }
    }
}
```
**Odpowiedź:** 2, 9, 12, 18, 19, 20, 22

## 6b

> **Treść zadania:** Dane z pliku `test.txt` (126 uczniów, 25 pytań, 0/1).
>
> Podaj, ilu uczniów uzyskało wynik (liczbę poprawnych odpowiedzi) wyższy od średniej w całej grupie.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
wyniki = []

with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        wyniki.append(sum(odpowiedzi[1:]))

srednia = sum(wyniki) / len(wyniki)
count = 0
for wynik in wyniki:
    if wynik > srednia:
        count += 1

print(count)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::vector<int> wyniki;
    std::ifstream plik("test.txt");
    std::string linia;
    std::getline(plik, linia); // pomijamy wiersz nagłówka
    while (std::getline(plik, linia)) {
        std::istringstream strumien(linia);
        int numer, x, suma = 0;
        strumien >> numer; // pierwsza liczba to numer ucznia
        while (strumien >> x) {
            suma += x;
        }
        wyniki.push_back(suma);
    }

    double srednia = 0;
    for (int wynik : wyniki) {
        srednia += wynik;
    }
    srednia /= wyniki.size();
    int count = 0;
    for (int wynik : wyniki) {
        if (wynik > srednia) {
            count += 1;
        }
    }
    std::println("{}", count);
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var wyniki = new ArrayList<Integer>();
        List<String> linie = Files.readAllLines(Path.of("test.txt"));
        for (String linia : linie.subList(1, linie.size())) { // pomijamy wiersz nagłówka
            String[] odpowiedzi = linia.strip().split("\\s+");
            int suma = 0;
            for (int i = 1; i < odpowiedzi.length; i++) { // pierwsza liczba to numer ucznia
                suma += Integer.parseInt(odpowiedzi[i]);
            }
            wyniki.add(suma);
        }

        double srednia = 0;
        for (int wynik : wyniki) {
            srednia += wynik;
        }
        srednia /= wyniki.size();
        int count = 0;
        for (int wynik : wyniki) {
            if (wynik > srednia) {
                count += 1;
            }
        }
        System.out.println(count);
    }
}
```
**Odpowiedź:** 55

## 6c

> **Treść zadania:** Dane z pliku `test.txt` (126 uczniów, 25 pytań, 0/1).
>
> Podaj, ilu uczniów otrzymało ocenę bardzo dobrą (powyżej 90% poprawnych odpowiedzi), a ilu niedostateczną (30% i mniej poprawnych odpowiedzi).

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
bardzo_dobre = 0
niedostateczne = 0

with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        procent = sum(odpowiedzi[1:]) / 25 * 100
        if procent > 90:
            bardzo_dobre += 1
        if procent <= 30:
            niedostateczne += 1

print("bardzo dobre:", bardzo_dobre, "niedostateczne:", niedostateczne)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>

int main() {
    int bardzo_dobre = 0;
    int niedostateczne = 0;
    std::ifstream plik("test.txt");
    std::string linia;
    std::getline(plik, linia); // pomijamy wiersz nagłówka
    while (std::getline(plik, linia)) {
        std::istringstream strumien(linia);
        int numer, x, suma = 0;
        strumien >> numer; // pierwsza liczba to numer ucznia
        while (strumien >> x) {
            suma += x;
        }
        double procent = suma / 25.0 * 100;
        if (procent > 90) {
            bardzo_dobre += 1;
        }
        if (procent <= 30) {
            niedostateczne += 1;
        }
    }
    std::println("bardzo dobre: {} niedostateczne: {}", bardzo_dobre, niedostateczne);
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int bardzoDobre = 0;
        int niedostateczne = 0;
        List<String> linie = Files.readAllLines(Path.of("test.txt"));
        for (String linia : linie.subList(1, linie.size())) { // pomijamy wiersz nagłówka
            String[] odpowiedzi = linia.strip().split("\\s+");
            int suma = 0;
            for (int i = 1; i < odpowiedzi.length; i++) { // pierwsza liczba to numer ucznia
                suma += Integer.parseInt(odpowiedzi[i]);
            }
            double procent = suma / 25.0 * 100;
            if (procent > 90) {
                bardzoDobre += 1;
            }
            if (procent <= 30) {
                niedostateczne += 1;
            }
        }
        System.out.println("bardzo dobre: " + bardzoDobre + " niedostateczne: " + niedostateczne);
    }
}
```
**Odpowiedź:** bardzo dobre: 1, niedostateczne: 6

## 6d

> **Treść zadania:** Dane z pliku `test.txt` (126 uczniów, 25 pytań, 0/1).
>
> Podaj numery uczniów, którzy poprawnie odpowiedzieli na pytania 5, 15 i 25.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        if odpowiedzi[5] == 1 and odpowiedzi[15] == 1 and odpowiedzi[25] == 1:
            print(odpowiedzi[0])
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::ifstream plik("test.txt");
    std::string linia;
    std::getline(plik, linia); // pomijamy wiersz nagłówka
    while (std::getline(plik, linia)) {
        std::istringstream strumien(linia);
        std::vector<int> odpowiedzi;
        int x;
        while (strumien >> x) {
            odpowiedzi.push_back(x);
        }
        if (odpowiedzi[5] == 1 && odpowiedzi[15] == 1 && odpowiedzi[25] == 1) {
            std::println("{}", odpowiedzi[0]);
        }
    }
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        List<String> linie = Files.readAllLines(Path.of("test.txt"));
        for (String linia : linie.subList(1, linie.size())) { // pomijamy wiersz nagłówka
            int[] odpowiedzi = Arrays.stream(linia.strip().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            if (odpowiedzi[5] == 1 && odpowiedzi[15] == 1 && odpowiedzi[25] == 1) {
                System.out.println(odpowiedzi[0]);
            }
        }
    }
}
```
**Odpowiedź:** 2, 45, 65, 70, 79

## 6e

> **Treść zadania:** Dane z pliku `test.txt`; epoki: pytania 1–5 prehistoria, 6–10 starożytność, 11–15 średniowiecze, 16–20 historia nowożytna, 21–25 historia najnowsza.
>
> Zestaw dla każdej epoki łączną liczbę poprawnych odpowiedzi uczniów na pytania z tej epoki i wykonaj czytelnie opisany wykres kolumnowy.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
epoki = ["prehistoria", "starożytność", "średniowiecze", "historia nowożytna", "historia najnowsza"]
poprawne = [0] * 5

with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        for pytanie in range(1, 26):
            poprawne[(pytanie - 1) // 5] += odpowiedzi[pytanie]

for i in range(5):
    print(epoki[i], poprawne[i])
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> epoki = {"prehistoria", "starożytność", "średniowiecze", "historia nowożytna", "historia najnowsza"};
    std::vector<int> poprawne(5, 0);
    std::ifstream plik("test.txt");
    std::string linia;
    std::getline(plik, linia); // pomijamy wiersz nagłówka
    while (std::getline(plik, linia)) {
        std::istringstream strumien(linia);
        std::vector<int> odpowiedzi;
        int x;
        while (strumien >> x) {
            odpowiedzi.push_back(x);
        }
        for (int pytanie = 1; pytanie < 26; pytanie++) {
            poprawne[(pytanie - 1) / 5] += odpowiedzi[pytanie];
        }
    }
    for (int i = 0; i < 5; i++) {
        std::println("{} {}", epoki[i], poprawne[i]);
    }
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        String[] epoki = {"prehistoria", "starożytność", "średniowiecze", "historia nowożytna", "historia najnowsza"};
        int[] poprawne = new int[5];
        List<String> linie = Files.readAllLines(Path.of("test.txt"));
        for (String linia : linie.subList(1, linie.size())) { // pomijamy wiersz nagłówka
            int[] odpowiedzi = Arrays.stream(linia.strip().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            for (int pytanie = 1; pytanie < 26; pytanie++) {
                poprawne[(pytanie - 1) / 5] += odpowiedzi[pytanie];
            }
        }
        for (int i = 0; i < 5; i++) {
            System.out.println(epoki[i] + " " + poprawne[i]);
        }
    }
}
```
**Odpowiedź:** prehistoria 278, starożytność 263, średniowiecze 281, historia nowożytna 320, historia najnowsza 298 (wykres kolumnowy wykonuje się w arkuszu kalkulacyjnym)
