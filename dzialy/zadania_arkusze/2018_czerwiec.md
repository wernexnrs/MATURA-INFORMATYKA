<h1 align="center">Matura 2018 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Zadanie 1. Wyszukiwanie liczb. Funkcja `F(T, x)` dostaje `n`-elementową tablicę `T[1..n]` liczb całkowitych uporządkowanych niemalejąco i liczbę `x`; zwraca prawdę, jeśli `x` występuje w `T`, a fałsz w przeciwnym razie:
>
> ```
> p ← 1; k ← n
> dopóki p <= k powtarzaj:
>     s ← (p+k) div 2
>     jeśli T[s] = x: wynikiem jest prawda, koniec
>     w przeciwnym razie
>         jeśli T[s] < x: p ← s+1
>         w przeciwnym razie: k ← s−1
> wynikiem jest fałsz
> ```
>
> - 1.1 — Dla `T = [3; 5; 7; 8; 9; 13; 33; 37; 40; 43]`: A) podaj wynik `F(T, 7)`; B) podaj, ile razy w pętli zmieni się wartość `p`, a ile `k`, dla `x = 7` i dla `x = 43`; C) podaj kolejne wartości `s` dla `x = 7`.
> - 1.2 — Ile razy dla `n = 100` jest spełniony warunek `p <= k`, gdy szukana liczba jest większa od wszystkich elementów tablicy?
> - 1.3 — Podaj wynik `F(T, 43)` dla nieuporządkowanej tablicy `T = [3; 5; 7; 8; 90; 13; 33; 37; 40; 43]`.

```py
def F(T, x):
    # wyszukiwanie binarne; T indeksowana od 1 jak w treści (T[0] nieużywane)
    n = len(T) - 1
    p, k = 1, n
    zmiany_p = zmiany_k = 0
    wartosci_s = []
    sprawdzenia = 0  # ile razy warunek p <= k był spełniony
    while p <= k:
        sprawdzenia += 1
        s = (p + k) // 2
        wartosci_s.append(s)
        if T[s] == x:
            return True, zmiany_p, zmiany_k, wartosci_s, sprawdzenia
        if T[s] < x:
            p = s + 1
            zmiany_p += 1
        else:
            k = s - 1
            zmiany_k += 1
    return False, zmiany_p, zmiany_k, wartosci_s, sprawdzenia


T = [None, 3, 5, 7, 8, 9, 13, 33, 37, 40, 43]

# 1.1 A, B, C
wynik, zp, zk, s, ile = F(T, 7)
print("x = 7:", wynik, "p:", zp, "k:", zk, "s:", s)
wynik, zp, zk, s, ile = F(T, 43)
print("x = 43:", "p:", zp, "k:", zk)

# 1.2 - n = 100, x większe od wszystkich elementów
T100 = [None] + list(range(1, 101))
print(F(T100, 1000)[4])

# 1.3
T_nieuporzadkowana = [None, 3, 5, 7, 8, 90, 13, 33, 37, 40, 43]
print(F(T_nieuporzadkowana, 43)[0])
```

```cpp
// C++23
#include <print>
#include <vector>

struct Wynik {
    bool znaleziono;
    int zmiany_p, zmiany_k;
    std::vector<int> wartosci_s;
    int sprawdzenia;  // ile razy warunek p <= k był spełniony
};

Wynik F(const std::vector<int>& T, int x) {
    // wyszukiwanie binarne; T indeksowana od 1 jak w treści (T[0] nieużywane)
    int n = T.size() - 1;
    int p = 1, k = n;
    Wynik w{false, 0, 0, {}, 0};
    while (p <= k) {
        w.sprawdzenia++;
        int s = (p + k) / 2;
        w.wartosci_s.push_back(s);
        if (T[s] == x) {
            w.znaleziono = true;
            return w;
        }
        if (T[s] < x) {
            p = s + 1;
            w.zmiany_p++;
        } else {
            k = s - 1;
            w.zmiany_k++;
        }
    }
    return w;
}

// wartość logiczna zapisana jak w Pythonie
const char* py(bool b) {
    return b ? "True" : "False";
}

int main() {
    std::vector<int> T = {0, 3, 5, 7, 8, 9, 13, 33, 37, 40, 43};

    // 1.1 A, B, C
    Wynik w = F(T, 7);
    std::println("x = 7: {} p: {} k: {} s: {}", py(w.znaleziono), w.zmiany_p, w.zmiany_k, w.wartosci_s);
    w = F(T, 43);
    std::println("x = 43: p: {} k: {}", w.zmiany_p, w.zmiany_k);

    // 1.2 - n = 100, x większe od wszystkich elementów
    std::vector<int> T100 = {0};
    for (int i = 1; i <= 100; i++)
        T100.push_back(i);
    std::println("{}", F(T100, 1000).sprawdzenia);

    // 1.3
    std::vector<int> T_nieuporzadkowana = {0, 3, 5, 7, 8, 90, 13, 33, 37, 40, 43};
    std::println("{}", py(F(T_nieuporzadkowana, 43).znaleziono));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    record Wynik(boolean znaleziono, int zmianyP, int zmianyK, List<Integer> wartosciS, int sprawdzenia) {}

    static Wynik F(int[] T, int x) {
        // wyszukiwanie binarne; T indeksowana od 1 jak w treści (T[0] nieużywane)
        int n = T.length - 1;
        int p = 1, k = n;
        int zmianyP = 0, zmianyK = 0;
        List<Integer> wartosciS = new ArrayList<>();
        int sprawdzenia = 0;  // ile razy warunek p <= k był spełniony
        while (p <= k) {
            sprawdzenia++;
            int s = (p + k) / 2;
            wartosciS.add(s);
            if (T[s] == x)
                return new Wynik(true, zmianyP, zmianyK, wartosciS, sprawdzenia);
            if (T[s] < x) {
                p = s + 1;
                zmianyP++;
            } else {
                k = s - 1;
                zmianyK++;
            }
        }
        return new Wynik(false, zmianyP, zmianyK, wartosciS, sprawdzenia);
    }

    // wartość logiczna zapisana jak w Pythonie
    static String py(boolean b) {
        return b ? "True" : "False";
    }

    public static void main(String[] args) {
        int[] T = {0, 3, 5, 7, 8, 9, 13, 33, 37, 40, 43};

        // 1.1 A, B, C
        Wynik w = F(T, 7);
        System.out.println("x = 7: " + py(w.znaleziono()) + " p: " + w.zmianyP() + " k: " + w.zmianyK()
                + " s: " + w.wartosciS());
        w = F(T, 43);
        System.out.println("x = 43: p: " + w.zmianyP() + " k: " + w.zmianyK());

        // 1.2 - n = 100, x większe od wszystkich elementów
        int[] T100 = new int[101];
        for (int i = 1; i <= 100; i++)
            T100[i] = i;
        System.out.println(F(T100, 1000).sprawdzenia());

        // 1.3
        int[] tNieuporzadkowana = {0, 3, 5, 7, 8, 90, 13, 33, 37, 40, 43};
        System.out.println(py(F(tNieuporzadkowana, 43).znaleziono()));
    }
}
```
**Odpowiedź:** 1.1: A. prawda; B. x = 7: p - 1, k - 1; x = 43: p - 3, k - 0; C. 5, 2, 3. 1.2: 7 razy. 1.3: fałsz.

