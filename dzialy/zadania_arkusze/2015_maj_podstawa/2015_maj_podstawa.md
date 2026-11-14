<h1 align="center">Matura 2015 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa-odpowiedzi.pdf)

## 1.1

> **Treść zadania:** Systemy pozycyjne. W systemie szóstkowym liczby zapisuje się cyframi 0–5 (np. 8 = 12₆, 39 = 103₆, 216 = 1000₆).
>
> Wszystkie liczby w poniższych działaniach są zapisane w systemie szóstkowym. Uzupełnij brakujące argumenty (też w systemie szóstkowym) tak, aby wyniki były poprawne:
> - `10 * ____ = 1000`
> - `425 − ____ = 41`
> - `154 / ____ = 55`

```py
def na_szostkowy(x):
    wynik = ""
    while x > 0:
        wynik = str(x % 6) + wynik
        x = x // 6
    return wynik


print(na_szostkowy(int("1000", 6) // int("10", 6)))  # 10 * ? = 1000
print(na_szostkowy(int("425", 6) - int("41", 6)))  # 425 - ? = 41
print(na_szostkowy(int("154", 6) // int("55", 6)))  # 154 / ? = 55
```

```cpp
// C++23
#include <iostream>
#include <string>

std::string na_szostkowy(long long x) {
    std::string wynik = "";
    while (x > 0) {
        wynik = std::to_string(x % 6) + wynik;
        x = x / 6;
    }
    return wynik;
}

int main() {
    // std::stoll(napis, nullptr, 6) - zamiana z systemu szóstkowego, jak int(napis, 6) w Pythonie
    std::cout << na_szostkowy(std::stoll("1000", nullptr, 6) / std::stoll("10", nullptr, 6)) << '\n';  // 10 * ? = 1000
    std::cout << na_szostkowy(std::stoll("425", nullptr, 6) - std::stoll("41", nullptr, 6)) << '\n';   // 425 - ? = 41
    std::cout << na_szostkowy(std::stoll("154", nullptr, 6) / std::stoll("55", nullptr, 6)) << '\n';  // 154 / ? = 55
}
```

```java
// Java 25
public class Zadanie {
    static String naSzostkowy(long x) {
        String wynik = "";
        while (x > 0) {
            wynik = (x % 6) + wynik;
            x = x / 6;
        }
        return wynik;
    }

    public static void main(String[] args) {
        // Long.parseLong(napis, 6) - zamiana z systemu szóstkowego, jak int(napis, 6) w Pythonie
        System.out.println(naSzostkowy(Long.parseLong("1000", 6) / Long.parseLong("10", 6)));  // 10 * ? = 1000
        System.out.println(naSzostkowy(Long.parseLong("425", 6) - Long.parseLong("41", 6)));   // 425 - ? = 41
        System.out.println(naSzostkowy(Long.parseLong("154", 6) / Long.parseLong("55", 6)));  // 154 / ? = 55
    }
}
```
**Odpowiedź:** 10 * 100 = 1000, 425 − 344 = 41, 154 / 2 = 55

## 1.2

> **Treść zadania:** Zapisz (listą kroków, schematem blokowym lub w języku programowania) algorytm obliczający wartość liczby zapisanej w systemie szóstkowym.
>
> Specyfikacja:
> - Dane: `d` — dodatnia liczba całkowita, długość zapisu liczby w systemie szóstkowym; `C[1..d]` — kolejne cyfry tego zapisu, poczynając od cyfry najmniej znaczącej.
> - Wynik: `w` — wartość liczby.
>
> Przykład: dla d = 4 i C = [0, 0, 0, 1] wynikiem jest w = 216.

```py
def wartosc(d, C):  # C[0] - cyfra najmniej znacząca
    w = 0
    for i in range(d - 1, -1, -1):
        w = w * 6 + C[i]
    return w


print(wartosc(4, [0, 0, 0, 1]))
```

