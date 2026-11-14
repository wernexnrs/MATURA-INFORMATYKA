<h1 align="center">Matura 2026 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Algorytm Szyfr szyfruje tekst jawny T[1..n] (n znaków) kluczem k (dodatnia liczba całkowita) i zapisuje szyfrogram w tablicy S[1..n]:
>
> ```
> a ← n div k
> c ← n − a
> dla i = 1, 2, ..., n wykonuj
>     jeżeli i mod k = 0
>         b ← i div k
>         S[n − a + b] ← T[i]
>     w przeciwnym razie
>         S[c] ← T[i]
>         c ← c − 1
> ```
>
> - 1.1 — Podaj szyfrogram dla tekstu `defragmentacja` z kluczem k = 3 oraz dla tekstu `tropikalny` z kluczem k = 5.
> - 1.2 — Podaj wartość klucza k, dla której szyfrogram jest zawsze identyczny z tekstem jawnym.
> - 1.3 — Podaj wartość klucza k, dla której (przy każdym n) szyfrogram jest zawsze tekstem jawnym zapisanym od końca (np. `serwer` → `rewres`); wartość może zależeć od n.

```py
def szyfr(tekst, k):
    # tablice T i S indeksowane od 1, jak w treści (pozycja 0 nieużywana)
    n = len(tekst)
    T = [""] + list(tekst)
    S = [""] * (n + 1)
    a = n // k
    c = n - a
    for i in range(1, n + 1):
        if i % k == 0:
            b = i // k
            S[n - a + b] = T[i]
        else:
            S[c] = T[i]
            c = c - 1
    return "".join(S[1:])


# 1.1
print(szyfr("defragmentacja", 3))
print(szyfr("tropikalny", 5))

# 1.2 - dla k = 1 każdy znak trafia na swoje miejsce
print(szyfr("serwer", 1))

# 1.3 - dla k > n (np. k = n + 1) warunek i mod k = 0 nigdy nie zachodzi,
# więc znaki są wpisywane od końca
print(szyfr("serwer", len("serwer") + 1))
```

```cpp
// C++23
#include <print>
#include <string>
#include <vector>

std::string szyfr(const std::string& tekst, int k) {
    // tablice T i S indeksowane od 1, jak w treści (pozycja 0 nieużywana)
    int n = tekst.size();
    std::string T = " " + tekst;
    std::string S(n + 1, ' ');
    int a = n / k;
    int c = n - a;
    for (int i = 1; i <= n; i++) {
        if (i % k == 0) {
            int b = i / k;
            S[n - a + b] = T[i];
        } else {
            S[c] = T[i];
            c = c - 1;
        }
    }
    return S.substr(1);
}

int main() {
    // 1.1
    std::println("{}", szyfr("defragmentacja", 3));
    std::println("{}", szyfr("tropikalny", 5));

    // 1.2 - dla k = 1 każdy znak trafia na swoje miejsce
    std::println("{}", szyfr("serwer", 1));

    // 1.3 - dla k > n (np. k = n + 1) warunek i mod k = 0 nigdy nie zachodzi,
    // więc znaki są wpisywane od końca
    std::println("{}", szyfr("serwer", std::string("serwer").size() + 1));
}
```

```java
// Java 25
public class Zadanie {
    static String szyfr(String tekst, int k) {
        // tablice T i S indeksowane od 1, jak w treści (pozycja 0 nieużywana)
        int n = tekst.length();
        char[] T = (" " + tekst).toCharArray();
        char[] S = new char[n + 1];
        int a = n / k;
        int c = n - a;
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                int b = i / k;
                S[n - a + b] = T[i];
            } else {
                S[c] = T[i];
                c = c - 1;
            }
        }
        return new String(S, 1, n);
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        System.out.println(szyfr("defragmentacja", 3));
        System.out.println(szyfr("tropikalny", 5));

        // 1.2 - dla k = 1 każdy znak trafia na swoje miejsce
        System.out.println(szyfr("serwer", 1));

        // 1.3 - dla k > n (np. k = n + 1) warunek i mod k = 0 nigdy nie zachodzi,
        // więc znaki są wpisywane od końca
        System.out.println(szyfr("serwer", "serwer".length() + 1));
    }
}
```

**Odpowiedź:** 1.1: defragmentacja, k = 3 → ajatemaredfgnc; tropikalny, k = 5 → nlakportiy. 1.2: k = 1. 1.3: k = n + 1 (dowolne k > n).

