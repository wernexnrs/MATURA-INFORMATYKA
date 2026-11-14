<h1 align="center">Matura 2020 — lipiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Zadanie 1 (analiza algorytmu). Dla liczby całkowitej `n > 1` algorytm wypełnia tablice `P` i `S`:
>
> ```
> dla i = 1, 2, ..., n wykonuj
>     P[i] ← 1
>     S[i] ← 0
> dla j = 2, 3, ..., n wykonuj
>     jeżeli P[j] = 1
>         i ← j * j
>         dopóki i ≤ n wykonuj
>             P[i] ← 0
>             i ← i + j
>     S[j] ← S[j-1] + P[j]
> ```
>
> - 1.1 — dla `n = 10` podaj wartości `P[1]`, …, `P[10]`.
> - 1.2 — dla `n = 10` podaj wartości `S[1]`, …, `S[10]`.
> - 1.3 — dokończ zdanie: dla `1 < a ≤ b ≤ n` wartość `S[b] − S[a−1]` jest równa: A. liczbie dzielników pierwszych liczby `b − a`; B. liczbie liczb pierwszych w przedziale `[a, b]`; C. NWD liczb `a` i `b`; D. liczbie liczb pierwszych w przedziale `[a − 1, b]`.

```py
n = 10
P = [0] * (n + 1)  # indeksy 1..n, jak w treści
S = [0] * (n + 1)

for i in range(1, n + 1):
    P[i] = 1
    S[i] = 0

# sito Eratostenesa: P[j] = 1 dla liczb pierwszych (oraz dla 1, której pętla nie rusza)
for j in range(2, n + 1):
    if P[j] == 1:
        i = j * j
        while i <= n:
            P[i] = 0
            i = i + j
    # S[j] - ile liczb pierwszych jest w przedziale [2, j]
    S[j] = S[j - 1] + P[j]

print(P[1:])
print(S[1:])

# 1.3 - S[b] - S[a - 1] = suma P[a..b], a > 1, więc to liczba liczb pierwszych w [a, b]
a, b = 3, 10
print(S[b] - S[a - 1])
```

```cpp
// C++23
#include <print>
#include <vector>

int main() {
    int n = 10;
    std::vector<int> P(n + 1, 0);  // indeksy 1..n, jak w treści
    std::vector<int> S(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        P[i] = 1;
        S[i] = 0;
    }

    // sito Eratostenesa: P[j] = 1 dla liczb pierwszych (oraz dla 1, której pętla nie rusza)
    for (int j = 2; j <= n; j++) {
        if (P[j] == 1) {
            int i = j * j;
            while (i <= n) {
                P[i] = 0;
                i = i + j;
            }
        }
        // S[j] - ile liczb pierwszych jest w przedziale [2, j]
        S[j] = S[j - 1] + P[j];
    }

    std::println("{}", std::vector<int>(P.begin() + 1, P.end()));
    std::println("{}", std::vector<int>(S.begin() + 1, S.end()));

    // 1.3 - S[b] - S[a - 1] = suma P[a..b], a > 1, więc to liczba liczb pierwszych w [a, b]
    int a = 3, b = 10;
    std::println("{}", S[b] - S[a - 1]);
}
```