## 2.1 i 2.3

> **Treść zadania:** Zadanie 2. Liczby Fibonacciego: `F1 = 1`, `F2 = 1`, `Fn = F(n−1) + F(n−2)` dla `n ≥ 3`. Rekurencyjna funkcja `F(n)` zwraca 1 dla `n = 1` lub `n = 2`, a w przeciwnym razie `F(n−1) + F(n−2)`.
>
> - 2.1 — Zapisz algorytm iteracyjny obliczający `Fn` dla dowolnego `n ≥ 1` bez użycia tablic.
> - 2.3 — Korzystając ze wzorów prawdziwych dla `k ≥ 2`: `F(2k) = F(k+1)² − F(k−1)²` oraz `F(2k−1) = F(k)² + F(k−1)²`, zapisz szybszy algorytm rekurencyjny obliczający `Fn` dla `n ≥ 1`.

```py
def fib_iteracyjnie(n):
    # 2.1 - bez tablic, tylko dwie ostatnie wartości
    f1 = f2 = 1
    for i in range(3, n + 1):
        f1, f2 = f2, f1 + f2
    return f2


def fib_szybko(n):
    # 2.3 - F(2k) = F(k+1)^2 - F(k-1)^2, F(2k-1) = F(k)^2 + F(k-1)^2
    if n == 1 or n == 2:
        return 1
    if n % 2 == 0:
        k = n // 2
        return fib_szybko(k + 1) ** 2 - fib_szybko(k - 1) ** 2
    k = (n + 1) // 2
    return fib_szybko(k) ** 2 + fib_szybko(k - 1) ** 2


print(fib_iteracyjnie(45), fib_szybko(45))
for n in range(1, 30):
    assert fib_iteracyjnie(n) == fib_szybko(n)
```

```cpp
// C++23
#include <cassert>
#include <print>

long long fib_iteracyjnie(int n) {
    // 2.1 - bez tablic, tylko dwie ostatnie wartości
    long long f1 = 1, f2 = 1;
    for (int i = 3; i <= n; i++) {
        long long nowa = f1 + f2;
        f1 = f2;
        f2 = nowa;
    }
    return f2;
}

long long fib_szybko(int n) {
    // 2.3 - F(2k) = F(k+1)^2 - F(k-1)^2, F(2k-1) = F(k)^2 + F(k-1)^2
    if (n == 1 || n == 2)
        return 1;
    if (n % 2 == 0) {
        int k = n / 2;
        long long a = fib_szybko(k + 1), b = fib_szybko(k - 1);
        return a * a - b * b;
    }
    int k = (n + 1) / 2;
    long long a = fib_szybko(k), b = fib_szybko(k - 1);
    return a * a + b * b;
}

int main() {
    std::println("{} {}", fib_iteracyjnie(45), fib_szybko(45));
    for (int n = 1; n < 30; n++)
        assert(fib_iteracyjnie(n) == fib_szybko(n));
}
```

```java
// Java 25
public class Zadanie {
    static long fibIteracyjnie(int n) {
        // 2.1 - bez tablic, tylko dwie ostatnie wartości
        long f1 = 1, f2 = 1;
        for (int i = 3; i <= n; i++) {
            long nowa = f1 + f2;
            f1 = f2;
            f2 = nowa;
        }
        return f2;
    }

    static long fibSzybko(int n) {
        // 2.3 - F(2k) = F(k+1)^2 - F(k-1)^2, F(2k-1) = F(k)^2 + F(k-1)^2
        if (n == 1 || n == 2)
            return 1;
        if (n % 2 == 0) {
            int k = n / 2;
            long a = fibSzybko(k + 1), b = fibSzybko(k - 1);
            return a * a - b * b;
        }
        int k = (n + 1) / 2;
        long a = fibSzybko(k), b = fibSzybko(k - 1);
        return a * a + b * b;
    }

    public static void main(String[] args) {
        System.out.println(fibIteracyjnie(45) + " " + fibSzybko(45));
        for (int n = 1; n < 30; n++)
            if (fibIteracyjnie(n) != fibSzybko(n))
                throw new AssertionError("n = " + n);
    }
}
```
**Odpowiedź:** F45 = 1134903170 (obie funkcje)

