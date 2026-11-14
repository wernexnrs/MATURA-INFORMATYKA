<h1 align="center">Matura 2017 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Zadanie 1. Sitko. Dana jest procedura z parametrem — dodatnią liczbą całkowitą `n`:
>
> ```
> Sitko(n):
>     dla i = 1, 2, ..., n: Czyjest[i] ← prawda
>     j ← 1
>     dopóki j*j < n: j ← j+1
>     dla i = 2, 3, ..., j wykonuj
>         kw ← i*i; poz ← kw
>         dopóki poz ≤ n wykonuj
>             (*) Czyjest[poz] ← fałsz
>             poz ← poz + kw
> ```
>
> - 1.1 — Podaj wartość `j` oraz `Czyjest[k]` po wykonaniu `Sitko(n)` dla par: `n=10, k=9` (wzór: `j=4`, prawda), `n=10, k=5`, `n=100, k=10`, `n=100, k=75`.
> - 1.2 — Dla `Sitko(100)` podaj, ile razy wykona się wiersz `(*)` dla `i` = 3, 5, 9 (dla `i=2` jest to 25) oraz łączną liczbę wykonań wiersza `(*)` w całej procedurze.
> - 1.3 — Liczba jest kwadratowa, jeśli da się ją zapisać jako `a·b² + c·d²`, gdzie `a, b, c, d` są dodatnimi liczbami całkowitymi, a `b, d > 1`. Korzystając z tablicy `Czyjest[1..n]` obliczonej przez `Sitko(n)`, zapisz algorytm, który dla liczby `k` (`1 ≤ k ≤ n`) zwraca prawdę, gdy `k` jest kwadratowa, a fałsz w przeciwnym razie.

```py
import math


def sitko(n):
    czyjest = [False] * (n + 1)   # indeksy 1..n
    j = 1
    while j * j < n:
        j += 1
    wykonania = {}                # i -> liczba wykonań wiersza (*)
    for i in range(2, j + 1):
        kw = i * i
        poz = kw
        wykonania[i] = 0
        while poz <= n:
            czyjest[poz] = True   # (*)
            wykonania[i] += 1
            poz += kw
    return j, czyjest, wykonania


def czy_kwadratowa(k, czyjest):
    # k = a*b^2 + c*d^2 (b, d > 1) <=> k = x + (k - x), gdzie czyjest[x] i czyjest[k - x]
    for x in range(1, k):
        if czyjest[x] and czyjest[k - x]:
            return True
    return False


# 1.1
for n, k in [(10, 9), (10, 5), (100, 10), (100, 75)]:
    j, czyjest, wykonania = sitko(n)
    print(n, k, j, czyjest[k])

# 1.2
j, czyjest, wykonania = sitko(100)
for i in [2, 3, 5, 9]:
    print(i, wykonania[i])
razem = sum(wykonania.values())
print("razem:", razem)
print("ln 100:", math.log(100) > razem)
print("100:", 100 > razem)
print("100 * (1/2^2 + ... + 1/10^2):", 100 * sum(1 / i ** 2 for i in range(2, 11)) > razem)
print("sqrt(100):", math.sqrt(100) > razem)

# 1.3
print([k for k in range(1, 101) if czy_kwadratowa(k, czyjest)])
```