```java
// Java 25
import java.util.Arrays;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int n = 10;
        int[] P = new int[n + 1];  // indeksy 1..n, jak w treści
        int[] S = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            P[i] = 1;
            S[i] = 0;
        }

        // sito Eratostenesa: P[j] = 1 dla liczb pierwszych (oraz dla 1, której pętla nie rusza)
        for (int j = 2; j <= n; j++) {
            if (P[j] == 1) {
                int i = j * j;
                while (i <= n) {
                    P[i] = 0;
                    i = i + j;
                }
            }
            // S[j] - ile liczb pierwszych jest w przedziale [2, j]
            S[j] = S[j - 1] + P[j];
        }

        System.out.println(Arrays.toString(Arrays.copyOfRange(P, 1, n + 1)));
        System.out.println(Arrays.toString(Arrays.copyOfRange(S, 1, n + 1)));

        // 1.3 - S[b] - S[a - 1] = suma P[a..b], a > 1, więc to liczba liczb pierwszych w [a, b]
        int a = 3, b = 10;
        System.out.println(S[b] - S[a - 1]);
    }
}
```
**Odpowiedź:** 1.1: P = 1, 1, 1, 0, 1, 0, 1, 0, 0, 0; 1.2: S = 0, 1, 2, 2, 3, 3, 4, 4, 4, 4; 1.3: B (liczba liczb pierwszych w przedziale [a, b])

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2 (ułamki egipskie). Ułamek egipski to ułamek postaci `1/m`, gdzie `m > 1` jest całkowite. Każdą dodatnią liczbę wymierną `a < 1` można przedstawić jako sumę ułamków egipskich o różnych mianownikach. Metoda rozkładu:
> 1. Znajdź najmniejszą liczbę całkowitą `n` nie mniejszą od `1/a`; `1/n` jest największym ułamkiem egipskim w rozkładzie `a`.
> 2. Oblicz `r = a − 1/n`. Jeśli `r = 0`, rozkład jest gotowy; w przeciwnym razie tą samą metodą rozłóż `r` i dopisz jego składniki do rozkładu `a`.
>
> Przykład: `4/5 = 1/2 + 1/4 + 1/20`.
>
> - 2.1 — wyznacz tą metodą rozkłady liczb `8/15` i `5/6`.
> - 2.2 — napisz algorytm, który dla liczby `a = p/q` (`p`, `q` całkowite dodatnie, `p < q`) wypisze rosnący ciąg różnych mianowników `m1 < m2 < … < mk` takich, że `p/q = 1/m1 + 1/m2 + … + 1/mk` (dla `p = 4`, `q = 5`: 2, 4, 20). Wolno używać tylko operacji arytmetycznych (w tym div i mod), porównań, wypisywania, instrukcji sterujących, przypisań, własnych funkcji oraz funkcji sufit.

```py
def rozklad(p, q):
    # rozkład p/q (p < q) na sumę ułamków egipskich - zwraca mianowniki
    mianowniki = []
    while p > 0:
        m = (q + p - 1) // p  # sufit z q/p - najmniejsze m, dla którego 1/m <= p/q
        mianowniki.append(m)
        # p/q - 1/m = (p*m - q) / (q*m)
        p, q = p * m - q, q * m
    return mianowniki


print(rozklad(8, 15))
print(rozklad(5, 6))
print(rozklad(4, 5))
```

```cpp
// C++23
#include <print>
#include <vector>

std::vector<long long> rozklad(long long p, long long q) {
    // rozkład p/q (p < q) na sumę ułamków egipskich - zwraca mianowniki
    std::vector<long long> mianowniki;
    while (p > 0) {
        long long m = (q + p - 1) / p;  // sufit z q/p - najmniejsze m, dla którego 1/m <= p/q
        mianowniki.push_back(m);
        // p/q - 1/m = (p*m - q) / (q*m)
        long long nowe_p = p * m - q;
        q = q * m;
        p = nowe_p;
    }
    return mianowniki;
}

int main() {
    std::println("{}", rozklad(8, 15));
    std::println("{}", rozklad(5, 6));
    std::println("{}", rozklad(4, 5));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    static List<Long> rozklad(long p, long q) {
        // rozkład p/q (p < q) na sumę ułamków egipskich - zwraca mianowniki
        var mianowniki = new ArrayList<Long>();
        while (p > 0) {
            long m = (q + p - 1) / p;  // sufit z q/p - najmniejsze m, dla którego 1/m <= p/q
            mianowniki.add(m);
            // p/q - 1/m = (p*m - q) / (q*m)
            long noweP = p * m - q;
            q = q * m;
            p = noweP;
        }
        return mianowniki;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(rozklad(8, 15));
        System.out.println(rozklad(5, 6));
        System.out.println(rozklad(4, 5));
    }
}
```
**Odpowiedź:** 2.1: 8/15 = 1/2 + 1/30; 5/6 = 1/2 + 1/3. 2.2: algorytm powyżej (dla 4/5: 2, 4, 20)