## 4.1

> **Treść zadania:** Zadanie 4. Scalanie. Pliki `dane1.txt` i `dane2.txt` mają po 1000 wierszy; w każdym jest niemalejący ciąg dziesięciu liczb całkowitych z przedziału [0, 100] oddzielonych spacjami. Pliki `przyklad1.txt` i `przyklad2.txt` zawierają dane przykładowe (po 5 wierszy).
>
> Porównaj ciągi w odpowiadających sobie wierszach obu plików i podaj, w ilu wierszach ostatnia liczba obu ciągów jest taka sama. Dla plików przykładowych wynik to 3. Odpowiedź zapisz w pliku `wynik4_1.txt`.

```py
licznik = 0

with open("dane1.txt") as dane1, open("dane2.txt") as dane2:
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = list(map(int, wiersz1.split()))
        b = list(map(int, wiersz2.split()))
        if a[-1] == b[-1]:
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// zamienia wiersz z liczbami na wektor liczb
std::vector<int> liczby(const std::string& wiersz) {
    std::istringstream ss(wiersz);
    std::vector<int> wynik;
    int x;
    while (ss >> x)
        wynik.push_back(x);
    return wynik;
}

int main() {
    int licznik = 0;

    std::ifstream dane1("dane1.txt"), dane2("dane2.txt");
    std::string wiersz1, wiersz2;
    while (std::getline(dane1, wiersz1) && std::getline(dane2, wiersz2)) {
        auto a = liczby(wiersz1);
        auto b = liczby(wiersz2);
        if (a.back() == b.back())
            licznik++;
    }

    std::println("{}", licznik);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;

        List<String> dane1 = Files.readAllLines(Path.of("dane1.txt"));
        List<String> dane2 = Files.readAllLines(Path.of("dane2.txt"));
        for (int i = 0; i < Math.min(dane1.size(), dane2.size()); i++) {
            String[] a = dane1.get(i).trim().split("\\s+");
            String[] b = dane2.get(i).trim().split("\\s+");
            if (Integer.parseInt(a[a.length - 1]) == Integer.parseInt(b[b.length - 1]))
                licznik++;
        }

        System.out.println(licznik);
    }
}
```
**Odpowiedź:** 32

## 4.2

> **Treść zadania:** Dla odpowiadających sobie wierszy plików `dane1.txt` i `dane2.txt` (po 1000 niemalejących ciągów 10 liczb z [0, 100]) podaj, ile jest par ciągów, w których każdy z dwóch ciągów zawiera dokładnie 5 liczb parzystych i 5 nieparzystych. Dla plików przykładowych wynik to 1. Odpowiedź zapisz w pliku `wynik4_2.txt`.

```py
def parzystych(ciag):
    ile = 0
    for liczba in ciag:
        if liczba % 2 == 0:
            ile += 1
    return ile


licznik = 0

with open("dane1.txt") as dane1, open("dane2.txt") as dane2:
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = list(map(int, wiersz1.split()))
        b = list(map(int, wiersz2.split()))
        # 10 liczb, z czego 5 parzystych => 5 nieparzystych
        if parzystych(a) == 5 and parzystych(b) == 5:
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// zamienia wiersz z liczbami na wektor liczb
std::vector<int> liczby(const std::string& wiersz) {
    std::istringstream ss(wiersz);
    std::vector<int> wynik;
    int x;
    while (ss >> x)
        wynik.push_back(x);
    return wynik;
}

int parzystych(const std::vector<int>& ciag) {
    int ile = 0;
    for (int liczba : ciag)
        if (liczba % 2 == 0)
            ile++;
    return ile;
}

int main() {
    int licznik = 0;

    std::ifstream dane1("dane1.txt"), dane2("dane2.txt");
    std::string wiersz1, wiersz2;
    while (std::getline(dane1, wiersz1) && std::getline(dane2, wiersz2)) {
        auto a = liczby(wiersz1);
        auto b = liczby(wiersz2);
        // 10 liczb, z czego 5 parzystych => 5 nieparzystych
        if (parzystych(a) == 5 && parzystych(b) == 5)
            licznik++;
    }

    std::println("{}", licznik);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Zadanie {
    static int parzystych(String wiersz) {
        int ile = 0;
        for (String liczba : wiersz.trim().split("\\s+"))
            if (Integer.parseInt(liczba) % 2 == 0)
                ile++;
        return ile;
    }

    public static void main(String[] args) throws Exception {
        int licznik = 0;

        List<String> dane1 = Files.readAllLines(Path.of("dane1.txt"));
        List<String> dane2 = Files.readAllLines(Path.of("dane2.txt"));
        for (int i = 0; i < Math.min(dane1.size(), dane2.size()); i++) {
            // 10 liczb, z czego 5 parzystych => 5 nieparzystych
            if (parzystych(dane1.get(i)) == 5 && parzystych(dane2.get(i)) == 5)
                licznik++;
        }

        System.out.println(licznik);
    }
}
```
**Odpowiedź:** 50