## 2.1 i 2.2

> **Treść zadania:** Dana jest liczba n > 1 i tablica liczb całkowitych T[1..n]. Dla 1 ≤ k < n tablica T jest k-podobna, gdy T[1..k] = T[n − k + 1..n] (początkowe k elementów jest równe końcowym k elementom); ponadto każda tablica jest 0-podobna. Przykład: [1,2,1,1,2,1,1] jest 0-, 1- i 4-podobna; [1,2,2] jest tylko 0-podobna; [2,2,2] jest 0-, 1- i 2-podobna (ale nie 3-podobna, bo k < n).
>
> - 2.1 — Dla tablic [1,2,3,4] oraz [3,5,3,5,3,5,3,5,3,5] podaj największe k, dla którego tablica jest k-podobna.
> - 2.2 — Zapisz (w pseudokodzie lub wybranym języku) algorytm, który dla n > 1 i tablicy T[1..n] wyznacza największe k, dla którego T jest k-podobna.

```py
def najwieksze_k(T):
    # T indeksowana od 0; sprawdzamy kolejne k od n - 1 w dół
    n = len(T)
    k = n - 1
    while k > 0:
        jest = True
        for i in range(k):
            if T[i] != T[n - k + i]:
                jest = False
        if jest:
            return k
        k = k - 1
    return 0


print(najwieksze_k([1, 2, 1, 1, 2, 1, 1]))  # przykład z treści: 4
print(najwieksze_k([1, 2, 3, 4]))
print(najwieksze_k([3, 5, 3, 5, 3, 5, 3, 5, 3, 5]))
```

```cpp
// C++23
#include <print>
#include <vector>

int najwieksze_k(const std::vector<int>& T) {
    // T indeksowana od 0; sprawdzamy kolejne k od n - 1 w dół
    int n = T.size();
    int k = n - 1;
    while (k > 0) {
        bool jest = true;
        for (int i = 0; i < k; i++) {
            if (T[i] != T[n - k + i]) {
                jest = false;
            }
        }
        if (jest) {
            return k;
        }
        k = k - 1;
    }
    return 0;
}

int main() {
    std::println("{}", najwieksze_k({1, 2, 1, 1, 2, 1, 1}));  // przykład z treści: 4
    std::println("{}", najwieksze_k({1, 2, 3, 4}));
    std::println("{}", najwieksze_k({3, 5, 3, 5, 3, 5, 3, 5, 3, 5}));
}
```

```java
// Java 25
public class Zadanie {
    static int najwiekszeK(int[] T) {
        // T indeksowana od 0; sprawdzamy kolejne k od n - 1 w dół
        int n = T.length;
        int k = n - 1;
        while (k > 0) {
            boolean jest = true;
            for (int i = 0; i < k; i++) {
                if (T[i] != T[n - k + i]) {
                    jest = false;
                }
            }
            if (jest) {
                return k;
            }
            k = k - 1;
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(najwiekszeK(new int[]{1, 2, 1, 1, 2, 1, 1}));  // przykład z treści: 4
        System.out.println(najwiekszeK(new int[]{1, 2, 3, 4}));
        System.out.println(najwiekszeK(new int[]{3, 5, 3, 5, 3, 5, 3, 5, 3, 5}));
    }
}
```

**Odpowiedź:** 2.1: [1,2,3,4] → 0, [3,5,3,5,3,5,3,5,3,5] → 8. 2.2: funkcja `najwieksze_k` powyżej.

> W zasadach oceniania w pierwszym wierszu tabeli do 2.1 wpisano tablicę [1,2,3,2,4] zamiast [1,2,3,4] z arkusza — wynik (0) jest dla obu taki sam.

## 3.1

> **Treść zadania:** Np-para to dwa kolejne znaki napisu, z których pierwszy stoi na pozycji nieparzystej, a drugi na parzystej (pozycje od 1): napis dzielimy na pary znaków 1–2, 3–4, 5–6… (np. w `MATURA` np-pary to MA, TU, RA). Plik `dane.txt` zawiera jeden napis parzystej długości złożony z wielkich liter alfabetu angielskiego. Odpowiedzi zapisz w pliku `wyniki3.txt`, poprzedzając każdą numerem zadania. Plik `dane_przyklad.txt` służy do testów.
>
> Podaj, ile razy zdarza się, że dwie bezpośrednio po sobie następujące np-pary są takie same. Przykład: dla `CABABC` wynik to 0, dla `ABABAB` — 2 (dwukrotnie AB, AB; pary BA nie są np-parami); dla pliku przykładowego — 2.

