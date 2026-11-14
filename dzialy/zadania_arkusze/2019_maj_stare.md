<h1 align="center">Matura 2019 — maj, poziom rozszerzony (stara formuła)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.3

> **Treść zadania:** Zadanie 1 (dwie tablice). Dla dodatniej liczby całkowitej `n` i tablicy liczb całkowitych `A[1..n]` algorytm oblicza tablicę `C[1..n]`:
>
> ```
> dla i = 1, 2, ..., n:
>     C[i] = 1
>     dla j = 1, 2, ..., i-1:
>         jeśli A[j] < A[i] oraz C[j] + 1 > C[i]:
>             C[i] = C[j] + 1
> ```
>
> - 1.1 — podaj zawartość tablicy `C` dla tablic `A`: `[1,2,3,4]`, `[1,3,2,5]`, `[3,5,1,4,6,7,2,10,9,11]`, `[3,1,4,2,6,5,7]` (dla przykładu: `[4,2,3,1,5]` → `[1,1,2,1,3]`, `[3,3,3,3]` → `[1,1,1,1]`).
> - 1.3 — podaj przykładową ośmioelementową tablicę `A`, dla której w tablicy `C` co najmniej raz pojawi się liczba 6, ale nie pojawi się liczba 7.

```py
def oblicz_C(A):
    n = len(A)
    C = [0] * n
    for i in range(n):
        C[i] = 1
        for j in range(i):
            if A[j] < A[i] and C[j] + 1 > C[i]:
                C[i] = C[j] + 1
    return C


# 1.1
for A in [[4, 2, 3, 1, 5], [3, 3, 3, 3], [1, 2, 3, 4], [1, 3, 2, 5],
          [3, 5, 1, 4, 6, 7, 2, 10, 9, 11], [3, 1, 4, 2, 6, 5, 7]]:
    print(A, oblicz_C(A))

# 1.3 - C[i] to długość najdłuższego rosnącego podciągu kończącego się na A[i],
# więc potrzebny jest rosnący podciąg długości 6, ale nie 7
A = [1, 2, 3, 4, 5, 6, 1, 1]
print(A, oblicz_C(A), max(oblicz_C(A)))
```

```cpp
// C++23
#include <algorithm>
#include <print>
#include <vector>

std::vector<int> oblicz_C(const std::vector<int>& A) {
    int n = A.size();
    std::vector<int> C(n, 0);
    for (int i = 0; i < n; i++) {
        C[i] = 1;
        for (int j = 0; j < i; j++)
            if (A[j] < A[i] && C[j] + 1 > C[i])
                C[i] = C[j] + 1;
    }
    return C;
}

int main() {
    // 1.1
    std::vector<std::vector<int>> tablice = {{4, 2, 3, 1, 5}, {3, 3, 3, 3}, {1, 2, 3, 4}, {1, 3, 2, 5},
                                             {3, 5, 1, 4, 6, 7, 2, 10, 9, 11}, {3, 1, 4, 2, 6, 5, 7}};
    for (const auto& A : tablice)
        std::println("{} {}", A, oblicz_C(A));

    // 1.3 - C[i] to długość najdłuższego rosnącego podciągu kończącego się na A[i],
    // więc potrzebny jest rosnący podciąg długości 6, ale nie 7
    std::vector<int> A = {1, 2, 3, 4, 5, 6, 1, 1};
    std::println("{} {} {}", A, oblicz_C(A), std::ranges::max(oblicz_C(A)));
}
```

```java
// Java 25
import java.util.Arrays;

public class Zadanie {
    static int[] obliczC(int[] A) {
        int n = A.length;
        int[] C = new int[n];
        for (int i = 0; i < n; i++) {
            C[i] = 1;
            for (int j = 0; j < i; j++)
                if (A[j] < A[i] && C[j] + 1 > C[i])
                    C[i] = C[j] + 1;
        }
        return C;
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        int[][] tablice = {{4, 2, 3, 1, 5}, {3, 3, 3, 3}, {1, 2, 3, 4}, {1, 3, 2, 5},
                           {3, 5, 1, 4, 6, 7, 2, 10, 9, 11}, {3, 1, 4, 2, 6, 5, 7}};
        for (int[] A : tablice)
            System.out.println(Arrays.toString(A) + " " + Arrays.toString(obliczC(A)));

        // 1.3 - C[i] to długość najdłuższego rosnącego podciągu kończącego się na A[i],
        // więc potrzebny jest rosnący podciąg długości 6, ale nie 7
        int[] A = {1, 2, 3, 4, 5, 6, 1, 1};
        int[] C = obliczC(A);
        System.out.println(Arrays.toString(A) + " " + Arrays.toString(C) + " " + Arrays.stream(C).max().getAsInt());
    }
}
```