## 4.3

> **Treść zadania:** Policz, ile jest par ciągów w odpowiadających sobie wierszach plików `dane1.txt` i `dane2.txt`, które są zbudowane z tych samych liczb (krotności powtórzeń mogą być różne), i wypisz numery tych wierszy. Dla plików przykładowych odpowiedź to: 2 pary, wiersze 1 i 5. Odpowiedź zapisz w pliku `wynik4_3.txt`.

```py
wiersze = []

with open("dane1.txt") as dane1, open("dane2.txt") as dane2:
    nr = 1
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = set(map(int, wiersz1.split()))
        b = set(map(int, wiersz2.split()))
        # porównujemy zbiory (a nie listy utworzone ze zbiorów - ich kolejność nie jest gwarantowana)
        if a == b:
            wiersze.append(nr)
        nr += 1

print(len(wiersze))
print(*wiersze, sep=", ")
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <set>
#include <sstream>
#include <string>
#include <vector>

// zamienia wiersz z liczbami na zbiór liczb
std::set<int> zbior(const std::string& wiersz) {
    std::istringstream ss(wiersz);
    std::set<int> wynik;
    int x;
    while (ss >> x)
        wynik.insert(x);
    return wynik;
}

int main() {
    std::vector<int> wiersze;

    std::ifstream dane1("dane1.txt"), dane2("dane2.txt");
    std::string wiersz1, wiersz2;
    int nr = 1;
    while (std::getline(dane1, wiersz1) && std::getline(dane2, wiersz2)) {
        if (zbior(wiersz1) == zbior(wiersz2))
            wiersze.push_back(nr);
        nr++;
    }

    std::println("{}", wiersze.size());
    for (size_t i = 0; i < wiersze.size(); i++)
        std::print("{}{}", i > 0 ? ", " : "", wiersze[i]);
    std::println();
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Zadanie {
    // zamienia wiersz z liczbami na zbiór liczb
    static Set<Integer> zbior(String wiersz) {
        Set<Integer> wynik = new HashSet<>();
        for (String liczba : wiersz.trim().split("\\s+"))
            wynik.add(Integer.parseInt(liczba));
        return wynik;
    }

    public static void main(String[] args) throws Exception {
        List<String> wiersze = new ArrayList<>();

        List<String> dane1 = Files.readAllLines(Path.of("dane1.txt"));
        List<String> dane2 = Files.readAllLines(Path.of("dane2.txt"));
        for (int i = 0; i < Math.min(dane1.size(), dane2.size()); i++)
            if (zbior(dane1.get(i)).equals(zbior(dane2.get(i))))
                wiersze.add(String.valueOf(i + 1));

        System.out.println(wiersze.size());
        System.out.println(String.join(", ", wiersze));
    }
}
```
**Odpowiedź:** 1 para ciągów, wiersz 999

## 4.4

> **Treść zadania:** Scalanie dwóch ciągów niemalejących polega na porównywaniu bieżących pierwszych elementów obu ciągów i przepisywaniu mniejszego (lub równego) do ciągu wynikowego; gdy jeden ciąg się wyczerpie, resztę drugiego przepisuje się na koniec. Napisz program, który scali ciągi z odpowiadających sobie wierszy plików `dane1.txt` i `dane2.txt` i zapisze wyniki (po 20 liczb rozdzielonych spacjami, każdy w osobnym wierszu) w pliku `wynik4_4.txt`. Dla plików przykładowych pierwszy wiersz wyniku to `3 3 9 9 12 12 12 14 14 19 19 26 26 32 32 33 33 33 36 36`.