## 4.1, 4.2 i 4.3

> **Treść zadania:** Zadanie 4 (dokumenty). Plik `identyfikator.txt` zawiera 200 wierszy; w każdym identyfikator dokumentu złożony z serii (trzy wielkie litery alfabetu łacińskiego) i sześciu cyfr, np. `CIS459437` (dane przykładowe: `identyfikator_przyklad.txt`, 20 wierszy). Wyniki zapisuj po jednym identyfikatorze w wierszu, w kolejności z pliku.
>
> - 4.1 — podaj identyfikatory o największej sumie cyfr części numerycznej; wynik zapisz w pliku `wyniki4_1.txt` (dla przykładu: `CHY728985`).
> - 4.2 — podaj identyfikatory, których seria lub numer jest palindromem; wynik zapisz w pliku `wyniki4_2.txt` (dla przykładu: `KOK201272`, `PIP417543`, `MOS302203`).
> - 4.3 — pierwsza cyfra numeru jest cyfrą kontrolną. Litery serii zamieniamy na liczby A=10, B=11, …, Z=35; wartości pozostałych ośmiu elementów (trzy litery i pięć cyfr po cyfrze kontrolnej) mnożymy kolejno przez wagi 7, 3, 1, 7, 3, 1, 7, 3, sumujemy i bierzemy resztę z dzielenia przez 10. Identyfikator jest poprawny, gdy wynik jest równy cyfrze kontrolnej (np. dla `CIS459437` suma wynosi 274, 274 mod 10 = 4). Podaj wszystkie niepoprawne identyfikatory; wynik zapisz w pliku `wyniki4_3.txt` (dla przykładu: `NHO307984`, `SEH422297`, `MOS302203`).

