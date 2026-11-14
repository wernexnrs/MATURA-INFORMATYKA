<h1 align="center">Matura 2009 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

> **Treść zadania:** Zadanie 1 (rzut oszczepem). Wyniki zawodników:
> - A: 60,51 61,34 61,85 61,97 62,79 63,00 63,81 63,88
> - B: 60,41 60,44 60,85 62,71 61,79 60,00
> - C: 61,45 60,89 60,20 60,01 59,22 58,99 58,75
>
> Algorytm dla niepustego ciągu liczb dodatnich:
>
> ```
> 1. aktualna ← pierwsza liczba
> 2. jeśli brak kolejnej liczby → wypisz TAK, koniec
> 3. następna ← kolejna liczba
> 4. jeśli następna > aktualna: aktualna ← następna, wróć do 2
>    w przeciwnym razie → wypisz NIE, koniec
> ```
>
> - 1a — określ, kiedy algorytm wypisuje TAK, a kiedy NIE (uzupełnij wynik w specyfikacji);
> - 1b — podaj, ile razy zostanie wykonany krok 3 dla ciągu wyników zawodników A, B i C.

```py
def algorytm(ciag):
    ile_razy = 0  # ile razy wykonano krok 3.
    aktualna = ciag[0]
    i = 1
    while i < len(ciag):
        nastepna = ciag[i]
        ile_razy += 1
        i += 1
        if nastepna > aktualna:
            aktualna = nastepna
        else:
            return "NIE", ile_razy
    return "TAK", ile_razy


A = [60.51, 61.34, 61.85, 61.97, 62.79, 63.00, 63.81, 63.88]
B = [60.41, 60.44, 60.85, 62.71, 61.79, 60.00]
C = [61.45, 60.89, 60.20, 60.01, 59.22, 58.99, 58.75]

for ciag in [A, B, C]:
    print(*algorytm(ciag))
```

```cpp
// C++23
#include <print>
#include <string>
#include <utility>
#include <vector>

std::pair<std::string, int> algorytm(const std::vector<double>& ciag) {
    int ile_razy = 0; // ile razy wykonano krok 3.
    double aktualna = ciag[0];
    size_t i = 1;
    while (i < ciag.size()) {
        double nastepna = ciag[i];
        ile_razy++;
        i++;
        if (nastepna > aktualna)
            aktualna = nastepna;
        else
            return {"NIE", ile_razy};
    }
    return {"TAK", ile_razy};
}

int main() {
    std::vector<double> A = {60.51, 61.34, 61.85, 61.97, 62.79, 63.00, 63.81, 63.88};
    std::vector<double> B = {60.41, 60.44, 60.85, 62.71, 61.79, 60.00};
    std::vector<double> C = {61.45, 60.89, 60.20, 60.01, 59.22, 58.99, 58.75};

    for (const auto& ciag : {A, B, C}) {
        auto [odpowiedz, ile_razy] = algorytm(ciag);
        std::println("{} {}", odpowiedz, ile_razy);
    }
}
```

```java
// Java 25
public class Zadanie {
    record Wynik(String odpowiedz, int ileRazy) {}

    static Wynik algorytm(double[] ciag) {
        int ileRazy = 0; // ile razy wykonano krok 3.
        double aktualna = ciag[0];
        int i = 1;
        while (i < ciag.length) {
            double nastepna = ciag[i];
            ileRazy++;
            i++;
            if (nastepna > aktualna)
                aktualna = nastepna;
            else
                return new Wynik("NIE", ileRazy);
        }
        return new Wynik("TAK", ileRazy);
    }

    public static void main(String[] args) {
        double[] A = {60.51, 61.34, 61.85, 61.97, 62.79, 63.00, 63.81, 63.88};
        double[] B = {60.41, 60.44, 60.85, 62.71, 61.79, 60.00};
        double[] C = {61.45, 60.89, 60.20, 60.01, 59.22, 58.99, 58.75};

        for (double[] ciag : new double[][]{A, B, C}) {
            Wynik w = algorytm(ciag);
            System.out.println(w.odpowiedz() + " " + w.ileRazy());
        }
    }
}
```
**Odpowiedź:** a) TAK, gdy ciąg jest rosnący, w przeciwnym przypadku NIE; b) A: 7, B: 4, C: 1

## 1c

> **Treść zadania:** Zmodyfikuj algorytm z zadania 1 tak, aby dla niepustego, skończonego ciągu liczb dodatnich znajdował najlepszy wynik zawodnika, czyli największą liczbę w ciągu. Zapisz go w wybranej notacji.

