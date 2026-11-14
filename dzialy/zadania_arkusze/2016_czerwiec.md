<h1 align="center">Matura 2016 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Rekurencja. Dla dodatniej liczby całkowitej n dana jest funkcja:
>
> ```
> F(n):
>   jeżeli n = 1 lub n = 2
>       s ← n
>   w przeciwnym razie
>       s ← n * F(n−2)
>       s ← s * (n+1)
>   wynikiem jest s
> ```
>
> - 1.1 — Podaj wartości F(n) dla n = 1, 2, 3, 4, 5, 6.
> - 1.2 — Wypisz ciąg wywołań funkcji F dla n = 11 (np. dla n = 3 jest to F(3), F(1)).
> - 1.3 — Wskaż, jaką wartość oblicza algorytm: a) (n+1)(n+2)/2, b) (n+1)!, c) n^(n/2).

```py
wywolania = []


def F(n):
    wywolania.append(f"F({n})")
    if n == 1 or n == 2:
        s = n
    else:
        s = n * F(n - 2)
    s = s * (n + 1)
    return s


# 1.1
for n in range(1, 7):
    print(n, F(n))

# 1.2
wywolania = []
F(11)
print(", ".join(wywolania))

# 1.3 - porównanie z (n+1)!
silnia = 1
for n in range(1, 11):
    silnia *= n + 1
    print(n, F(n), silnia)
```

```cpp
// C++23
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> wywolania;

long long F(int n) {
    wywolania.push_back("F(" + std::to_string(n) + ")");
    long long s;
    if (n == 1 || n == 2)
        s = n;
    else
        s = n * F(n - 2);
    s = s * (n + 1);
    return s;
}

int main() {
    // 1.1
    for (int n = 1; n < 7; n++)
        std::cout << n << ' ' << F(n) << '\n';

    // 1.2
    wywolania.clear();
    F(11);
    for (size_t i = 0; i < wywolania.size(); i++)
        std::cout << (i > 0 ? ", " : "") << wywolania[i];
    std::cout << '\n';

    // 1.3 - porównanie z (n+1)!
    long long silnia = 1;
    for (int n = 1; n < 11; n++) {
        silnia *= n + 1;
        std::cout << n << ' ' << F(n) << ' ' << silnia << '\n';
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static List<String> wywolania = new ArrayList<>();

    static long F(int n) {
        wywolania.add("F(" + n + ")");
        long s;
        if (n == 1 || n == 2)
            s = n;
        else
            s = n * F(n - 2);
        s = s * (n + 1);
        return s;
    }

    public static void main(String[] args) {
        // 1.1
        for (int n = 1; n < 7; n++)
            System.out.println(n + " " + F(n));

        // 1.2
        wywolania.clear();
        F(11);
        System.out.println(String.join(", ", wywolania));

        // 1.3 - porównanie z (n+1)!
        long silnia = 1;
        for (int n = 1; n < 11; n++) {
            silnia *= n + 1;
            System.out.println(n + " " + F(n) + " " + silnia);
        }
    }
}
```
**Odpowiedź:** 1.1: F(1..6) = 2, 6, 24, 120, 720, 5040; 1.2: F(11), F(9), F(7), F(5), F(3), F(1); 1.3: (n+1)!

## 2.1, 2.2 i 2.3

> **Treść zadania:** Dziwny porządek. Na planecie X wśród dodatnich liczb całkowitych każda liczba parzysta jest mniejsza od każdej nieparzystej. Liczby parzyste są uporządkowane normalnie (2 < 4 < 6 < …), a nieparzyste odwrotnie — największa jest 1 (… < 5 < 3 < 1). Na przykład liczby 1–6 w kolejności rosnącej to: 2, 4, 6, 5, 3, 1.
>
> - 2.1 — Uporządkuj rosnąco według porządku planety X zbiór {3, 6, 8, 11, 15, 20, 35, 70, 100, 1000}.
> - 2.2 — Dopisz dwa elementy do zbioru {_, _, 27, 16, 7, 32} tak, aby jego najmniejszym elementem (według porządku X) była liczba 10.
> - 2.3 — Zapisz (pseudokodem lub w języku programowania) algorytm, który dla dodatniej liczby całkowitej `n` i tablicy `A[1..n]` dodatnich liczb całkowitych znajduje największą liczbę w tablicy według porządku planety X.

