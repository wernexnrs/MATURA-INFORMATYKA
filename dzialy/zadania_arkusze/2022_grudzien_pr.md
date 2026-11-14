<h1 align="center">Matura próbna 2022 — grudzień (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2022-grudzien-probna-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2022-grudzien-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2022-grudzien-probna-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania (Kosmiczny mecz):** Plik `mecz.txt` zawiera jeden wiersz – napis z 10 000 znaków `A` i `B` opisujący wyniki kolejnych rozgrywek meczu (znak oznacza drużynę, która wygrała daną rozgrywkę i zdobyła punkt). Odpowiedzi zapisz w pliku `wyniki1.txt`, poprzedzając każdą numerem zadania (plik `mecz_przyklad.txt` służy do testów).
>
> - **1.1** — Policz, ile razy rozgrywkę wygrała inna drużyna niż poprzednią (dwa kolejne znaki są różne). Przykład: dla `ABBBABA` odpowiedź to 4; dla pliku przykładowego – 1798.
> - **1.2** — Pierwszy set trwa do pierwszej rozgrywki, po której jedna z drużyn ma co najmniej 1000 punktów, a przeciwna co najmniej 3 punkty mniej (np. 1000:500, 997:1000, 1500:1497 kończą seta; 999:1000 czy 1500:1500 nie). Podaj zwycięzcę pierwszego seta i wynik w tym momencie (punkty A : punkty B). Dla pliku przykładowego: `A 1000:5`.
> - **1.3** — Dobra passa to co najmniej 10 wygranych z rzędu jednej drużyny (maksymalny ciąg – zaczyna się na początku meczu lub po przegranej i kończy z końcem meczu lub przed przegraną). Podaj łączną liczbę dobrych pass obu drużyn oraz długość najdłuższej passy i drużynę, która ją osiągnęła (jest jedna taka). Przykład: w `BBBBBBBBBBAABBAAAAAAAAAAABA` są 2 dobre passy, najdłuższa ma długość 11 (drużyna A).

```py
with open("mecz.txt") as file:
    mecz = file.readline().strip()

# 1.1
zmiany = 0
for i in range(1, len(mecz)):
    if mecz[i] != mecz[i - 1]:
        zmiany += 1
print("1.1", zmiany)

# 1.2
punkty_a = 0
punkty_b = 0
for znak in mecz:
    if znak == "A":
        punkty_a += 1
    else:
        punkty_b += 1
    if (punkty_a >= 1000 or punkty_b >= 1000) and abs(punkty_a - punkty_b) >= 3:
        break
if punkty_a > punkty_b:
    print("1.2", "A", str(punkty_a) + ":" + str(punkty_b))
else:
    print("1.2", "B", str(punkty_a) + ":" + str(punkty_b))

# 1.3 - dzielimy mecz na maksymalne bloki jednakowych znaków
dobre_passy = 0
najdluzsza = 0
druzyna = ""
dlugosc = 1
for i in range(1, len(mecz) + 1):
    if i < len(mecz) and mecz[i] == mecz[i - 1]:
        dlugosc += 1
    else:
        # koniec bloku mecz[i - dlugosc .. i - 1]
        if dlugosc >= 10:
            dobre_passy += 1
            if dlugosc > najdluzsza:
                najdluzsza = dlugosc
                druzyna = mecz[i - 1]
        dlugosc = 1
print("1.3", dobre_passy, druzyna, najdluzsza)
```
```cpp
// C++23
#include <cstdlib>
#include <fstream>
#include <print>
#include <string>

int main() {
    std::ifstream plik("mecz.txt");
    std::string mecz;
    plik >> mecz;

    // 1.1
    int zmiany = 0;
    for (size_t i = 1; i < mecz.size(); i++)
        if (mecz[i] != mecz[i - 1]) zmiany++;
    std::println("1.1 {}", zmiany);

    // 1.2
    int punkty_a = 0;
    int punkty_b = 0;
    for (char znak : mecz) {
        if (znak == 'A')
            punkty_a++;
        else
            punkty_b++;
        if ((punkty_a >= 1000 || punkty_b >= 1000) && std::abs(punkty_a - punkty_b) >= 3) break;
    }
    if (punkty_a > punkty_b)
        std::println("1.2 A {}:{}", punkty_a, punkty_b);
    else
        std::println("1.2 B {}:{}", punkty_a, punkty_b);

    // 1.3 - dzielimy mecz na maksymalne bloki jednakowych znaków
    int dobre_passy = 0;
    int najdluzsza = 0;
    char druzyna = ' ';
    int dlugosc = 1;
    for (size_t i = 1; i <= mecz.size(); i++) {
        if (i < mecz.size() && mecz[i] == mecz[i - 1]) {
            dlugosc++;
        } else {
            // koniec bloku mecz[i - dlugosc .. i - 1]
            if (dlugosc >= 10) {
                dobre_passy++;
                if (dlugosc > najdluzsza) {
                    najdluzsza = dlugosc;
                    druzyna = mecz[i - 1];
                }
            }
            dlugosc = 1;
        }
    }
    std::println("1.3 {} {} {}", dobre_passy, druzyna, najdluzsza);
}
```
```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        String mecz = Files.readAllLines(Path.of("mecz.txt")).get(0).strip();

        // 1.1
        int zmiany = 0;
        for (int i = 1; i < mecz.length(); i++)
            if (mecz.charAt(i) != mecz.charAt(i - 1)) zmiany++;
        System.out.println("1.1 " + zmiany);

        // 1.2
        int punktyA = 0;
        int punktyB = 0;
        for (char znak : mecz.toCharArray()) {
            if (znak == 'A')
                punktyA++;
            else
                punktyB++;
            if ((punktyA >= 1000 || punktyB >= 1000) && Math.abs(punktyA - punktyB) >= 3) break;
        }
        if (punktyA > punktyB)
            System.out.println("1.2 A " + punktyA + ":" + punktyB);
        else
            System.out.println("1.2 B " + punktyA + ":" + punktyB);

        // 1.3 - dzielimy mecz na maksymalne bloki jednakowych znaków
        int dobrePassy = 0;
        int najdluzsza = 0;
        char druzyna = ' ';
        int dlugosc = 1;
        for (int i = 1; i <= mecz.length(); i++) {
            if (i < mecz.length() && mecz.charAt(i) == mecz.charAt(i - 1)) {
                dlugosc++;
            } else {
                // koniec bloku mecz[i - dlugosc .. i - 1]
                if (dlugosc >= 10) {
                    dobrePassy++;
                    if (dlugosc > najdluzsza) {
                        najdluzsza = dlugosc;
                        druzyna = mecz.charAt(i - 1);
                    }
                }
                dlugosc = 1;
            }
        }
        System.out.println("1.3 " + dobrePassy + " " + druzyna + " " + najdluzsza);
    }
}
```

**Odpowiedź:** 1.1: 5030; 1.2: B 1001:1004; 1.3: 6 B 15

## 2.1, 2.2, 2.3 i 2.4

> **Treść zadania (Strzałki):** Dla dodatniego N rysujemy punkty o numerach 1..N. Funkcja `strzałka(x, y)` rysuje strzałkę z punktu x do y, a rekurencyjna funkcja `rysuj(x)` działa tak:
>
> ```
> funkcja rysuj(x)
>   jeżeli 2*x ≤ N:     strzałka(x, 2*x);     rysuj(2*x)
>   jeżeli 2*x+1 ≤ N:   strzałka(x, 2*x+1);   rysuj(2*x+1)
> ```
>
> - **2.1** — Dla N = 10 narysuj punkty 1..10 i strzałki powstałe po wywołaniu `rysuj(1)`.
> - **2.2** — Podaj, ile strzałek zostanie narysowanych po wywołaniu `rysuj(1)`: a) dla N = 20, b) dla dowolnego N.
> - **2.3** — Dla N = 2047 podaj, po ilu strzałkach (zgodnie z ich zwrotem) trzeba przejść z punktu 1 do punktu N (dla N = 5 z punktu 1 do 5 – po dwóch).
> - **2.4** — Plik `pary.txt` zawiera 1000 par liczb całkowitych z zakresu [1, 100 000] (w wierszu, oddzielone spacją; druga liczba jest większa od pierwszej). Napisz program, który wypisze te pary (x, y), dla których z punktu x da się dojść do punktu y po jednej lub kilku strzałkach zgodnie z ich zwrotami (np. z 1 do 4 – tak, z 3 do 5 – nie). Wynik zapisz w `wyniki2.txt`.