```cpp
// C++23
#include <iostream>
#include <vector>

long long wartosc(int d, const std::vector<int>& C) {  // C[0] - cyfra najmniej znacząca
    long long w = 0;
    for (int i = d - 1; i >= 0; i--)
        w = w * 6 + C[i];
    return w;
}

int main() {
    std::cout << wartosc(4, {0, 0, 0, 1}) << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static long wartosc(int d, int[] C) {  // C[0] - cyfra najmniej znacząca
        long w = 0;
        for (int i = d - 1; i >= 0; i--)
            w = w * 6 + C[i];
        return w;
    }

    public static void main(String[] args) {
        System.out.println(wartosc(4, new int[] {0, 0, 0, 1}));
    }
}
```
**Odpowiedź:** dla d = 4 i C = [0, 0, 0, 1] → 216

## 2.1

> **Treść zadania:** Dwie tablice. Dane: dodatnie liczby całkowite `n`, `k` oraz tablica `A[1..n]` liczb całkowitych z przedziału ⟨1, k⟩. Wynik: tablica `T[1..k]` liczb z przedziału ⟨0, n⟩. Algorytm:
>
> ```
> Krok 1. dla i = 1, 2, ..., k wykonaj T[i] ← 0
> Krok 2. dla i = 1, 2, ..., n wykonaj
>           pozycja ← A[i]
>           T[pozycja] ← T[pozycja] + 1
> ```
>
> Podaj zawartość tablicy T dla danych:
> - n = 6, k = 6, A = [3, 5, 6, 2, 1, 4],
> - n = 7, k = 4, A = [2, 3, 4, 2, 3, 1, 2],
> - n = 7, k = 3, A = [3, 2, 3, 2, 3, 2, 3],
> - n = 5, k = 8, A = [3, 3, 1, 5, 8].
>
> Uzupełnij też specyfikację: co oznacza wartość T[i] (dla 1 ≤ i ≤ k).

```py
def zlicz(n, k, A):
    T = [0] * (k + 1)  # T[0] nieużywane
    for i in range(n):
        pozycja = A[i]
        T[pozycja] = T[pozycja] + 1
    return T[1:]


print(zlicz(6, 6, [3, 5, 6, 2, 1, 4]))
print(zlicz(7, 4, [2, 3, 4, 2, 3, 1, 2]))
print(zlicz(7, 3, [3, 2, 3, 2, 3, 2, 3]))
print(zlicz(5, 8, [3, 3, 1, 5, 8]))
```

```cpp
// C++23
#include <iostream>
#include <string>
#include <vector>

std::vector<int> zlicz(int n, int k, const std::vector<int>& A) {
    std::vector<int> T(k + 1, 0);  // T[0] nieużywane
    for (int i = 0; i < n; i++) {
        int pozycja = A[i];
        T[pozycja] = T[pozycja] + 1;
    }
    return std::vector<int>(T.begin() + 1, T.end());
}

std::string jako_lista(const std::vector<int>& T) {  // zapis jak lista w Pythonie
    std::string s = "[";
    for (size_t i = 0; i < T.size(); i++) {
        if (i > 0) s += ", ";
        s += std::to_string(T[i]);
    }
    return s + "]";
}

int main() {
    std::cout << jako_lista(zlicz(6, 6, {3, 5, 6, 2, 1, 4})) << '\n';
    std::cout << jako_lista(zlicz(7, 4, {2, 3, 4, 2, 3, 1, 2})) << '\n';
    std::cout << jako_lista(zlicz(7, 3, {3, 2, 3, 2, 3, 2, 3})) << '\n';
    std::cout << jako_lista(zlicz(5, 8, {3, 3, 1, 5, 8})) << '\n';
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static int[] zlicz(int n, int k, int[] A) {
        int[] T = new int[k + 1];  // T[0] nieużywane
        for (int i = 0; i < n; i++) {
            int pozycja = A[i];
            T[pozycja] = T[pozycja] + 1;
        }
        return Arrays.copyOfRange(T, 1, k + 1);
    }

    public static void main(String[] args) {
        // Arrays.toString daje zapis [1, 2, 3] - taki sam jak lista w Pythonie
        System.out.println(Arrays.toString(zlicz(6, 6, new int[] {3, 5, 6, 2, 1, 4})));
        System.out.println(Arrays.toString(zlicz(7, 4, new int[] {2, 3, 4, 2, 3, 1, 2})));
        System.out.println(Arrays.toString(zlicz(7, 3, new int[] {3, 2, 3, 2, 3, 2, 3})));
        System.out.println(Arrays.toString(zlicz(5, 8, new int[] {3, 3, 1, 5, 8})));
    }
}
```
**Odpowiedź:** T[i] to liczba wystąpień liczby i w tablicy A; [1, 1, 1, 1, 1, 1], [1, 3, 2, 1], [0, 3, 4], [1, 0, 2, 0, 1, 0, 0, 1]