```py
def scal(a, b):
    wynik = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            wynik.append(a[i])
            i += 1
        else:
            wynik.append(b[j])
            j += 1
    # jeden z ciągów się wyczerpał - przepisujemy resztę drugiego
    wynik += a[i:]
    wynik += b[j:]
    return wynik


with open("dane1.txt") as dane1, open("dane2.txt") as dane2, open("wynik4_4.txt", "w") as plik:
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = list(map(int, wiersz1.split()))
        b = list(map(int, wiersz2.split()))
        plik.write(" ".join(map(str, scal(a, b))) + "\n")
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// zamienia wiersz z liczbami na wektor liczb
std::vector<int> liczby(const std::string& wiersz) {
    std::istringstream ss(wiersz);
    std::vector<int> wynik;
    int x;
    while (ss >> x)
        wynik.push_back(x);
    return wynik;
}

std::vector<int> scal(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> wynik;
    size_t i = 0, j = 0;
    while (i < a.size() && j < b.size()) {
        if (a[i] <= b[j]) {
            wynik.push_back(a[i]);
            i++;
        } else {
            wynik.push_back(b[j]);
            j++;
        }
    }
    // jeden z ciągów się wyczerpał - przepisujemy resztę drugiego
    wynik.insert(wynik.end(), a.begin() + i, a.end());
    wynik.insert(wynik.end(), b.begin() + j, b.end());
    return wynik;
}

int main() {
    std::ifstream dane1("dane1.txt"), dane2("dane2.txt");
    std::ofstream plik("wynik4_4.txt");
    std::string wiersz1, wiersz2;
    while (std::getline(dane1, wiersz1) && std::getline(dane2, wiersz2)) {
        auto wynik = scal(liczby(wiersz1), liczby(wiersz2));
        for (size_t i = 0; i < wynik.size(); i++)
            std::print(plik, "{}{}", i > 0 ? " " : "", wynik[i]);
        std::println(plik);
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    // zamienia wiersz z liczbami na listę liczb
    static List<Integer> liczby(String wiersz) {
        List<Integer> wynik = new ArrayList<>();
        for (String liczba : wiersz.trim().split("\\s+"))
            wynik.add(Integer.parseInt(liczba));
        return wynik;
    }

    static List<Integer> scal(List<Integer> a, List<Integer> b) {
        List<Integer> wynik = new ArrayList<>();
        int i = 0, j = 0;
        while (i < a.size() && j < b.size()) {
            if (a.get(i) <= b.get(j)) {
                wynik.add(a.get(i));
                i++;
            } else {
                wynik.add(b.get(j));
                j++;
            }
        }
        // jeden z ciągów się wyczerpał - przepisujemy resztę drugiego
        wynik.addAll(a.subList(i, a.size()));
        wynik.addAll(b.subList(j, b.size()));
        return wynik;
    }

    public static void main(String[] args) throws Exception {
        List<String> dane1 = Files.readAllLines(Path.of("dane1.txt"));
        List<String> dane2 = Files.readAllLines(Path.of("dane2.txt"));
        try (var plik = new PrintWriter("wynik4_4.txt")) {
            for (int i = 0; i < Math.min(dane1.size(), dane2.size()); i++) {
                List<String> napisy = new ArrayList<>();
                for (int x : scal(liczby(dane1.get(i)), liczby(dane2.get(i))))
                    napisy.add(String.valueOf(x));
                plik.println(String.join(" ", napisy));
            }
        }
    }
}
```
**Odpowiedź:** plik wynik4_4.txt (pierwsze wiersze: 1 5 6 6 8 13 13 14 15 15 24 24 33 33 34 35 36 41 44 45, 4 8 8 14 16 17 19 22 28 28 33 38 42 43 45 45 46 46 49 49, …)

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 5. Pomiary temperatury. Plik `pomiary.txt` ma 200 wierszy danych (pierwszy wiersz jest nagłówkowy); w każdym jest 12 pól oddzielonych średnikami: data, godzina oraz temperatury (°C, z dokładnością do 0,01, przecinek dziesiętny) zarejestrowane przez czujniki 1–10, np. `2016-01-05;11:11;0,61;-4,98;...;4,53`. Odpowiedzi zapisz w pliku `wyniki5.txt`, poprzedzając je numerami zadań.
>
> Oblicz średnią roczną temperaturę zmierzoną przez czujnik nr 5 w godzinach od 5:00 do 12:00 włącznie, zaokrągloną do dwóch miejsc po przecinku.

```py
suma = 0
ile = 0

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        godzina = dane[1]
        if "05:00" <= godzina <= "12:00":  # format GG:MM - można porównywać jak napisy
            suma += float(dane[2 + 4].replace(",", "."))  # czujnik5
            ile += 1

print(f"{suma / ile:.2f}")
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz na pola rozdzielone średnikiem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, ';'))
        pola.push_back(pole);
    return pola;
}

// "-4,98" -> -4.98
double na_liczbe(std::string tekst) {
    std::replace(tekst.begin(), tekst.end(), ',', '.');
    return std::stod(tekst);
}

int main() {
    double suma = 0;
    int ile = 0;

    std::ifstream plik("pomiary.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto dane = podziel(linia);
        std::string godzina = dane[1];
        if ("05:00" <= godzina && godzina <= "12:00") {  // format GG:MM - można porównywać jak napisy
            suma += na_liczbe(dane[2 + 4]);  // czujnik5
            ile++;
        }
    }

    std::println("{:.2f}", suma / ile);
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Zadanie {
    // liczba z 2 miejscami po kropce, jak f"{x:.2f}" w Pythonie
    static String dwaMiejsca(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).toPlainString();
    }

    public static void main(String[] args) throws Exception {
        double suma = 0;
        int ile = 0;

        List<String> linie = Files.readAllLines(Path.of("pomiary.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] dane = linia.strip().split(";");
            String godzina = dane[1];
            // format GG:MM - można porównywać jak napisy
            if (godzina.compareTo("05:00") >= 0 && godzina.compareTo("12:00") <= 0) {
                suma += Double.parseDouble(dane[2 + 4].replace(",", "."));  // czujnik5
                ile++;
            }
        }

        System.out.println(dwaMiejsca(suma / ile));
    }
}
```
**Odpowiedź:** 12,50

## 5.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Każdy pomiar z pliku `pomiary.txt` przelicz na skalę Kelvina (`T[K] = 273,15 + T[°C]`) i zaokrąglij w dół do liczby całkowitej. Dla każdego z 10 czujników podaj, które z tak otrzymanych wartości występują najczęściej. Wynik zapisz w `wyniki5.txt`.