```py
with open("dane.txt") as file:
    napis = file.readline().strip()

pary = [napis[i:i + 2] for i in range(0, len(napis), 2)]
licznik = 0
for i in range(len(pary) - 1):
    if pary[i] == pary[i + 1]:
        licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>
#include <vector>

int main() {
    std::ifstream plik("dane.txt");
    std::string napis;
    plik >> napis;  // wczytanie słowa pomija biały znak (także '\r') - jak strip()

    std::vector<std::string> pary;
    for (size_t i = 0; i < napis.size(); i += 2) {
        pary.push_back(napis.substr(i, 2));
    }
    int licznik = 0;
    for (size_t i = 0; i + 1 < pary.size(); i++) {
        if (pary[i] == pary[i + 1]) {
            licznik += 1;
        }
    }

    std::println("{}", licznik);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        String napis = Files.readAllLines(Path.of("dane.txt")).get(0).strip();

        List<String> pary = new ArrayList<>();
        for (int i = 0; i < napis.length(); i += 2) {
            pary.add(napis.substring(i, Math.min(i + 2, napis.length())));
        }
        int licznik = 0;
        for (int i = 0; i < pary.size() - 1; i++) {
            if (pary.get(i).equals(pary.get(i + 1))) {
                licznik += 1;
            }
        }

        System.out.println(licznik);
    }
}
```

**Odpowiedź:** 17

## 3.2

> **Treść zadania:** Dane jak w zadaniu 3.1 (napis w pliku `dane.txt`, np-pary to znaki z pozycji 1–2, 3–4, …).
>
> Fragment napisu złożony z całych, kolejnych np-par jest parzyście pierwszy, jeśli suma kodów ASCII wszystkich jego znaków jest liczbą pierwszą. Podaj najdłuższy parzyście pierwszy fragment napisu z pliku (jest jeden taki). Przykład: w `NEWSROOM` fragment NEWS ma sumę 317 (liczba pierwsza), a najdłuższy taki fragment to WSROOM (suma 487); dla pliku przykładowego wynik to `FORMYKINRMRMATYKYKATYKATFO`.

```py
def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    d = 2
    while d * d <= liczba:
        if liczba % d == 0:
            return False
        d += 1
    return True


with open("dane.txt") as file:
    napis = file.readline().strip()

najdluzszy = ""
for poczatek in range(0, len(napis), 2):  # fragment zaczyna się od początku np-pary
    suma = 0
    for koniec in range(poczatek, len(napis), 2):
        suma += ord(napis[koniec]) + ord(napis[koniec + 1])
        if czy_pierwsza(suma) and koniec + 2 - poczatek > len(najdluzszy):
            najdluzszy = napis[poczatek:koniec + 2]

print(najdluzszy)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

bool czy_pierwsza(int liczba) {
    if (liczba < 2) {
        return false;
    }
    int d = 2;
    while (d * d <= liczba) {
        if (liczba % d == 0) {
            return false;
        }
        d += 1;
    }
    return true;
}

int main() {
    std::ifstream plik("dane.txt");
    std::string napis;
    plik >> napis;

    std::string najdluzszy = "";
    for (size_t poczatek = 0; poczatek < napis.size(); poczatek += 2) {  // fragment zaczyna się od początku np-pary
        int suma = 0;
        for (size_t koniec = poczatek; koniec < napis.size(); koniec += 2) {
            suma += napis[koniec] + napis[koniec + 1];  // kody ASCII liter
            if (czy_pierwsza(suma) && koniec + 2 - poczatek > najdluzszy.size()) {
                najdluzszy = napis.substr(poczatek, koniec + 2 - poczatek);
            }
        }
    }

    std::println("{}", najdluzszy);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static boolean czyPierwsza(int liczba) {
        if (liczba < 2) {
            return false;
        }
        int d = 2;
        while (d * d <= liczba) {
            if (liczba % d == 0) {
                return false;
            }
            d += 1;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        String napis = Files.readAllLines(Path.of("dane.txt")).get(0).strip();

        String najdluzszy = "";
        for (int poczatek = 0; poczatek < napis.length(); poczatek += 2) {  // fragment zaczyna się od początku np-pary
            int suma = 0;
            for (int koniec = poczatek; koniec < napis.length(); koniec += 2) {
                suma += napis.charAt(koniec) + napis.charAt(koniec + 1);  // kody ASCII liter
                if (czyPierwsza(suma) && koniec + 2 - poczatek > najdluzszy.length()) {
                    najdluzszy = napis.substring(poczatek, koniec + 2);
                }
            }
        }

        System.out.println(najdluzszy);
    }
}
```