```py
def mniejsza(a, b):
    # czy a << b na planecie X
    if a % 2 == 0 and b % 2 == 1:
        return True
    if a % 2 == 1 and b % 2 == 0:
        return False
    if a % 2 == 0:  # obie parzyste - zwykły porządek
        return a < b
    return a > b    # obie nieparzyste - odwrotny porządek


def klucz(a):
    # klucz sortowania: najpierw parzyste rosnąco, potem nieparzyste malejąco
    if a % 2 == 0:
        return (0, a)
    return (1, -a)


def najwiekszy(A):
    # 2.3
    maks = A[0]
    for x in A[1:]:
        if mniejsza(maks, x):
            maks = x
    return maks


# 2.1
print(sorted([3, 6, 8, 11, 15, 20, 35, 70, 100, 1000], key=klucz))

# 2.2 - najmniejszym elementem ma być 10, np. dopisujemy 10 i 1
print(min([10, 1, 27, 16, 7, 32], key=klucz))

# 2.3
print(najwiekszy([3, 6, 8, 11, 15, 20, 35, 70, 100, 1000]))
print(najwiekszy([2, 4, 6, 8]))
```

```cpp
// C++23
#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

bool mniejsza(int a, int b) {
    // czy a << b na planecie X
    if (a % 2 == 0 && b % 2 == 1)
        return true;
    if (a % 2 == 1 && b % 2 == 0)
        return false;
    if (a % 2 == 0)  // obie parzyste - zwykły porządek
        return a < b;
    return a > b;    // obie nieparzyste - odwrotny porządek
}

std::pair<int, int> klucz(int a) {
    // klucz sortowania: najpierw parzyste rosnąco, potem nieparzyste malejąco
    if (a % 2 == 0)
        return {0, a};
    return {1, -a};
}

int najwiekszy(const std::vector<int>& A) {
    // 2.3
    int maks = A[0];
    for (size_t i = 1; i < A.size(); i++)
        if (mniejsza(maks, A[i]))
            maks = A[i];
    return maks;
}

void wypisz(const std::vector<int>& lista) {  // zapis jak lista w Pythonie
    std::cout << '[';
    for (size_t i = 0; i < lista.size(); i++)
        std::cout << (i > 0 ? ", " : "") << lista[i];
    std::cout << "]\n";
}

int main() {
    // 2.1
    std::vector<int> liczby = {3, 6, 8, 11, 15, 20, 35, 70, 100, 1000};
    std::ranges::stable_sort(liczby, {}, klucz);
    wypisz(liczby);

    // 2.2 - najmniejszym elementem ma być 10, np. dopisujemy 10 i 1
    std::cout << std::ranges::min(std::vector<int>{10, 1, 27, 16, 7, 32}, {}, klucz) << '\n';

    // 2.3
    std::cout << najwiekszy({3, 6, 8, 11, 15, 20, 35, 70, 100, 1000}) << '\n';
    std::cout << najwiekszy({2, 4, 6, 8}) << '\n';
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static boolean mniejsza(int a, int b) {
        // czy a << b na planecie X
        if (a % 2 == 0 && b % 2 == 1)
            return true;
        if (a % 2 == 1 && b % 2 == 0)
            return false;
        if (a % 2 == 0)  // obie parzyste - zwykły porządek
            return a < b;
        return a > b;    // obie nieparzyste - odwrotny porządek
    }

    // porządek sortowania: najpierw parzyste rosnąco, potem nieparzyste malejąco
    static Comparator<Integer> klucz = Comparator.comparingInt((Integer a) -> a % 2 == 0 ? 0 : 1)
            .thenComparingInt(a -> a % 2 == 0 ? a : -a);

    static int najwiekszy(int[] A) {
        // 2.3
        int maks = A[0];
        for (int i = 1; i < A.length; i++)
            if (mniejsza(maks, A[i]))
                maks = A[i];
        return maks;
    }

    public static void main(String[] args) {
        // 2.1
        var liczby = new ArrayList<>(List.of(3, 6, 8, 11, 15, 20, 35, 70, 100, 1000));
        liczby.sort(klucz);
        System.out.println(liczby);

        // 2.2 - najmniejszym elementem ma być 10, np. dopisujemy 10 i 1
        System.out.println(Collections.min(List.of(10, 1, 27, 16, 7, 32), klucz));

        // 2.3
        System.out.println(najwiekszy(new int[] {3, 6, 8, 11, 15, 20, 35, 70, 100, 1000}));
        System.out.println(najwiekszy(new int[] {2, 4, 6, 8}));
    }
}
```
**Odpowiedź:** 2.1: 6, 8, 20, 70, 100, 1000, 35, 15, 11, 3; 2.2: 10 i np. 1 (dowolna nieparzysta oprócz 7 i 27 albo parzysta większa od 10)

