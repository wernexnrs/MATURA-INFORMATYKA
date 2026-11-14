<h1 align="center">Matura 2025 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

> **Treść zadania:** Każdą liczbę całkowitą większą od 1 można rozłożyć na czynniki pierwsze.
>
> - 1.1 — Uzupełnij tabelę: dla n = 14, 27 i 33 zapisz rozkład na czynniki pierwsze oraz TAK, jeśli n jest iloczynem dokładnie dwóch różnych liczb pierwszych, albo NIE w przeciwnym razie (przykłady: 6 = 2 · 3 — TAK, 9 = 3 · 3 — NIE, 13 — NIE).
> - 1.2 — Dla n ≥ 2 tablica P[2..n] zawiera dla każdego i najmniejszy czynnik pierwszy liczby i (np. dla n = 19: P[4] = 2, P[9] = 3, P[15] = 3, P[17] = 17). Uzupełnij luki w algorytmie Rozkład tak, aby po jego wykonaniu P[i] = 1, gdy i jest liczbą pierwszą, P[i] = 2, gdy i jest iloczynem dokładnie dwóch różnych liczb pierwszych, i P[i] = 3 w pozostałych przypadkach:
>
> ```
> dla i = 2, 3, ..., n
>     jeżeli P[i] = i
>         P[i] = ......
>     inaczej
>         j1 ← P[i]
>         j2 ← i / j1
>         jeżeli j1 ≠ j2 oraz ......
>             P[i] = ......
>         inaczej
>             P[i] = ......
> ```

```py
def rozklad(n):
    czynniki = []
    d = 2
    while n > 1:
        if n % d == 0:
            czynniki.append(d)
            n //= d
        else:
            d += 1
    return czynniki


# 1.1
for n in [14, 27, 33]:
    czynniki = rozklad(n)
    dwie_rozne = len(czynniki) == 2 and czynniki[0] != czynniki[1]
    print(n, czynniki, "TAK" if dwie_rozne else "NIE")

# 1.2
n = 40
P = [0] * (n + 1)                   # P[2..n] - najmniejszy czynnik pierwszy liczby i
for i in range(2, n + 1):
    d = 2
    while i % d != 0:
        d += 1
    P[i] = d

for i in range(2, n + 1):           # algorytm Rozklad
    if P[i] == i:
        P[i] = 1
    else:
        j1 = P[i]
        j2 = i // j1
        if j1 != j2 and P[j2] == 1:     # P[j2] jest już przetworzone, bo j2 < i
            P[i] = 2
        else:
            P[i] = 3

print(P[2:])
```

```cpp
// C++23
#include <print>
#include <vector>

std::vector<int> rozklad(int n) {
    std::vector<int> czynniki;
    int d = 2;
    while (n > 1) {
        if (n % d == 0) {
            czynniki.push_back(d);
            n /= d;
        } else {
            d += 1;
        }
    }
    return czynniki;
}

int main() {
    // 1.1 (wektor wypisuje się jak lista w Pythonie: [2, 7])
    for (int n : {14, 27, 33}) {
        std::vector<int> czynniki = rozklad(n);
        bool dwie_rozne = czynniki.size() == 2 && czynniki[0] != czynniki[1];
        std::println("{} {} {}", n, czynniki, dwie_rozne ? "TAK" : "NIE");
    }

    // 1.2
    int n = 40;
    std::vector<int> P(n + 1, 0);       // P[2..n] - najmniejszy czynnik pierwszy liczby i
    for (int i = 2; i <= n; i++) {
        int d = 2;
        while (i % d != 0) {
            d += 1;
        }
        P[i] = d;
    }

    for (int i = 2; i <= n; i++) {      // algorytm Rozklad
        if (P[i] == i) {
            P[i] = 1;
        } else {
            int j1 = P[i];
            int j2 = i / j1;
            if (j1 != j2 && P[j2] == 1) {   // P[j2] jest już przetworzone, bo j2 < i
                P[i] = 2;
            } else {
                P[i] = 3;
            }
        }
    }

    std::println("{}", std::vector<int>(P.begin() + 2, P.end()));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Zadanie {
    static List<Integer> rozklad(int n) {
        List<Integer> czynniki = new ArrayList<>();
        int d = 2;
        while (n > 1) {
            if (n % d == 0) {
                czynniki.add(d);
                n /= d;
            } else {
                d += 1;
            }
        }
        return czynniki;
    }

    public static void main(String[] args) throws Exception {
        // 1.1 (lista wypisuje się jak w Pythonie: [2, 7])
        for (int n : new int[]{14, 27, 33}) {
            List<Integer> czynniki = rozklad(n);
            boolean dwieRozne = czynniki.size() == 2 && !czynniki.get(0).equals(czynniki.get(1));
            System.out.println(n + " " + czynniki + " " + (dwieRozne ? "TAK" : "NIE"));
        }

        // 1.2
        int n = 40;
        int[] P = new int[n + 1];           // P[2..n] - najmniejszy czynnik pierwszy liczby i
        for (int i = 2; i <= n; i++) {
            int d = 2;
            while (i % d != 0) {
                d += 1;
            }
            P[i] = d;
        }

        for (int i = 2; i <= n; i++) {      // algorytm Rozklad
            if (P[i] == i) {
                P[i] = 1;
            } else {
                int j1 = P[i];
                int j2 = i / j1;
                if (j1 != j2 && P[j2] == 1) {   // P[j2] jest już przetworzone, bo j2 < i
                    P[i] = 2;
                } else {
                    P[i] = 3;
                }
            }
        }

        System.out.println(Arrays.toString(Arrays.copyOfRange(P, 2, n + 1)));
    }
}
```