```cpp
// C++23
#include <cmath>
#include <map>
#include <print>
#include <string>
#include <vector>

struct Sitko {
    int j;
    std::vector<bool> czyjest;     // indeksy 1..n
    std::map<int, int> wykonania;  // i -> liczba wykonań wiersza (*)
};

Sitko sitko(int n) {
    Sitko s;
    s.czyjest.assign(n + 1, false);
    int j = 1;
    while (j * j < n)
        j++;
    s.j = j;
    for (int i = 2; i <= j; i++) {
        int kw = i * i;
        int poz = kw;
        s.wykonania[i] = 0;
        while (poz <= n) {
            s.czyjest[poz] = true;  // (*)
            s.wykonania[i]++;
            poz += kw;
        }
    }
    return s;
}

bool czy_kwadratowa(int k, const std::vector<bool>& czyjest) {
    // k = a*b^2 + c*d^2 (b, d > 1) <=> k = x + (k - x), gdzie czyjest[x] i czyjest[k - x]
    for (int x = 1; x < k; x++)
        if (czyjest[x] && czyjest[k - x])
            return true;
    return false;
}

// wartość logiczna zapisana jak w Pythonie
std::string py(bool b) {
    return b ? "True" : "False";
}

int main() {
    // 1.1
    int pary[4][2] = {{10, 9}, {10, 5}, {100, 10}, {100, 75}};
    for (auto& [n, k] : pary) {
        Sitko s = sitko(n);
        std::println("{} {} {} {}", n, k, s.j, py(s.czyjest[k]));
    }

    // 1.2
    Sitko s = sitko(100);
    for (int i : {2, 3, 5, 9})
        std::println("{} {}", i, s.wykonania[i]);
    int razem = 0;
    for (auto& [i, ile] : s.wykonania)
        razem += ile;
    std::println("razem: {}", razem);
    std::println("ln 100: {}", py(std::log(100) > razem));
    std::println("100: {}", py(100 > razem));
    double suma = 0;
    for (int i = 2; i <= 10; i++)
        suma += 1.0 / (i * i);
    std::println("100 * (1/2^2 + ... + 1/10^2): {}", py(100 * suma > razem));
    std::println("sqrt(100): {}", py(std::sqrt(100) > razem));

    // 1.3
    std::vector<int> kwadratowe;
    for (int k = 1; k <= 100; k++)
        if (czy_kwadratowa(k, s.czyjest))
            kwadratowe.push_back(k);
    std::println("{}", kwadratowe);
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

public class Zadanie {
    record Sitko(int j, boolean[] czyjest, TreeMap<Integer, Integer> wykonania) {}

    static Sitko sitko(int n) {
        boolean[] czyjest = new boolean[n + 1];  // indeksy 1..n
        int j = 1;
        while (j * j < n)
            j++;
        var wykonania = new TreeMap<Integer, Integer>();  // i -> liczba wykonań wiersza (*)
        for (int i = 2; i <= j; i++) {
            int kw = i * i;
            int poz = kw;
            wykonania.put(i, 0);
            while (poz <= n) {
                czyjest[poz] = true;  // (*)
                wykonania.put(i, wykonania.get(i) + 1);
                poz += kw;
            }
        }
        return new Sitko(j, czyjest, wykonania);
    }

    static boolean czyKwadratowa(int k, boolean[] czyjest) {
        // k = a*b^2 + c*d^2 (b, d > 1) <=> k = x + (k - x), gdzie czyjest[x] i czyjest[k - x]
        for (int x = 1; x < k; x++)
            if (czyjest[x] && czyjest[k - x])
                return true;
        return false;
    }

    // wartość logiczna zapisana jak w Pythonie
    static String py(boolean b) {
        return b ? "True" : "False";
    }

    public static void main(String[] args) {
        // 1.1
        int[][] pary = {{10, 9}, {10, 5}, {100, 10}, {100, 75}};
        for (int[] para : pary) {
            int n = para[0], k = para[1];
            Sitko s = sitko(n);
            System.out.println(n + " " + k + " " + s.j() + " " + py(s.czyjest()[k]));
        }

        // 1.2
        Sitko s = sitko(100);
        for (int i : new int[]{2, 3, 5, 9})
            System.out.println(i + " " + s.wykonania().get(i));
        int razem = 0;
        for (int ile : s.wykonania().values())
            razem += ile;
        System.out.println("razem: " + razem);
        System.out.println("ln 100: " + py(Math.log(100) > razem));
        System.out.println("100: " + py(100 > razem));
        double suma = 0;
        for (int i = 2; i <= 10; i++)
            suma += 1.0 / (i * i);
        System.out.println("100 * (1/2^2 + ... + 1/10^2): " + py(100 * suma > razem));
        System.out.println("sqrt(100): " + py(Math.sqrt(100) > razem));

        // 1.3
        List<Integer> kwadratowe = new ArrayList<>();
        for (int k = 1; k <= 100; k++)
            if (czyKwadratowa(k, s.czyjest()))
                kwadratowe.add(k);
        System.out.println(kwadratowe);
    }
}
```
**Odpowiedź:** 1.1: (10, 9): j = 4, prawda; (10, 5): 4, fałsz; (100, 10): 10, fałsz; (100, 75): 10, prawda. 1.2: i = 2: 25, 3: 11, 5: 4, 9: 1; większe od łącznej liczby wykonań: 100 oraz 100 · (1/2² + … + 1/10²). 1.3: funkcja `czy_kwadratowa`.

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2. Regularność. Rozważamy słowa nad alfabetem {A, B}. Regularność `reg(w)` definiujemy tak:
> - słowo jednoliterowe jest palindromem i `reg(w) = 1`;
> - dłuższe słowo zapisujemy jako `w = w1 Z w2` (długość nieparzysta, `Z` — jedna litera) lub `w = w1 w2` (długość parzysta), gdzie `w1`, `w2` mają równe długości; jeśli `w` nie jest palindromem, to `reg(w) = 0`, a jeśli jest — `reg(w) = reg(w1) + 1`.
>
> Np. `reg(BAAAB) = 3`, `reg(BABBAB) = 3`.
>
> - 2.1 — Podaj `reg(w)` dla słów: `BABBBB`, `BAAAAB`, `B`, `BBB`, `AAAAAAAA`.
> - 2.2 — Uzupełnij luki w rekurencyjnej funkcji `REG(w, n)` (dane: `n` — długość, `w[1..n]` — słowo; wynik: `reg(w)`):
>
> ```
> jeżeli n = 1: wynikiem jest .....
> w przeciwnym przypadku
>     m ← n/2 (dla n parzystego) albo (n-1)/2 (dla nieparzystego)
>     dla i = 1..m: jeżeli w[i] ≠ ..... : wynikiem jest 0, koniec
>     x ← w[1..m]
>     wynikiem jest 1 + .....
> ```