## 2.2

> **Treść zadania:** Korzystając z algorytmu z zadania 2.1, zapisz algorytm, który znajdzie element występujący w tablicy A najczęściej, tzn. taki, którego liczba wystąpień jest większa od liczby wystąpień każdego innego elementu (zakładamy, że taki element zawsze istnieje).
>
> Specyfikacja — dane: dodatnie liczby całkowite `n`, `k` i tablica `A[1..n]` liczb z przedziału ⟨1, k⟩; wynik: `y` — element występujący w A najczęściej.
>
> Przykład: dla [1, 2, 3, 2, 2] wynikiem jest 2, a dla [1, 2, 3, 3, 2, 3, 3, 3] — 3.

```py
def najczestszy(n, k, A):
    T = [0] * (k + 1)
    for i in range(n):
        T[A[i]] += 1
    y = 1
    for i in range(2, k + 1):
        if T[i] > T[y]:
            y = i
    return y


print(najczestszy(5, 3, [1, 2, 3, 2, 2]))
print(najczestszy(8, 3, [1, 2, 3, 3, 2, 3, 3, 3]))
```

```cpp
// C++23
#include <iostream>
#include <vector>

int najczestszy(int n, int k, const std::vector<int>& A) {
    std::vector<int> T(k + 1, 0);
    for (int i = 0; i < n; i++)
        T[A[i]] += 1;
    int y = 1;
    for (int i = 2; i <= k; i++)
        if (T[i] > T[y])
            y = i;
    return y;
}

int main() {
    std::cout << najczestszy(5, 3, {1, 2, 3, 2, 2}) << '\n';
    std::cout << najczestszy(8, 3, {1, 2, 3, 3, 2, 3, 3, 3}) << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static int najczestszy(int n, int k, int[] A) {
        int[] T = new int[k + 1];
        for (int i = 0; i < n; i++)
            T[A[i]] += 1;
        int y = 1;
        for (int i = 2; i <= k; i++)
            if (T[i] > T[y])
                y = i;
        return y;
    }

    public static void main(String[] args) {
        System.out.println(najczestszy(5, 3, new int[] {1, 2, 3, 2, 2}));
        System.out.println(najczestszy(8, 3, new int[] {1, 2, 3, 3, 2, 3, 3, 3}));
    }
}
```
**Odpowiedź:** 2 oraz 3 (dla przykładów z treści)

## 4.1

> **Treść zadania:** Fabryka GAZELA produkuje od 2005 roku samochody czterech marek. W I kwartale 2005 roku wyprodukowano: Dama — 237, Granta — 198, Dorkas — 207, Lodera — 312 sztuk.
> - Do końca 2009 roku produkcja co kwartał rosła względem poprzedniego kwartału: Dama o 2%, Granta o 2,7%, Dorkas o 3%, Lodera o 2%.
> - W 2010 roku produkcja w każdym kwartale była taka sama jak w ostatnim kwartale 2009 roku.
> - W latach 2011–2012 produkcja co kwartał malała: Dama o 1%, Granta o 1,2%, Dorkas o 1,9%, Lodera o 2,5%.
>
> Wszystkie obliczane wartości zaokrąglaj w dół do liczb całkowitych. Odpowiedzi (poza wykresem z 4.5) zapisz w pliku `wynik4.txt`, poprzedzając je numerem zadania.
>
> Ile samochodów każdej marki wyprodukowano w ostatnim kwartale 2011 roku?

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
marki = ["Dama", "Granta", "Dorkas", "Lodera"]
start = [237, 198, 207, 312]
wzrost = [1020, 1027, 1030, 1020]  # w promilach: +2%, +2,7%, +3%, +2%
spadek = [990, 988, 981, 975]  # -1%, -1,2%, -1,9%, -2,5%