```py
def najwiekszy(ciag):
    maks = ciag[0]
    for liczba in ciag[1:]:
        if liczba > maks:
            maks = liczba
    return maks


print(najwiekszy([60.41, 60.44, 60.85, 62.71, 61.79, 60.00]))
```

```cpp
// C++23
#include <print>
#include <vector>

double najwiekszy(const std::vector<double>& ciag) {
    double maks = ciag[0];
    for (size_t i = 1; i < ciag.size(); i++)
        if (ciag[i] > maks) maks = ciag[i];
    return maks;
}

int main() {
    std::println("{}", najwiekszy({60.41, 60.44, 60.85, 62.71, 61.79, 60.00}));
}
```

```java
// Java 25
public class Zadanie {
    static double najwiekszy(double[] ciag) {
        double maks = ciag[0];
        for (int i = 1; i < ciag.length; i++)
            if (ciag[i] > maks) maks = ciag[i];
        return maks;
    }

    public static void main(String[] args) {
        System.out.println(najwiekszy(new double[]{60.41, 60.44, 60.85, 62.71, 61.79, 60.00}));
    }
}
```
**Odpowiedź:** algorytm wyznaczania maksimum (dla zawodnika B: 62.71)

## 2a i 2b

> **Treść zadania:** Zadanie 2. Ceny podawane są w systemie dwójkowym i dziesiętnym (z dwoma miejscami po przecinku).
> - 2a — uzupełnij cennik: kakao 111,11₂ = 7,75; herbata czarna 100,01₂ = ?; herbata owocowa ? = 4,50; capuccino 101,00₂ = ?; kawa espresso ? = 6,00;
> - 2b — zapisz algorytm przeliczania ceny z systemu dwójkowego na dziesiętny. Dane: napis `s` złożony z zer i jedynek, przecinka i dwóch cyfr binarnych po przecinku (część przed przecinkiem niepusta). Wynik: wartość dziesiętna `w` tej liczby.

```py
def dwojkowy_na_dziesietny(s):
    calkowita, ulamkowa = s.split(",")
    w = 0
    for cyfra in calkowita:
        w = w * 2 + int(cyfra)
    w = w + int(ulamkowa[0]) * 0.5 + int(ulamkowa[1]) * 0.25
    return w


def dziesietny_na_dwojkowy(x):
    calkowita = int(x)
    ulamkowa = x - calkowita
    napis = bin(calkowita)[2:] + ","
    for _ in range(2):
        ulamkowa *= 2
        napis += str(int(ulamkowa))
        ulamkowa -= int(ulamkowa)
    return napis


print("kakao", dwojkowy_na_dziesietny("111,11"))
print("herbata czarna", dwojkowy_na_dziesietny("100,01"))
print("herbata owocowa", dziesietny_na_dwojkowy(4.50))
print("capuccino", dwojkowy_na_dziesietny("101,00"))
print("kawa espresso", dziesietny_na_dwojkowy(6.00))
```

```cpp
// C++23
#include <format>
#include <print>
#include <string>

double dwojkowy_na_dziesietny(const std::string& s) {
    size_t przecinek = s.find(',');
    std::string calkowita = s.substr(0, przecinek);
    std::string ulamkowa = s.substr(przecinek + 1);
    double w = 0;
    for (char cyfra : calkowita)
        w = w * 2 + (cyfra - '0');
    w = w + (ulamkowa[0] - '0') * 0.5 + (ulamkowa[1] - '0') * 0.25;
    return w;
}

std::string dziesietny_na_dwojkowy(double x) {
    int calkowita = (int)x;
    double ulamkowa = x - calkowita;
    std::string napis = std::format("{:b}", calkowita) + ","; // {:b} - zapis dwójkowy
    for (int k = 0; k < 2; k++) {
        ulamkowa *= 2;
        napis += std::to_string((int)ulamkowa);
        ulamkowa -= (int)ulamkowa;
    }
    return napis;
}

// liczba rzeczywista wypisana jak w Pythonie (5.0 zamiast 5)
std::string zapis(double x) {
    std::string s = std::format("{}", x);
    if (s.find_first_of(".e") == std::string::npos) s += ".0";
    return s;
}

int main() {
    std::println("kakao {}", zapis(dwojkowy_na_dziesietny("111,11")));
    std::println("herbata czarna {}", zapis(dwojkowy_na_dziesietny("100,01")));
    std::println("herbata owocowa {}", dziesietny_na_dwojkowy(4.50));
    std::println("capuccino {}", zapis(dwojkowy_na_dziesietny("101,00")));
    std::println("kawa espresso {}", dziesietny_na_dwojkowy(6.00));
}
```