```py
def REG(w, n):
    if n == 1:
        return 1
    m = n // 2                      # dla n nieparzystego to (n - 1) / 2
    for i in range(m):              # w[i] porównujemy z w[n + 1 - i] (tu indeksy od 0)
        if w[i] != w[n - 1 - i]:
            return 0
    return 1 + REG(w[:m], m)


# 2.1
for w in ["BABBAB", "BABBBB", "BAAAAB", "B", "BBB", "AAAAAAAA"]:
    print(w, REG(w, len(w)))
```

```cpp
// C++23
#include <print>
#include <string>

int REG(const std::string& w, int n) {
    if (n == 1)
        return 1;
    int m = n / 2;                  // dla n nieparzystego to (n - 1) / 2
    for (int i = 0; i < m; i++)     // w[i] porównujemy z w[n + 1 - i] (tu indeksy od 0)
        if (w[i] != w[n - 1 - i])
            return 0;
    return 1 + REG(w.substr(0, m), m);
}

int main() {
    // 2.1
    for (std::string w : {"BABBAB", "BABBBB", "BAAAAB", "B", "BBB", "AAAAAAAA"})
        std::println("{} {}", w, REG(w, w.size()));
}
```

```java
// Java 25
public class Zadanie {
    static int REG(String w, int n) {
        if (n == 1)
            return 1;
        int m = n / 2;                  // dla n nieparzystego to (n - 1) / 2
        for (int i = 0; i < m; i++)     // w[i] porównujemy z w[n + 1 - i] (tu indeksy od 0)
            if (w.charAt(i) != w.charAt(n - 1 - i))
                return 0;
        return 1 + REG(w.substring(0, m), m);
    }

    public static void main(String[] args) {
        // 2.1
        for (String w : new String[]{"BABBAB", "BABBBB", "BAAAAB", "B", "BBB", "AAAAAAAA"})
            System.out.println(w + " " + REG(w, w.length()));
    }
}
```
**Odpowiedź:** 2.1: 3, 0, 1, 1, 2, 4. 2.2: wynikiem jest 1; w[i] ≠ w[n + 1 - i]; wynikiem jest 1 + REG(x, m).

## 3.1 i 3.2

> **Treść zadania:** Zadanie 3. Zegary. Zegary w trzech oddziałach pokazują liczbę minut od początku doby: oddział A w systemie dwójkowym, B — czwórkowym, C — szesnastkowym. Oddziały leżą w różnych strefach czasowych. W pewnej chwili wskazania wynosiły: A: `00010110100`, B: `000330`, C: `078`.
>
> - 3.1 — Oceń prawdziwość zdań: wszystkie wskazania są wielokrotnościami 6; różnica wskazań każdej pary zegarów jest wielokrotnością 60; największe wskazanie ma zegar A, a najmniejsze zegar C.
> - 3.2 — Po pewnym czasie odczytano zegary jednocześnie, ale część cyfr (X) była nieczytelna: A: `000110100XX`, B: `001XX2`, C: `X96`. Podaj pełne wskazania wszystkich trzech zegarów.

```py
A = int("00010110100", 2)
B = int("000330", 4)
C = int("078", 16)

# 3.1
print(A, B, C)
print(A % 6 == 0 and B % 6 == 0 and C % 6 == 0)
print((A - B) % 60 == 0 and (A - C) % 60 == 0 and (B - C) % 60 == 0)

# 3.2 - szukamy wartości pasujących do wzorców; po tym samym czasie t od pierwszego odczytu
# wszystkie zegary przesunęły się o tyle samo minut (pomijamy przejście przez północ)
def pasuje(liczba, wzorzec, podstawa):
    cyfry = "0123456789ABCDEF"
    zapis = ""
    for _ in range(len(wzorzec)):
        zapis = cyfry[liczba % podstawa] + zapis
        liczba //= podstawa
    if liczba > 0:
        return False
    for z, w in zip(zapis, wzorzec):
        if w != "X" and z != w:
            return False
    return True


for t in range(0, 24 * 60):
    if pasuje(A + t, "000110100XX", 2) and pasuje(B + t, "001XX2", 4) and pasuje(C + t, "X96", 16):
        print(bin(A + t)[2:].zfill(11), A + t)
        print(B + t, C + t)
```