**Odpowiedź:** INRZWZASEKYPYPYIEKDLEKODASINWNWNUPJNINEKYPDLUZASJNINYPUPWZRZ… (napis długości 544, zgodny z kluczem w całości)

## 3.3

> **Treść zadania:** Dane jak w zadaniu 3.1.
>
> Dla każdej różnej np-pary policz, ile razy występuje w napisie. Ustaw np-pary rosnąco według liczby wystąpień (żadne dwie nie mają tej samej liczby wystąpień; każdą parę zapisujemy raz) i podaj napis powstały z ich połączenia. Przykład: `RAPARA` → PA (1), RA (2) → `PARA`; `ABCABABACABA` → AB (1), CA (2), BA (3) → `ABCABA`; dla pliku przykładowego: `INFORMATYK`.

```py
with open("dane.txt") as file:
    napis = file.readline().strip()

ile = {}
for i in range(0, len(napis), 2):
    para = napis[i:i + 2]
    ile[para] = ile.get(para, 0) + 1

pary = sorted(ile, key=lambda para: ile[para])
print("".join(pary))
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
    std::ifstream plik("dane.txt");
    std::string napis;
    plik >> napis;

    // pary w kolejności pierwszego wystąpienia (jak klucze słownika w Pythonie)
    std::vector<std::pair<std::string, int>> ile;
    for (size_t i = 0; i < napis.size(); i += 2) {
        std::string para = napis.substr(i, 2);
        auto it = std::ranges::find(ile, para, &std::pair<std::string, int>::first);
        if (it == ile.end()) {
            ile.push_back({para, 1});
        } else {
            it->second += 1;
        }
    }

    // sortowanie stabilne - przy równej liczbie wystąpień zostaje kolejność pierwszego wystąpienia
    std::ranges::stable_sort(ile, {}, &std::pair<std::string, int>::second);
    std::string wynik = "";
    for (const auto& [para, liczba] : ile) {
        wynik += para;
    }
    std::println("{}", wynik);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        String napis = Files.readAllLines(Path.of("dane.txt")).get(0).strip();

        // LinkedHashMap pamięta kolejność dodawania - jak słownik w Pythonie
        Map<String, Integer> ile = new LinkedHashMap<>();
        for (int i = 0; i < napis.length(); i += 2) {
            String para = napis.substring(i, i + 2);
            ile.put(para, ile.getOrDefault(para, 0) + 1);
        }

        // List.sort jest stabilne - przy remisie zostaje kolejność pierwszego wystąpienia
        List<String> pary = new ArrayList<>(ile.keySet());
        pary.sort((p1, p2) -> Integer.compare(ile.get(p1), ile.get(p2)));
        System.out.println(String.join("", pary));
    }
}
```

**Odpowiedź:** BYLTOZIELONYUPRAWNYIURODZAJNYPASWZDLUZRZEKINIL

## 4.1, 4.2 i 4.3

> **Treść zadania:** Miasta leżą w punktach o współrzędnych całkowitych; drogi biegną tylko w kierunkach północ–południe i wschód–zachód, więc odległość miast (x1, y1) i (x2, y2) to d = |x1 − x2| + |y1 − y2|. Plik `mapa.txt` zawiera dane 1000 miast; i-ty wiersz opisuje miasto nr i: wspX i wspY (liczby całkowite z [−250, 250]) oraz liczbę mieszkańców w tysiącach (od 1 do 50000), oddzielone spacjami. Odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając każdą numerem zadania. Plik `mapa_przyklad.txt` (50 miast) służy do testów.
>
> - 4.1 — Podaj numer miasta o największej liczbie mieszkańców i tę liczbę (w tysiącach); jest jedno takie miasto (dla pliku przykładowego: `10 48967`).
> - 4.2 — Podaj najmniejszą odległość między dwoma miastami oraz wszystkie pary numerów miast (każdą parę raz, w osobnym wierszu), które dzieli ta odległość (dla pliku przykładowego: 7, pary 14 15 oraz 27 32).
> - 4.3 — Aglomeracja to największy kwadrat o lewym dolnym rogu w (0, 0), prawym górnym rogu o dodatnich współrzędnych całkowitych i bokach równoległych do osi, którego gęstość zaludnienia jest większa od 2. Gęstość to suma mieszkańców miast leżących ściśle wewnątrz kwadratu (bez brzegów) podzielona przez jego pole. Podaj długość boku aglomeracji i łączną liczbę jej mieszkańców (dla pliku przykładowego: `94 17674`).

