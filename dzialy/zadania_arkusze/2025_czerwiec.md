<h1 align="center">Matura 2025 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

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
> - 1.1 — Podaj wynik f(a, b) dla par (42, 2), (4, 125), (103, 104).
> - 1.2 — Ile łącznie razy zostanie wywołana funkcja f, jeśli pierwszym wywołaniem jest f(987654321, 123456789)?
> - 1.3 — Ile łącznie razy zostanie wykonana instrukcja w ← w + a, jeśli pierwszym wywołaniem jest a) f(2024, 1000), b) f(2024, 1234)?

```py
def skroc(x):
    return x // 10


def dopisz(x):
    return x * 10


def ostatnia(x):
    return x % 10


wywolania = 0
dodawania = 0


def f(a, b):
    global wywolania, dodawania
    wywolania += 1
    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b))
    w = dopisz(w)
    while k > 0:
        w = w + a
        dodawania += 1
        k = k - 1
    return w


# 1.1
for a, b in [(42, 2), (4, 125), (103, 104)]:
    print(a, b, f(a, b))

# 1.2
wywolania = 0
f(987654321, 123456789)
print("1.2", wywolania)

# 1.3
for a, b in [(2024, 1000), (2024, 1234)]:
    dodawania = 0
    f(a, b)
    print("1.3", a, b, dodawania)
```

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

long long skroc(long long x) {
    return x / 10;
}

long long dopisz(long long x) {
    return x * 10;
}

long long ostatnia(long long x) {
    return x % 10;
}

int wywolania = 0;
int dodawania = 0;

long long f(long long a, long long b) {
    wywolania += 1;
    if (b == 0) {
        return 0;
    }
    long long k = ostatnia(b);
    long long w = f(a, skroc(b));
    w = dopisz(w);
    while (k > 0) {
        w = w + a;
        dodawania += 1;
        k = k - 1;
    }
    return w;
}

int main() {
    // 1.1
    std::vector<std::pair<long long, long long>> pary = {{42, 2}, {4, 125}, {103, 104}};
    for (auto [a, b] : pary) {
        std::println("{} {} {}", a, b, f(a, b));
    }

    // 1.2 (wynik a * b nie mieści się w int - stąd long long)
    wywolania = 0;
    f(987654321, 123456789);
    std::println("1.2 {}", wywolania);

    // 1.3
    std::vector<std::pair<long long, long long>> pary3 = {{2024, 1000}, {2024, 1234}};
    for (auto [a, b] : pary3) {
        dodawania = 0;
        f(a, b);
        std::println("1.3 {} {} {}", a, b, dodawania);
    }
}
```

```java
// Java 25
public class Zadanie {
    static long skroc(long x) {
        return x / 10;
    }

    static long dopisz(long x) {
        return x * 10;
    }

    static long ostatnia(long x) {
        return x % 10;
    }

    static int wywolania = 0;
    static int dodawania = 0;