```cpp
// C++23
#include <print>
#include <string>

// wartość logiczna zapisana jak w Pythonie
std::string py(bool b) {
    return b ? "True" : "False";
}

// 3.2 - szukamy wartości pasujących do wzorców; po tym samym czasie t od pierwszego odczytu
// wszystkie zegary przesunęły się o tyle samo minut (pomijamy przejście przez północ)
bool pasuje(int liczba, const std::string& wzorzec, int podstawa) {
    const std::string cyfry = "0123456789ABCDEF";
    std::string zapis;
    for (size_t i = 0; i < wzorzec.size(); i++) {
        zapis = cyfry[liczba % podstawa] + zapis;
        liczba /= podstawa;
    }
    if (liczba > 0)
        return false;
    for (size_t i = 0; i < wzorzec.size(); i++)
        if (wzorzec[i] != 'X' && zapis[i] != wzorzec[i])
            return false;
    return true;
}

// zapis binarny uzupełniony zerami z przodu do podanej długości
std::string binarnie(int liczba, int dlugosc) {
    std::string zapis;
    while (liczba > 0) {
        zapis = char('0' + liczba % 2) + zapis;
        liczba /= 2;
    }
    while ((int)zapis.size() < dlugosc)
        zapis = "0" + zapis;
    return zapis;
}

int main() {
    int A = std::stoi("00010110100", nullptr, 2);
    int B = std::stoi("000330", nullptr, 4);
    int C = std::stoi("078", nullptr, 16);

    // 3.1
    std::println("{} {} {}", A, B, C);
    std::println("{}", py(A % 6 == 0 && B % 6 == 0 && C % 6 == 0));
    std::println("{}", py((A - B) % 60 == 0 && (A - C) % 60 == 0 && (B - C) % 60 == 0));

    // 3.2
    for (int t = 0; t < 24 * 60; t++) {
        if (pasuje(A + t, "000110100XX", 2) && pasuje(B + t, "001XX2", 4) && pasuje(C + t, "X96", 16)) {
            std::println("{} {}", binarnie(A + t, 11), A + t);
            std::println("{} {}", B + t, C + t);
        }
    }
}
```

```java
// Java 25
public class Zadanie {
    // wartość logiczna zapisana jak w Pythonie
    static String py(boolean b) {
        return b ? "True" : "False";
    }

    // 3.2 - szukamy wartości pasujących do wzorców; po tym samym czasie t od pierwszego odczytu
    // wszystkie zegary przesunęły się o tyle samo minut (pomijamy przejście przez północ)
    static boolean pasuje(int liczba, String wzorzec, int podstawa) {
        String cyfry = "0123456789ABCDEF";
        String zapis = "";
        for (int i = 0; i < wzorzec.length(); i++) {
            zapis = cyfry.charAt(liczba % podstawa) + zapis;
            liczba /= podstawa;
        }
        if (liczba > 0)
            return false;
        for (int i = 0; i < wzorzec.length(); i++)
            if (wzorzec.charAt(i) != 'X' && zapis.charAt(i) != wzorzec.charAt(i))
                return false;
        return true;
    }

    public static void main(String[] args) {
        int A = Integer.parseInt("00010110100", 2);
        int B = Integer.parseInt("000330", 4);
        int C = Integer.parseInt("078", 16);

        // 3.1
        System.out.println(A + " " + B + " " + C);
        System.out.println(py(A % 6 == 0 && B % 6 == 0 && C % 6 == 0));
        System.out.println(py((A - B) % 60 == 0 && (A - C) % 60 == 0 && (B - C) % 60 == 0));

        // 3.2
        for (int t = 0; t < 24 * 60; t++) {
            if (pasuje(A + t, "000110100XX", 2) && pasuje(B + t, "001XX2", 4) && pasuje(C + t, "X96", 16)) {
                // zapis binarny uzupełniony zerami z przodu do 11 cyfr
                String binarnie = "0".repeat(11) + Integer.toBinaryString(A + t);
                System.out.println(binarnie.substring(binarnie.length() - 11) + " " + (A + t));
                System.out.println((B + t) + " " + (C + t));
            }
        }
    }
}
```
**Odpowiedź:** 3.1: F, P, P (A = 180, B = 60, C = 120). 3.2: A: 00011010010, B: 001122, C: 096.

## 4.1

> **Treść zadania:** Zadanie 4. Punkty. Plik `punkty.txt` zawiera 1000 wierszy; w każdym są dwie liczby całkowite z przedziału [0, 10000] oddzielone spacją — współrzędne `(x, y)` punktu. Punkty się nie powtarzają. Odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając każdą numerem zadania.
>
> Podaj, ile jest punktów, których obie współrzędne są liczbami pierwszymi.

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


licznik = 0

