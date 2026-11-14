<h1 align="center">Matura próbna 2021 — kwiecień</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

> Rozwiązanie nieprzetestowane na danych CKE.

W pliku `liczby.txt` każdy wiersz zawiera jedną liczbę zapisaną w systemie pozycyjnym, a ostatnia cyfra wiersza oznacza podstawę tego systemu (np. `10112` to liczba `1011` w systemie dwójkowym). Treść podpunktów odtworzono na podstawie wcześniejszego rozwiązania z repozytorium.

## 6.1

> **Treść zadania:** *(Rekonstrukcja — brak oficjalnego arkusza; treść odtworzona na podstawie opisu i kodu rozwiązania.)* Plik `liczby.txt`: w każdym wierszu liczba zapisana w systemie pozycyjnym, a ostatnia cyfra wiersza to podstawa tego systemu (np. `10112` oznacza `1011` w systemie dwójkowym).
>
> Podaj, ile liczb w pliku jest zapisanych w systemie szóstkowym.

```py
# ile liczb jest zapisanych w systemie szóstkowym
ile = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        if line[-1] == "6":
            ile += 1

print(ile)
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    // ile liczb jest zapisanych w systemie szóstkowym
    int ile = 0;

    std::ifstream plik("liczby.txt");
    std::string linia;
    while (plik >> linia) {
        if (linia.back() == '6') ile++;
    }

    std::println("{}", ile);
}
```
```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // ile liczb jest zapisanych w systemie szóstkowym
        int ile = 0;

        for (var linia : Files.readAllLines(Path.of("liczby.txt"))) {
            linia = linia.strip();
            if (linia.endsWith("6")) ile++;
        }

        System.out.println(ile);
    }
}
```

## 6.2

> **Treść zadania:** *(Rekonstrukcja — brak oficjalnego arkusza; treść odtworzona na podstawie opisu i kodu rozwiązania.)* Dane z pliku `liczby.txt` (ostatnia cyfra wiersza to podstawa systemu).
>
> Podaj, ile liczb zapisanych w systemie siódemkowym nie zawiera w zapisie cyfry 6.

```py
# ile liczb zapisanych w systemie siódemkowym nie zawiera cyfry 6
ile = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], line[-1]
        if podstawa == "7" and "6" not in cyfry:
            ile += 1

print(ile)
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    // ile liczb zapisanych w systemie siódemkowym nie zawiera cyfry 6
    int ile = 0;

    std::ifstream plik("liczby.txt");
    std::string linia;
    while (plik >> linia) {
        std::string cyfry = linia.substr(0, linia.size() - 1);
        char podstawa = linia.back();
        if (podstawa == '7' && !cyfry.contains('6')) ile++;
    }

    std::println("{}", ile);
}
```
```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // ile liczb zapisanych w systemie siódemkowym nie zawiera cyfry 6
        int ile = 0;

        for (var linia : Files.readAllLines(Path.of("liczby.txt"))) {
            linia = linia.strip();
            String cyfry = linia.substring(0, linia.length() - 1);
            char podstawa = linia.charAt(linia.length() - 1);
            if (podstawa == '7' && !cyfry.contains("6")) ile++;
        }

        System.out.println(ile);
    }
}
```

## 6.3

> **Treść zadania:** *(Rekonstrukcja — brak oficjalnego arkusza; treść odtworzona na podstawie opisu i kodu rozwiązania.)* Dane z pliku `liczby.txt` (ostatnia cyfra wiersza to podstawa systemu).
>
> Podaj, ile liczb zapisanych w systemie dwójkowym jest nieparzystych.

```py
# ile liczb zapisanych w systemie dwójkowym jest nieparzystych
ile = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], line[-1]
        if podstawa == "2" and int(cyfry, 2) % 2 == 1:
            ile += 1

print(ile)
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    // ile liczb zapisanych w systemie dwójkowym jest nieparzystych
    int ile = 0;

    std::ifstream plik("liczby.txt");
    std::string linia;
    while (plik >> linia) {
        std::string cyfry = linia.substr(0, linia.size() - 1);
        char podstawa = linia.back();
        // liczba dwójkowa jest nieparzysta, gdy jej ostatnia cyfra to 1
        if (podstawa == '2' && cyfry.back() == '1') ile++;
    }

    std::println("{}", ile);
}
```
```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // ile liczb zapisanych w systemie dwójkowym jest nieparzystych
        int ile = 0;

        for (var linia : Files.readAllLines(Path.of("liczby.txt"))) {
            linia = linia.strip();
            String cyfry = linia.substring(0, linia.length() - 1);
            char podstawa = linia.charAt(linia.length() - 1);
            // liczba dwójkowa jest nieparzysta, gdy jej ostatnia cyfra to 1
            if (podstawa == '2' && cyfry.endsWith("1")) ile++;
        }

        System.out.println(ile);
    }
}
```