```py
strzalki = []


def rysuj(x, N):
    if 2 * x <= N:
        strzalki.append((x, 2 * x))
        rysuj(2 * x, N)
    if 2 * x + 1 <= N:
        strzalki.append((x, 2 * x + 1))
        rysuj(2 * x + 1, N)


# 2.1 - lista strzałek dla N = 10 (punkt x łączy się z 2x i 2x+1 - drzewo binarne)
rysuj(1, 10)
print("2.1", strzalki)

# 2.2 - każdy punkt poza 1 ma dokładnie jedną strzałkę wchodzącą (od x // 2)
strzalki = []
rysuj(1, 20)
print("2.2", len(strzalki), "ogólnie N - 1")

# 2.3 - idąc od N do 1 przechodzimy do N // 2
N = 2047
kroki = 0
while N > 1:
    N //= 2
    kroki += 1
print("2.3", kroki)


# 2.4 - z x da się dojść do y, gdy dzieląc y przez 2 (całkowicie) dojdziemy do x
def osiagalny(x, y):
    while y > x:
        y //= 2
    return x == y


print("2.4")
with open("pary.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        if osiagalny(x, y):
            print(x, y)
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <utility>
#include <vector>

std::vector<std::pair<int, int>> strzalki;

void rysuj(int x, int N) {
    if (2 * x <= N) {
        strzalki.push_back({x, 2 * x});
        rysuj(2 * x, N);
    }
    if (2 * x + 1 <= N) {
        strzalki.push_back({x, 2 * x + 1});
        rysuj(2 * x + 1, N);
    }
}

// 2.4 - z x da się dojść do y, gdy dzieląc y przez 2 (całkowicie) dojdziemy do x
bool osiagalny(long long x, long long y) {
    while (y > x) y /= 2;
    return x == y;
}

int main() {
    // 2.1 - lista strzałek dla N = 10 (punkt x łączy się z 2x i 2x+1 - drzewo binarne)
    rysuj(1, 10);
    std::println("2.1 {}", strzalki);  // format [(1, 2), (2, 4), ...] jak w Pythonie

    // 2.2 - każdy punkt poza 1 ma dokładnie jedną strzałkę wchodzącą (od x // 2)
    strzalki.clear();
    rysuj(1, 20);
    std::println("2.2 {} ogólnie N - 1", strzalki.size());

    // 2.3 - idąc od N do 1 przechodzimy do N // 2
    int N = 2047;
    int kroki = 0;
    while (N > 1) {
        N /= 2;
        kroki++;
    }
    std::println("2.3 {}", kroki);

    std::println("2.4");
    std::ifstream plik("pary.txt");
    long long x, y;
    while (plik >> x >> y)
        if (osiagalny(x, y)) std::println("{} {}", x, y);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static List<String> strzalki = new ArrayList<>();  // strzałki zapisane jako "(x, y)"

    static void rysuj(int x, int N) {
        if (2 * x <= N) {
            strzalki.add("(" + x + ", " + 2 * x + ")");
            rysuj(2 * x, N);
        }
        if (2 * x + 1 <= N) {
            strzalki.add("(" + x + ", " + (2 * x + 1) + ")");
            rysuj(2 * x + 1, N);
        }
    }

    // 2.4 - z x da się dojść do y, gdy dzieląc y przez 2 (całkowicie) dojdziemy do x
    static boolean osiagalny(long x, long y) {
        while (y > x) y /= 2;
        return x == y;
    }

    public static void main(String[] args) throws Exception {
        // 2.1 - lista strzałek dla N = 10 (punkt x łączy się z 2x i 2x+1 - drzewo binarne)
        rysuj(1, 10);
        System.out.println("2.1 " + strzalki);  // format [(1, 2), (2, 4), ...] jak w Pythonie

        // 2.2 - każdy punkt poza 1 ma dokładnie jedną strzałkę wchodzącą (od x // 2)
        strzalki.clear();
        rysuj(1, 20);
        System.out.println("2.2 " + strzalki.size() + " ogólnie N - 1");

        // 2.3 - idąc od N do 1 przechodzimy do N // 2
        int N = 2047;
        int kroki = 0;
        while (N > 1) {
            N /= 2;
            kroki++;
        }
        System.out.println("2.3 " + kroki);

        System.out.println("2.4");
        for (var linia : Files.readAllLines(Path.of("pary.txt"))) {
            if (linia.isBlank()) continue;
            var xy = linia.trim().split("\\s+");
            long x = Long.parseLong(xy[0]), y = Long.parseLong(xy[1]);
            if (osiagalny(x, y)) System.out.println(x + " " + y);
        }
    }
}
```