def produkcja(m):  # lista produkcji w kolejnych kwartałach 2005-2012
    kwartaly = [start[m]]
    for _ in range(19):  # do końca 2009 roku
        kwartaly.append(kwartaly[-1] * wzrost[m] // 1000)
    for _ in range(4):  # 2010 - bez zmian
        kwartaly.append(kwartaly[-1])
    for _ in range(8):  # 2011 i 2012 - spadek
        kwartaly.append(kwartaly[-1] * spadek[m] // 1000)
    return kwartaly


for m in range(4):
    print(marki[m], produkcja(m)[27])  # IV kwartał 2011 to kwartał nr 28
```

```cpp
// C++23
#include <iostream>
#include <string>
#include <vector>

const std::vector<std::string> marki = {"Dama", "Granta", "Dorkas", "Lodera"};
const std::vector<long long> start = {237, 198, 207, 312};
const std::vector<long long> wzrost = {1020, 1027, 1030, 1020};  // w promilach: +2%, +2,7%, +3%, +2%
const std::vector<long long> spadek = {990, 988, 981, 975};      // -1%, -1,2%, -1,9%, -2,5%

std::vector<long long> produkcja(int m) {  // lista produkcji w kolejnych kwartałach 2005-2012
    std::vector<long long> kwartaly = {start[m]};
    for (int i = 0; i < 19; i++)  // do końca 2009 roku
        kwartaly.push_back(kwartaly.back() * wzrost[m] / 1000);
    for (int i = 0; i < 4; i++)  // 2010 - bez zmian
        kwartaly.push_back(kwartaly.back());
    for (int i = 0; i < 8; i++)  // 2011 i 2012 - spadek
        kwartaly.push_back(kwartaly.back() * spadek[m] / 1000);
    return kwartaly;
}

int main() {
    for (int m = 0; m < 4; m++)
        std::cout << marki[m] << ' ' << produkcja(m)[27] << '\n';  // IV kwartał 2011 to kwartał nr 28
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static String[] marki = {"Dama", "Granta", "Dorkas", "Lodera"};
    static long[] start = {237, 198, 207, 312};
    static long[] wzrost = {1020, 1027, 1030, 1020};  // w promilach: +2%, +2,7%, +3%, +2%
    static long[] spadek = {990, 988, 981, 975};      // -1%, -1,2%, -1,9%, -2,5%

    static List<Long> produkcja(int m) {  // lista produkcji w kolejnych kwartałach 2005-2012
        var kwartaly = new ArrayList<Long>(List.of(start[m]));
        for (int i = 0; i < 19; i++)  // do końca 2009 roku
            kwartaly.add(kwartaly.getLast() * wzrost[m] / 1000);
        for (int i = 0; i < 4; i++)  // 2010 - bez zmian
            kwartaly.add(kwartaly.getLast());
        for (int i = 0; i < 8; i++)  // 2011 i 2012 - spadek
            kwartaly.add(kwartaly.getLast() * spadek[m] / 1000);
        return kwartaly;
    }

    public static void main(String[] args) {
        for (int m = 0; m < 4; m++)
            System.out.println(marki[m] + " " + produkcja(m).get(27));  // IV kwartał 2011 to kwartał nr 28
    }
}
```
**Odpowiedź:** Dama 317, Granta 300, Dorkas 322, Lodera 398

## 4.2

> **Treść zadania:** Dane jak w zadaniu 4.1 (produkcja czterech marek w kolejnych kwartałach, wartości zaokrąglane w dół). Załóż, że w kolejnych latach produkcja spada tak samo jak w latach 2011–2012. Wskaż markę, której kwartalna produkcja najwcześniej stanie się mniejsza od jej produkcji z I kwartału 2005 roku. Podaj markę, liczbę wyprodukowanych wtedy samochodów oraz kwartał i rok.

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
marki = ["Dama", "Granta", "Dorkas", "Lodera"]
start = [237, 198, 207, 312]
wzrost = [1020, 1027, 1030, 1020]
spadek = [990, 988, 981, 975]

najwczesniej = None
for m in range(4):
    kwartaly = [start[m]]
    for _ in range(19):
        kwartaly.append(kwartaly[-1] * wzrost[m] // 1000)
    for _ in range(4):
        kwartaly.append(kwartaly[-1])
    while kwartaly[-1] >= start[m]:  # spadek trwa aż do zejścia poniżej produkcji z I kw. 2005
        kwartaly.append(kwartaly[-1] * spadek[m] // 1000)
    numer = len(kwartaly) - 1  # numer kwartału liczony od 0 (I kw. 2005)
    if najwczesniej is None or numer < najwczesniej[0]:
        najwczesniej = (numer, marki[m], kwartaly[-1])

numer, marka, liczba = najwczesniej
print(marka, liczba, "kwartał:", numer % 4 + 1, "rok:", 2005 + numer // 4)
```

```cpp
// C++23
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> marki = {"Dama", "Granta", "Dorkas", "Lodera"};
    std::vector<long long> start = {237, 198, 207, 312};
    std::vector<long long> wzrost = {1020, 1027, 1030, 1020};
    std::vector<long long> spadek = {990, 988, 981, 975};

    int naj_numer = -1;  // -1 oznacza "jeszcze nic" (None w Pythonie)
    std::string naj_marka;
    long long naj_liczba = 0;
    for (int m = 0; m < 4; m++) {
        std::vector<long long> kwartaly = {start[m]};
        for (int i = 0; i < 19; i++)
            kwartaly.push_back(kwartaly.back() * wzrost[m] / 1000);
        for (int i = 0; i < 4; i++)
            kwartaly.push_back(kwartaly.back());
        while (kwartaly.back() >= start[m])  // spadek trwa aż do zejścia poniżej produkcji z I kw. 2005
            kwartaly.push_back(kwartaly.back() * spadek[m] / 1000);
        int numer = kwartaly.size() - 1;  // numer kwartału liczony od 0 (I kw. 2005)
        if (naj_numer == -1 || numer < naj_numer) {
            naj_numer = numer;
            naj_marka = marki[m];
            naj_liczba = kwartaly.back();
        }
    }
    std::cout << naj_marka << ' ' << naj_liczba << " kwartał: " << naj_numer % 4 + 1
              << " rok: " << 2005 + naj_numer / 4 << '\n';
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    public static void main(String[] args) {
        String[] marki = {"Dama", "Granta", "Dorkas", "Lodera"};
        long[] start = {237, 198, 207, 312};
        long[] wzrost = {1020, 1027, 1030, 1020};
        long[] spadek = {990, 988, 981, 975};

        int najNumer = -1;  // -1 oznacza "jeszcze nic" (None w Pythonie)
        String najMarka = "";
        long najLiczba = 0;
        for (int m = 0; m < 4; m++) {
            var kwartaly = new ArrayList<Long>(List.of(start[m]));
            for (int i = 0; i < 19; i++)
                kwartaly.add(kwartaly.getLast() * wzrost[m] / 1000);
            for (int i = 0; i < 4; i++)
                kwartaly.add(kwartaly.getLast());
            while (kwartaly.getLast() >= start[m])  // spadek trwa aż do zejścia poniżej produkcji z I kw. 2005
                kwartaly.add(kwartaly.getLast() * spadek[m] / 1000);
            int numer = kwartaly.size() - 1;  // numer kwartału liczony od 0 (I kw. 2005)
            if (najNumer == -1 || numer < najNumer) {
                najNumer = numer;
                najMarka = marki[m];
                najLiczba = kwartaly.getLast();
            }
        }
        System.out.println(najMarka + " " + najLiczba + " kwartał: " + (najNumer % 4 + 1) + " rok: " + (2005 + najNumer / 4));
    }
}
```
**Odpowiedź:** Lodera, 305 sztuk, II kwartał 2014 roku

## 4.3 i 4.4

> **Treść zadania:** Dane jak w zadaniu 4.1 (produkcja czterech marek w kolejnych kwartałach 2005–2012, wartości zaokrąglane w dół).
> - 4.3 — Podaj dla każdej marki, w ilu kwartałach od początku 2005 do końca 2012 roku produkcja przekraczała 300 sztuk.
> - 4.4 — Podaj, ile samochodów łącznie wyprodukowano w fabryce do końca 2010 roku.
> - (4.5 — utwórz czytelny wykres kolumnowy 3D produkcji każdej marki w kolejnych latach 2005–2012.)

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
marki = ["Dama", "Granta", "Dorkas", "Lodera"]
start = [237, 198, 207, 312]
wzrost = [1020, 1027, 1030, 1020]
spadek = [990, 988, 981, 975]

razem_do_2010 = 0
for m in range(4):
    kwartaly = [start[m]]
    for _ in range(19):
        kwartaly.append(kwartaly[-1] * wzrost[m] // 1000)
    for _ in range(4):
        kwartaly.append(kwartaly[-1])
    for _ in range(8):
        kwartaly.append(kwartaly[-1] * spadek[m] // 1000)

    ponad_300 = 0
    for x in kwartaly:
        if x > 300:
            ponad_300 += 1
    print("4.3", marki[m], ponad_300)

    razem_do_2010 += sum(kwartaly[:24])  # 24 kwartały: 2005-2010

print("4.4", razem_do_2010)
```

```cpp
// C++23
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> marki = {"Dama", "Granta", "Dorkas", "Lodera"};
    std::vector<long long> start = {237, 198, 207, 312};
    std::vector<long long> wzrost = {1020, 1027, 1030, 1020};
    std::vector<long long> spadek = {990, 988, 981, 975};

    long long razem_do_2010 = 0;
    for (int m = 0; m < 4; m++) {
        std::vector<long long> kwartaly = {start[m]};
        for (int i = 0; i < 19; i++)
            kwartaly.push_back(kwartaly.back() * wzrost[m] / 1000);
        for (int i = 0; i < 4; i++)
            kwartaly.push_back(kwartaly.back());
        for (int i = 0; i < 8; i++)
            kwartaly.push_back(kwartaly.back() * spadek[m] / 1000);

        int ponad_300 = 0;
        for (long long x : kwartaly)
            if (x > 300) ponad_300++;
        std::cout << "4.3 " << marki[m] << ' ' << ponad_300 << '\n';

        for (int i = 0; i < 24; i++)  // 24 kwartały: 2005-2010
            razem_do_2010 += kwartaly[i];
    }
    std::cout << "4.4 " << razem_do_2010 << '\n';
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    public static void main(String[] args) {
        String[] marki = {"Dama", "Granta", "Dorkas", "Lodera"};
        long[] start = {237, 198, 207, 312};
        long[] wzrost = {1020, 1027, 1030, 1020};
        long[] spadek = {990, 988, 981, 975};

        long razemDo2010 = 0;
        for (int m = 0; m < 4; m++) {
            var kwartaly = new ArrayList<Long>(List.of(start[m]));
            for (int i = 0; i < 19; i++)
                kwartaly.add(kwartaly.getLast() * wzrost[m] / 1000);
            for (int i = 0; i < 4; i++)
                kwartaly.add(kwartaly.getLast());
            for (int i = 0; i < 8; i++)
                kwartaly.add(kwartaly.getLast() * spadek[m] / 1000);

            int ponad300 = 0;
            for (long x : kwartaly)
                if (x > 300) ponad300++;
            System.out.println("4.3 " + marki[m] + " " + ponad300);

            for (int i = 0; i < 24; i++)  // 24 kwartały: 2005-2010
                razemDo2010 += kwartaly.get(i);
        }
        System.out.println("4.4 " + razemDo2010);
    }
}
```
**Odpowiedź:** 4.3: Dama 18, Granta 9, Dorkas 17, Lodera 32; 4.4: 29368 (wykres 4.5 wykonuje się w arkuszu kalkulacyjnym)

## 5.1

> **Treść zadania:** W pliku `slowa.txt` jest 1000 słów, a w pliku `nowe.txt` — 25 słów. Słowa składają się z małych liter alfabetu łacińskiego, mają co najwyżej 12 znaków, każde w osobnym wierszu. Odpowiedzi zapisz w pliku `wynik5.txt`, poprzedzając je numerem zadania.
>
> Dla każdego n od 1 do 12 wyznacz, ile wierszy pliku `slowa.txt` zawiera słowa n-literowe. Wypisz w osobnych wierszach pary: n oraz liczba takich słów.

```py
dlugosci = [0] * 13

with open("slowa.txt") as file:
    for line in file:
        slowo = line.strip()
        dlugosci[len(slowo)] += 1

for n in range(1, 13):
    print(n, dlugosci[n])
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<int> dlugosci(13, 0);
    std::ifstream plik("slowa.txt");
    std::string slowo;
    while (plik >> slowo)
        dlugosci[slowo.size()] += 1;

    for (int n = 1; n < 13; n++)
        std::cout << n << ' ' << dlugosci[n] << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int[] dlugosci = new int[13];
        for (var line : Files.readAllLines(Path.of("slowa.txt")))
            dlugosci[line.strip().length()] += 1;

        for (int n = 1; n < 13; n++)
            System.out.println(n + " " + dlugosci[n]);
    }
}
```
**Odpowiedź:** 1 84, 2 65, 3 92, 4 75, 5 104, 6 75, 7 95, 8 71, 9 81, 10 62, 11 102, 12 94

## 5.2

> **Treść zadania:** Pliki `slowa.txt` (1000 słów) i `nowe.txt` (25 słów). Dla każdego słowa z `nowe.txt` wypisz to słowo oraz dwie liczby oddzielone spacją:
> - liczbę wystąpień tego słowa w pliku `slowa.txt`,
> - liczbę wystąpień jego odbicia lustrzanego (słowa czytanego od końca, np. „mapa” → „apam”) w pliku `slowa.txt`.
>
> Słowo jednoliterowe jest swoim własnym odbiciem lustrzanym. Odpowiedź zapisz w `wynik5.txt`.

```py
slowa = []

with open("slowa.txt") as file:
    for line in file:
        slowa.append(line.strip())

with open("nowe.txt") as file:
    for line in file:
        slowo = line.strip()
        print(slowo, slowa.count(slowo), slowa.count(slowo[::-1]))
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> slowa;
    std::ifstream plik("slowa.txt");
    std::string slowo;
    while (plik >> slowo)
        slowa.push_back(slowo);

    std::ifstream nowe("nowe.txt");
    while (nowe >> slowo) {
        std::string odwrocone(slowo.rbegin(), slowo.rend());
        std::cout << slowo << ' ' << std::ranges::count(slowa, slowo) << ' '
                  << std::ranges::count(slowa, odwrocone) << '\n';
    }
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var slowa = new ArrayList<String>();
        for (var line : Files.readAllLines(Path.of("slowa.txt")))
            slowa.add(line.strip());

        for (var line : Files.readAllLines(Path.of("nowe.txt"))) {
            var slowo = line.strip();
            var odwrocone = new StringBuilder(slowo).reverse().toString();
            System.out.println(slowo + " " + Collections.frequency(slowa, slowo) + " " + Collections.frequency(slowa, odwrocone));
        }
    }
}
```
**Odpowiedź:** hxqsf 4 5, erraegrdsj 0 0, cpcxpzj 3 1, arphlqleftqm 10 1, wdt 0 4, … , rceij 5 0