with open("punkty.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        if czy_pierwsza(x) and czy_pierwsza(y):
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <print>

bool czy_pierwsza(long long x) {
    if (x < 2)
        return false;
    for (long long i = 2; i * i <= x; i++)
        if (x % i == 0)
            return false;
    return true;
}

int main() {
    int licznik = 0;

    std::ifstream plik("punkty.txt");
    long long x, y;
    while (plik >> x >> y)
        if (czy_pierwsza(x) && czy_pierwsza(y))
            licznik++;

    std::println("{}", licznik);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static boolean czyPierwsza(long x) {
        if (x < 2)
            return false;
        for (long i = 2; i * i <= x; i++)
            if (x % i == 0)
                return false;
        return true;
    }

    public static void main(String[] args) throws Exception {
        int licznik = 0;

        for (String linia : Files.readAllLines(Path.of("punkty.txt"))) {
            String[] pola = linia.trim().split("\\s+");
            long x = Long.parseLong(pola[0]), y = Long.parseLong(pola[1]);
            if (czyPierwsza(x) && czyPierwsza(y))
                licznik++;
        }

        System.out.println(licznik);
    }
}
```
**Odpowiedź:** 18

## 4.2

> **Treść zadania:** Dla punktów z pliku `punkty.txt` (1000 par współrzędnych z [0, 10000]): dwie liczby są cyfropodobne, jeśli do ich zapisu użyto dokładnie tego samego zbioru cyfr (np. 123 i 1321 są cyfropodobne, a 505 i 55 — nie). Podaj, ile jest punktów, których współrzędne są cyfropodobne. Wynik dopisz do `wyniki4.txt`.

```py
licznik = 0

with open("punkty.txt") as file:
    for line in file:
        x, y = line.split()
        # cyfropodobne - zbiory użytych cyfr są równe (porównujemy zbiory, nie listy)
        if set(x) == set(y):
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <set>
#include <string>

int main() {
    int licznik = 0;

    std::ifstream plik("punkty.txt");
    std::string x, y;
    while (plik >> x >> y) {
        // cyfropodobne - zbiory użytych cyfr są równe (porównujemy zbiory, nie listy)
        std::set<char> cyfry_x(x.begin(), x.end());
        std::set<char> cyfry_y(y.begin(), y.end());
        if (cyfry_x == cyfry_y)
            licznik++;
    }

    std::println("{}", licznik);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.Set;

public class Zadanie {
    static Set<Character> zbiorCyfr(String liczba) {
        Set<Character> zbior = new HashSet<>();
        for (char c : liczba.toCharArray())
            zbior.add(c);
        return zbior;
    }

    public static void main(String[] args) throws Exception {
        int licznik = 0;

        for (String linia : Files.readAllLines(Path.of("punkty.txt"))) {
            String[] pola = linia.trim().split("\\s+");
            // cyfropodobne - zbiory użytych cyfr są równe (porównujemy zbiory, nie listy)
            if (zbiorCyfr(pola[0]).equals(zbiorCyfr(pola[1])))
                licznik++;
        }

        System.out.println(licznik);
    }
}
```
**Odpowiedź:** 5

## 4.3

> **Treść zadania:** Wśród punktów z pliku `punkty.txt` znajdź dwa najbardziej oddalone od siebie (taka para jest jedna). Podaj współrzędne obu punktów oraz odległość między nimi zaokrągloną do liczby całkowitej, gdzie `|AB| = √((xA−xB)² + (yA−yB)²)`. Wynik dopisz do `wyniki4.txt`.

```py
import math

punkty = []
with open("punkty.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        punkty.append((x, y))

najwieksza = -1  # kwadrat odległości - porównujemy bez pierwiastka
for i in range(len(punkty)):
    for j in range(i + 1, len(punkty)):
        x1, y1 = punkty[i]
        x2, y2 = punkty[j]
        kwadrat = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if kwadrat > najwieksza:
            najwieksza = kwadrat
            para = (punkty[i], punkty[j])

print(para[0], para[1], round(math.sqrt(najwieksza)))
```

```cpp
// C++23
#include <cmath>
#include <fstream>
#include <print>
#include <utility>
#include <vector>

int main() {
    std::vector<std::pair<long long, long long>> punkty;
    std::ifstream plik("punkty.txt");
    long long x, y;
    while (plik >> x >> y)
        punkty.push_back({x, y});

    long long najwieksza = -1;  // kwadrat odległości - porównujemy bez pierwiastka
    std::pair<long long, long long> p1, p2;
    for (size_t i = 0; i < punkty.size(); i++) {
        for (size_t j = i + 1; j < punkty.size(); j++) {
            auto [x1, y1] = punkty[i];
            auto [x2, y2] = punkty[j];
            long long kwadrat = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
            if (kwadrat > najwieksza) {
                najwieksza = kwadrat;
                p1 = punkty[i];
                p2 = punkty[j];
            }
        }
    }

    std::println("({}, {}) ({}, {}) {}", p1.first, p1.second, p2.first, p2.second,
                 std::llround(std::sqrt(najwieksza)));
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    record Punkt(long x, long y) {
        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }

    public static void main(String[] args) throws Exception {
        List<Punkt> punkty = new ArrayList<>();
        for (String linia : Files.readAllLines(Path.of("punkty.txt"))) {
            String[] pola = linia.trim().split("\\s+");
            punkty.add(new Punkt(Long.parseLong(pola[0]), Long.parseLong(pola[1])));
        }

        long najwieksza = -1;  // kwadrat odległości - porównujemy bez pierwiastka
        Punkt p1 = null, p2 = null;
        for (int i = 0; i < punkty.size(); i++) {
            for (int j = i + 1; j < punkty.size(); j++) {
                Punkt a = punkty.get(i), b = punkty.get(j);
                long kwadrat = (a.x() - b.x()) * (a.x() - b.x()) + (a.y() - b.y()) * (a.y() - b.y());
                if (kwadrat > najwieksza) {
                    najwieksza = kwadrat;
                    p1 = a;
                    p2 = b;
                }
            }
        }

        System.out.println(p1 + " " + p2 + " " + Math.round(Math.sqrt(najwieksza)));
    }
}
```
**Odpowiedź:** (9901, 593) i (35, 9583), odległość 13348

## 4.4

> **Treść zadania:** Kwadrat K ma bok długości 10000, środek symetrii w początku układu współrzędnych i boki równoległe do osi. Dla punktów z pliku `punkty.txt` podaj, ile z nich leży: a) wewnątrz K (bez boków), b) na bokach K, c) na zewnątrz K. Wynik dopisz do `wyniki4.txt`.

```py
wewnatrz = na_boku = na_zewnatrz = 0

with open("punkty.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        # kwadrat K: -5000 <= x, y <= 5000 (bok 10000, środek w (0, 0))
        if abs(x) < 5000 and abs(y) < 5000:
            wewnatrz += 1
        elif abs(x) <= 5000 and abs(y) <= 5000:
            na_boku += 1
        else:
            na_zewnatrz += 1

print(wewnatrz, na_boku, na_zewnatrz)
```

```cpp
// C++23
#include <cstdlib>
#include <fstream>
#include <print>

int main() {
    int wewnatrz = 0, na_boku = 0, na_zewnatrz = 0;

    std::ifstream plik("punkty.txt");
    long long x, y;
    while (plik >> x >> y) {
        // kwadrat K: -5000 <= x, y <= 5000 (bok 10000, środek w (0, 0))
        if (std::llabs(x) < 5000 && std::llabs(y) < 5000)
            wewnatrz++;
        else if (std::llabs(x) <= 5000 && std::llabs(y) <= 5000)
            na_boku++;
        else
            na_zewnatrz++;
    }

    std::println("{} {} {}", wewnatrz, na_boku, na_zewnatrz);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int wewnatrz = 0, naBoku = 0, naZewnatrz = 0;

        for (String linia : Files.readAllLines(Path.of("punkty.txt"))) {
            String[] pola = linia.trim().split("\\s+");
            long x = Long.parseLong(pola[0]), y = Long.parseLong(pola[1]);
            // kwadrat K: -5000 <= x, y <= 5000 (bok 10000, środek w (0, 0))
            if (Math.abs(x) < 5000 && Math.abs(y) < 5000)
                wewnatrz++;
            else if (Math.abs(x) <= 5000 && Math.abs(y) <= 5000)
                naBoku++;
            else
                naZewnatrz++;
        }

        System.out.println(wewnatrz + " " + naBoku + " " + naZewnatrz);
    }
}
```
**Odpowiedź:** a) 249, b) 2, c) 749

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 5. Firma transportowa. Plik `transport.txt` (dane rozdzielone tabulatorami, pierwszy wiersz nagłówkowy) opisuje samochody firmy: marka i model (jedno pole), rok produkcji, cena zakupu w zł, numer rejestracyjny, przebieg w km, data ostatniego remontu. Wartość samochodu maleje o 5% ceny zakupu za każdy rok od roku produkcji oraz o 2% ceny zakupu za każde pełne 100 000 km przebiegu (np. auto z 2015 r. za 70 000 zł z przebiegiem 350 000 km jest w 2017 r. warte 70 000 − 7000 − 4200 = 58 800 zł). Odpowiedzi zapisz w pliku `wyniki5.txt`, poprzedzając je numerami zadań.
>
> - a) Podaj wartość w roku 2017 samochodu Volvo FH o numerze `ERA 092 TR` oraz jego amortyzację z tytułu upływu czasu i z tytułu przebiegu.
> - b) Znajdź samochód o najniższej wartości w 2017 r.; podaj jego markę i model, numer rejestracyjny i wartość.

```py
def amortyzacja(rok, cena, przebieg):
    czasowa = cena * 5 * (2017 - rok) // 100
    zuzycie = cena * 2 * (przebieg // 100000) // 100
    return czasowa, zuzycie


najmniejsza = None
with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        czasowa, zuzycie = amortyzacja(int(rok), int(cena), int(przebieg))
        wartosc = int(cena) - czasowa - zuzycie

        # a)
        if nr == "ERA 092 TR":
            print(model, wartosc, czasowa, zuzycie)

        # b)
        if najmniejsza is None or wartosc < najmniejsza:
            najmniejsza = wartosc
            najtanszy = (model, nr, wartosc)

print(*najtanszy)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz na pola rozdzielone tabulatorem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, '\t'))
        pola.push_back(pole);
    return pola;
}

int main() {
    bool pierwszy = true;
    long long najmniejsza = 0;
    std::string najtanszy_model, najtanszy_nr;

    std::ifstream plik("transport.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto pola = podziel(linia);
        std::string model = pola[0], nr = pola[3];
        long long rok = std::stoll(pola[1]), cena = std::stoll(pola[2]), przebieg = std::stoll(pola[4]);
        long long czasowa = cena * 5 * (2017 - rok) / 100;
        long long zuzycie = cena * 2 * (przebieg / 100000) / 100;
        long long wartosc = cena - czasowa - zuzycie;

        // a)
        if (nr == "ERA 092 TR")
            std::println("{} {} {} {}", model, wartosc, czasowa, zuzycie);

        // b)
        if (pierwszy || wartosc < najmniejsza) {
            pierwszy = false;
            najmniejsza = wartosc;
            najtanszy_model = model;
            najtanszy_nr = nr;
        }
    }

    std::println("{} {} {}", najtanszy_model, najtanszy_nr, najmniejsza);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        Long najmniejsza = null;
        String najtanszy = "";

        List<String> linie = Files.readAllLines(Path.of("transport.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            String model = pola[0], nr = pola[3];
            long rok = Long.parseLong(pola[1]), cena = Long.parseLong(pola[2]), przebieg = Long.parseLong(pola[4]);
            long czasowa = cena * 5 * (2017 - rok) / 100;
            long zuzycie = cena * 2 * (przebieg / 100000) / 100;
            long wartosc = cena - czasowa - zuzycie;

            // a)
            if (nr.equals("ERA 092 TR"))
                System.out.println(model + " " + wartosc + " " + czasowa + " " + zuzycie);

            // b)
            if (najmniejsza == null || wartosc < najmniejsza) {
                najmniejsza = wartosc;
                najtanszy = model + " " + nr + " " + wartosc;
            }
        }

        System.out.println(najtanszy);
    }
}
```
**Odpowiedź:** a) wartość 43 610 zł, amortyzacja czasowa 40 050 zł, z przebiegu 5 340 zł; b) DAF LF45, ERA 132 TR, 17 390 zł

## 5.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Pole z marką i modelem samochodu w pliku `transport.txt` zawiera markę i model oddzielone spacją. Wyodrębnij markę każdego samochodu i dla każdej marki podaj: a) liczbę samochodów tej marki, b) średni przebieg (w km, zaokrąglony do liczby całkowitej). Wykonaj wykres kolumnowy średniego przebiegu dla każdej marki z tytułem i etykietami osi poziomej. Wynik zapisz w `wyniki5.txt`.

```py
liczba = {}
suma_przebiegow = {}

with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        marka = model.split()[0]
        liczba[marka] = liczba.get(marka, 0) + 1
        suma_przebiegow[marka] = suma_przebiegow.get(marka, 0) + int(przebieg)

for marka in sorted(liczba):
    print(marka, liczba[marka], round(suma_przebiegow[marka] / liczba[marka]))
```

```cpp
// C++23
#include <cmath>
#include <fstream>
#include <map>
#include <print>
#include <sstream>
#include <string>
#include <vector>

// dzieli wiersz na pola rozdzielone tabulatorem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, '\t'))
        pola.push_back(pole);
    return pola;
}