## 4.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** W pliku `ubezpieczenia.txt` są dane 331 osób ubezpieczonych na życie: nazwisko, imię, data urodzenia (RRRR-MM-DD) i miejsce zamieszkania, rozdzielone średnikami; pierwszy wiersz to nagłówek (np. `Czarnecka;Ewelina;1960-10-01;srednie miasto`). Imiona wszystkich kobiet (i tylko kobiet) kończą się literą „a”. Wyniki zapisz w pliku `wyniki_4.txt`, poprzedzając je numerem zadania.
>
> Utwórz zestawienie: dla każdego miesiąca (styczeń, luty, …) liczba osób, które mają w nim urodziny.

```py
miesiace = [0] * 13

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        miesiace[int(data[5:7])] += 1

for miesiac in range(1, 13):
    print(miesiac, miesiace[miesiac])
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<int> miesiace(13, 0);
    std::ifstream plik("ubezpieczenia.txt");
    std::string line;
    std::getline(plik, line);  // nagłówek
    while (std::getline(plik, line)) {
        // pola: nazwisko;imie;data;miejsce - data to trzecie pole, miesiąc na pozycjach 5-6
        size_t p1 = line.find(';'), p2 = line.find(';', p1 + 1);
        std::string data = line.substr(p2 + 1, 10);
        miesiace[std::stoi(data.substr(5, 2))] += 1;
    }
    for (int miesiac = 1; miesiac < 13; miesiac++)
        std::cout << miesiac << ' ' << miesiace[miesiac] << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int[] miesiace = new int[13];
        var linie = Files.readAllLines(Path.of("ubezpieczenia.txt"));
        for (var line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            var p = line.strip().split(";");  // nazwisko, imie, data, miejsce
            miesiace[Integer.parseInt(p[2].substring(5, 7))] += 1;
        }
        for (int miesiac = 1; miesiac < 13; miesiac++)
            System.out.println(miesiac + " " + miesiace[miesiac]);
    }
}
```
**Odpowiedź:** 1: 26, 2: 22, 3: 30, 4: 27, 5: 25, 6: 31, 7: 33, 8: 19, 9: 29, 10: 32, 11: 28, 12: 29

## 4.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `ubezpieczenia.txt` (nazwisko; imię; data urodzenia; miejsce zamieszkania; imiona kobiet kończą się na „a”). Utwórz zestawienie podające dla każdego miejsca zamieszkania liczbę ubezpieczonych kobiet.