**Odpowiedź:** 2.1: strzałki 1→2, 1→3, 2→4, 2→5, 3→6, 3→7, 4→8, 4→9, 5→10; 2.2: a) 19, b) N − 1; 2.3: 10; 2.4: 47 3044, 7650 61204, 1 245, 7 63669, 9125 18250, 5 43246

## 3.1, 3.2, 3.3 i 3.4

> **Treść zadania (Liczby):**
>
> - **3.1** — Uzupełnij luki w algorytmie sita Eratostenesa, który dla N > 1 wypełnia tablicę logiczną `SITO[1..N]` (PRAWDA dla liczb pierwszych, FAŁSZ dla złożonych):
>
> ```
> SITO[1] ← FAŁSZ
> dla i = 2, ..., N:  SITO[i] ← PRAWDA
> dla i = 2, 3, ..., ____
>   jeżeli SITO[i] = ____
>     j ← ____
>     dopóki j ≤ N:  SITO[j] ← ____;  j ← ____
> ```
>
> Plik `liczby.txt` zawiera 100 liczb parzystych z zakresu [4, 1 000 000], po jednej w wierszu. Odpowiedzi do 3.2–3.4 zapisz w `wyniki3.txt` z numerem zadania (do testów: `liczby_przyklad.txt`).
>
> - **3.2** — Podaj, dla ilu liczb x z pliku liczba x − 1 jest pierwsza.
> - **3.3** — Dla każdej liczby wyznacz, na ile sposobów da się ją zapisać jako sumę dwóch liczb pierwszych (rozkłady różniące się tylko kolejnością składników są takie same, np. 22 = 19 + 3 = 17 + 5 = 11 + 11). Podaj liczbę o największej liczbie rozkładów wraz z tą liczbą oraz liczbę o najmniejszej liczbie rozkładów wraz z tą liczbą. Dla pliku przykładowego: `996 37 4 1`.
> - **3.4** — Zapisz każdą liczbę w systemie szesnastkowym i dla każdej cyfry 0–F podaj, ile razy łącznie występuje we wszystkich tych zapisach (w formacie `cyfra:liczba`, np. `0:2`, `1:3`, …).