int main() {
    std::map<std::string, long long> liczba;  // std::map trzyma klucze posortowane
    std::map<std::string, long long> suma_przebiegow;

    std::ifstream plik("transport.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto pola = podziel(linia);
        std::string marka = pola[0].substr(0, pola[0].find(' '));
        liczba[marka]++;
        suma_przebiegow[marka] += std::stoll(pola[4]);
    }

    for (auto& [marka, ile] : liczba) {
        // std::nearbyint zaokrągla połówki do parzystej, tak jak round() w Pythonie
        double srednia = (double)suma_przebiegow[marka] / ile;
        std::println("{} {} {}", marka, ile, (long long)std::nearbyint(srednia));
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        Map<String, Long> liczba = new TreeMap<>();  // TreeMap trzyma klucze posortowane
        Map<String, Long> sumaPrzebiegow = new TreeMap<>();

        List<String> linie = Files.readAllLines(Path.of("transport.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            String marka = pola[0].split(" ")[0];
            liczba.merge(marka, 1L, Long::sum);
            sumaPrzebiegow.merge(marka, Long.parseLong(pola[4]), Long::sum);
        }

        for (String marka : liczba.keySet()) {
            // Math.rint zaokrągla połówki do parzystej, tak jak round() w Pythonie
            double srednia = (double) sumaPrzebiegow.get(marka) / liczba.get(marka);
            System.out.println(marka + " " + liczba.get(marka) + " " + (long) Math.rint(srednia));
        }
    }
}
```
**Odpowiedź:** DAF 30 / 273 240, Iveco 12 / 657 434, MAN 18 / 289 637, Mercedes 17 / 486 546, Renault 17 / 519 936, Scania 17 / 557 118, Volvo 23 / 307 130 (+ wykres kolumnowy)

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Na podstawie pliku `transport.txt` utwórz zestawienie liczby samochodów poszczególnych marek wyprodukowanych w kolejnych latach od 2006 do 2015 włącznie. Wynik zapisz w `wyniki5.txt`.

```py
zestawienie = {}  # (rok, marka) -> liczba samochodów
marki = set()

with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        marka = model.split()[0]
        marki.add(marka)
        zestawienie[(int(rok), marka)] = zestawienie.get((int(rok), marka), 0) + 1

marki = sorted(marki)
print("rok", *marki)
for rok in range(2006, 2016):
    print(rok, *[zestawienie.get((rok, marka), 0) for marka in marki])
```

```cpp
// C++23
#include <fstream>
#include <map>
#include <print>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

// dzieli wiersz na pola rozdzielone tabulatorem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, '\t'))
        pola.push_back(pole);
    return pola;
}