```py
kobiety = {}

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        if imie[-1] == "a":
            kobiety[miejsce] = kobiety.get(miejsce, 0) + 1

for miejsce in kobiety:
    print(miejsce, kobiety[miejsce])
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

int main() {
    // lista par (miejsce, liczba) - zachowuje kolejność pierwszego pojawienia się, jak słownik w Pythonie
    std::vector<std::pair<std::string, int>> kobiety;

    std::ifstream plik("ubezpieczenia.txt");
    std::string line;
    std::getline(plik, line);  // nagłówek
    while (std::getline(plik, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        std::stringstream ss(line);
        std::string nazwisko, imie, data, miejsce;
        std::getline(ss, nazwisko, ';');
        std::getline(ss, imie, ';');
        std::getline(ss, data, ';');
        std::getline(ss, miejsce, ';');
        if (imie.back() == 'a') {
            bool znalezione = false;
            for (auto& [m, ile] : kobiety)
                if (m == miejsce) {
                    ile++;
                    znalezione = true;
                }
            if (!znalezione) kobiety.push_back({miejsce, 1});
        }
    }
    for (const auto& [miejsce, ile] : kobiety)
        std::cout << miejsce << ' ' << ile << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var kobiety = new LinkedHashMap<String, Integer>();  // zachowuje kolejność, jak słownik w Pythonie
        var linie = Files.readAllLines(Path.of("ubezpieczenia.txt"));
        for (var line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            var p = line.strip().split(";");  // nazwisko, imie, data, miejsce
            String imie = p[1], miejsce = p[3];
            if (imie.endsWith("a"))
                kobiety.merge(miejsce, 1, Integer::sum);
        }
        for (var e : kobiety.entrySet())
            System.out.println(e.getKey() + " " + e.getValue());
    }
}
```
**Odpowiedź:** wieś 24, małe miasto 20, średnie miasto 59, duże miasto 97

## 4.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `ubezpieczenia.txt`. Kwota ubezpieczenia wynosi 25 000 zł dla kobiet i 30 000 zł dla mężczyzn. Miesięczna składka to procent kwoty ubezpieczenia zależny od wieku:
> - do 30 lat — 0,1%,
> - od 31 do 45 lat — 0,15%,
> - od 46 lat — 0,12%.
>
> Osobom, których wiek przekroczył 60 lat, dolicza się do składki 49 zł. Wiek liczymy rocznikami (na 1 stycznia 2016 r.: 2016 − rok urodzenia). Oblicz sumę miesięcznych składek za styczeń 2016 roku osobno dla kobiet i osobno dla mężczyzn; każdy wynik zaokrąglij do dwóch miejsc po przecinku.