    static long f(long a, long b) {
        wywolania += 1;
        if (b == 0) {
            return 0;
        }
        long k = ostatnia(b);
        long w = f(a, skroc(b));
        w = dopisz(w);
        while (k > 0) {
            w = w + a;
            dodawania += 1;
            k = k - 1;
        }
        return w;
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        long[][] pary = {{42, 2}, {4, 125}, {103, 104}};
        for (long[] p : pary) {
            System.out.println(p[0] + " " + p[1] + " " + f(p[0], p[1]));
        }

        // 1.2 (wynik a * b nie mieści się w int - stąd long)
        wywolania = 0;
        f(987654321L, 123456789L);
        System.out.println("1.2 " + wywolania);

        // 1.3
        long[][] pary3 = {{2024, 1000}, {2024, 1234}};
        for (long[] p : pary3) {
            dodawania = 0;
            f(p[0], p[1]);
            System.out.println("1.3 " + p[0] + " " + p[1] + " " + dodawania);
        }
    }
}
```

**Odpowiedź:** 1.1: f(42, 2) = 84, f(4, 125) = 500, f(103, 104) = 10712 (funkcja liczy a · b). 1.2: 10. 1.3: a) 1, b) 10.

## 2.1

> **Treść zadania:** Operacja cięcia (dla liczb ≥ 10) dzieli zapis dziesiętny liczby na dwa niepuste fragmenty, np. 14379 można przeciąć na 1 i 4379, 14 i 379, 143 i 79, 1437 i 9 (fragment „02” ma wartość 2). Dla liczby k o parzystej liczbie cyfr cięcie na połowę daje liczbę a (lewa połowa cyfr) i b (prawa połowa).
>
> Napisz w pseudojęzyku lub wybranym języku algorytm, który dla dodatniej liczby całkowitej k o parzystej liczbie cyfr wyznaczy a i b powstałe przez cięcie na połowę (np. 123456 → a = 123, b = 456; 120056 → a = 120, b = 56). Algorytm może operować tylko na liczbach całkowitych i podstawowych operacjach arytmetycznych, bez funkcji wbudowanych (w szczególności bez konwersji na napisy).

```py
def polowy(k):
    dlugosc = 0
    x = k
    while x > 0:
        x = x // 10
        dlugosc = dlugosc + 1
    potega = 1
    for i in range(dlugosc // 2):
        potega = potega * 10
    a = k // potega
    b = k % potega
    return a, b


print(polowy(123456))
print(polowy(120056))
```

```cpp
// C++23
#include <print>
#include <utility>

std::pair<int, int> polowy(int k) {
    int dlugosc = 0;
    int x = k;
    while (x > 0) {
        x = x / 10;
        dlugosc = dlugosc + 1;
    }
    int potega = 1;
    for (int i = 0; i < dlugosc / 2; i++) {
        potega = potega * 10;
    }
    int a = k / potega;
    int b = k % potega;
    return {a, b};
}

int main() {
    // para wypisuje się w nawiasach, tak jak krotka w Pythonie: (123, 456)
    std::println("{}", polowy(123456));
    std::println("{}", polowy(120056));
}
```

```java
// Java 25
public class Zadanie {
    static int[] polowy(int k) {
        int dlugosc = 0;
        int x = k;
        while (x > 0) {
            x = x / 10;
            dlugosc = dlugosc + 1;
        }
        int potega = 1;
        for (int i = 0; i < dlugosc / 2; i++) {
            potega = potega * 10;
        }
        int a = k / potega;
        int b = k % potega;
        return new int[]{a, b};
    }

    public static void main(String[] args) throws Exception {
        for (int k : new int[]{123456, 120056}) {
            int[] p = polowy(k);
            System.out.println("(" + p[0] + ", " + p[1] + ")");
        }
    }
}
```

**Odpowiedź:** funkcja `polowy` (dla 123456 → a = 123, b = 456; dla 120056 → a = 120, b = 56).

## 2.2

> **Treść zadania:** Liczbę k o parzystej liczbie cyfr nazywamy połowicznie względnie pierwszą, gdy NWD liczb powstałych z cięcia jej zapisu na połowę (zob. 2.1) jest równy 1 (np. 3487: NWD(34, 87) = 1 — tak; 230095: NWD(230, 95) = 5 — nie). Plik `liczby1.txt` zawiera 500 dodatnich liczb całkowitych mających 4, 6 lub 8 cyfr, po jednej w wierszu.
>
> Napisz program, który poda, ile liczb z pliku jest połowicznie względnie pierwszych. Odpowiedź zapisz w pliku `wyniki2_2.txt`. Do testów służy plik `liczby1_przyklad.txt` (50 liczb).

```py
from math import gcd


def polowy(k):
    dlugosc = 0
    x = k
    while x > 0:
        x = x // 10
        dlugosc = dlugosc + 1
    potega = 10 ** (dlugosc // 2)
    return k // potega, k % potega


ile = 0
with open("liczby1.txt") as file:
    for wiersz in file:
        a, b = polowy(int(wiersz))
        if gcd(a, b) == 1:
            ile += 1
print(ile)
```

```cpp
// C++23
#include <fstream>
#include <numeric>
#include <print>
#include <utility>

std::pair<long long, long long> polowy(long long k) {
    int dlugosc = 0;
    long long x = k;
    while (x > 0) {
        x = x / 10;
        dlugosc = dlugosc + 1;
    }
    long long potega = 1;
    for (int i = 0; i < dlugosc / 2; i++) {
        potega *= 10;
    }
    return {k / potega, k % potega};
}

int main() {
    int ile = 0;
    std::ifstream plik("liczby1.txt");
    long long liczba;
    while (plik >> liczba) {
        auto [a, b] = polowy(liczba);
        if (std::gcd(a, b) == 1) {
            ile += 1;
        }
    }
    std::println("{}", ile);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static long[] polowy(long k) {
        int dlugosc = 0;
        long x = k;
        while (x > 0) {
            x = x / 10;
            dlugosc = dlugosc + 1;
        }
        long potega = 1;
        for (int i = 0; i < dlugosc / 2; i++) {
            potega *= 10;
        }
        return new long[]{k / potega, k % potega};
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws Exception {
        int ile = 0;
        for (String wiersz : Files.readAllLines(Path.of("liczby1.txt"))) {
            long[] p = polowy(Long.parseLong(wiersz.trim()));
            if (gcd(p[0], p[1]) == 1) {
                ile += 1;
            }
        }
        System.out.println(ile);
    }
}
```

**Odpowiedź:** 296.

## 2.3

> **Treść zadania:** Dla liczby całkowitej n ≥ 10 rozważamy wszystkie możliwe cięcia (zob. 2.1) zapisu liczby n². Stopniem Kaprekara liczby n nazywamy liczbę tych cięć, w których suma powstałych dwóch liczb jest mniejsza lub równa n. Przykłady: 89² = 7921 i żadne cięcie nie daje sumy ≤ 89, więc stopień wynosi 0; 2757² = 7601049 — warunek spełniają cięcia 760|1049 i 76|01049, więc stopień wynosi 2. Plik `liczby2.txt` zawiera 1000 liczb całkowitych z przedziału [10, 30000].
>
> Napisz program, który wyznaczy największy stopień Kaprekara wśród liczb z pliku oraz liczbę, która go ma (jest tylko jedna taka). Odpowiedź zapisz w pliku `wyniki2_3.txt`. Do testów służy plik `liczby2_przyklad.txt`.

```py
def stopien_kaprekara(n):
    kwadrat = str(n * n)
    stopien = 0
    for i in range(1, len(kwadrat)):
        a = int(kwadrat[:i])
        b = int(kwadrat[i:])
        if a + b <= n:
            stopien += 1
    return stopien


najlepszy_stopien = -1
najlepsza_liczba = 0
with open("liczby2.txt") as file:
    for wiersz in file:
        n = int(wiersz)
        s = stopien_kaprekara(n)
        if s > najlepszy_stopien:
            najlepszy_stopien = s
            najlepsza_liczba = n
print(najlepszy_stopien)
print(najlepsza_liczba)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

int stopien_kaprekara(long long n) {
    std::string kwadrat = std::to_string(n * n);
    int stopien = 0;
    for (size_t i = 1; i < kwadrat.size(); i++) {
        long long a = std::stoll(kwadrat.substr(0, i));
        long long b = std::stoll(kwadrat.substr(i));
        if (a + b <= n) {
            stopien += 1;
        }
    }
    return stopien;
}

int main() {
    int najlepszy_stopien = -1;
    long long najlepsza_liczba = 0;
    std::ifstream plik("liczby2.txt");
    long long n;
    while (plik >> n) {
        int s = stopien_kaprekara(n);
        if (s > najlepszy_stopien) {
            najlepszy_stopien = s;
            najlepsza_liczba = n;
        }
    }
    std::println("{}", najlepszy_stopien);
    std::println("{}", najlepsza_liczba);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    static int stopienKaprekara(long n) {
        String kwadrat = String.valueOf(n * n);
        int stopien = 0;
        for (int i = 1; i < kwadrat.length(); i++) {
            long a = Long.parseLong(kwadrat.substring(0, i));
            long b = Long.parseLong(kwadrat.substring(i));
            if (a + b <= n) {
                stopien += 1;
            }
        }
        return stopien;
    }

    public static void main(String[] args) throws Exception {
        int najlepszyStopien = -1;
        long najlepszaLiczba = 0;
        for (String wiersz : Files.readAllLines(Path.of("liczby2.txt"))) {
            long n = Long.parseLong(wiersz.trim());
            int s = stopienKaprekara(n);
            if (s > najlepszyStopien) {
                najlepszyStopien = s;
                najlepszaLiczba = n;
            }
        }
        System.out.println(najlepszyStopien);
        System.out.println(najlepszaLiczba);
    }
}
```

**Odpowiedź:** stopień 4, liczba 7746.

## 3.1, 3.2, 3.3 i 3.4

> **Treść zadania:** Plik `dane.txt` zawiera jeden napis złożony z 10 000 znaków (kody ASCII 33–126), wśród których ukryte są liczby. Liczba ukryta to niepusty ciąg cyfr, przed którym i za którym nie stoi cyfra (np. w `356xv@@4vdfvdfD#$%@@#245` ukryte są 356, 4 i 245). Numer telefonu to ukryta liczba złożona z dokładnie 9 cyfr. Odpowiedzi zapisz w plikach `wyniki3_1.txt` … `wyniki3_4.txt`. Plik `dane_przyklad.txt` (200 znaków) służy do testów.
>
> - 3.1 — Podaj, ile ukrytych liczb zaczyna się od cyfr `50` (każde wystąpienie liczymy osobno). Np. w `fs@dx+cd50450505VfF^&x50` są dwie takie liczby: 50450505 i 50.
> - 3.2 — Podaj najczęściej występującą w pliku cyfrę i liczbę jej wystąpień (jest jedna taka cyfra; dla pliku przykładowego: `0 17`).
> - 3.3 — Wypisz wszystkie numery telefonów zaczynające się od cyfry 5, w kolejności występowania w pliku.
> - 3.4 — Podaj te numery telefonów, które składają się z najmniejszej liczby różnych cyfr.

```py
with open("dane.txt") as file:
    napis = file.read().strip()

# wydzielenie liczb - maksymalnych ciągów cyfr
liczby = []
biezaca = ""
for znak in napis:
    if znak.isdigit():
        biezaca += znak
    else:
        if biezaca != "":
            liczby.append(biezaca)
        biezaca = ""
if biezaca != "":
    liczby.append(biezaca)

# 3.1
print("3.1", sum(1 for liczba in liczby if liczba.startswith("50")))

# 3.2
ile = [0] * 10
for znak in napis:
    if znak.isdigit():
        ile[int(znak)] += 1
najczestsza = ile.index(max(ile))
print("3.2", najczestsza, ile[najczestsza])

# 3.3
telefony = [liczba for liczba in liczby if len(liczba) == 9]
print("3.3")
for telefon in telefony:
    if telefon[0] == "5":
        print(telefon)

# 3.4
najmniej = min(len(set(telefon)) for telefon in telefony)
print("3.4")
for telefon in telefony:
    if len(set(telefon)) == najmniej:
        print(telefon)
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

int main() {
    std::ifstream plik("dane.txt");
    std::string napis;
    std::getline(plik, napis);
    while (!napis.empty() && std::isspace((unsigned char)napis.back())) {
        napis.pop_back();  // odpowiednik strip() - usuwa m.in. znak '\r'
    }

    // wydzielenie liczb - maksymalnych ciągów cyfr
    std::vector<std::string> liczby;
    std::string biezaca = "";
    for (char znak : napis) {
        if (std::isdigit((unsigned char)znak)) {
            biezaca += znak;
        } else {
            if (biezaca != "") {
                liczby.push_back(biezaca);
            }
            biezaca = "";
        }
    }
    if (biezaca != "") {
        liczby.push_back(biezaca);
    }

    // 3.1
    int ile50 = 0;
    for (const std::string& liczba : liczby) {
        if (liczba.starts_with("50")) {
            ile50 += 1;
        }
    }
    std::println("3.1 {}", ile50);

    // 3.2
    std::vector<int> ile(10, 0);
    for (char znak : napis) {
        if (std::isdigit((unsigned char)znak)) {
            ile[znak - '0'] += 1;
        }
    }
    int najczestsza = std::ranges::max_element(ile) - ile.begin();  // pierwsza z największych
    std::println("3.2 {} {}", najczestsza, ile[najczestsza]);

    // 3.3
    std::vector<std::string> telefony;
    for (const std::string& liczba : liczby) {
        if (liczba.size() == 9) {
            telefony.push_back(liczba);
        }
    }
    std::println("3.3");
    for (const std::string& telefon : telefony) {
        if (telefon[0] == '5') {
            std::println("{}", telefon);
        }
    }

    // 3.4 - liczba różnych cyfr w numerze
    auto rozne = [](const std::string& s) {
        return std::set<char>(s.begin(), s.end()).size();
    };
    size_t najmniej = 10;
    for (const std::string& telefon : telefony) {
        najmniej = std::min(najmniej, rozne(telefon));
    }
    std::println("3.4");
    for (const std::string& telefon : telefony) {
        if (rozne(telefon) == najmniej) {
            std::println("{}", telefon);
        }
    }
}
```

```java
// Java 25
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

        // wydzielenie liczb - maksymalnych ciągów cyfr
        List<String> liczby = new ArrayList<>();
        String biezaca = "";
        for (char znak : napis.toCharArray()) {
            if (cyfra(znak)) {
                biezaca += znak;
            } else {
                if (!biezaca.equals("")) {
                    liczby.add(biezaca);
                }
                biezaca = "";
            }
        }
        if (!biezaca.equals("")) {
            liczby.add(biezaca);
        }

        // 3.1
        int ile50 = 0;
        for (String liczba : liczby) {
            if (liczba.startsWith("50")) {
                ile50 += 1;
            }
        }
        System.out.println("3.1 " + ile50);

        // 3.2
        int[] ile = new int[10];
        for (char znak : napis.toCharArray()) {
            if (cyfra(znak)) {
                ile[znak - '0'] += 1;
            }
        }
        int najczestsza = 0;
        for (int c = 1; c < 10; c++) {
            if (ile[c] > ile[najczestsza]) {
                najczestsza = c;
            }
        }
        System.out.println("3.2 " + najczestsza + " " + ile[najczestsza]);

        // 3.3
        List<String> telefony = new ArrayList<>();
        for (String liczba : liczby) {
            if (liczba.length() == 9) {
                telefony.add(liczba);
            }
        }
        System.out.println("3.3");
        for (String telefon : telefony) {
            if (telefon.charAt(0) == '5') {
                System.out.println(telefon);
            }
        }

        // 3.4
        long najmniej = 10;
        for (String telefon : telefony) {
            najmniej = Math.min(najmniej, rozne(telefon));
        }
        System.out.println("3.4");
        for (String telefon : telefony) {
            if (rozne(telefon) == najmniej) {
                System.out.println(telefon);
            }
        }
    }
}
```

**Odpowiedź:** 3.1: 4. 3.2: cyfra 1, 342 wystąpienia. 3.3: 588095244, 593151643, 583327270, 565269349, 583672019, 506585224, 574489008, 587103844, 510672749, 529135372, 515437684, 589477488. 3.4: 033035335, 050525250 (po 3 różne cyfry).
