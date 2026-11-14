<h1 align="center">Matura próbna 2024 — grudzień (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2024-grudzien-probna-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2024-grudzien-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2024-grudzien-probna-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

> **Treść zadania:** Dla dodatniej liczby całkowitej n niech J(n) oznacza ciąg kolejnych pozycji jedynek w zapisie dwójkowym n, licząc pozycje od 1 od najmniej znaczącej (ostatniej) cyfry. Przykład: 19 = 10011₂, więc J(19) = (1, 2, 5).
>
> - 1.1 — Uzupełnij tabelę: podaj zapis dwójkowy i J(n) dla n = 6 oraz n = 42, a także liczbę n (i jej zapis dwójkowy), dla której J(n) = (1, 2, 4, 7).
> - 1.2 — Zapisz algorytm (w pseudojęzyku lub języku programowania), który dla dodatniej liczby całkowitej n wypisuje kolejne elementy ciągu J(n) (dla n = 19: 1, 2, 5). Wolno używać tylko zmiennych całkowitych, operacji arytmetycznych (+, −, ·, /, div, mod), porównań, instrukcji sterujących i własnych funkcji; zabronione są funkcje wbudowane, w szczególności konwersje typów.

```py
# 1.2 - wypisuje kolejne elementy J(n) (tylko operacje na liczbach całkowitych)
def J(n):
    pozycja = 1
    while n > 0:
        if n % 2 == 1:
            print(pozycja, end=" ")
        n = n // 2
        pozycja = pozycja + 1
    print()


# 1.1
for n in [19, 6, 42, 75]:
    print(n, bin(n)[2:], end=": ")
    J(n)
# brakująca liczba n dla J(n) = (1, 2, 4, 7): 2^0 + 2^1 + 2^3 + 2^6
print(1 + 2 + 8 + 64)
```

```cpp
// C++23
#include <print>
#include <string>
#include <vector>

// 1.2 - wypisuje kolejne elementy J(n) (tylko operacje na liczbach całkowitych)
void J(int n) {
    int pozycja = 1;
    while (n > 0) {
        if (n % 2 == 1) {
            std::print("{} ", pozycja);
        }
        n = n / 2;
        pozycja = pozycja + 1;
    }
    std::println();
}

int main() {
    // 1.1
    std::vector<int> liczby = {19, 6, 42, 75};
    for (int n : liczby) {
        std::print("{} {:b}: ", n, n);
        J(n);
    }
    // brakująca liczba n dla J(n) = (1, 2, 4, 7): 2^0 + 2^1 + 2^3 + 2^6
    std::println("{}", 1 + 2 + 8 + 64);
}
```

```java
// Java 25
public class Zadanie {
    // 1.2 - wypisuje kolejne elementy J(n) (tylko operacje na liczbach całkowitych)
    static void J(int n) {
        int pozycja = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                System.out.print(pozycja + " ");
            }
            n = n / 2;
            pozycja = pozycja + 1;
        }
        System.out.println();
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        int[] liczby = {19, 6, 42, 75};
        for (int n : liczby) {
            System.out.print(n + " " + Integer.toBinaryString(n) + ": ");
            J(n);
        }
        // brakująca liczba n dla J(n) = (1, 2, 4, 7): 2^0 + 2^1 + 2^3 + 2^6
        System.out.println(1 + 2 + 8 + 64);
    }
}
```

**Odpowiedź:** 1.1: J(6) = (2, 3); 42 = 101010₂, J(42) = (2, 4, 6); J(n) = (1, 2, 4, 7) dla n = 75 = 1001011₂. 1.2: funkcja `J`.

## 2.1 i 2.2

> **Treść zadania:** Dana jest funkcja rekurencyjna F(x, p), gdzie x jest nieujemną liczbą całkowitą, a p liczbą całkowitą spełniającą 1 < p < 10:
>
> ```
> F(x, p):
>     jeżeli x = 0
>         podaj wynik 0
>     w przeciwnym przypadku
>         c ← x mod p
>         jeżeli c mod 2 = 1
>             podaj wynik F(x div p, p) + c
>         w przeciwnym przypadku
>             podaj wynik F(x div p, p) − c
> ```
>
> - 2.1 — Uzupełnij tabelę: dla par (x, p) = (130, 3) oraz (220, 4) podaj wartość F(x, p) i łączną liczbę wywołań funkcji F (wliczając pierwsze). Przykład: F(125, 2) = 6, wywołań jest 8.
> - 2.2 — Dla p = 3 i p = 4 podaj największą liczbę x < 100, dla której F(x, p) = 0.

```py
wywolania = 0


def F(x, p):
    global wywolania
    wywolania += 1
    if x == 0:
        return 0
    c = x % p
    if c % 2 == 1:
        return F(x // p, p) + c
    return F(x // p, p) - c


# 2.1
for x, p in [(125, 2), (130, 3), (220, 4)]:
    wywolania = 0
    wynik = F(x, p)
    print(x, p, wynik, wywolania)

# 2.2 - największe x < 100, dla którego F(x, p) = 0
for p in [3, 4]:
    x = 99
    while F(x, p) != 0:
        x -= 1
    print(p, x)
```

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

int wywolania = 0;

int F(int x, int p) {
    wywolania += 1;
    if (x == 0) {
        return 0;
    }
    int c = x % p;
    if (c % 2 == 1) {
        return F(x / p, p) + c;
    }
    return F(x / p, p) - c;
}

int main() {
    // 2.1
    std::vector<std::pair<int, int>> dane = {{125, 2}, {130, 3}, {220, 4}};
    for (auto [x, p] : dane) {
        wywolania = 0;
        int wynik = F(x, p);
        std::println("{} {} {} {}", x, p, wynik, wywolania);
    }

    // 2.2 - największe x < 100, dla którego F(x, p) = 0
    for (int p : {3, 4}) {
        int x = 99;
        while (F(x, p) != 0) {
            x -= 1;
        }
        std::println("{} {}", p, x);
    }
}
```

```java
// Java 25
public class Zadanie {
    static int wywolania = 0;

    static int F(int x, int p) {
        wywolania += 1;
        if (x == 0) {
            return 0;
        }
        int c = x % p;
        if (c % 2 == 1) {
            return F(x / p, p) + c;
        }
        return F(x / p, p) - c;
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        int[][] dane = {{125, 2}, {130, 3}, {220, 4}};
        for (int[] para : dane) {
            int x = para[0], p = para[1];
            wywolania = 0;
            int wynik = F(x, p);
            System.out.println(x + " " + p + " " + wynik + " " + wywolania);
        }

        // 2.2 - największe x < 100, dla którego F(x, p) = 0
        for (int p : new int[]{3, 4}) {
            int x = 99;
            while (F(x, p) != 0) {
                x -= 1;
            }
            System.out.println(p + " " + x);
        }
    }
}
```

**Odpowiedź:** 2.1: F(130, 3) = 2 (6 wywołań), F(220, 4) = 7 (5 wywołań). 2.2: p = 3 → x = 96, p = 4 → x = 97.

## 3.1, 3.2 i 3.3

> **Treść zadania:** Plik `liczby.txt` zawiera 2000 różnych liczb całkowitych z zakresu [1000, 9999], każdą w osobnym wierszu. Odpowiedzi zapisz w pliku `wyniki3.txt`, poprzedzając każdą numerem zadania. Plik `liczby_przyklad.txt` zawiera 20 liczb do testów.
>
> - 3.1 — Znajdź liczby, które są kwadratami liczb całkowitych. Podaj, ile ich jest, oraz tę, która występuje w pliku jako pierwsza.
> - 3.2 — Wypisz wszystkie liczby z pliku, które mają co najmniej 5 różnych dzielników pierwszych (w pliku przykładowym jest jedna taka liczba: 2730).
> - 3.3 — Dla każdej liczby z jej czterech cyfr tworzymy największą i najmniejszą możliwą liczbę (zera traktujemy jak zwykłe cyfry, np. dla 2047: 7420 − 0247 = 7173) i obliczamy ich różnicę (dla 3151: 5311 − 1135 = 4176). Podaj, ile razy ta różnica jest mniejsza od danej liczby, ile razy większa, a ile razy równa, oraz wypisz każdą liczbę, dla której różnica jest jej równa. Dla pliku przykładowego: 8 razy mniejsza, 12 razy większa, ani razu równa.

```py
with open("liczby.txt") as file:
    liczby = [int(linia) for linia in file if linia.strip()]

# 3.1
kwadraty = []
for x in liczby:
    k = 1
    while k * k < x:
        k += 1
    if k * k == x:
        kwadraty.append(x)
print("3.1", len(kwadraty), kwadraty[0])


# 3.2
def rozne_dzielniki_pierwsze(n):
    ile = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            ile += 1
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ile += 1
    return ile


print("3.2")
for x in liczby:
    if rozne_dzielniki_pierwsze(x) >= 5:
        print(x)

# 3.3
mniejsze = 0
wieksze = 0
rowne = []
for x in liczby:
    cyfry = sorted(str(x))
    najmniejsza = int("".join(cyfry))
    najwieksza = int("".join(reversed(cyfry)))
    roznica = najwieksza - najmniejsza
    if roznica < x:
        mniejsze += 1
    elif roznica > x:
        wieksze += 1
    else:
        rowne.append(x)
print("3.3", mniejsze, wieksze, rowne)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <vector>

int rozne_dzielniki_pierwsze(int n) {
    int ile = 0;
    int d = 2;
    while (d * d <= n) {
        if (n % d == 0) {
            ile += 1;
            while (n % d == 0) {
                n /= d;
            }
        }
        d += 1;
    }
    if (n > 1) {
        ile += 1;
    }
    return ile;
}

int main() {
    std::ifstream plik("liczby.txt");
    std::vector<int> liczby;
    int x;
    while (plik >> x) {
        liczby.push_back(x);
    }

    // 3.1
    std::vector<int> kwadraty;
    for (int x : liczby) {
        int k = 1;
        while (k * k < x) {
            k += 1;
        }
        if (k * k == x) {
            kwadraty.push_back(x);
        }
    }
    std::println("3.1 {} {}", kwadraty.size(), kwadraty[0]);

    // 3.2
    std::println("3.2");
    for (int x : liczby) {
        if (rozne_dzielniki_pierwsze(x) >= 5) {
            std::println("{}", x);
        }
    }

    // 3.3
    int mniejsze = 0;
    int wieksze = 0;
    std::vector<int> rowne;
    for (int x : liczby) {
        std::string cyfry = std::to_string(x);
        std::ranges::sort(cyfry);
        int najmniejsza = std::stoi(cyfry);
        std::ranges::reverse(cyfry);
        int najwieksza = std::stoi(cyfry);
        int roznica = najwieksza - najmniejsza;
        if (roznica < x) {
            mniejsze += 1;
        } else if (roznica > x) {
            wieksze += 1;
        } else {
            rowne.push_back(x);
        }
    }
    std::println("3.3 {} {} {}", mniejsze, wieksze, rowne);  // wektor wypisze się jak lista: [6174]
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Zadanie {
    static int rozneDzielnikiPierwsze(int n) {
        int ile = 0;
        int d = 2;
        while (d * d <= n) {
            if (n % d == 0) {
                ile += 1;
                while (n % d == 0) {
                    n /= d;
                }
            }
            d += 1;
        }
        if (n > 1) {
            ile += 1;
        }
        return ile;
    }

    public static void main(String[] args) throws Exception {
        List<Integer> liczby = new ArrayList<>();
        for (String linia : Files.readAllLines(Path.of("liczby.txt"))) {
            if (!linia.isBlank()) {
                liczby.add(Integer.parseInt(linia.trim()));
            }
        }

        // 3.1
        List<Integer> kwadraty = new ArrayList<>();
        for (int x : liczby) {
            int k = 1;
            while (k * k < x) {
                k += 1;
            }
            if (k * k == x) {
                kwadraty.add(x);
            }
        }
        System.out.println("3.1 " + kwadraty.size() + " " + kwadraty.get(0));

        // 3.2
        System.out.println("3.2");
        for (int x : liczby) {
            if (rozneDzielnikiPierwsze(x) >= 5) {
                System.out.println(x);
            }
        }

        // 3.3
        int mniejsze = 0;
        int wieksze = 0;
        List<Integer> rowne = new ArrayList<>();
        for (int x : liczby) {
            char[] cyfry = String.valueOf(x).toCharArray();
            Arrays.sort(cyfry);
            String rosnaco = new String(cyfry);
            int najmniejsza = Integer.parseInt(rosnaco);
            int najwieksza = Integer.parseInt(new StringBuilder(rosnaco).reverse().toString());
            int roznica = najwieksza - najmniejsza;
            if (roznica < x) {
                mniejsze += 1;
            } else if (roznica > x) {
                wieksze += 1;
            } else {
                rowne.add(x);
            }
        }
        System.out.println("3.3 " + mniejsze + " " + wieksze + " " + rowne);  // lista wypisze się jako [6174]
    }
}
```

**Odpowiedź:** 3.1: 20 kwadratów, pierwszy to 4489. 3.2: 2730, 8190, 2310, 4620, 7770, 8610, 4830, 4290, 6930, 6630. 3.3: mniejszych 947, większych 1052, równa: 6174.

## 4.1, 4.2 i 4.3

> **Treść zadania:** Plik `prostokaty.txt` opisuje 5000 prostokątów, po jednym w wierszu: dwie dodatnie liczby całkowite nie większe niż 40 000, oddzielone spacją — wysokość h i szerokość s. Odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając każdą numerem zadania. Plik `prostokaty_przyklad.txt` zawiera 20 prostokątów do testów.
>
> - 4.1 — Podaj najmniejsze i największe pole prostokąta w pliku (dla pliku przykładowego: 252 i 9409).
> - 4.2 — Prostokąt (s, h) mieści się w prostokącie (s', h'), gdy s ≤ s' i h ≤ h'. Znajdź najdłuższy ciąg kolejnych prostokątów z pliku, w którym każdy prostokąt (poza pierwszym) mieści się w poprzednim. Podaj długość ciągu oraz wysokość i szerokość jego ostatniego prostokąta (dla pliku przykładowego: `4 83 5`).
> - 4.3 — Prostokąty o tej samej wysokości można sklejać: powstaje prostokąt o tej wysokości i szerokości równej sumie szerokości. Podaj największe szerokości, jakie można uzyskać, sklejając dokładnie 2, 3 i 5 prostokątów opisanych w różnych (niekoniecznie kolejnych) wierszach pliku (dla pliku przykładowego: 183, 266, 409).

```py
prostokaty = []
with open("prostokaty.txt") as file:
    for linia in file:
        if linia.strip():
            h, s = map(int, linia.split())
            prostokaty.append((h, s))

# 4.1
pola = [h * s for h, s in prostokaty]
print("4.1", min(pola), max(pola))

# 4.2
najdluzszy = 1
koniec = 0
dlugosc = 1
for i in range(1, len(prostokaty)):
    h, s = prostokaty[i]
    h_pop, s_pop = prostokaty[i - 1]
    if s <= s_pop and h <= h_pop:
        dlugosc += 1
    else:
        dlugosc = 1
    if dlugosc > najdluzszy:
        najdluzszy = dlugosc
        koniec = i
print("4.2", najdluzszy, prostokaty[koniec][0], prostokaty[koniec][1])

# 4.3 - dla każdej wysokości bierzemy k najszerszych prostokątów
szerokosci = {}
for h, s in prostokaty:
    if h not in szerokosci:
        szerokosci[h] = []
    szerokosci[h].append(s)
for k in [2, 3, 5]:
    najlepsza = 0
    for h in szerokosci:
        lista = sorted(szerokosci[h], reverse=True)
        if len(lista) >= k:
            najlepsza = max(najlepsza, sum(lista[:k]))
    print("4.3", k, najlepsza)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <functional>
#include <map>
#include <print>
#include <vector>

int main() {
    std::ifstream plik("prostokaty.txt");
    std::vector<std::pair<long long, long long>> prostokaty;
    long long h, s;
    while (plik >> h >> s) {
        prostokaty.push_back({h, s});
    }

    // 4.1 (pola nie mieszczą się bezpiecznie w int - używamy long long)
    long long najmniejsze = prostokaty[0].first * prostokaty[0].second;
    long long najwieksze = najmniejsze;
    for (auto [h, s] : prostokaty) {
        najmniejsze = std::min(najmniejsze, h * s);
        najwieksze = std::max(najwieksze, h * s);
    }
    std::println("4.1 {} {}", najmniejsze, najwieksze);

    // 4.2
    int najdluzszy = 1;
    int koniec = 0;
    int dlugosc = 1;
    for (size_t i = 1; i < prostokaty.size(); i++) {
        auto [h, s] = prostokaty[i];
        auto [h_pop, s_pop] = prostokaty[i - 1];
        if (s <= s_pop && h <= h_pop) {
            dlugosc += 1;
        } else {
            dlugosc = 1;
        }
        if (dlugosc > najdluzszy) {
            najdluzszy = dlugosc;
            koniec = i;
        }
    }
    std::println("4.2 {} {} {}", najdluzszy, prostokaty[koniec].first, prostokaty[koniec].second);

    // 4.3 - dla każdej wysokości bierzemy k najszerszych prostokątów
    std::map<long long, std::vector<long long>> szerokosci;
    for (auto [h, s] : prostokaty) {
        szerokosci[h].push_back(s);
    }
    for (int k : {2, 3, 5}) {
        long long najlepsza = 0;
        for (auto& [h, lista] : szerokosci) {
            std::vector<long long> posortowane = lista;
            std::ranges::sort(posortowane, std::greater<>());
            if ((int)posortowane.size() >= k) {
                long long suma = 0;
                for (int j = 0; j < k; j++) {
                    suma += posortowane[j];
                }
                najlepsza = std::max(najlepsza, suma);
            }
        }
        std::println("4.3 {} {}", k, najlepsza);
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        List<long[]> prostokaty = new ArrayList<>();
        for (String linia : Files.readAllLines(Path.of("prostokaty.txt"))) {
            if (!linia.isBlank()) {
                String[] t = linia.trim().split("\\s+");
                prostokaty.add(new long[]{Long.parseLong(t[0]), Long.parseLong(t[1])});
            }
        }

        // 4.1 (pola nie mieszczą się bezpiecznie w int - używamy long)
        long najmniejsze = Long.MAX_VALUE;
        long najwieksze = 0;
        for (long[] p : prostokaty) {
            najmniejsze = Math.min(najmniejsze, p[0] * p[1]);
            najwieksze = Math.max(najwieksze, p[0] * p[1]);
        }
        System.out.println("4.1 " + najmniejsze + " " + najwieksze);

        // 4.2
        int najdluzszy = 1;
        int koniec = 0;
        int dlugosc = 1;
        for (int i = 1; i < prostokaty.size(); i++) {
            long h = prostokaty.get(i)[0], s = prostokaty.get(i)[1];
            long hPop = prostokaty.get(i - 1)[0], sPop = prostokaty.get(i - 1)[1];
            if (s <= sPop && h <= hPop) {
                dlugosc += 1;
            } else {
                dlugosc = 1;
            }
            if (dlugosc > najdluzszy) {
                najdluzszy = dlugosc;
                koniec = i;
            }
        }
        System.out.println("4.2 " + najdluzszy + " " + prostokaty.get(koniec)[0] + " " + prostokaty.get(koniec)[1]);

        // 4.3 - dla każdej wysokości bierzemy k najszerszych prostokątów
        Map<Long, List<Long>> szerokosci = new HashMap<>();
        for (long[] p : prostokaty) {
            szerokosci.computeIfAbsent(p[0], klucz -> new ArrayList<>()).add(p[1]);
        }
        for (int k : new int[]{2, 3, 5}) {
            long najlepsza = 0;
            for (List<Long> lista : szerokosci.values()) {
                List<Long> posortowane = new ArrayList<>(lista);
                posortowane.sort(Comparator.reverseOrder());
                if (posortowane.size() >= k) {
                    long suma = 0;
                    for (int j = 0; j < k; j++) {
                        suma += posortowane.get(j);
                    }
                    najlepsza = Math.max(najlepsza, suma);
                }
            }
            System.out.println("4.3 " + k + " " + najlepsza);
        }
    }
}
```

**Odpowiedź:** 4.1: najmniejsze pole 10425, największe 1545605418. 4.2: `10 1001 627`. 4.3: 2 prostokąty: 79506, 3 prostokąty: 118786, 5 prostokątów: 180895.

## 6

> **Treść zadania:** Wykonaj działania na liczbach zapisanych w systemie piątkowym i podaj wyniki również w systemie piątkowym: 2024₅ + 1044₅ oraz 2024₅ − 1044₅.

```py
def na_dziesietny(napis, podstawa):
    liczba = 0
    for c in napis:
        liczba = liczba * podstawa + int(c)
    return liczba


def z_dziesietnego(liczba, podstawa):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % podstawa) + wynik
        liczba = liczba // podstawa
    return wynik


a = na_dziesietny("2024", 5)
b = na_dziesietny("1044", 5)
print(z_dziesietnego(a + b, 5), z_dziesietnego(a - b, 5))
```

```cpp
// C++23
#include <print>
#include <string>

long long na_dziesietny(const std::string& napis, int podstawa) {
    long long liczba = 0;
    for (char c : napis) {
        liczba = liczba * podstawa + (c - '0');
    }
    return liczba;
}

std::string z_dziesietnego(long long liczba, int podstawa) {
    std::string wynik = "";
    while (liczba > 0) {
        wynik = std::to_string(liczba % podstawa) + wynik;
        liczba = liczba / podstawa;
    }
    return wynik;
}

int main() {
    long long a = na_dziesietny("2024", 5);
    long long b = na_dziesietny("1044", 5);
    std::println("{} {}", z_dziesietnego(a + b, 5), z_dziesietnego(a - b, 5));
}
```

```java
// Java 25
public class Zadanie {
    static long naDziesietny(String napis, int podstawa) {
        long liczba = 0;
        for (char c : napis.toCharArray()) {
            liczba = liczba * podstawa + (c - '0');
        }
        return liczba;
    }

    static String zDziesietnego(long liczba, int podstawa) {
        String wynik = "";
        while (liczba > 0) {
            wynik = (liczba % podstawa) + wynik;
            liczba = liczba / podstawa;
        }
        return wynik;
    }

    public static void main(String[] args) throws Exception {
        long a = naDziesietny("2024", 5);
        long b = naDziesietny("1044", 5);
        System.out.println(zDziesietnego(a + b, 5) + " " + zDziesietnego(a - b, 5));
    }
}
```

**Odpowiedź:** 2024₅ + 1044₅ = 3123₅, 2024₅ − 1044₅ = 430₅.