```py
# 3.1 - sito Eratostenesa (luki: N (wystarczy pierwiastek z N), PRAWDA, i * i, FAŁSZ, j + i)
def sito(N):
    SITO = [True] * (N + 1)
    SITO[0] = False
    SITO[1] = False
    i = 2
    while i * i <= N:
        if SITO[i]:
            j = i * i
            while j <= N:
                SITO[j] = False
                j = j + i
        i += 1
    return SITO


liczby = []
with open("liczby.txt") as file:
    for line in file:
        liczby.append(int(line))

SITO = sito(1000000)

# 3.2
ile = 0
for x in liczby:
    if SITO[x - 1]:
        ile += 1
print("3.2", ile)

# 3.3 - rozkład x = p + (x - p), p <= x - p
najwiecej, liczba_max = -1, 0
najmniej, liczba_min = 10 ** 9, 0
for x in liczby:
    rozklady = 0
    for p in range(2, x // 2 + 1):
        if SITO[p] and SITO[x - p]:
            rozklady += 1
    if rozklady > najwiecej:
        najwiecej, liczba_max = rozklady, x
    if rozklady < najmniej:
        najmniej, liczba_min = rozklady, x
print("3.3", liczba_max, najwiecej, liczba_min, najmniej)

# 3.4
cyfry = "0123456789ABCDEF"
ile_cyfr = [0] * 16
for x in liczby:
    while x > 0:
        ile_cyfr[x % 16] += 1
        x //= 16
print("3.4")
for i in range(16):
    print(cyfry[i] + ":" + str(ile_cyfr[i]))
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <string>
#include <vector>

// 3.1 - sito Eratostenesa (luki: N (wystarczy pierwiastek z N), PRAWDA, i * i, FAŁSZ, j + i)
std::vector<bool> sito(int N) {
    std::vector<bool> SITO(N + 1, true);
    SITO[0] = false;
    SITO[1] = false;
    for (long long i = 2; i * i <= N; i++) {
        if (SITO[i]) {
            for (long long j = i * i; j <= N; j += i) SITO[j] = false;
        }
    }
    return SITO;
}

int main() {
    std::vector<int> liczby;
    std::ifstream plik("liczby.txt");
    int x;
    while (plik >> x) liczby.push_back(x);

    std::vector<bool> SITO = sito(1000000);

    // 3.2
    int ile = 0;
    for (int x : liczby)
        if (SITO[x - 1]) ile++;
    std::println("3.2 {}", ile);

    // 3.3 - rozkład x = p + (x - p), p <= x - p
    int najwiecej = -1, liczba_max = 0;
    int najmniej = 1000000000, liczba_min = 0;
    for (int x : liczby) {
        int rozklady = 0;
        for (int p = 2; p <= x / 2; p++)
            if (SITO[p] && SITO[x - p]) rozklady++;
        if (rozklady > najwiecej) {
            najwiecej = rozklady;
            liczba_max = x;
        }
        if (rozklady < najmniej) {
            najmniej = rozklady;
            liczba_min = x;
        }
    }
    std::println("3.3 {} {} {} {}", liczba_max, najwiecej, liczba_min, najmniej);

    // 3.4
    std::string cyfry = "0123456789ABCDEF";
    std::vector<int> ile_cyfr(16, 0);
    for (int x : liczby) {
        while (x > 0) {
            ile_cyfr[x % 16]++;
            x /= 16;
        }
    }
    std::println("3.4");
    for (int i = 0; i < 16; i++) std::println("{}:{}", cyfry[i], ile_cyfr[i]);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    // 3.1 - sito Eratostenesa (luki: N (wystarczy pierwiastek z N), PRAWDA, i * i, FAŁSZ, j + i)
    static boolean[] sito(int N) {
        boolean[] SITO = new boolean[N + 1];
        Arrays.fill(SITO, true);
        SITO[0] = false;
        SITO[1] = false;
        for (long i = 2; i * i <= N; i++) {
            if (SITO[(int) i]) {
                for (long j = i * i; j <= N; j += i) SITO[(int) j] = false;
            }
        }
        return SITO;
    }

    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<Integer>();
        for (var linia : Files.readAllLines(Path.of("liczby.txt")))
            if (!linia.isBlank()) liczby.add(Integer.parseInt(linia.trim()));

        boolean[] SITO = sito(1000000);

        // 3.2
        int ile = 0;
        for (int x : liczby)
            if (SITO[x - 1]) ile++;
        System.out.println("3.2 " + ile);

        // 3.3 - rozkład x = p + (x - p), p <= x - p
        int najwiecej = -1, liczbaMax = 0;
        int najmniej = 1000000000, liczbaMin = 0;
        for (int x : liczby) {
            int rozklady = 0;
            for (int p = 2; p <= x / 2; p++)
                if (SITO[p] && SITO[x - p]) rozklady++;
            if (rozklady > najwiecej) {
                najwiecej = rozklady;
                liczbaMax = x;
            }
            if (rozklady < najmniej) {
                najmniej = rozklady;
                liczbaMin = x;
            }
        }
        System.out.println("3.3 " + liczbaMax + " " + najwiecej + " " + liczbaMin + " " + najmniej);

        // 3.4
        String cyfry = "0123456789ABCDEF";
        int[] ileCyfr = new int[16];
        for (int x : liczby) {
            while (x > 0) {
                ileCyfr[x % 16]++;
                x /= 16;
            }
        }
        System.out.println("3.4");
        for (int i = 0; i < 16; i++) System.out.println(cyfry.charAt(i) + ":" + ileCyfr[i]);
    }
}
```

**Odpowiedź:** 3.1: luki kolejno: N (wystarczy √N), PRAWDA, i * i, FAŁSZ, j + i; 3.2: 21; 3.3: 910620 9932 18676 195; 3.4: 0:32, 1:26, 2:37, 3:31, 4:43, 5:25, 6:28, 7:23, 8:38, 9:28, A:45, B:33, C:29, D:23, E:44, F:10