```py
wystapienia = [{} for _ in range(10)]  # dla każdego czujnika: kelwiny -> liczba wystąpień

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        for c in range(10):
            # temperatura w setnych częściach stopnia, żeby uniknąć błędów float
            setne = int(dane[2 + c].replace(",", "").replace("-", ""))
            if dane[2 + c].startswith("-"):
                setne = -setne
            kelwiny = (27315 + setne) // 100  # zaokrąglenie w dół
            wystapienia[c][kelwiny] = wystapienia[c].get(kelwiny, 0) + 1

for c in range(10):
    najczesciej = max(wystapienia[c].values())
    wartosci = [k for k in wystapienia[c] if wystapienia[c][k] == najczesciej]
    print(f"czujnik{c + 1}", *sorted(wartosci))
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz na pola rozdzielone średnikiem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, ';'))
        pola.push_back(pole);
    return pola;
}

// dzielenie z zaokrągleniem w dół (jak // w Pythonie, także dla liczb ujemnych)
int podziel_w_dol(int a, int b) {
    int q = a / b;
    if (a % b != 0 && (a < 0) != (b < 0))
        q--;
    return q;
}

int main() {
    std::vector<std::map<int, int>> wystapienia(10);  // dla każdego czujnika: kelwiny -> liczba wystąpień

    std::ifstream plik("pomiary.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto dane = podziel(linia);
        for (int c = 0; c < 10; c++) {
            // temperatura w setnych częściach stopnia, żeby uniknąć błędów float
            std::string tekst = dane[2 + c];
            std::erase(tekst, ',');
            std::erase(tekst, '-');
            int setne = std::stoi(tekst);
            if (dane[2 + c].starts_with("-"))
                setne = -setne;
            int kelwiny = podziel_w_dol(27315 + setne, 100);  // zaokrąglenie w dół
            wystapienia[c][kelwiny]++;
        }
    }

    for (int c = 0; c < 10; c++) {
        int najczesciej = 0;
        for (auto& [k, ile] : wystapienia[c])
            najczesciej = std::max(najczesciej, ile);
        std::print("czujnik{}", c + 1);
        for (auto& [k, ile] : wystapienia[c])  // std::map - klucze już posortowane
            if (ile == najczesciej)
                std::print(" {}", k);
        std::println();
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.TreeMap;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // dla każdego czujnika: kelwiny -> liczba wystąpień
        List<TreeMap<Integer, Integer>> wystapienia = new ArrayList<>();
        for (int c = 0; c < 10; c++)
            wystapienia.add(new TreeMap<>());

        List<String> linie = Files.readAllLines(Path.of("pomiary.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] dane = linia.strip().split(";");
            for (int c = 0; c < 10; c++) {
                // temperatura w setnych częściach stopnia, żeby uniknąć błędów float
                int setne = Integer.parseInt(dane[2 + c].replace(",", "").replace("-", ""));
                if (dane[2 + c].startsWith("-"))
                    setne = -setne;
                int kelwiny = Math.floorDiv(27315 + setne, 100);  // zaokrąglenie w dół
                wystapienia.get(c).merge(kelwiny, 1, Integer::sum);
            }
        }

        for (int c = 0; c < 10; c++) {
            int najczesciej = Collections.max(wystapienia.get(c).values());
            var wiersz = new StringBuilder("czujnik" + (c + 1));
            for (var wpis : wystapienia.get(c).entrySet())  // TreeMap - klucze już posortowane
                if (wpis.getValue() == najczesciej)
                    wiersz.append(" ").append(wpis.getKey());
            System.out.println(wiersz);
        }
    }
}
```
**Odpowiedź:** 287, 288 (lub 286), 283, 284, 284, 287 (lub 296), 286, 288, 285, 286

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Na podstawie pliku `pomiary.txt` podaj średnie temperatury (°C, zaokrąglone do dwóch miejsc po przecinku) odczytane przez czujnik nr 10 w poszczególnych miesiącach 2016 roku. Przedstaw je na wykresie słupkowym z etykietami danych, opisami osi i tytułem. Wynik zapisz w `wyniki5.txt`.

```py
suma = {}
ile = {}

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        miesiac = int(dane[0][5:7])
        suma[miesiac] = suma.get(miesiac, 0) + float(dane[11].replace(",", "."))  # czujnik10
        ile[miesiac] = ile.get(miesiac, 0) + 1

for miesiac in sorted(suma):
    print(miesiac, f"{suma[miesiac] / ile[miesiac]:.2f}")
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz na pola rozdzielone średnikiem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, ';'))
        pola.push_back(pole);
    return pola;
}

// "-4,98" -> -4.98
double na_liczbe(std::string tekst) {
    std::replace(tekst.begin(), tekst.end(), ',', '.');
    return std::stod(tekst);
}

int main() {
    std::map<int, double> suma;  // std::map - miesiące posortowane
    std::map<int, int> ile;

    std::ifstream plik("pomiary.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto dane = podziel(linia);
        int miesiac = std::stoi(dane[0].substr(5, 2));
        suma[miesiac] += na_liczbe(dane[11]);  // czujnik10
        ile[miesiac]++;
    }

    for (auto& [miesiac, s] : suma)
        std::println("{} {:.2f}", miesiac, s / ile[miesiac]);
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Zadanie {
    // liczba z 2 miejscami po kropce, jak f"{x:.2f}" w Pythonie
    static String dwaMiejsca(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).toPlainString();
    }

    public static void main(String[] args) throws Exception {
        Map<Integer, Double> suma = new TreeMap<>();  // TreeMap - miesiące posortowane
        Map<Integer, Integer> ile = new TreeMap<>();

        List<String> linie = Files.readAllLines(Path.of("pomiary.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] dane = linia.strip().split(";");
            int miesiac = Integer.parseInt(dane[0].substring(5, 7));
            suma.merge(miesiac, Double.parseDouble(dane[11].replace(",", ".")), Double::sum);  // czujnik10
            ile.merge(miesiac, 1, Integer::sum);
        }

        for (int miesiac : suma.keySet())
            System.out.println(miesiac + " " + dwaMiejsca(suma.get(miesiac) / ile.get(miesiac)));
    }
}
```
**Odpowiedź:** sty 0,91; lut 0,16; mar 2,30; kwi 12,84; maj 13,56; cze 14,54; lip 22,22; sie 22,23; wrz 16,03; paź 15,03; lis 15,54; gru 0,65 (+ wykres słupkowy)

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Na podstawie pliku `pomiary.txt` (wszystkie odczyty wszystkich czujników) podaj, w którym z przedziałów temperatur: `(−10, 15⟩` czy `(15, 20⟩` (°C) mieści się więcej pomiarów, oraz podaj tę liczbę. Wynik zapisz w `wyniki5.txt`.