int main() {
    std::map<std::pair<int, std::string>, int> zestawienie;  // (rok, marka) -> liczba samochodów
    std::set<std::string> marki;                             // std::set trzyma marki posortowane

    std::ifstream plik("transport.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto pola = podziel(linia);
        std::string marka = pola[0].substr(0, pola[0].find(' '));
        marki.insert(marka);
        zestawienie[{std::stoi(pola[1]), marka}]++;
    }

    std::print("rok");
    for (const auto& marka : marki)
        std::print(" {}", marka);
    std::println();
    for (int rok = 2006; rok < 2016; rok++) {
        std::print("{}", rok);
        for (const auto& marka : marki) {
            auto it = zestawienie.find({rok, marka});
            std::print(" {}", it == zestawienie.end() ? 0 : it->second);
        }
        std::println();
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        Map<String, Integer> zestawienie = new HashMap<>();  // "rok marka" -> liczba samochodów
        TreeSet<String> marki = new TreeSet<>();             // TreeSet trzyma marki posortowane

        List<String> linie = Files.readAllLines(Path.of("transport.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            String marka = pola[0].split(" ")[0];
            marki.add(marka);
            zestawienie.merge(Integer.parseInt(pola[1]) + " " + marka, 1, Integer::sum);
        }

        var naglowek = new StringBuilder("rok");
        for (String marka : marki)
            naglowek.append(" ").append(marka);
        System.out.println(naglowek);
        for (int rok = 2006; rok < 2016; rok++) {
            var wiersz = new StringBuilder(String.valueOf(rok));
            for (String marka : marki)
                wiersz.append(" ").append(zestawienie.getOrDefault(rok + " " + marka, 0));
            System.out.println(wiersz);
        }
    }
}
```
**Odpowiedź:** np. 2006: Iveco 5; 2009: DAF 2, Iveco 2, MAN 4, Mercedes 4, Renault 2, Scania 4, Volvo 8; … (pełna tabela z programu)

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Na podstawie pliku `transport.txt` znajdź cztery samochody, dla których od daty ostatniego remontu do 1 stycznia 2017 r. upłynęło najwięcej czasu. Dla każdego podaj markę i model, numer rejestracyjny oraz liczbę dni od ostatniego remontu do 1.01.2017. Wynik zapisz w `wyniki5.txt`.

```py
from datetime import date

samochody = []

with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        r, m, d = map(int, remont.split("-"))
        dni = (date(2017, 1, 1) - date(r, m, d)).days
        samochody.append((dni, model, nr))

samochody.sort(reverse=True)
for dni, model, nr in samochody[:4]:
    print(model, nr, dni)
```

```cpp
// C++23
#include <algorithm>
#include <chrono>
#include <fstream>
#include <functional>
#include <print>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

using namespace std::chrono;

// dzieli wiersz na pola rozdzielone tabulatorem (i usuwa \r z końca)
std::vector<std::string> podziel(std::string linia) {
    if (!linia.empty() && linia.back() == '\r')
        linia.pop_back();
    std::vector<std::string> pola;
    std::stringstream ss(linia);
    std::string pole;
    while (std::getline(ss, pole, '\t'))
        pola.push_back(pole);
    return pola;
}

int main() {
    std::vector<std::tuple<int, std::string, std::string>> samochody;  // (dni, model, nr)

    std::ifstream plik("transport.txt");
    std::string linia;
    std::getline(plik, linia);  // nagłówek
    while (std::getline(plik, linia)) {
        auto pola = podziel(linia);
        std::string remont = pola[5];  // rrrr-mm-dd
        int r = std::stoi(remont.substr(0, 4));
        unsigned m = std::stoi(remont.substr(5, 2)), d = std::stoi(remont.substr(8, 2));
        sys_days data_remontu = year(r) / month(m) / day(d);
        sys_days poczatek_2017 = year(2017) / January / 1;
        int dni = (poczatek_2017 - data_remontu).count();
        samochody.push_back({dni, pola[0], pola[3]});
    }

    std::sort(samochody.begin(), samochody.end(), std::greater<>());  // malejąco
    for (int i = 0; i < 4; i++) {
        auto& [dni, model, nr] = samochody[i];
        std::println("{} {} {}", model, nr, dni);
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Zadanie {
    record Samochod(long dni, String model, String nr) {}

    public static void main(String[] args) throws Exception {
        List<Samochod> samochody = new ArrayList<>();

        List<String> linie = Files.readAllLines(Path.of("transport.txt"));
        for (String linia : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            String[] pola = linia.strip().split("\t");
            LocalDate remont = LocalDate.parse(pola[5]);
            long dni = ChronoUnit.DAYS.between(remont, LocalDate.of(2017, 1, 1));
            samochody.add(new Samochod(dni, pola[0], pola[3]));
        }

        // malejąco po (dni, model, nr) - jak sort(reverse=True) w Pythonie
        samochody.sort(Comparator.comparingLong(Samochod::dni)
                .thenComparing(Samochod::model)
                .thenComparing(Samochod::nr)
                .reversed());
        for (Samochod s : samochody.subList(0, 4))
            System.out.println(s.model() + " " + s.nr() + " " + s.dni());
    }
}
```
**Odpowiedź:** Mercedes Atego ERA 112 TR 722, Iveco Strails ERA 212 TR 708, Iveco Strails ERA 213 TR 708, Iveco Trakker Euro5 ERA 214 TR 708