**Odpowiedź:** 1.1: 14 = 2 · 7 – TAK; 27 = 3 · 3 · 3 – NIE; 33 = 3 · 11 – TAK. 1.2: luki: `P[i] = 1`; `P[j2] = 1`; `P[i] = 2`; `P[i] = 3`.

## 2.1, 2.2 i 2.3

> **Treść zadania:** Funkcje pomocnicze dla nieujemnej liczby całkowitej x: skróć(x) usuwa ostatnią cyfrę zapisu dziesiętnego (skróć(249) = 24, skróć(5) = 0), dopisz(x) dopisuje na końcu cyfrę 0 (dopisz(29) = 290, dopisz(0) = 0), ostatnia(x) zwraca ostatnią cyfrę (ostatnia(307) = 7). Dla nieujemnych liczb całkowitych a, b dana jest funkcja:
>
> ```
> f(a, b):
>     jeżeli b = 0
>         wynik 0, zakończ
>     k ← ostatnia(b)
>     w ← f(a, skróć(b))
>     w ← dopisz(w)
>     dopóki k > 0 powtarzaj
>         w ← w + a
>         k ← k − 1
>     wynik w
> ```
>
> - 2.1 — Podaj wynik f(a, b) dla par (42, 2), (4, 125), (103, 104).
> - 2.2 — Ile łącznie razy zostanie wywołana funkcja f, jeśli pierwszym wywołaniem jest f(987654321, 123456789)?
> - 2.3 — Ile łącznie razy zostanie wykonana instrukcja w ← w + a, jeśli pierwszym wywołaniem jest a) f(2024, 1000), b) f(2024, 1234)?

```py
wywolania = 0
dodawania = 0


def f(a, b):
    global wywolania, dodawania
    wywolania += 1
    if b == 0:
        return 0
    k = b % 10                  # ostatnia(b)
    w = f(a, b // 10)           # skróć(b)
    w = w * 10                  # dopisz(w)
    while k > 0:
        w = w + a
        dodawania += 1
        k -= 1
    return w


# 2.1 (funkcja oblicza a * b)
for a, b in [(42, 2), (4, 125), (103, 104)]:
    print(a, b, f(a, b))

# 2.2
wywolania = 0
f(987654321, 123456789)
print(wywolania)

# 2.3
for a, b in [(2024, 1000), (2024, 1234)]:
    dodawania = 0
    f(a, b)
    print(a, b, dodawania)
```

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

int wywolania = 0;
int dodawania = 0;

long long f(long long a, long long b) {
    wywolania += 1;
    if (b == 0) {
        return 0;
    }
    long long k = b % 10;           // ostatnia(b)
    long long w = f(a, b / 10);     // skróć(b)
    w = w * 10;                     // dopisz(w)
    while (k > 0) {
        w = w + a;
        dodawania += 1;
        k -= 1;
    }
    return w;
}

int main() {
    // 2.1 (funkcja oblicza a * b)
    std::vector<std::pair<long long, long long>> pary = {{42, 2}, {4, 125}, {103, 104}};
    for (auto [a, b] : pary) {
        std::println("{} {} {}", a, b, f(a, b));
    }

    // 2.2
    wywolania = 0;
    f(987654321, 123456789);
    std::println("{}", wywolania);

    // 2.3
    std::vector<std::pair<long long, long long>> pary3 = {{2024, 1000}, {2024, 1234}};
    for (auto [a, b] : pary3) {
        dodawania = 0;
        f(a, b);
        std::println("{} {} {}", a, b, dodawania);
    }
}
```

```java
// Java 25
public class Zadanie {
    static int wywolania = 0;
    static int dodawania = 0;