**Odpowiedź:** 1.1: [1,2,3,4] → [1,2,3,4], [1,3,2,5] → [1,2,2,3], [3,5,1,4,6,7,2,10,9,11] → [1,2,1,2,3,4,2,5,5,6], [3,1,4,2,6,5,7] → [1,1,2,2,3,3,4]. 1.3: np. [1,2,3,4,5,6,1,1] (rosnący podciąg długości 6, brak rosnącego podciągu długości 7).

> W kluczu w wierszu trzecim tablicy A wpisano omyłkowo [6,5,1,4,6,7,2,10,9,11] zamiast [3,5,1,4,6,7,2,10,9,11] z arkusza; podana tablica C ([1,2,1,2,3,4,2,5,5,6]) odpowiada tablicy z arkusza.

## 2.1, 2.2 i 2.3

> **Treść zadania:** Zadanie 2 (test pierwszości). We wszystkich podpunktach wolno używać tylko dodawania, odejmowania, mnożenia, dzielenia, dzielenia całkowitego, reszty z dzielenia oraz własnych funkcji (i funkcji z wcześniejszych podpunktów).
>
> - 2.1 — napisz funkcję `pot(a, k)`, której wynikiem jest `a^k mod k` dla liczb naturalnych `2 ≤ a < k`.
> - 2.2 — test Fermata: liczba całkowita `k > 2` jest prawdopodobnie pierwsza, jeśli dla każdego całkowitego `a`, `2 ≤ a < k`, zachodzi `a^k mod k = a`. Napisz funkcję `testF(k)` zwracającą 1, gdy `k` jest prawdopodobnie pierwsza, i 0 w przeciwnym razie (możesz użyć `pot`).
> - 2.3 — liczby Carmichaela to liczby złożone, które są prawdopodobnie pierwsze. Napisz funkcję `czyLC(k)` (`k > 2`) zwracającą 1, gdy `k` jest liczbą Carmichaela, i 0 w przeciwnym razie (możesz użyć `testF`).

```py
def pot(a, k):
    # a^k mod k - po każdym mnożeniu bierzemy resztę, żeby liczby nie rosły
    p = 1
    for i in range(k):
        p = p * a % k
    return p


def testF(k):
    for a in range(2, k):
        if pot(a, k) != a:
            return 0
    return 1


def czy_pierwsza(k):
    if k < 2:
        return 0
    d = 2
    while d * d <= k:
        if k % d == 0:
            return 0
        d += 1
    return 1


def czyLC(k):
    # liczba Carmichaela = złożona, ale przechodzi test Fermata
    if testF(k) == 1 and czy_pierwsza(k) == 0:
        return 1
    return 0


print(pot(3, 7), testF(7), testF(9))
print([k for k in range(3, 3000) if czyLC(k) == 1])
```

```cpp
// C++23
#include <print>
#include <vector>

long long pot(long long a, long long k) {
    // a^k mod k - po każdym mnożeniu bierzemy resztę, żeby liczby nie rosły
    long long p = 1;
    for (long long i = 0; i < k; i++)
        p = p * a % k;
    return p;
}

int testF(long long k) {
    for (long long a = 2; a < k; a++)
        if (pot(a, k) != a)
            return 0;
    return 1;
}

int czy_pierwsza(long long k) {
    if (k < 2)
        return 0;
    long long d = 2;
    while (d * d <= k) {
        if (k % d == 0)
            return 0;
        d++;
    }
    return 1;
}

int czyLC(long long k) {
    // liczba Carmichaela = złożona, ale przechodzi test Fermata
    if (testF(k) == 1 && czy_pierwsza(k) == 0)
        return 1;
    return 0;
}

int main() {
    std::println("{} {} {}", pot(3, 7), testF(7), testF(9));
    std::vector<int> carmichael;
    for (int k = 3; k < 3000; k++)
        if (czyLC(k) == 1)
            carmichael.push_back(k);
    std::println("{}", carmichael);
}
```