```py
identyfikatory = []
with open("identyfikator.txt") as file:
    for line in file:
        identyfikatory.append(line.strip())


def suma_cyfr(liczba):
    suma = 0
    for c in liczba:
        suma += int(c)
    return suma


# 4.1
najwieksza = max(suma_cyfr(x[3:]) for x in identyfikatory)
with open("wyniki4_1.txt", "w") as wynik:
    for x in identyfikatory:
        if suma_cyfr(x[3:]) == najwieksza:
            print(x, file=wynik)

# 4.2
with open("wyniki4_2.txt", "w") as wynik:
    for x in identyfikatory:
        seria, numer = x[:3], x[3:]
        if seria == seria[::-1] or numer == numer[::-1]:
            print(x, file=wynik)

# 4.3
wagi = [7, 3, 1, 7, 3, 1, 7, 3]


def czy_poprawny(x):
    # litery A..Z -> 10..35, cyfra kontrolna x[3] pomijana
    wartosci = []
    for c in x[:3]:
        wartosci.append(ord(c) - ord("A") + 10)
    for c in x[4:]:
        wartosci.append(int(c))
    suma = 0
    for i in range(len(wagi)):
        suma += wagi[i] * wartosci[i]
    return suma % 10 == int(x[3])


with open("wyniki4_3.txt", "w") as wynik:
    for x in identyfikatory:
        if not czy_poprawny(x):
            print(x, file=wynik)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <vector>

int suma_cyfr(const std::string& liczba) {
    int suma = 0;
    for (char c : liczba)
        suma += c - '0';
    return suma;
}

bool czy_palindrom(const std::string& s) {
    return s == std::string(s.rbegin(), s.rend());
}

const std::vector<int> wagi = {7, 3, 1, 7, 3, 1, 7, 3};

bool czy_poprawny(const std::string& x) {
    // litery A..Z -> 10..35, cyfra kontrolna x[3] pomijana
    std::vector<int> wartosci;
    for (int i = 0; i < 3; i++)
        wartosci.push_back(x[i] - 'A' + 10);
    for (size_t i = 4; i < x.size(); i++)
        wartosci.push_back(x[i] - '0');
    int suma = 0;
    for (size_t i = 0; i < wagi.size(); i++)
        suma += wagi[i] * wartosci[i];
    return suma % 10 == x[3] - '0';
}

int main() {
    std::vector<std::string> identyfikatory;
    std::ifstream plik("identyfikator.txt");
    std::string linia;
    while (plik >> linia)
        identyfikatory.push_back(linia);

    // 4.1
    int najwieksza = 0;
    for (const auto& x : identyfikatory)
        najwieksza = std::max(najwieksza, suma_cyfr(x.substr(3)));
    std::ofstream wynik1("wyniki4_1.txt");
    for (const auto& x : identyfikatory)
        if (suma_cyfr(x.substr(3)) == najwieksza)
            std::println(wynik1, "{}", x);

    // 4.2
    std::ofstream wynik2("wyniki4_2.txt");
    for (const auto& x : identyfikatory) {
        std::string seria = x.substr(0, 3), numer = x.substr(3);
        if (czy_palindrom(seria) || czy_palindrom(numer))
            std::println(wynik2, "{}", x);
    }

    // 4.3
    std::ofstream wynik3("wyniki4_3.txt");
    for (const auto& x : identyfikatory)
        if (!czy_poprawny(x))
            std::println(wynik3, "{}", x);
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

public class Zadanie {
    static int sumaCyfr(String liczba) {
        int suma = 0;
        for (char c : liczba.toCharArray())
            suma += c - '0';
        return suma;
    }

    static boolean czyPalindrom(String s) {
        return s.equals(new StringBuilder(s).reverse().toString());
    }

    static final int[] wagi = {7, 3, 1, 7, 3, 1, 7, 3};

    static boolean czyPoprawny(String x) {
        // litery A..Z -> 10..35, cyfra kontrolna x[3] pomijana
        var wartosci = new ArrayList<Integer>();
        for (int i = 0; i < 3; i++)
            wartosci.add(x.charAt(i) - 'A' + 10);
        for (int i = 4; i < x.length(); i++)
            wartosci.add(x.charAt(i) - '0');
        int suma = 0;
        for (int i = 0; i < wagi.length; i++)
            suma += wagi[i] * wartosci.get(i);
        return suma % 10 == x.charAt(3) - '0';
    }

    public static void main(String[] args) throws Exception {
        var identyfikatory = new ArrayList<String>();
        for (String line : Files.readAllLines(Path.of("identyfikator.txt")))
            if (!line.isBlank())
                identyfikatory.add(line.strip());

        // 4.1
        int najwieksza = 0;
        for (String x : identyfikatory)
            najwieksza = Math.max(najwieksza, sumaCyfr(x.substring(3)));
        try (var wynik = new PrintWriter("wyniki4_1.txt")) {
            for (String x : identyfikatory)
                if (sumaCyfr(x.substring(3)) == najwieksza)
                    wynik.println(x);
        }

        // 4.2
        try (var wynik = new PrintWriter("wyniki4_2.txt")) {
            for (String x : identyfikatory) {
                String seria = x.substring(0, 3), numer = x.substring(3);
                if (czyPalindrom(seria) || czyPalindrom(numer))
                    wynik.println(x);
            }
        }

        // 4.3
        try (var wynik = new PrintWriter("wyniki4_3.txt")) {
            for (String x : identyfikatory)
                if (!czyPoprawny(x))
                    wynik.println(x);
        }
    }
}
```
**Odpowiedź:** 4.1: GYJ959787, JOK786969 (suma cyfr 45). 4.2: MBF340043, JKJ452719, GFG148345, AXA231829, KIK866983, LOL695279. 4.3: LIK235378, MBF340043, HFG378931, KIJ511146, NUK840936, OKH427482, RTS278686