```py
miasta = []  # (x, y, wielkosc); miasto nr i ma indeks i - 1
with open("mapa.txt") as file:
    for linia in file:
        x, y, wielkosc = map(int, linia.split())
        miasta.append((x, y, wielkosc))
n = len(miasta)

# 4.1
numer = 0
for i in range(n):
    if miasta[i][2] > miasta[numer][2]:
        numer = i
print("4.1", numer + 1, miasta[numer][2])

# 4.2
najmniejsza = 10 ** 9
pary = []
for i in range(n):
    for j in range(i + 1, n):
        d = abs(miasta[i][0] - miasta[j][0]) + abs(miasta[i][1] - miasta[j][1])
        if d < najmniejsza:
            najmniejsza = d
            pary = [(i + 1, j + 1)]
        elif d == najmniejsza:
            pary.append((i + 1, j + 1))
print("4.2", najmniejsza)
for a, b in pary:
    print(a, b)

# 4.3 - kwadrat (0,0)-(bok,bok), liczymy tylko miasta leżące wewnątrz
najwiekszy_bok = 0
for bok in range(1, 501):
    ludnosc = 0
    for x, y, wielkosc in miasta:
        if 0 < x < bok and 0 < y < bok:
            ludnosc += wielkosc
    if ludnosc / (bok * bok) > 2:
        najwiekszy_bok = bok
        najwieksza_ludnosc = ludnosc
print("4.3", najwiekszy_bok, najwieksza_ludnosc)
```

```cpp
// C++23
#include <cstdlib>
#include <fstream>
#include <print>
#include <utility>
#include <vector>

struct Miasto {
    int x, y, wielkosc;
};

int main() {
    std::vector<Miasto> miasta;  // miasto nr i ma indeks i - 1
    std::ifstream plik("mapa.txt");
    int x, y, wielkosc;
    while (plik >> x >> y >> wielkosc) {
        miasta.push_back({x, y, wielkosc});
    }
    int n = miasta.size();

    // 4.1
    int numer = 0;
    for (int i = 0; i < n; i++) {
        if (miasta[i].wielkosc > miasta[numer].wielkosc) {
            numer = i;
        }
    }
    std::println("4.1 {} {}", numer + 1, miasta[numer].wielkosc);

    // 4.2
    int najmniejsza = 1000000000;
    std::vector<std::pair<int, int>> pary;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int d = std::abs(miasta[i].x - miasta[j].x) + std::abs(miasta[i].y - miasta[j].y);
            if (d < najmniejsza) {
                najmniejsza = d;
                pary = {{i + 1, j + 1}};
            } else if (d == najmniejsza) {
                pary.push_back({i + 1, j + 1});
            }
        }
    }
    std::println("4.2 {}", najmniejsza);
    for (auto [a, b] : pary) {
        std::println("{} {}", a, b);
    }

    // 4.3 - kwadrat (0,0)-(bok,bok), liczymy tylko miasta leżące wewnątrz
    int najwiekszy_bok = 0;
    int najwieksza_ludnosc = 0;
    for (int bok = 1; bok <= 500; bok++) {
        int ludnosc = 0;
        for (const Miasto& m : miasta) {
            if (0 < m.x && m.x < bok && 0 < m.y && m.y < bok) {
                ludnosc += m.wielkosc;
            }
        }
        if ((double)ludnosc / (bok * bok) > 2) {
            najwiekszy_bok = bok;
            najwieksza_ludnosc = ludnosc;
        }
    }
    std::println("4.3 {} {}", najwiekszy_bok, najwieksza_ludnosc);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    record Miasto(int x, int y, int wielkosc) {}

    public static void main(String[] args) throws Exception {
        List<Miasto> miasta = new ArrayList<>();  // miasto nr i ma indeks i - 1
        for (String linia : Files.readAllLines(Path.of("mapa.txt"))) {
            if (linia.isBlank()) {
                continue;
            }
            String[] t = linia.trim().split("\\s+");
            miasta.add(new Miasto(Integer.parseInt(t[0]), Integer.parseInt(t[1]), Integer.parseInt(t[2])));
        }
        int n = miasta.size();

        // 4.1
        int numer = 0;
        for (int i = 0; i < n; i++) {
            if (miasta.get(i).wielkosc() > miasta.get(numer).wielkosc()) {
                numer = i;
            }
        }
        System.out.println("4.1 " + (numer + 1) + " " + miasta.get(numer).wielkosc());

        // 4.2
        int najmniejsza = 1000000000;
        List<int[]> pary = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                Miasto a = miasta.get(i), b = miasta.get(j);
                int d = Math.abs(a.x() - b.x()) + Math.abs(a.y() - b.y());
                if (d < najmniejsza) {
                    najmniejsza = d;
                    pary.clear();
                    pary.add(new int[]{i + 1, j + 1});
                } else if (d == najmniejsza) {
                    pary.add(new int[]{i + 1, j + 1});
                }
            }
        }
        System.out.println("4.2 " + najmniejsza);
        for (int[] p : pary) {
            System.out.println(p[0] + " " + p[1]);
        }

        // 4.3 - kwadrat (0,0)-(bok,bok), liczymy tylko miasta leżące wewnątrz
        int najwiekszyBok = 0;
        int najwiekszaLudnosc = 0;
        for (int bok = 1; bok <= 500; bok++) {
            int ludnosc = 0;
            for (Miasto m : miasta) {
                if (0 < m.x() && m.x() < bok && 0 < m.y() && m.y() < bok) {
                    ludnosc += m.wielkosc();
                }
            }
            if ((double) ludnosc / (bok * bok) > 2) {
                najwiekszyBok = bok;
                najwiekszaLudnosc = ludnosc;
            }
        }
        System.out.println("4.3 " + najwiekszyBok + " " + najwiekszaLudnosc);
    }
}
```