```py
suma_kobiety = 0
suma_mezczyzni = 0

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        wiek = 2016 - int(data[:4])  # liczymy rocznikami

        # składka w tysięcznych częściach procenta (0,1% = 100, 0,15% = 150, 0,12% = 120),
        # żeby uniknąć błędów zaokrągleń float
        if wiek <= 30:
            procent = 100
        elif wiek <= 45:
            procent = 150
        else:
            procent = 120

        if imie[-1] == "a":
            kwota = 25000
        else:
            kwota = 30000

        skladka = kwota * procent / 100000
        if wiek > 60:
            skladka += 49

        if imie[-1] == "a":
            suma_kobiety += skladka
        else:
            suma_mezczyzni += skladka

print(f"{suma_kobiety:.2f}")
print(f"{suma_mezczyzni:.2f}")
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>

int main() {
    double suma_kobiety = 0, suma_mezczyzni = 0;

    std::ifstream plik("ubezpieczenia.txt");
    std::string line;
    std::getline(plik, line);  // nagłówek
    while (std::getline(plik, line)) {
        std::stringstream ss(line);
        std::string nazwisko, imie, data;
        std::getline(ss, nazwisko, ';');
        std::getline(ss, imie, ';');
        std::getline(ss, data, ';');
        int wiek = 2016 - std::stoi(data.substr(0, 4));  // liczymy rocznikami

        // składka w tysięcznych częściach procenta (0,1% = 100, 0,15% = 150, 0,12% = 120),
        // żeby uniknąć błędów zaokrągleń float
        int procent;
        if (wiek <= 30)
            procent = 100;
        else if (wiek <= 45)
            procent = 150;
        else
            procent = 120;

        bool kobieta = imie.back() == 'a';
        int kwota = kobieta ? 25000 : 30000;

        double skladka = kwota * procent / 100000.0;
        if (wiek > 60)
            skladka += 49;

        if (kobieta)
            suma_kobiety += skladka;
        else
            suma_mezczyzni += skladka;
    }
    std::println("{:.2f}", suma_kobiety);
    std::println("{:.2f}", suma_mezczyzni);
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.Locale;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        double sumaKobiety = 0, sumaMezczyzni = 0;

        var linie = Files.readAllLines(Path.of("ubezpieczenia.txt"));
        for (var line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            var p = line.strip().split(";");  // nazwisko, imie, data, miejsce
            String imie = p[1];
            int wiek = 2016 - Integer.parseInt(p[2].substring(0, 4));  // liczymy rocznikami

            // składka w tysięcznych częściach procenta (0,1% = 100, 0,15% = 150, 0,12% = 120),
            // żeby uniknąć błędów zaokrągleń float
            int procent;
            if (wiek <= 30)
                procent = 100;
            else if (wiek <= 45)
                procent = 150;
            else
                procent = 120;

            boolean kobieta = imie.endsWith("a");
            int kwota = kobieta ? 25000 : 30000;

            double skladka = kwota * procent / 100000.0;
            if (wiek > 60)
                skladka += 49;

            if (kobieta)
                sumaKobiety += skladka;
            else
                sumaMezczyzni += skladka;
        }
        // Locale.ROOT - kropka dziesiętna, jak w Pythonie
        System.out.println(String.format(Locale.ROOT, "%.2f", sumaKobiety));
        System.out.println(String.format(Locale.ROOT, "%.2f", sumaMezczyzni));
    }
}
```
**Odpowiedź:** kobiety 8961,50 zł, mężczyźni 6261,00 zł

## 4.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Dane z pliku `ubezpieczenia.txt` (wiek liczony rocznikami na 1 stycznia 2016 r.). Utwórz zestawienie liczby osób w przedziałach wiekowych 20–29, 30–39, 40–49, 50–59, 60–69, 70–79 i sporządź czytelnie opisany wykres kolumnowy tego zestawienia.

```py
przedzialy = {}  # początek przedziału (20, 30, ..., 70) -> liczba osób

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        wiek = 2016 - int(data[:4])
        poczatek = wiek // 10 * 10
        przedzialy[poczatek] = przedzialy.get(poczatek, 0) + 1

for poczatek in range(20, 80, 10):
    print(f"{poczatek}-{poczatek + 9}", przedzialy.get(poczatek, 0))
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>

int main() {
    std::map<int, int> przedzialy;  // początek przedziału (20, 30, ..., 70) -> liczba osób

    std::ifstream plik("ubezpieczenia.txt");
    std::string line;
    std::getline(plik, line);  // nagłówek
    while (std::getline(plik, line)) {
        std::stringstream ss(line);
        std::string nazwisko, imie, data;
        std::getline(ss, nazwisko, ';');
        std::getline(ss, imie, ';');
        std::getline(ss, data, ';');
        int wiek = 2016 - std::stoi(data.substr(0, 4));
        int poczatek = wiek / 10 * 10;
        przedzialy[poczatek]++;
    }
    for (int poczatek = 20; poczatek < 80; poczatek += 10)
        std::cout << poczatek << '-' << poczatek + 9 << ' ' << przedzialy[poczatek] << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var przedzialy = new HashMap<Integer, Integer>();  // początek przedziału (20, 30, ..., 70) -> liczba osób
        var linie = Files.readAllLines(Path.of("ubezpieczenia.txt"));
        for (var line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            var p = line.strip().split(";");  // nazwisko, imie, data, miejsce
            int wiek = 2016 - Integer.parseInt(p[2].substring(0, 4));
            int poczatek = wiek / 10 * 10;
            przedzialy.merge(poczatek, 1, Integer::sum);
        }
        for (int poczatek = 20; poczatek < 80; poczatek += 10)
            System.out.println(poczatek + "-" + (poczatek + 9) + " " + przedzialy.getOrDefault(poczatek, 0));
    }
}
```
**Odpowiedź:** 20-29: 62, 30-39: 56, 40-49: 64, 50-59: 56, 60-69: 71, 70-79: 22 (+ wykres kolumnowy)