```java
// Java 25
import java.util.ArrayList;

public class Zadanie {
    static long pot(long a, long k) {
        // a^k mod k - po każdym mnożeniu bierzemy resztę, żeby liczby nie rosły
        long p = 1;
        for (long i = 0; i < k; i++)
            p = p * a % k;
        return p;
    }

    static int testF(long k) {
        for (long a = 2; a < k; a++)
            if (pot(a, k) != a)
                return 0;
        return 1;
    }

    static int czyPierwsza(long k) {
        if (k < 2)
            return 0;
        long d = 2;
        while (d * d <= k) {
            if (k % d == 0)
                return 0;
            d++;
        }
        return 1;
    }

    static int czyLC(long k) {
        // liczba Carmichaela = złożona, ale przechodzi test Fermata
        if (testF(k) == 1 && czyPierwsza(k) == 0)
            return 1;
        return 0;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(pot(3, 7) + " " + testF(7) + " " + testF(9));
        var carmichael = new ArrayList<Integer>();
        for (int k = 3; k < 3000; k++)
            if (czyLC(k) == 1)
                carmichael.add(k);
        System.out.println(carmichael);
    }
}
```

**Odpowiedź:** funkcje `pot`, `testF` i `czyLC`; sprawdzenie: pot(3, 7) = 3, testF(7) = 1, testF(9) = 0, liczby Carmichaela < 3000: 561, 1105, 1729, 2465, 2821.

## 4.1, 4.2 i 4.3

> **Treść zadania:** Zadanie 4 (działki). Plik `dzialki.txt` zawiera 50 map kwadratowych działek 30×30; każda mapa to 30 wierszy po 30 znaków, a po każdej mapie jest jeden pusty wiersz. Działki numerujemy w kolejności z pliku. Znak `.` oznacza pole puste, `*` — pole porośnięte trawą, `X` — przeszkodę terenową. Odpowiedzi zapisz w pliku `wynik4.txt`, poprzedzając je numerem zadania (dane przykładowe: `przyklad.txt`, 5 map).
>
> - 4.1 — podaj, ile działek ma co najmniej 70% powierzchni porośniętej trawą (dla przykładu: 1).
> - 4.2 — są dwie działki, których mapy są identyczne po obróceniu jednej z nich o 180°. Podaj ich numery (dla przykładu: 2 i 3).
> - 4.3 — w lewym górnym (północno-zachodnim) rogu działki trzeba wytyczyć kwadratowy plac bez przeszkód (tylko pola `.` i `*`). Znajdź działkę, na której zmieści się taki plac o największej powierzchni; podaj jej numer i długość boku placu, a jeśli takich działek jest kilka — numery wszystkich (dla przykładu: działka 4, bok 7).