    static long f(long a, long b) {
        wywolania += 1;
        if (b == 0) {
            return 0;
        }
        long k = b % 10;            // ostatnia(b)
        long w = f(a, b / 10);      // skróć(b)
        w = w * 10;                 // dopisz(w)
        while (k > 0) {
            w = w + a;
            dodawania += 1;
            k -= 1;
        }
        return w;
    }

    public static void main(String[] args) throws Exception {
        // 2.1 (funkcja oblicza a * b)
        long[][] pary = {{42, 2}, {4, 125}, {103, 104}};
        for (long[] p : pary) {
            System.out.println(p[0] + " " + p[1] + " " + f(p[0], p[1]));
        }

        // 2.2
        wywolania = 0;
        f(987654321L, 123456789L);
        System.out.println(wywolania);

        // 2.3
        long[][] pary3 = {{2024, 1000}, {2024, 1234}};
        for (long[] p : pary3) {
            dodawania = 0;
            f(p[0], p[1]);
            System.out.println(p[0] + " " + p[1] + " " + dodawania);
        }
    }
}
```

**Odpowiedź:** 2.1: 84, 500, 10712. 2.2: 10. 2.3: a) 1, b) 10.

## 4.1, 4.2, 4.3 i 4.4

> **Treść zadania:** Plik `dane.txt` zawiera jeden napis złożony z 10 000 znaków (kody ASCII 33–126), wśród których ukryte są liczby. Liczba ukryta to niepusty ciąg cyfr, przed którym i za którym nie stoi cyfra (np. w `356xv@@4vdfvdfD#$%@@#245` ukryte są 356, 4 i 245). Numer telefonu to ukryta liczba złożona z dokładnie 9 cyfr. Odpowiedzi zapisz w plikach `wyniki4_1.txt` … `wyniki4_4.txt`. Plik `dane_przyklad.txt` (200 znaków) służy do testów.
>
> - 4.1 — Podaj, ile ukrytych liczb zaczyna się od cyfr `50` (każde wystąpienie liczymy osobno). Np. w `fs@dx+cd50450505VfF^&x50` są dwie takie liczby: 50450505 i 50.
> - 4.2 — Podaj najczęściej występującą w pliku cyfrę i liczbę jej wystąpień (jest jedna taka cyfra; dla pliku przykładowego: `0 17`).
> - 4.3 — Wypisz wszystkie numery telefonów zaczynające się od cyfry 5, w kolejności występowania w pliku.
> - 4.4 — Podaj te numery telefonów, które składają się z najmniejszej liczby różnych cyfr.

```py
with open("dane.txt") as file:
    napis = file.read().strip()

# wydzielenie ukrytych liczb (maksymalnych ciągów cyfr)
liczby = []
biezaca = ""
for znak in napis + " ":
    if znak.isdigit():
        biezaca += znak
    else:
        if biezaca != "":
            liczby.append(biezaca)
        biezaca = ""

# 4.1
ile = 0
for liczba in liczby:
    if liczba[:2] == "50":
        ile += 1
with open("wyniki4_1.txt", "w") as wynik:
    print(ile, file=wynik)

# 4.2
wystapienia = [0] * 10
for znak in napis:
    if znak.isdigit():
        wystapienia[int(znak)] += 1
najwiecej = max(wystapienia)
with open("wyniki4_2.txt", "w") as wynik:
    print(wystapienia.index(najwiecej), najwiecej, file=wynik)

# 4.3
telefony = [liczba for liczba in liczby if len(liczba) == 9]
with open("wyniki4_3.txt", "w") as wynik:
    for telefon in telefony:
        if telefon[0] == "5":
            print(telefon, file=wynik)

# 4.4
najmniej = min(len(set(telefon)) for telefon in telefony)
with open("wyniki4_4.txt", "w") as wynik:
    for telefon in telefony:
        if len(set(telefon)) == najmniej:
            print(telefon, file=wynik)
```