## 6.4

> **Treść zadania:** *(Rekonstrukcja — brak oficjalnego arkusza; treść odtworzona na podstawie opisu i kodu rozwiązania.)* Dane z pliku `liczby.txt` (ostatnia cyfra wiersza to podstawa systemu).
>
> Podaj sumę (w systemie dziesiętnym) wszystkich liczb zapisanych w systemie czwórkowym.

```py
# suma (dziesiętnie) wszystkich liczb zapisanych w systemie czwórkowym
suma = 0

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], line[-1]
        if podstawa == "4":
            suma += int(cyfry, 4)

print(suma)
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int main() {
    // suma (dziesiętnie) wszystkich liczb zapisanych w systemie czwórkowym
    long long suma = 0;

    std::ifstream plik("liczby.txt");
    std::string linia;
    while (plik >> linia) {
        std::string cyfry = linia.substr(0, linia.size() - 1);
        char podstawa = linia.back();
        if (podstawa == '4') suma += std::stoll(cyfry, nullptr, 4);
    }

    std::println("{}", suma);
}
```
```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // suma (dziesiętnie) wszystkich liczb zapisanych w systemie czwórkowym
        long suma = 0;

        for (var linia : Files.readAllLines(Path.of("liczby.txt"))) {
            linia = linia.strip();
            String cyfry = linia.substring(0, linia.length() - 1);
            char podstawa = linia.charAt(linia.length() - 1);
            if (podstawa == '4') suma += Long.parseLong(cyfry, 4);
        }

        System.out.println(suma);
    }
}
```

## 6.5

> **Treść zadania:** *(Rekonstrukcja — brak oficjalnego arkusza; treść odtworzona na podstawie opisu i kodu rozwiązania.)* Dane z pliku `liczby.txt` (ostatnia cyfra wiersza to podstawa systemu).
>
> Podaj największą i najmniejszą liczbę z pliku — w postaci zapisanej w pliku oraz jej wartość dziesiętną.

```py
# największa i najmniejsza liczba w pliku (zapis z pliku i wartość dziesiętna)
liczby = []

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        cyfry, podstawa = line[:-1], int(line[-1])
        liczby.append((int(cyfry, podstawa), line))

najwieksza = max(liczby)
najmniejsza = min(liczby)
print(najwieksza[1], najwieksza[0])
print(najmniejsza[1], najmniejsza[0])
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <utility>
#include <vector>

int main() {
    // największa i najmniejsza liczba w pliku (zapis z pliku i wartość dziesiętna)
    std::vector<std::pair<long long, std::string>> liczby;

    std::ifstream plik("liczby.txt");
    std::string linia;
    while (plik >> linia) {
        std::string cyfry = linia.substr(0, linia.size() - 1);
        int podstawa = linia.back() - '0';
        liczby.push_back({std::stoll(cyfry, nullptr, podstawa), linia});
    }

    auto najwieksza = *std::max_element(liczby.begin(), liczby.end());
    auto najmniejsza = *std::min_element(liczby.begin(), liczby.end());
    std::println("{} {}", najwieksza.second, najwieksza.first);
    std::println("{} {}", najmniejsza.second, najmniejsza.first);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    record Liczba(long wartosc, String zapis) {}

    public static void main(String[] args) throws Exception {
        // największa i najmniejsza liczba w pliku (zapis z pliku i wartość dziesiętna)
        var liczby = new ArrayList<Liczba>();

        for (var linia : Files.readAllLines(Path.of("liczby.txt"))) {
            linia = linia.strip();
            String cyfry = linia.substring(0, linia.length() - 1);
            int podstawa = linia.charAt(linia.length() - 1) - '0';
            liczby.add(new Liczba(Long.parseLong(cyfry, podstawa), linia));
        }

        // porównujemy najpierw wartość, potem zapis (jak krotki w Pythonie)
        var porownanie = Comparator.comparingLong(Liczba::wartosc).thenComparing(Liczba::zapis);
        var najwieksza = Collections.max(liczby, porownanie);
        var najmniejsza = Collections.min(liczby, porownanie);
        System.out.println(najwieksza.zapis() + " " + najwieksza.wartosc());
        System.out.println(najmniejsza.zapis() + " " + najmniejsza.wartosc());
    }
}
```
