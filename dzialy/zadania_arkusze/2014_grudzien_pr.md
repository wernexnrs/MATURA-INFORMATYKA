<h1 align="center">Matura próbna 2014 — grudzień (formuła od 2015)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/Czesc_1/A1Informatyka_PR_cz%C4%99%C5%9B%C4%87_I.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/Czesc_2/A1Informatyka_PR_cz%C4%99%C5%9B%C4%87_II.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/Czesc_2/Dane_Pr/DANE_PR.zip) --- [ODPOWIEDZI I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/A1A2A3A4A7Informatyka_PR_cz%C4%99%C5%9B%C4%87_I_model_odpowiedzi.pdf) --- [ODPOWIEDZI II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/A1A2A3A4A7Informatyka_PR_czesc_II_model_odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Zadanie 1. Liczby Armstronga. Liczba `n`-cyfrowa jest liczbą Armstronga (narcystyczną), jeśli równa się sumie swoich cyfr podniesionych do potęgi `n`, np. `153 = 1³ + 5³ + 3³`.
>
> - 1.1 — sprawdź (P/F), czy liczbami Armstronga są `6`, `407` i `2278`.
> - 1.2 — zapisz algorytm, który dla liczby całkowitej dodatniej `k` umieści jej cyfry w tablicy `tab_cyfr[]` od najmniej do najbardziej znaczącej i zwróci liczbę cyfr `n`. Przykład: `k = 54321` → `n = 5`, `tab_cyfr = [1,2,3,4,5]`.
> - 1.3 — zapisz algorytm sprawdzający, czy `k` jest liczbą narcystyczną, mając dane `k`, `n`, tablicę `tab_cyfr[]` (jak w 1.2) i funkcję `potega(a, n)`. Wynik: PRAWDA albo FAŁSZ.

```py
def cyfry(k):
    # 1.2 - cyfry od najmniej znaczacej, n - liczba cyfr
    tab_cyfr = []
    while True:
        tab_cyfr.append(k % 10)
        k = k // 10
        if k == 0:
            break
    return len(tab_cyfr), tab_cyfr


def czy_armstronga(k):
    # 1.3 - odejmujemy od k kolejne cyfry podniesione do potegi n
    n, tab_cyfr = cyfry(k)
    for j in range(n):
        k = k - tab_cyfr[j] ** n
    return k == 0


print(cyfry(54321))
for k in [6, 407, 2278]:
    print(k, "P" if czy_armstronga(k) else "F")
```

```cpp
// C++23
#include <print>
#include <vector>

// 1.2 - cyfry od najmniej znaczacej, n - liczba cyfr (n = tab_cyfr.size())
std::vector<int> cyfry(int k) {
    std::vector<int> tab_cyfr;
    while (true) {
        tab_cyfr.push_back(k % 10);
        k = k / 10;
        if (k == 0) break;
    }
    return tab_cyfr;
}

// potęga całkowita a^n
long long potega(int a, int n) {
    long long wynik = 1;
    for (int i = 0; i < n; i++) wynik *= a;
    return wynik;
}

bool czy_armstronga(long long k) {
    // 1.3 - odejmujemy od k kolejne cyfry podniesione do potegi n
    std::vector<int> tab_cyfr = cyfry(k);
    int n = tab_cyfr.size();
    for (int j = 0; j < n; j++) {
        k = k - potega(tab_cyfr[j], n);
    }
    return k == 0;
}

int main() {
    std::vector<int> c = cyfry(54321);
    std::println("({}, {})", c.size(), c);
    for (int k : {6, 407, 2278}) {
        std::println("{} {}", k, czy_armstronga(k) ? "P" : "F");
    }
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    // 1.2 - cyfry od najmniej znaczacej, n - liczba cyfr (n = tabCyfr.size())
    static List<Integer> cyfry(int k) {
        var tabCyfr = new ArrayList<Integer>();
        while (true) {
            tabCyfr.add(k % 10);
            k = k / 10;
            if (k == 0) break;
        }
        return tabCyfr;
    }

    static boolean czyArmstronga(int k) {
        // 1.3 - odejmujemy od k kolejne cyfry podniesione do potegi n
        var tabCyfr = cyfry(k);
        int n = tabCyfr.size();
        long reszta = k;
        for (int j = 0; j < n; j++) {
            long potega = 1;
            for (int p = 0; p < n; p++) potega *= tabCyfr.get(j);
            reszta = reszta - potega;
        }
        return reszta == 0;
    }

    public static void main(String[] args) throws Exception {
        var c = cyfry(54321);
        System.out.println("(" + c.size() + ", " + c + ")");
        for (int k : new int[]{6, 407, 2278}) {
            System.out.println(k + " " + (czyArmstronga(k) ? "P" : "F"));
        }
    }
}
```

**Odpowiedź:** 1.1: 6 — P, 407 — P, 2278 — F; dla k = 54321: n = 5, tab_cyfr = [1, 2, 3, 4, 5]

## 3.1 i 3.3

> **Treść zadania:** Zadanie 3. Kodowanie. Gdy tekst zawiera mniej niż 255 różnych znaków, można przypisać im kolejne kody binarne (większe od 0) o najmniejszej wystarczającej liczbie bitów i zapisać je jeden za drugim w bajtach; niewykorzystane bity ostatniego bajtu uzupełnia się zerami. Przykład: `HANIA` przy kodach `H=001, A=010, N=011, I=100` daje bajty `41` i `196`.
>
> - 3.1 — zdekoduj tekst zapisany w dwóch bajtach o wartościach dziesiętnych `110` i `64`, jeśli każdy znak ma 2 bity: `K=01`, `A=10`, `J=11`.
> - 3.3 — zapisz algorytm dekodowania: dane są tablica bajtów `v[]` o `n` elementach, liczba różnych znaków `r`, tablica par `{znak, kod}` `t[]` i liczba bitów na znak `bity`; wynikiem jest tekst źródłowy `s`. Można użyć funkcji `testBit(bajt, numerBitu)` (czy bit jest równy 1) oraz `ustawBit(bajt, numerBitu)` (ustawia bit na 1).

```py
def dekoduj(v, t, bity):
    # v - bajty tekstu skompresowanego, t - slownik {kod: znak}
    # bity czytamy od najstarszego bitu kazdego bajtu
    ciag_bitow = ""
    for bajt in v:
        ciag_bitow += bin(bajt)[2:].zfill(8)
    s = ""
    for i in range(0, len(ciag_bitow) - bity + 1, bity):
        kod = int(ciag_bitow[i:i + bity], 2)
        if kod in t:            # kod 0 to bity wolne na koncu
            s += t[kod]
    return s


print(bin(110)[2:].zfill(8), bin(64)[2:].zfill(8))
print(dekoduj([110, 64], {1: "K", 2: "A", 3: "J"}, 2))
print(dekoduj([41, 196], {1: "H", 2: "A", 3: "N", 4: "I"}, 3))
```

```cpp
// C++23
#include <map>
#include <print>
#include <string>
#include <vector>

// zapis binarny bajtu na 8 bitach (jak bin(x)[2:].zfill(8))
std::string bin8(int x) {
    std::string s = "";
    for (int i = 7; i >= 0; i--) s += char('0' + ((x >> i) & 1));
    return s;
}

std::string dekoduj(const std::vector<int>& v, std::map<int, char> t, int bity) {
    // v - bajty tekstu skompresowanego, t - slownik {kod: znak}
    // bity czytamy od najstarszego bitu kazdego bajtu
    std::string ciag_bitow = "";
    for (int bajt : v) ciag_bitow += bin8(bajt);
    std::string s = "";
    for (int i = 0; i + bity <= (int)ciag_bitow.size(); i += bity) {
        int kod = std::stoi(ciag_bitow.substr(i, bity), nullptr, 2);
        if (t.contains(kod)) s += t[kod];  // kod 0 to bity wolne na koncu
    }
    return s;
}

int main() {
    std::println("{} {}", bin8(110), bin8(64));
    std::println("{}", dekoduj({110, 64}, {{1, 'K'}, {2, 'A'}, {3, 'J'}}, 2));
    std::println("{}", dekoduj({41, 196}, {{1, 'H'}, {2, 'A'}, {3, 'N'}, {4, 'I'}}, 3));
}
```

```java
// Java 25
import java.util.Map;

public class Zadanie {
    // zapis binarny bajtu na 8 bitach (jak bin(x)[2:].zfill(8))
    static String bin8(int x) {
        String s = Integer.toBinaryString(x);
        return "0".repeat(8 - s.length()) + s;
    }

    static String dekoduj(int[] v, Map<Integer, String> t, int bity) {
        // v - bajty tekstu skompresowanego, t - slownik {kod: znak}
        // bity czytamy od najstarszego bitu kazdego bajtu
        var ciagBitow = new StringBuilder();
        for (int bajt : v) ciagBitow.append(bin8(bajt));
        var s = new StringBuilder();
        for (int i = 0; i + bity <= ciagBitow.length(); i += bity) {
            int kod = Integer.parseInt(ciagBitow.substring(i, i + bity), 2);
            if (t.containsKey(kod)) s.append(t.get(kod));  // kod 0 to bity wolne na koncu
        }
        return s.toString();
    }

    public static void main(String[] args) throws Exception {
        System.out.println(bin8(110) + " " + bin8(64));
        System.out.println(dekoduj(new int[]{110, 64}, Map.of(1, "K", 2, "A", 3, "J"), 2));
        System.out.println(dekoduj(new int[]{41, 196}, Map.of(1, "H", 2, "A", 3, "N", 4, "I"), 3));
    }
}
```

**Odpowiedź:** 3.1: 01101110 01000000 — KAJAK

## 3.2

> **Treść zadania:** Kodowanie tekstu jak w zadaniu 3. Zapisz algorytm, który dla łańcucha znaków `s` zwraca liczbę `r` różnych znaków w tym tekście (zakładamy `r < 100`).

```py
def rozne_znaki(s):
    R = []
    for znak in s:
        if znak not in R:
            R.append(znak)
    return len(R)


print(rozne_znaki("AAAABBBCCCBBBAAACC"), rozne_znaki("HANIA"))
```

```cpp
// C++23
#include <algorithm>
#include <print>
#include <string>
#include <vector>

int rozne_znaki(const std::string& s) {
    std::vector<char> R;
    for (char znak : s) {
        if (std::ranges::find(R, znak) == R.end()) R.push_back(znak);
    }
    return R.size();
}

int main() {
    std::println("{} {}", rozne_znaki("AAAABBBCCCBBBAAACC"), rozne_znaki("HANIA"));
}
```

```java
// Java 25
import java.util.ArrayList;

public class Zadanie {
    static int rozneZnaki(String s) {
        var R = new ArrayList<Character>();
        for (char znak : s.toCharArray()) {
            if (!R.contains(znak)) R.add(znak);
        }
        return R.size();
    }

    public static void main(String[] args) throws Exception {
        System.out.println(rozneZnaki("AAAABBBCCCBBBAAACC") + " " + rozneZnaki("HANIA"));
    }
}
```

**Odpowiedź:** dla "HANIA" r = 4

## 4.1 i 4.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 4. Wirujący dysk i mrówka. Ruch punktu po okręgu o środku `(0,0)` opisują wzory `x = r·sin(2πt/T)`, `y = r·cos(2πt/T)`, gdzie `r` — promień, `t` — czas, `T` — okres obiegu. Wyniki zapisz w pliku `dysk_mrowka.txt`, poprzedzając każdy numerem zadania.
>
> - 4.1 — dla `r = 5`, `T = 12,5` i kroku czasowego `Δt = 0,05`, zaczynając od `t = 3`, podaj, po jakim czasie (z dokładnością do setnych sekundy) współrzędna `y` mrówki stanie się większa od `x`.
> - 4.3 — mrówka idzie od środka obracającej się tarczy wzdłuż promienia z prędkością `v`, więc `r = v·t` i jej torem jest spirala (jak w zadaniu 4.2: `T = 10`, `v = 1`). Dla `Δt = 0,5` oblicz łączną długość odcinków łączących kolejne punkty toru w ciągu pierwszych 10 sekund, zaczynając od `(0,0)`. Wynik podaj z dokładnością do 4 miejsc po przecinku.

```py
import math

# 4.1 - x = r*sin(2*pi*t/T), y = r*cos(2*pi*t/T)
r, T, dt, t_pocz = 5, 12.5, 0.05, 3
krok = 0
while True:
    t = t_pocz + krok * dt
    x = r * math.sin(2 * math.pi * t / T)
    y = r * math.cos(2 * math.pi * t / T)
    if y > x:
        print("4.1", round(t - t_pocz, 2), "(czas od poczatku ruchu:", round(t, 2), ")")
        break
    krok += 1

# 4.3 - spirala r = v*t, T = 10, dt = 0,5, pierwsze 10 sekund
T, dt, v = 10, 0.5, 1
punkty = []
for i in range(21):
    t = i * dt
    punkty.append((v * t * math.sin(2 * math.pi * t / T), v * t * math.cos(2 * math.pi * t / T)))

dlugosc = 0
for i in range(1, len(punkty)):
    dlugosc += math.dist(punkty[i - 1], punkty[i])
print("4.3", f"{dlugosc:.4f}")
```

```cpp
// C++23
#include <cmath>
#include <format>
#include <numbers>
#include <print>
#include <string>
#include <utility>
#include <vector>

// liczba rzeczywista wypisana tak jak w Pythonie (np. 4.85, 3.0)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find('.') == std::string::npos) s += ".0";
    return s;
}

// round(x, 2) z Pythona
double zaokraglij2(double x) {
    return std::stod(std::format("{:.2f}", x));
}

int main() {
    const double pi = std::numbers::pi;

    // 4.1 - x = r*sin(2*pi*t/T), y = r*cos(2*pi*t/T)
    double r = 5, T = 12.5, dt = 0.05, t_pocz = 3;
    int krok = 0;
    while (true) {
        double t = t_pocz + krok * dt;
        double x = r * std::sin(2 * pi * t / T);
        double y = r * std::cos(2 * pi * t / T);
        if (y > x) {
            std::println("4.1 {} (czas od poczatku ruchu: {} )", jak_python(zaokraglij2(t - t_pocz)),
                         jak_python(zaokraglij2(t)));
            break;
        }
        krok++;
    }

    // 4.3 - spirala r = v*t, T = 10, dt = 0,5, pierwsze 10 sekund
    T = 10, dt = 0.5;
    double v = 1;
    std::vector<std::pair<double, double>> punkty;
    for (int i = 0; i < 21; i++) {
        double t = i * dt;
        punkty.push_back({v * t * std::sin(2 * pi * t / T), v * t * std::cos(2 * pi * t / T)});
    }

    double dlugosc = 0;
    for (size_t i = 1; i < punkty.size(); i++) {
        dlugosc += std::hypot(punkty[i].first - punkty[i - 1].first, punkty[i].second - punkty[i - 1].second);
    }
    std::println("4.3 {:.4f}", dlugosc);
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Locale;

public class Zadanie {
    // round(x, 2) z Pythona
    static double zaokraglij2(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).doubleValue();
    }

    public static void main(String[] args) throws Exception {
        // 4.1 - x = r*sin(2*pi*t/T), y = r*cos(2*pi*t/T)
        double r = 5, T = 12.5, dt = 0.05, tPocz = 3;
        int krok = 0;
        while (true) {
            double t = tPocz + krok * dt;
            double x = r * Math.sin(2 * Math.PI * t / T);
            double y = r * Math.cos(2 * Math.PI * t / T);
            if (y > x) {
                System.out.println("4.1 " + zaokraglij2(t - tPocz) + " (czas od poczatku ruchu: " + zaokraglij2(t) + " )");
                break;
            }
            krok++;
        }

        // 4.3 - spirala r = v*t, T = 10, dt = 0,5, pierwsze 10 sekund
        T = 10;
        dt = 0.5;
        double v = 1;
        var punkty = new ArrayList<double[]>();
        for (int i = 0; i < 21; i++) {
            double t = i * dt;
            punkty.add(new double[]{v * t * Math.sin(2 * Math.PI * t / T), v * t * Math.cos(2 * Math.PI * t / T)});
        }

        double dlugosc = 0;
        for (int i = 1; i < punkty.size(); i++) {
            dlugosc += Math.hypot(punkty.get(i)[0] - punkty.get(i - 1)[0], punkty.get(i)[1] - punkty.get(i - 1)[1]);
        }
        System.out.println("4.3 " + String.format(Locale.ROOT, "%.4f", dlugosc));
    }
}
```

**Odpowiedź:** 4.1: 4,85 s (czyli 7,85 s od początku ruchu); 4.3: 33,6520

## 4.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Wirujący dysk i mrówka jak w zadaniu 4. Mrówka startuje ze środka tarczy i idzie wzdłuż promienia z prędkością `v`, więc jej odległość od środka to `r = v·t`, a tor (dla obserwatora z zewnątrz) jest spiralą. Dla `T = 10`, `Δt = 0,5`, `v = 1` wykreśl tor ruchu mrówki w ciągu pierwszych 10 sekund i zapisz czytelny wykres w pliku.

```py
import math

# punkty spirali do wykresu punktowego (x, y) w arkuszu
with open("spirala_4_2.txt", "w") as wynik:
    wynik.write("t;x;y\n")
    for i in range(21):
        t = i * 0.5
        x = t * math.sin(2 * math.pi * t / 10)
        y = t * math.cos(2 * math.pi * t / 10)
        wynik.write(f"{t};{x:.4f};{y:.4f}\n")
```

```cpp
// C++23
#include <cmath>
#include <format>
#include <fstream>
#include <numbers>
#include <string>

// liczba rzeczywista wypisana tak jak w Pythonie (np. 0.5, 1.0)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find('.') == std::string::npos) s += ".0";
    return s;
}

int main() {
    const double pi = std::numbers::pi;
    // punkty spirali do wykresu punktowego (x, y) w arkuszu
    std::ofstream wynik("spirala_4_2.txt");
    wynik << "t;x;y\n";
    for (int i = 0; i < 21; i++) {
        double t = i * 0.5;
        double x = t * std::sin(2 * pi * t / 10);
        double y = t * std::cos(2 * pi * t / 10);
        wynik << std::format("{};{:.4f};{:.4f}\n", jak_python(t), x, y);
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.util.Locale;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        // punkty spirali do wykresu punktowego (x, y) w arkuszu
        try (var wynik = new PrintWriter("spirala_4_2.txt")) {
            wynik.print("t;x;y\n");
            for (int i = 0; i < 21; i++) {
                double t = i * 0.5;
                double x = t * Math.sin(2 * Math.PI * t / 10);
                double y = t * Math.cos(2 * Math.PI * t / 10);
                wynik.print(t + ";" + String.format(Locale.ROOT, "%.4f;%.4f", x, y) + "\n");
            }
        }
    }
}
```

**Odpowiedź:** wykres punktowy z liniami (spirala) tworzymy z pliku `spirala_4_2.txt`

## 5.1, 5.2 i 5.3

> **Treść zadania:** Zadanie 5. Zawody sportowe. W pliku `dziennik.txt` jest 310 liczb (po jednej w wierszu) — długości najlepszych skoków Mateusza w cm w kolejnych dniach treningowych. Pozytywna seria treningowa to maksymalny (nieprzedłużalny) ciąg kolejnych dni, w którym każdy wynik jest lepszy od poprzedniego. Przykład: w ciągu `478 475 470 480 481 481 475 477 480 482 470` najdłuższa seria to `475 477 480 482` (4 dni, poprawa o 7 cm). Odpowiedzi zapisz w pliku `wynik5.txt`, poprzedzając każdą numerem zadania.
>
> - 5.1 — podaj, ile było pozytywnych serii dłuższych niż 3 dni.
> - 5.2 — podaj długość najdłuższego i najkrótszego skoku oraz numery tych wyników (licząc od początku dziennika).
> - 5.3 — podaj długość (w dniach) najdłuższej pozytywnej serii i o ile centymetrów Mateusz poprawił w niej wynik.

```py
wyniki = []
with open("dziennik.txt") as file:
    for line in file:
        if line.strip():
            wyniki.append(int(line))

# 5.1 i 5.3 - pozytywne serie: (dlugosc, poprawa)
serie = []
poczatek = 0
for i in range(1, len(wyniki) + 1):
    if i == len(wyniki) or wyniki[i] <= wyniki[i - 1]:
        serie.append((i - poczatek, wyniki[i - 1] - wyniki[poczatek]))
        poczatek = i

print("5.1", sum(1 for dlugosc, poprawa in serie if dlugosc > 3))

najdluzszy = max(wyniki)
najkrotszy = min(wyniki)
print("5.2", najdluzszy, wyniki.index(najdluzszy) + 1, najkrotszy, wyniki.index(najkrotszy) + 1)

print("5.3", *max(serie))
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <utility>
#include <vector>

int main() {
    std::vector<int> wyniki;
    std::ifstream plik("dziennik.txt");
    int liczba;
    while (plik >> liczba) wyniki.push_back(liczba);
    int n = wyniki.size();

    // 5.1 i 5.3 - pozytywne serie: (dlugosc, poprawa)
    std::vector<std::pair<int, int>> serie;
    int poczatek = 0;
    for (int i = 1; i <= n; i++) {
        if (i == n || wyniki[i] <= wyniki[i - 1]) {
            serie.push_back({i - poczatek, wyniki[i - 1] - wyniki[poczatek]});
            poczatek = i;
        }
    }

    int ile = 0;
    for (auto [dlugosc, poprawa] : serie) {
        if (dlugosc > 3) ile++;
    }
    std::println("5.1 {}", ile);

    // max_element/min_element zwracają pierwsze wystąpienie (jak index w Pythonie)
    auto najdluzszy = std::ranges::max_element(wyniki);
    auto najkrotszy = std::ranges::min_element(wyniki);
    std::println("5.2 {} {} {} {}", *najdluzszy, najdluzszy - wyniki.begin() + 1, *najkrotszy,
                 najkrotszy - wyniki.begin() + 1);

    auto najlepsza = std::ranges::max(serie);  // porównanie par: najpierw długość, potem poprawa
    std::println("5.3 {} {}", najlepsza.first, najlepsza.second);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var wyniki = new ArrayList<Integer>();
        for (String line : Files.readAllLines(Path.of("dziennik.txt"))) {
            if (!line.isBlank()) wyniki.add(Integer.parseInt(line.strip()));
        }
        int n = wyniki.size();

        // 5.1 i 5.3 - pozytywne serie: {dlugosc, poprawa}
        var serie = new ArrayList<int[]>();
        int poczatek = 0;
        for (int i = 1; i <= n; i++) {
            if (i == n || wyniki.get(i) <= wyniki.get(i - 1)) {
                serie.add(new int[]{i - poczatek, wyniki.get(i - 1) - wyniki.get(poczatek)});
                poczatek = i;
            }
        }

        int ile = 0;
        for (int[] seria : serie) {
            if (seria[0] > 3) ile++;
        }
        System.out.println("5.1 " + ile);

        int najdluzszy = Collections.max(wyniki);
        int najkrotszy = Collections.min(wyniki);
        System.out.println("5.2 " + najdluzszy + " " + (wyniki.indexOf(najdluzszy) + 1) + " " + najkrotszy + " "
                + (wyniki.indexOf(najkrotszy) + 1));

        // porównanie par: najpierw długość, potem poprawa
        int[] najlepsza = serie.get(0);
        for (int[] seria : serie) {
            if (seria[0] > najlepsza[0] || (seria[0] == najlepsza[0] && seria[1] > najlepsza[1])) najlepsza = seria;
        }
        System.out.println("5.3 " + najlepsza[0] + " " + najlepsza[1]);
    }
}
```

**Odpowiedź:** 5.1: 11; 5.2: najdłuższy 601 (176. wynik), najkrótszy 401 (17. wynik); 5.3: 6 dni, poprawa o 158 cm