**Odpowiedź:** 4.1: 254 2483; 4.2: odległość 2, pary: 30 170, 120 176, 422 637, 426 599, 737 778; 4.3: 114 26078.

## 5

> **Treść zadania:** Uzupełnij brakujące liczby tak, aby obie równości były prawdziwe: 1251₆ + …₆ = 500₁₀ = …₃ − 110102₃ (pierwsza luka w systemie szóstkowym, druga w trójkowym).

```py
def na_system(liczba, podstawa):
    cyfry = ""
    while liczba > 0:
        cyfry = str(liczba % podstawa) + cyfry
        liczba //= podstawa
    return cyfry


# 1251(6) + x(6) = 500(10) = y(3) - 110102(3)
x = 500 - int("1251", 6)
y = 500 + int("110102", 3)
print(na_system(x, 6), na_system(y, 3))
```

```cpp
// C++23
#include <print>
#include <string>

std::string na_system(int liczba, int podstawa) {
    std::string cyfry = "";
    while (liczba > 0) {
        cyfry = std::to_string(liczba % podstawa) + cyfry;
        liczba /= podstawa;
    }
    return cyfry;
}

int main() {
    // 1251(6) + x(6) = 500(10) = y(3) - 110102(3)
    // std::stoi(napis, nullptr, podstawa) działa jak int(napis, podstawa) w Pythonie
    int x = 500 - std::stoi("1251", nullptr, 6);
    int y = 500 + std::stoi("110102", nullptr, 3);
    std::println("{} {}", na_system(x, 6), na_system(y, 3));
}
```

```java
// Java 25
public class Zadanie {
    static String naSystem(int liczba, int podstawa) {
        String cyfry = "";
        while (liczba > 0) {
            cyfry = (liczba % podstawa) + cyfry;
            liczba /= podstawa;
        }
        return cyfry;
    }

    public static void main(String[] args) throws Exception {
        // 1251(6) + x(6) = 500(10) = y(3) - 110102(3)
        // Integer.parseInt(napis, podstawa) działa jak int(napis, podstawa) w Pythonie
        int x = 500 - Integer.parseInt("1251", 6);
        int y = 500 + Integer.parseInt("110102", 3);
        System.out.println(naSystem(x, 6) + " " + naSystem(y, 3));
    }
}
```

**Odpowiedź:** (1251)₆ + (501)₆ = (500)₁₀ = (1010221)₃ − (110102)₃