```java
// Java 25
public class Zadanie {
    static double dwojkowyNaDziesietny(String s) {
        String[] czesci = s.split(",");
        String calkowita = czesci[0], ulamkowa = czesci[1];
        double w = 0;
        for (char cyfra : calkowita.toCharArray())
            w = w * 2 + (cyfra - '0');
        w = w + (ulamkowa.charAt(0) - '0') * 0.5 + (ulamkowa.charAt(1) - '0') * 0.25;
        return w;
    }

    static String dziesietnyNaDwojkowy(double x) {
        int calkowita = (int) x;
        double ulamkowa = x - calkowita;
        String napis = Integer.toBinaryString(calkowita) + ",";
        for (int k = 0; k < 2; k++) {
            ulamkowa *= 2;
            napis += (int) ulamkowa;
            ulamkowa -= (int) ulamkowa;
        }
        return napis;
    }

    public static void main(String[] args) {
        System.out.println("kakao " + dwojkowyNaDziesietny("111,11"));
        System.out.println("herbata czarna " + dwojkowyNaDziesietny("100,01"));
        System.out.println("herbata owocowa " + dziesietnyNaDwojkowy(4.50));
        System.out.println("capuccino " + dwojkowyNaDziesietny("101,00"));
        System.out.println("kawa espresso " + dziesietnyNaDwojkowy(6.00));
    }
}
```
**Odpowiedź:** herbata czarna 4,25; herbata owocowa 100,10; capuccino 5,00; kawa espresso 110,00

## 4a i 4b

> **Treść zadania:** Zadanie 4 (temperatury). Plik `temp.txt` zawiera średnie temperatury miesięczne w Warszawie w latach 1779–2006: w każdym wierszu rok i 12 temperatur (liczby z przecinkiem dziesiętnym, oddzielone spacjami). Odpowiedzi zapisz w pliku `zad_4.txt`, poprzedzając je literą podpunktu. Średnia roczna to suma 12 średnich miesięcznych podzielona przez 12.
> - 4a — podaj najniższą średnią roczną temperaturę (z dwoma miejscami po przecinku) i rok jej wystąpienia;
> - 4b — podaj najwyższą średnią roczną temperaturę (z dwoma miejscami po przecinku) i rok jej wystąpienia.

```py
srednie = []

with open("temp.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split()
        rok = int(dane[0])
        temperatury = list(map(float, dane[1:]))
        srednie.append((sum(temperatury) / 12, rok))

najnizsza = min(srednie)
najwyzsza = max(srednie)
print("a)", round(najnizsza[0], 2), najnizsza[1])
print("b)", round(najwyzsza[0], 2), najwyzsza[1])
```

```cpp
// C++23
#include <algorithm>
#include <cmath>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::vector<std::pair<double, int>> srednie; // (średnia, rok)
    std::ifstream plik("temp.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        std::replace(linia.begin(), linia.end(), ',', '.'); // przecinek dziesiętny -> kropka
        std::istringstream ss(linia);
        int rok;
        if (!(ss >> rok)) continue;
        double suma = 0, t;
        for (int i = 0; i < 12; i++) {
            ss >> t;
            suma += t;
        }
        srednie.push_back({suma / 12, rok});
    }

    // pary porównują się najpierw po średniej, potem po roku - jak krotki w Pythonie
    auto najnizsza = *std::min_element(srednie.begin(), srednie.end());
    auto najwyzsza = *std::max_element(srednie.begin(), srednie.end());
    std::println("a) {} {}", std::round(najnizsza.first * 100) / 100, najnizsza.second);
    std::println("b) {} {}", std::round(najwyzsza.first * 100) / 100, najwyzsza.second);
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    record Srednia(double wartosc, int rok) {}

    public static void main(String[] args) throws Exception {
        var srednie = new ArrayList<Srednia>();
        for (String linia : Files.readAllLines(Path.of("temp.txt"))) {
            if (linia.isBlank()) continue;
            String[] dane = linia.strip().replace(",", ".").split("\\s+");
            int rok = Integer.parseInt(dane[0]);
            double suma = 0;
            for (int i = 1; i <= 12; i++) suma += Double.parseDouble(dane[i]);
            srednie.add(new Srednia(suma / 12, rok));
        }

        // porównujemy najpierw po średniej, potem po roku - jak krotki w Pythonie
        var porownanie = Comparator.comparingDouble(Srednia::wartosc).thenComparingInt(Srednia::rok);
        Srednia najnizsza = Collections.min(srednie, porownanie);
        Srednia najwyzsza = Collections.max(srednie, porownanie);
        System.out.println("a) " + Math.round(najnizsza.wartosc() * 100) / 100.0 + " " + najnizsza.rok());
        System.out.println("b) " + Math.round(najwyzsza.wartosc() * 100) / 100.0 + " " + najwyzsza.rok());
    }
}
```
**Odpowiedź:** a) 4,74 — rok 1829; b) 9,82 — rok 1989