## 6.1

> **Treść zadania:** W pliku `liczby.txt` jest 999 kodów liczb, każdy w osobnym wierszu. Ostatnia cyfra kodu to podstawa systemu (od 2 do 9), a cyfry od pierwszej do przedostatniej to zapis liczby w tym systemie (np. `12345678` oznacza liczbę 1234567 w systemie ósemkowym). Kod zaczyna się cyfrą większą od 0 i ma co najwyżej 10 cyfr (wartość może nie mieścić się w 32-bitowym typie całkowitym). Odpowiedzi zapisz w plikach `wyniki_6_1.txt` … `wyniki_6_5.txt`.
>
> Podaj, ile liczb w pliku zapisano w systemie ósemkowym.

```py
licznik = 0

with open("liczby.txt") as file:
    for line in file:
        if line.strip()[-1] == "8":
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>

int main() {
    int licznik = 0;
    std::ifstream plik("liczby.txt");
    std::string kod;
    while (plik >> kod)
        if (kod.back() == '8')
            licznik++;
    std::cout << licznik << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        for (var line : Files.readAllLines(Path.of("liczby.txt")))
            if (line.strip().endsWith("8"))
                licznik++;
        System.out.println(licznik);
    }
}
```
**Odpowiedź:** 103

## 6.2

> **Treść zadania:** Plik `liczby.txt` zawiera 999 kodów (ostatnia cyfra — podstawa systemu 2–9, pozostałe — zapis liczby). Podaj, ile wierszy zawiera liczby zapisane w systemie czwórkowym, w których zapisie nie występuje cyfra 0. Odpowiedź zapisz w `wyniki_6_2.txt`.

```py
licznik = 0

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        if kod[-1] == "4" and "0" not in kod[:-1]:
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>

int main() {
    int licznik = 0;
    std::ifstream plik("liczby.txt");
    std::string kod;
    while (plik >> kod) {
        std::string liczba = kod.substr(0, kod.size() - 1);  // kod bez ostatniej cyfry (podstawy)
        if (kod.back() == '4' && liczba.find('0') == std::string::npos)
            licznik++;
    }
    std::cout << licznik << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        for (var line : Files.readAllLines(Path.of("liczby.txt"))) {
            var kod = line.strip();
            var liczba = kod.substring(0, kod.length() - 1);  // kod bez ostatniej cyfry (podstawy)
            if (kod.endsWith("4") && !liczba.contains("0"))
                licznik++;
        }
        System.out.println(licznik);
    }
}
```
**Odpowiedź:** 29

## 6.3

> **Treść zadania:** Plik `liczby.txt` zawiera 999 kodów (ostatnia cyfra — podstawa systemu 2–9, pozostałe — zapis liczby). Podaj, ile wierszy zawiera liczby parzyste zapisane w systemie dwójkowym. Odpowiedź zapisz w `wyniki_6_3.txt`.

```py
licznik = 0

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        # liczba dwójkowa jest parzysta, gdy jej ostatnia cyfra (przedostatni znak kodu) to 0
        if kod[-1] == "2" and kod[-2] == "0":
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>

int main() {
    int licznik = 0;
    std::ifstream plik("liczby.txt");
    std::string kod;
    while (plik >> kod) {
        // liczba dwójkowa jest parzysta, gdy jej ostatnia cyfra (przedostatni znak kodu) to 0
        if (kod[kod.size() - 1] == '2' && kod[kod.size() - 2] == '0')
            licznik++;
    }
    std::cout << licznik << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        for (var line : Files.readAllLines(Path.of("liczby.txt"))) {
            var kod = line.strip();
            // liczba dwójkowa jest parzysta, gdy jej ostatnia cyfra (przedostatni znak kodu) to 0
            if (kod.charAt(kod.length() - 1) == '2' && kod.charAt(kod.length() - 2) == '0')
                licznik++;
        }
        System.out.println(licznik);
    }
}
```
**Odpowiedź:** 153