```cpp
// C++23
#include <algorithm>
#include <cctype>
#include <fstream>
#include <print>
#include <set>
#include <string>
#include <vector>

// liczba różnych cyfr w napisie
size_t rozne(const std::string& s) {
    return std::set<char>(s.begin(), s.end()).size();
}

int main() {
    std::ifstream plik("dane.txt");
    std::string napis;
    std::getline(plik, napis);
    while (!napis.empty() && std::isspace((unsigned char)napis.back())) {
        napis.pop_back();  // odpowiednik strip() - usuwa m.in. znak '\r'
    }

    // wydzielenie ukrytych liczb (maksymalnych ciągów cyfr)
    std::vector<std::string> liczby;
    std::string biezaca = "";
    for (char znak : napis + " ") {
        if (std::isdigit((unsigned char)znak)) {
            biezaca += znak;
        } else {
            if (biezaca != "") {
                liczby.push_back(biezaca);
            }
            biezaca = "";
        }
    }

    // 4.1
    int ile = 0;
    for (const std::string& liczba : liczby) {
        if (liczba.substr(0, 2) == "50") {
            ile += 1;
        }
    }
    std::ofstream wynik1("wyniki4_1.txt");
    std::println(wynik1, "{}", ile);

    // 4.2
    std::vector<int> wystapienia(10, 0);
    for (char znak : napis) {
        if (std::isdigit((unsigned char)znak)) {
            wystapienia[znak - '0'] += 1;
        }
    }
    auto najwiecej = std::ranges::max_element(wystapienia);  // pierwsza z największych
    std::ofstream wynik2("wyniki4_2.txt");
    std::println(wynik2, "{} {}", najwiecej - wystapienia.begin(), *najwiecej);

    // 4.3
    std::vector<std::string> telefony;
    for (const std::string& liczba : liczby) {
        if (liczba.size() == 9) {
            telefony.push_back(liczba);
        }
    }
    std::ofstream wynik3("wyniki4_3.txt");
    for (const std::string& telefon : telefony) {
        if (telefon[0] == '5') {
            std::println(wynik3, "{}", telefon);
        }
    }

    // 4.4
    size_t najmniej = 10;
    for (const std::string& telefon : telefony) {
        najmniej = std::min(najmniej, rozne(telefon));
    }
    std::ofstream wynik4("wyniki4_4.txt");
    for (const std::string& telefon : telefony) {
        if (rozne(telefon) == najmniej) {
            std::println(wynik4, "{}", telefon);
        }
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
    static boolean cyfra(char znak) {
        return znak >= '0' && znak <= '9';
    }

    // liczba różnych cyfr w napisie
    static long rozne(String s) {
        return s.chars().distinct().count();
    }

    public static void main(String[] args) throws Exception {
        String napis = Files.readString(Path.of("dane.txt")).strip();

        // wydzielenie ukrytych liczb (maksymalnych ciągów cyfr)
        List<String> liczby = new ArrayList<>();
        String biezaca = "";
        for (char znak : (napis + " ").toCharArray()) {
            if (cyfra(znak)) {
                biezaca += znak;
            } else {
                if (!biezaca.equals("")) {
                    liczby.add(biezaca);
                }
                biezaca = "";
            }
        }

        // 4.1
        int ile = 0;
        for (String liczba : liczby) {
            if (liczba.startsWith("50")) {
                ile += 1;
            }
        }
        try (PrintWriter wynik = new PrintWriter("wyniki4_1.txt")) {
            wynik.println(ile);
        }

        // 4.2
        int[] wystapienia = new int[10];
        for (char znak : napis.toCharArray()) {
            if (cyfra(znak)) {
                wystapienia[znak - '0'] += 1;
            }
        }
        int najczestsza = 0;
        for (int c = 1; c < 10; c++) {
            if (wystapienia[c] > wystapienia[najczestsza]) {
                najczestsza = c;
            }
        }
        try (PrintWriter wynik = new PrintWriter("wyniki4_2.txt")) {
            wynik.println(najczestsza + " " + wystapienia[najczestsza]);
        }

        // 4.3
        List<String> telefony = new ArrayList<>();
        for (String liczba : liczby) {
            if (liczba.length() == 9) {
                telefony.add(liczba);
            }
        }
        try (PrintWriter wynik = new PrintWriter("wyniki4_3.txt")) {
            for (String telefon : telefony) {
                if (telefon.charAt(0) == '5') {
                    wynik.println(telefon);
                }
            }
        }

        // 4.4
        long najmniej = 10;
        for (String telefon : telefony) {
            najmniej = Math.min(najmniej, rozne(telefon));
        }
        try (PrintWriter wynik = new PrintWriter("wyniki4_4.txt")) {
            for (String telefon : telefony) {
                if (rozne(telefon) == najmniej) {
                    wynik.println(telefon);
                }
            }
        }
    }
}
```

**Odpowiedź:** 4.1: 4. 4.2: cyfra 1, 342 razy. 4.3: 588095244, 593151643, 583327270, 565269349, 583672019, 506585224, 574489008, 587103844, 510672749, 529135372, 515437684, 589477488. 4.4: 033035335, 050525250.