## 4c

> **Treść zadania:** Na podstawie pliku `temp.txt` dla każdego z 12 miesięcy podaj minimalną i maksymalną średnią miesięczną temperaturę odnotowaną w latach 1779–2006 (zapisz w `zad_4.txt`). Sporządź wykres punktowy ilustrujący to zestawienie, z czytelnym opisem.

```py
miesiace = [[] for _ in range(12)]

with open("temp.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split()
        for i in range(12):
            miesiace[i].append(float(dane[i + 1]))

for i in range(12):
    print(i + 1, min(miesiace[i]), max(miesiace[i]))
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

// liczba rzeczywista wypisana jak w Pythonie (13.0 zamiast 13)
std::string zapis(double x) {
    std::string s = std::format("{}", x);
    if (s.find_first_of(".e") == std::string::npos) s += ".0";
    return s;
}

int main() {
    std::vector<std::vector<double>> miesiace(12);
    std::ifstream plik("temp.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        std::replace(linia.begin(), linia.end(), ',', '.'); // przecinek dziesiętny -> kropka
        std::istringstream ss(linia);
        int rok;
        if (!(ss >> rok)) continue;
        double t;
        for (int i = 0; i < 12; i++) {
            ss >> t;
            miesiace[i].push_back(t);
        }
    }

    for (int i = 0; i < 12; i++)
        std::println("{} {} {}", i + 1, zapis(std::ranges::min(miesiace[i])), zapis(std::ranges::max(miesiace[i])));
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var miesiace = new ArrayList<List<Double>>();
        for (int i = 0; i < 12; i++) miesiace.add(new ArrayList<>());
        for (String linia : Files.readAllLines(Path.of("temp.txt"))) {
            if (linia.isBlank()) continue;
            String[] dane = linia.strip().replace(",", ".").split("\\s+");
            for (int i = 0; i < 12; i++)
                miesiace.get(i).add(Double.parseDouble(dane[i + 1]));
        }

        for (int i = 0; i < 12; i++)
            System.out.println((i + 1) + " " + Collections.min(miesiace.get(i)) + " " + Collections.max(miesiace.get(i)));
    }
}
```
**Odpowiedź:** (miesiąc, min, max) 1: -13,5 3,5; 2: -13,7 5,1; 3: -6,9 7,4; 4: 2,4 13,2; 5: 7,9 18,2; 6: 13,0 22,4; 7: 14,6 23,5; 8: 14,0 23,8; 9: 9,1 16,8; 10: 1,8 12,6; 11: -3,4 7,6; 12: -14,8 3,9 (wykres punktowy wykonuje się w arkuszu kalkulacyjnym)

## 4d

> **Treść zadania:** W pliku `temp.txt` znajdź najdłuższy malejący ciąg średnich temperatur sierpnia w kolejnych latach. Podaj rok początkowy, rok końcowy i długość tego ciągu (np. w ciągu 20,4; 18,3; 18,7; 19,6; 17,0; 16,6; 16,4; 16,4; 17,9 najdłuższy malejący fragment to 19,6; 17,0; 16,6; 16,4 o długości 4).