## 6.4

> **Treść zadania:** Plik `liczby.txt` zawiera 999 kodów (ostatnia cyfra — podstawa systemu 2–9, pozostałe — zapis liczby). Podaj w systemie dziesiętnym sumę wszystkich liczb zapisanych w systemie ósemkowym. Odpowiedź zapisz w `wyniki_6_4.txt`.

```py
suma = 0

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        if kod[-1] == "8":
            suma += int(kod[:-1], 8)

print(suma)
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>

int main() {
    long long suma = 0;
    std::ifstream plik("liczby.txt");
    std::string kod;
    while (plik >> kod)
        if (kod.back() == '8')
            suma += std::stoll(kod.substr(0, kod.size() - 1), nullptr, 8);  // zamiana z systemu ósemkowego
    std::cout << suma << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        long suma = 0;
        for (var line : Files.readAllLines(Path.of("liczby.txt"))) {
            var kod = line.strip();
            if (kod.endsWith("8"))
                suma += Long.parseLong(kod.substring(0, kod.length() - 1), 8);  // zamiana z systemu ósemkowego
        }
        System.out.println(suma);
    }
}
```
**Odpowiedź:** 887918739

## 6.5

> **Treść zadania:** Plik `liczby.txt` zawiera 999 kodów (ostatnia cyfra — podstawa systemu 2–9, pozostałe — zapis liczby). Podaj kod największej i kod najmniejszej z zakodowanych liczb oraz ich wartości w systemie dziesiętnym. Odpowiedź zapisz w `wyniki_6_5.txt`.

```py
kod_min = kod_max = None
wartosc_min = wartosc_max = None

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        wartosc = int(kod[:-1], int(kod[-1]))
        if wartosc_min is None or wartosc < wartosc_min:
            wartosc_min = wartosc
            kod_min = kod
        if wartosc_max is None or wartosc > wartosc_max:
            wartosc_max = wartosc
            kod_max = kod

print(kod_max, wartosc_max)
print(kod_min, wartosc_min)
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::string kod_min, kod_max;  // pusty napis - jeszcze nic (None w Pythonie)
    long long wartosc_min = 0, wartosc_max = 0;

    std::ifstream plik("liczby.txt");
    std::string kod;
    while (plik >> kod) {
        int podstawa = kod.back() - '0';
        long long wartosc = std::stoll(kod.substr(0, kod.size() - 1), nullptr, podstawa);
        if (kod_min.empty() || wartosc < wartosc_min) {
            wartosc_min = wartosc;
            kod_min = kod;
        }
        if (kod_max.empty() || wartosc > wartosc_max) {
            wartosc_max = wartosc;
            kod_max = kod;
        }
    }
    std::cout << kod_max << ' ' << wartosc_max << '\n';
    std::cout << kod_min << ' ' << wartosc_min << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        String kodMin = null, kodMax = null;
        long wartoscMin = 0, wartoscMax = 0;

        for (var line : Files.readAllLines(Path.of("liczby.txt"))) {
            var kod = line.strip();
            int podstawa = kod.charAt(kod.length() - 1) - '0';
            long wartosc = Long.parseLong(kod.substring(0, kod.length() - 1), podstawa);
            if (kodMin == null || wartosc < wartoscMin) {
                wartoscMin = wartosc;
                kodMin = kod;
            }
            if (kodMax == null || wartosc > wartoscMax) {
                wartoscMax = wartosc;
                kodMax = kod;
            }
        }
        System.out.println(kodMax + " " + wartoscMax);
        System.out.println(kodMin + " " + wartoscMin);
    }
}
```
**Odpowiedź:** największa: 8066218209 (347931225), najmniejsza: 100002 (16)