```py
przedzial1 = 0  # (-10, 15]
przedzial2 = 0  # (15, 20]

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        for t in dane[2:]:
            t = float(t.replace(",", "."))
            if -10 < t <= 15:
                przedzial1 += 1
            elif 15 < t <= 20:
                przedzial2 += 1

if przedzial1 > przedzial2:
    print("(-10, 15]", przedzial1)
else:
    print("(15, 20]", przedzial2)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz na pola rozdzielone średnikiem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, ';'))
        pola.push_back(pole);
    return pola;
}

// "-4,98" -> -4.98
double na_liczbe(std::string tekst) {
    std::replace(tekst.begin(), tekst.end(), ',', '.');
    return std::stod(tekst);
}

int main() {
    int przedzial1 = 0;  // (-10, 15]
    int przedzial2 = 0;  // (15, 20]

    std::ifstream plik("pomiary.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto dane = podziel(linia);
        for (size_t i = 2; i < dane.size(); i++) {
            double t = na_liczbe(dane[i]);
            if (-10 < t && t <= 15)
                przedzial1++;
            else if (15 < t && t <= 20)
                przedzial2++;
        }
    }

    if (przedzial1 > przedzial2)
        std::println("(-10, 15] {}", przedzial1);
    else
        std::println("(15, 20] {}", przedzial2);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int przedzial1 = 0;  // (-10, 15]
        int przedzial2 = 0;  // (15, 20]

        List<String> linie = Files.readAllLines(Path.of("pomiary.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] dane = linia.strip().split(";");
            for (int i = 2; i < dane.length; i++) {
                double t = Double.parseDouble(dane[i].replace(",", "."));
                if (-10 < t && t <= 15)
                    przedzial1++;
                else if (15 < t && t <= 20)
                    przedzial2++;
            }
        }

        if (przedzial1 > przedzial2)
            System.out.println("(-10, 15] " + przedzial1);
        else
            System.out.println("(15, 20] " + przedzial2);
    }
}
```
**Odpowiedź:** (-10, 15], 1150 pomiarów

## 5.5

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Wyniki z 2017 roku zaginęły. Wiadomo, że w tych samych dniach miesiąca i godzinach co w 2016 r. odczyty zmieniły się tak:
> - Wniosek I — w dniach od 5. do 10. każdego miesiąca odczyty czujników 1, 2 i 9 były o 1,2°C niższe niż w 2016 r.;
> - Wniosek II — w lipcu i sierpniu wszystkie odczyty czujnika 8 wzrosły o 7% (wynik zaokrąglony w dół do dwóch miejsc po przecinku);
> - Wniosek III — w maju odczyty wszystkich czujników były dodatkowo wyższe o 0,9°C.
>
> Gdzie żaden wniosek nie ma zastosowania, odczyty są takie jak w 2016 r. Odtwórz temperatury czujników 1, 2, 8 i 9 w 2017 roku i dla tych czujników podaj pierwsze pomiary z dni 5.05.2017 i 7.07.2017: po zastosowaniu wniosków I i II oraz osobno po zastosowaniu wszystkich trzech wniosków. Wynik zapisz w `wyniki5.txt`.

```py
def na_setne(tekst):
    # "-4,98" -> -498 (liczymy w setnych częściach stopnia)
    setne = int(tekst.replace(",", "").replace("-", ""))
    if tekst.startswith("-"):
        return -setne
    return setne


def napis(setne):
    znak = "-" if setne < 0 else ""
    setne = abs(setne)
    return f"{znak}{setne // 100},{setne % 100:02d}"


czujniki = [1, 2, 8, 9]
pierwsze = {}  # data 2017 -> (godzina, wartości wg wniosków I i II, wartości wg wniosków I, II i III)

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        data = "2017" + dane[0][4:]
        miesiac = int(data[5:7])
        dzien = int(data[8:10])

        wynik_ab = []
        wynik_abc = []
        for c in czujniki:
            t = na_setne(dane[1 + c])
            if 5 <= dzien <= 10 and c in [1, 2, 9]:      # wniosek I
                t -= 120
            if miesiac in [7, 8] and c == 8:              # wniosek II (w dół do 2 miejsc)
                t = t * 107 // 100
            wynik_ab.append(t)
            if miesiac == 5:                              # wniosek III
                t += 90
            wynik_abc.append(t)

        if data not in pierwsze:  # pierwszy pomiar danego dnia (dane są uporządkowane)
            pierwsze[data] = (dane[1], wynik_ab, wynik_abc)

for data in ["2017-05-05", "2017-07-07"]:
    godzina, ab, abc = pierwsze[data]
    print(data, godzina, "czujniki 1, 2, 8, 9")
    print("  wnioski I i II:     ", *[napis(t) for t in ab])
    print("  wnioski I, II i III:", *[napis(t) for t in abc])
```