```py
lata = []
sierpien = []

with open("temp.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split()
        lata.append(int(dane[0]))
        sierpien.append(float(dane[8]))

dlugosc = 1
najdluzszy = 1
koniec = 0

for i in range(1, len(sierpien)):
    if sierpien[i] < sierpien[i - 1]:
        dlugosc += 1
    else:
        dlugosc = 1
    if dlugosc > najdluzszy:
        najdluzszy = dlugosc
        koniec = i

print(lata[koniec - najdluzszy + 1], lata[koniec], najdluzszy)
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
    std::vector<int> lata;
    std::vector<double> sierpien;
    std::ifstream plik("temp.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        std::replace(linia.begin(), linia.end(), ',', '.'); // przecinek dziesiętny -> kropka
        std::istringstream ss(linia);
        int rok;
        if (!(ss >> rok)) continue;
        double t;
        for (int i = 1; i <= 8; i++) ss >> t; // 8. liczba po roku to sierpień
        lata.push_back(rok);
        sierpien.push_back(t);
    }

    int dlugosc = 1, najdluzszy = 1, koniec = 0;
    for (int i = 1; i < (int)sierpien.size(); i++) {
        if (sierpien[i] < sierpien[i - 1])
            dlugosc++;
        else
            dlugosc = 1;
        if (dlugosc > najdluzszy) {
            najdluzszy = dlugosc;
            koniec = i;
        }
    }
    std::println("{} {} {}", lata[koniec - najdluzszy + 1], lata[koniec], najdluzszy);
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var lata = new ArrayList<Integer>();
        var sierpien = new ArrayList<Double>();
        for (String linia : Files.readAllLines(Path.of("temp.txt"))) {
            if (linia.isBlank()) continue;
            String[] dane = linia.strip().replace(",", ".").split("\\s+");
            lata.add(Integer.parseInt(dane[0]));
            sierpien.add(Double.parseDouble(dane[8]));
        }

        int dlugosc = 1, najdluzszy = 1, koniec = 0;
        for (int i = 1; i < sierpien.size(); i++) {
            if (sierpien.get(i) < sierpien.get(i - 1))
                dlugosc++;
            else
                dlugosc = 1;
            if (dlugosc > najdluzszy) {
                najdluzszy = dlugosc;
                koniec = i;
            }
        }
        System.out.println(lata.get(koniec - najdluzszy + 1) + " " + lata.get(koniec) + " " + najdluzszy);
    }
}
```
**Odpowiedź:** od 1982 do 1987, długość 6

## 5

> **Treść zadania:** Zadanie 5 (liczby pierwsze). Plik `liczby.txt` zawiera 500 liczb całkowitych dodatnich (co najwyżej 6-cyfrowych), po jednej w wierszu. Napisz program, który wybierze z pliku tylko te liczby, które są kwadratami liczb pierwszych (np. 49 = 7²), i zapisze je w pliku `zad_5.txt`. Program ma działać poprawnie dla dowolnych innych 500 takich liczb.

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
    with open("zad_5.txt", "w") as wynik:
        for line in file:
            liczba = int(line.strip())
            pierwiastek = int(liczba ** 0.5)
            while pierwiastek * pierwiastek > liczba:
                pierwiastek -= 1
            while (pierwiastek + 1) * (pierwiastek + 1) <= liczba:
                pierwiastek += 1
            if pierwiastek * pierwiastek == liczba and czy_pierwsza(pierwiastek):
                print(liczba)
                wynik.write(str(liczba) + "\n")
```

```cpp
// C++23
#include <cmath>
#include <fstream>
#include <print>

bool czy_pierwsza(long long x) {
    if (x < 2) return false;
    for (long long i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
    return true;
}

int main() {
    std::ifstream plik("liczby.txt");
    std::ofstream wynik("zad_5.txt");
    long long liczba;
    while (plik >> liczba) {
        long long pierwiastek = (long long)std::sqrt((double)liczba);
        // poprawka ewentualnego błędu zaokrąglenia sqrt
        while (pierwiastek * pierwiastek > liczba) pierwiastek--;
        while ((pierwiastek + 1) * (pierwiastek + 1) <= liczba) pierwiastek++;
        if (pierwiastek * pierwiastek == liczba && czy_pierwsza(pierwiastek)) {
            std::println("{}", liczba);
            wynik << liczba << "\n";
        }
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.*;

public class Zadanie {
    static boolean czyPierwsza(long x) {
        if (x < 2) return false;
        for (long i = 2; i * i <= x; i++)
            if (x % i == 0) return false;
        return true;
    }

    public static void main(String[] args) throws Exception {
        try (var wynik = new PrintWriter("zad_5.txt")) {
            for (String linia : Files.readAllLines(Path.of("liczby.txt"))) {
                if (linia.isBlank()) continue;
                long liczba = Long.parseLong(linia.strip());
                long pierwiastek = (long) Math.sqrt(liczba);
                // poprawka ewentualnego błędu zaokrąglenia sqrt
                while (pierwiastek * pierwiastek > liczba) pierwiastek--;
                while ((pierwiastek + 1) * (pierwiastek + 1) <= liczba) pierwiastek++;
                if (pierwiastek * pierwiastek == liczba && czyPierwsza(pierwiastek)) {
                    System.out.println(liczba);
                    wynik.println(liczba);
                }
            }
        }
    }
}
```
**Odpowiedź:** 5041, 1369, 32041, 844561, 4, 96721, 9, 942841, 49, 1849, 528529, 121, 961, 169