```py
mapy = []
with open("dzialki.txt") as file:
    wiersze = [line.strip() for line in file if line.strip() != ""]
for m in range(len(wiersze) // 30):
    mapy.append(wiersze[30 * m: 30 * m + 30])

# 4.1
ile = 0
for mapa in mapy:
    trawa = 0
    for wiersz in mapa:
        trawa += wiersz.count("*")
    if trawa >= 0.7 * 30 * 30:
        ile += 1
print("4.1", ile)


# 4.2 - obrót o 180 stopni: odwracamy kolejność wierszy i każdy wiersz
def obrot(mapa):
    return [wiersz[::-1] for wiersz in mapa[::-1]]


print("4.2", end=" ")
for i in range(len(mapy)):
    for j in range(i + 1, len(mapy)):
        if obrot(mapy[i]) == mapy[j]:
            print(i + 1, j + 1, end=" ")
print()


# 4.3
def najwiekszy_plac(mapa):
    bok = 0
    # kwadrat o boku bok + 1 mieści się, gdy w wierszach i kolumnach 0..bok nie ma X
    while bok < 30:
        dobry = True
        for i in range(bok + 1):
            for j in range(bok + 1):
                if mapa[i][j] == "X":
                    dobry = False
        if not dobry:
            break
        bok += 1
    return bok


boki = [najwiekszy_plac(mapa) for mapa in mapy]
najwiekszy = max(boki)
print("4.3", najwiekszy, end=" ")
for i in range(len(mapy)):
    if boki[i] == najwiekszy:
        print(i + 1, end=" ")
print()
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <vector>

using Mapa = std::vector<std::string>;

// 4.2 - obrót o 180 stopni: odwracamy kolejność wierszy i każdy wiersz
Mapa obrot(const Mapa& mapa) {
    Mapa wynik;
    for (int i = mapa.size() - 1; i >= 0; i--)
        wynik.push_back(std::string(mapa[i].rbegin(), mapa[i].rend()));
    return wynik;
}

// 4.3
int najwiekszy_plac(const Mapa& mapa) {
    int bok = 0;
    // kwadrat o boku bok + 1 mieści się, gdy w wierszach i kolumnach 0..bok nie ma X
    while (bok < 30) {
        bool dobry = true;
        for (int i = 0; i <= bok; i++)
            for (int j = 0; j <= bok; j++)
                if (mapa[i][j] == 'X')
                    dobry = false;
        if (!dobry)
            break;
        bok++;
    }
    return bok;
}

int main() {
    std::ifstream plik("dzialki.txt");
    std::vector<std::string> wiersze;
    std::string wiersz;
    while (plik >> wiersz)  // >> pomija puste wiersze między mapami
        wiersze.push_back(wiersz);

    std::vector<Mapa> mapy;
    for (size_t m = 0; m < wiersze.size() / 30; m++)
        mapy.push_back(Mapa(wiersze.begin() + 30 * m, wiersze.begin() + 30 * m + 30));

    // 4.1
    int ile = 0;
    for (const auto& mapa : mapy) {
        int trawa = 0;
        for (const auto& w : mapa)
            trawa += std::ranges::count(w, '*');
        if (trawa >= 0.7 * 30 * 30)
            ile++;
    }
    std::println("4.1 {}", ile);

    // 4.2
    std::print("4.2 ");
    for (size_t i = 0; i < mapy.size(); i++)
        for (size_t j = i + 1; j < mapy.size(); j++)
            if (obrot(mapy[i]) == mapy[j])
                std::print("{} {} ", i + 1, j + 1);
    std::println();

    // 4.3
    std::vector<int> boki;
    for (const auto& mapa : mapy)
        boki.push_back(najwiekszy_plac(mapa));
    int najwiekszy = std::ranges::max(boki);
    std::print("4.3 {} ", najwiekszy);
    for (size_t i = 0; i < mapy.size(); i++)
        if (boki[i] == najwiekszy)
            std::print("{} ", i + 1);
    std::println();
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    // 4.2 - obrót o 180 stopni: odwracamy kolejność wierszy i każdy wiersz
    static List<String> obrot(List<String> mapa) {
        var wynik = new ArrayList<String>();
        for (int i = mapa.size() - 1; i >= 0; i--)
            wynik.add(new StringBuilder(mapa.get(i)).reverse().toString());
        return wynik;
    }

    // 4.3
    static int najwiekszyPlac(List<String> mapa) {
        int bok = 0;
        // kwadrat o boku bok + 1 mieści się, gdy w wierszach i kolumnach 0..bok nie ma X
        while (bok < 30) {
            boolean dobry = true;
            for (int i = 0; i <= bok; i++)
                for (int j = 0; j <= bok; j++)
                    if (mapa.get(i).charAt(j) == 'X')
                        dobry = false;
            if (!dobry)
                break;
            bok++;
        }
        return bok;
    }

    public static void main(String[] args) throws Exception {
        var wiersze = new ArrayList<String>();
        for (String line : Files.readAllLines(Path.of("dzialki.txt")))
            if (!line.strip().isEmpty())
                wiersze.add(line.strip());

        var mapy = new ArrayList<List<String>>();
        for (int m = 0; m < wiersze.size() / 30; m++)
            mapy.add(wiersze.subList(30 * m, 30 * m + 30));

        // 4.1
        int ile = 0;
        for (var mapa : mapy) {
            int trawa = 0;
            for (String w : mapa)
                trawa += (int) w.chars().filter(c -> c == '*').count();
            if (trawa >= 0.7 * 30 * 30)
                ile++;
        }
        System.out.println("4.1 " + ile);

        // 4.2
        System.out.print("4.2 ");
        for (int i = 0; i < mapy.size(); i++)
            for (int j = i + 1; j < mapy.size(); j++)
                if (obrot(mapy.get(i)).equals(mapy.get(j)))
                    System.out.print((i + 1) + " " + (j + 1) + " ");
        System.out.println();

        // 4.3
        var boki = new ArrayList<Integer>();
        for (var mapa : mapy)
            boki.add(najwiekszyPlac(mapa));
        int najwiekszy = boki.stream().mapToInt(Integer::intValue).max().getAsInt();
        System.out.print("4.3 " + najwiekszy + " ");
        for (int i = 0; i < mapy.size(); i++)
            if (boki.get(i) == najwiekszy)
                System.out.print((i + 1) + " ");
        System.out.println();
    }
}
```

**Odpowiedź:** 4.1: 5; 4.2: działki 14 i 39; 4.3: bok 12, działki 28, 32, 45