```cpp
// C++23
#include <cstdlib>
#include <format>
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz na pola rozdzielone średnikiem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, ';'))
        pola.push_back(pole);
    return pola;
}

int na_setne(std::string tekst) {
    // "-4,98" -> -498 (liczymy w setnych częściach stopnia)
    bool ujemna = tekst.starts_with("-");
    std::erase(tekst, ',');
    std::erase(tekst, '-');
    int setne = std::stoi(tekst);
    return ujemna ? -setne : setne;
}

std::string napis(int setne) {
    std::string znak = setne < 0 ? "-" : "";
    setne = std::abs(setne);
    return std::format("{}{},{:02d}", znak, setne / 100, setne % 100);
}

// dzielenie z zaokrągleniem w dół (jak // w Pythonie, także dla liczb ujemnych)
int podziel_w_dol(int a, int b) {
    int q = a / b;
    if (a % b != 0 && (a < 0) != (b < 0))
        q--;
    return q;
}

struct Pomiar {
    std::string godzina;
    std::vector<int> ab, abc;  // wartości wg wniosków I i II oraz wg wniosków I, II i III
};

int main() {
    int czujniki[] = {1, 2, 8, 9};
    std::map<std::string, Pomiar> pierwsze;  // data 2017 -> pierwszy pomiar danego dnia

    std::ifstream plik("pomiary.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto dane = podziel(linia);
        std::string data = "2017" + dane[0].substr(4);
        int miesiac = std::stoi(data.substr(5, 2));
        int dzien = std::stoi(data.substr(8, 2));

        std::vector<int> wynik_ab, wynik_abc;
        for (int c : czujniki) {
            int t = na_setne(dane[1 + c]);
            if (5 <= dzien && dzien <= 10 && (c == 1 || c == 2 || c == 9))  // wniosek I
                t -= 120;
            if ((miesiac == 7 || miesiac == 8) && c == 8)                    // wniosek II (w dół do 2 miejsc)
                t = podziel_w_dol(t * 107, 100);
            wynik_ab.push_back(t);
            if (miesiac == 5)                                                // wniosek III
                t += 90;
            wynik_abc.push_back(t);
        }

        if (!pierwsze.contains(data))  // pierwszy pomiar danego dnia (dane są uporządkowane)
            pierwsze[data] = {dane[1], wynik_ab, wynik_abc};
    }

    for (std::string data : {"2017-05-05", "2017-07-07"}) {
        const Pomiar& p = pierwsze[data];
        std::println("{} {} czujniki 1, 2, 8, 9", data, p.godzina);
        std::print("  wnioski I i II:     ");
        for (int t : p.ab)
            std::print(" {}", napis(t));
        std::println();
        std::print("  wnioski I, II i III:");
        for (int t : p.abc)
            std::print(" {}", napis(t));
        std::println();
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Zadanie {
    static int naSetne(String tekst) {
        // "-4,98" -> -498 (liczymy w setnych częściach stopnia)
        int setne = Integer.parseInt(tekst.replace(",", "").replace("-", ""));
        if (tekst.startsWith("-"))
            return -setne;
        return setne;
    }

    static String napis(int setne) {
        String znak = setne < 0 ? "-" : "";
        setne = Math.abs(setne);
        return znak + setne / 100 + "," + String.format("%02d", setne % 100);
    }

    // wartości wg wniosków I i II oraz wg wniosków I, II i III
    record Pomiar(String godzina, List<Integer> ab, List<Integer> abc) {}

    public static void main(String[] args) throws Exception {
        int[] czujniki = {1, 2, 8, 9};
        Map<String, Pomiar> pierwsze = new HashMap<>();  // data 2017 -> pierwszy pomiar danego dnia

        List<String> linie = Files.readAllLines(Path.of("pomiary.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] dane = linia.strip().split(";");
            String data = "2017" + dane[0].substring(4);
            int miesiac = Integer.parseInt(data.substring(5, 7));
            int dzien = Integer.parseInt(data.substring(8, 10));

            List<Integer> wynikAb = new ArrayList<>();
            List<Integer> wynikAbc = new ArrayList<>();
            for (int c : czujniki) {
                int t = naSetne(dane[1 + c]);
                if (5 <= dzien && dzien <= 10 && (c == 1 || c == 2 || c == 9))  // wniosek I
                    t -= 120;
                if ((miesiac == 7 || miesiac == 8) && c == 8)                    // wniosek II (w dół do 2 miejsc)
                    t = Math.floorDiv(t * 107, 100);
                wynikAb.add(t);
                if (miesiac == 5)                                                // wniosek III
                    t += 90;
                wynikAbc.add(t);
            }

            // pierwszy pomiar danego dnia (dane są uporządkowane)
            pierwsze.putIfAbsent(data, new Pomiar(dane[1], wynikAb, wynikAbc));
        }

        for (String data : new String[]{"2017-05-05", "2017-07-07"}) {
            Pomiar p = pierwsze.get(data);
            System.out.println(data + " " + p.godzina() + " czujniki 1, 2, 8, 9");
            var ab = new StringBuilder("  wnioski I i II:     ");
            for (int t : p.ab())
                ab.append(" ").append(napis(t));
            System.out.println(ab);
            var abc = new StringBuilder("  wnioski I, II i III:");
            for (int t : p.abc())
                abc.append(" ").append(napis(t));
            System.out.println(abc);
        }
    }
}
```
**Odpowiedź:** 2017-05-05 07:05: I i II - czujnik1 9,46, czujnik2 9,39, czujnik8 14,52, czujnik9 10,45; I, II i III - 10,36, 10,29, 15,42, 11,35. 2017-07-07 00:04: 23,42, 19,39, 26,67, 20,70 (w obu wariantach)
