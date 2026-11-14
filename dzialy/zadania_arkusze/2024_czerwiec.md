<h1 align="center">Matura 2024 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

> **Treść zadania:** Mamy tablicę o w wierszach i k kolumnach oraz dodatnią liczbę n. Cyfry zapisu binarnego n wpisujemy wierszami od lewego górnego rogu; po wpisaniu ostatniej cyfry zaczynamy znowu od pierwszej, aż do zapełnienia tablicy. Szukamy cyfry w prawym dolnym rogu. Np. dla w = 5, k = 3, n = 19 (10011) w prawym dolnym rogu jest 1.
>
> - 1.1 — Wpisz cyfry binarne liczby n = 179 do tablicy o wymiarach w = 4, k = 5.
> - 1.2 — Zapisz algorytm, który dla dodatnich w, k, n wyznaczy cyfrę binarną stojącą w prawym dolnym rogu tablicy w × k. Wolno używać tylko podstawowych operacji arytmetycznych, porównań, odwołań do elementów tablicy i instrukcji sterujących (bez funkcji wbudowanych).

```py
# 1.1
def tablica(n, w, k):
    cyfry = bin(n)[2:]
    for i in range(w):
        wiersz = [cyfry[(i * k + j) % len(cyfry)] for j in range(k)]
        print(*wiersz)


tablica(179, 4, 5)


# 1.2 - tylko operacje arytmetyczne
def prawy_dolny(w, k, n):
    dl = 0             # liczba cyfr w zapisie binarnym n
    pom = n
    while pom > 0:
        pom = pom // 2
        dl = dl + 1
    poz = (w * k - 1) % dl   # pozycja cyfry w zapisie n, liczona od lewej od 0
    for i in range(dl - 1 - poz):
        n = n // 2
    return n % 2


print(prawy_dolny(5, 3, 19))
print(prawy_dolny(4, 5, 179))

# sprawdzenie z bezpośrednim wypełnianiem tablicy
for n in range(1, 300):
    for w in range(1, 8):
        for k in range(1, 8):
            cyfry = bin(n)[2:]
            assert prawy_dolny(w, k, n) == int(cyfry[(w * k - 1) % len(cyfry)])
```
```cpp
// C++23
#include <print>
#include <stdexcept>
#include <string>

std::string binarnie(int n) {
    std::string wynik;
    while (n > 0) {
        wynik = char('0' + n % 2) + wynik;
        n /= 2;
    }
    return wynik;
}

// 1.1
void tablica(int n, int w, int k) {
    std::string cyfry = binarnie(n);
    for (int i = 0; i < w; i++) {
        for (int j = 0; j < k; j++) {
            if (j > 0) std::print(" ");
            std::print("{}", cyfry[(i * k + j) % cyfry.size()]);
        }
        std::println();
    }
}

// 1.2 - tylko operacje arytmetyczne
int prawy_dolny(int w, int k, int n) {
    int dl = 0;  // liczba cyfr w zapisie binarnym n
    int pom = n;
    while (pom > 0) {
        pom = pom / 2;
        dl = dl + 1;
    }
    int poz = (w * k - 1) % dl;  // pozycja cyfry w zapisie n, liczona od lewej od 0
    for (int i = 0; i < dl - 1 - poz; i++) n = n / 2;
    return n % 2;
}

int main() {
    tablica(179, 4, 5);

    std::println("{}", prawy_dolny(5, 3, 19));
    std::println("{}", prawy_dolny(4, 5, 179));

    // sprawdzenie z bezpośrednim wypełnianiem tablicy
    for (int n = 1; n < 300; n++)
        for (int w = 1; w < 8; w++)
            for (int k = 1; k < 8; k++) {
                std::string cyfry = binarnie(n);
                if (prawy_dolny(w, k, n) != cyfry[(w * k - 1) % cyfry.size()] - '0')
                    throw std::logic_error("błąd dla n = " + std::to_string(n));
            }
}
```
```java
// Java 25
import java.util.*;

public class Zadanie {
    // 1.1
    static void tablica(int n, int w, int k) {
        String cyfry = Integer.toBinaryString(n);
        for (int i = 0; i < w; i++) {
            var wiersz = new ArrayList<String>();
            for (int j = 0; j < k; j++)
                wiersz.add(String.valueOf(cyfry.charAt((i * k + j) % cyfry.length())));
            System.out.println(String.join(" ", wiersz));
        }
    }

    // 1.2 - tylko operacje arytmetyczne
    static int prawyDolny(int w, int k, int n) {
        int dl = 0;  // liczba cyfr w zapisie binarnym n
        int pom = n;
        while (pom > 0) {
            pom = pom / 2;
            dl = dl + 1;
        }
        int poz = (w * k - 1) % dl;  // pozycja cyfry w zapisie n, liczona od lewej od 0
        for (int i = 0; i < dl - 1 - poz; i++) n = n / 2;
        return n % 2;
    }

    public static void main(String[] args) throws Exception {
        tablica(179, 4, 5);

        System.out.println(prawyDolny(5, 3, 19));
        System.out.println(prawyDolny(4, 5, 179));

        // sprawdzenie z bezpośrednim wypełnianiem tablicy
        for (int n = 1; n < 300; n++)
            for (int w = 1; w < 8; w++)
                for (int k = 1; k < 8; k++) {
                    String cyfry = Integer.toBinaryString(n);
                    if (prawyDolny(w, k, n) != cyfry.charAt((w * k - 1) % cyfry.length()) - '0')
                        throw new AssertionError("błąd dla n = " + n);
                }
    }
}
```

**Odpowiedź:** 1.1: 1 0 1 1 0 / 0 1 1 1 0 / 1 1 0 0 1 / 1 1 0 1 1. 1.2: funkcja `prawy_dolny` — w prawym dolnym rogu stoi cyfra o numerze (w · k − 1) mod (liczba cyfr n) licząc od lewej od 0 (dla w = 5, k = 3, n = 19 wynik 1).

## 2.1 i 2.2

> **Treść zadania:** Dana jest funkcja dla nieujemnej liczby całkowitej x:
>
> ```
> F(x):
>     jeżeli x = 0: wynikiem jest 0
>     w przeciwnym przypadku: wynikiem jest 2 + F(x div 2)
> ```
>
> - 2.1 — Dla x = 16 i x = 35 podaj wartość F(x) oraz łączną liczbę wywołań funkcji F (wliczając pierwsze). Przykład: x = 3 → F = 4, 3 wywołania.
> - 2.2 — Podaj najmniejszą i największą wartość x, dla której F(x) = 18.

```py
wywolania = 0


def F(x):
    global wywolania
    wywolania += 1
    if x == 0:
        return 0
    return 2 + F(x // 2)


# 2.1
for x in [3, 16, 35]:
    wywolania = 0
    print(x, F(x), wywolania)

# 2.2
x_18 = [x for x in range(2000) if F(x) == 18]
print(min(x_18), max(x_18))
```
```cpp
// C++23
#include <algorithm>
#include <print>
#include <vector>

int wywolania = 0;

int F(int x) {
    wywolania++;
    if (x == 0) return 0;
    return 2 + F(x / 2);
}

int main() {
    // 2.1
    for (int x : {3, 16, 35}) {
        wywolania = 0;
        int wynik = F(x);
        std::println("{} {} {}", x, wynik, wywolania);
    }

    // 2.2
    std::vector<int> x_18;
    for (int x = 0; x < 2000; x++)
        if (F(x) == 18) x_18.push_back(x);
    std::println("{} {}", std::ranges::min(x_18), std::ranges::max(x_18));
}
```
```java
// Java 25
import java.util.*;

public class Zadanie {
    static int wywolania = 0;

    static int F(int x) {
        wywolania++;
        if (x == 0) return 0;
        return 2 + F(x / 2);
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        for (int x : new int[] {3, 16, 35}) {
            wywolania = 0;
            int wynik = F(x);
            System.out.println(x + " " + wynik + " " + wywolania);
        }

        // 2.2
        var x18 = new ArrayList<Integer>();
        for (int x = 0; x < 2000; x++)
            if (F(x) == 18) x18.add(x);
        System.out.println(Collections.min(x18) + " " + Collections.max(x18));
    }
}
```

**Odpowiedź:** 2.1: 3 → 4, 3 wywołania; 16 → 10, 6 wywołań; 35 → 12, 7 wywołań. 2.2: najmniejsza 256, największa 511 (F(x) to podwojona liczba cyfr zapisu binarnego x, więc szukamy liczb 9-cyfrowych w systemie binarnym).

## 3.1, 3.2 i 3.3

> **Treść zadania:** Plik `slowa.txt` zawiera 1000 słów z małych liter alfabetu angielskiego, o długości od 1 do 200. Odpowiedzi zapisz w `wyniki3.txt`, poprzedzając je numerami zadań (przykład: `slowa_przyklad.txt`, 10 słów).
>
> - 3.1 — Podaj, w ilu słowach występuje fragment `k?t`, gdzie `?` to dowolna jedna litera (np. „alamakota”, „brokat”, ale nie „krata”). Przykład: 2.
> - 3.2 — ROT13 zamienia każdą literę na literę o 13 pozycji dalej (cyklicznie, a↔n, b↔o, …). Podaj, ile słów po zakodowaniu ROT13 staje się swoim odwróceniem (np. `aren` → `nera`), oraz wypisz najdłuższe z nich. Przykład: `2` i `aren`.
> - 3.3 — Wypisz wszystkie słowa, w których ta sama litera zajmuje co najmniej połowę pozycji (np. „owocowo” tak, „ambaras” nie). Przykład: terefere, ananas, bo, alabama.

```py
with open("slowa.txt") as file:
    slowa = [wiersz.strip() for wiersz in file]

# 3.1
ile = 0
for slowo in slowa:
    for i in range(len(slowo) - 2):
        if slowo[i] == "k" and slowo[i + 2] == "t":
            ile += 1
            break
print("3.1", ile)


# 3.2
def rot13(slowo):
    wynik = ""
    for litera in slowo:
        wynik += chr((ord(litera) - ord("a") + 13) % 26 + ord("a"))
    return wynik


dobre = [slowo for slowo in slowa if rot13(slowo) == slowo[::-1]]
print("3.2", len(dobre))
print(max(dobre, key=len))

# 3.3
print("3.3")
for slowo in slowa:
    for litera in set(slowo):
        if 2 * slowo.count(litera) >= len(slowo):
            print(slowo)
            break
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <vector>

// 3.2
std::string rot13(const std::string& slowo) {
    std::string wynik;
    for (char litera : slowo) wynik += (char)((litera - 'a' + 13) % 26 + 'a');
    return wynik;
}

int main() {
    std::vector<std::string> slowa;
    std::ifstream plik("slowa.txt");
    std::string linia;
    while (plik >> linia) slowa.push_back(linia);

    // 3.1
    int ile = 0;
    for (auto& slowo : slowa) {
        for (size_t i = 0; i + 2 < slowo.size(); i++) {
            if (slowo[i] == 'k' && slowo[i + 2] == 't') {
                ile++;
                break;
            }
        }
    }
    std::println("3.1 {}", ile);

    std::vector<std::string> dobre;
    for (auto& slowo : slowa) {
        std::string odwrocone(slowo.rbegin(), slowo.rend());
        if (rot13(slowo) == odwrocone) dobre.push_back(slowo);
    }
    std::println("3.2 {}", dobre.size());
    std::string najdluzsze = dobre[0];  // przy remisie pierwsze (jak max w Pythonie)
    for (auto& slowo : dobre)
        if (slowo.size() > najdluzsze.size()) najdluzsze = slowo;
    std::println("{}", najdluzsze);

    // 3.3
    std::println("3.3");
    for (auto& slowo : slowa) {
        for (char litera = 'a'; litera <= 'z'; litera++) {
            if (2 * std::count(slowo.begin(), slowo.end(), litera) >= (long)slowo.size()) {
                std::println("{}", slowo);
                break;
            }
        }
    }
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    // 3.2
    static String rot13(String slowo) {
        var wynik = new StringBuilder();
        for (char litera : slowo.toCharArray()) wynik.append((char) ((litera - 'a' + 13) % 26 + 'a'));
        return wynik.toString();
    }

    public static void main(String[] args) throws Exception {
        var slowa = new ArrayList<String>();
        for (var linia : Files.readAllLines(Path.of("slowa.txt"))) slowa.add(linia.strip());

        // 3.1
        int ile = 0;
        for (var slowo : slowa) {
            for (int i = 0; i + 2 < slowo.length(); i++) {
                if (slowo.charAt(i) == 'k' && slowo.charAt(i + 2) == 't') {
                    ile++;
                    break;
                }
            }
        }
        System.out.println("3.1 " + ile);

        var dobre = new ArrayList<String>();
        for (var slowo : slowa)
            if (rot13(slowo).equals(new StringBuilder(slowo).reverse().toString())) dobre.add(slowo);
        System.out.println("3.2 " + dobre.size());
        String najdluzsze = dobre.get(0);  // przy remisie pierwsze (jak max w Pythonie)
        for (var slowo : dobre)
            if (slowo.length() > najdluzsze.length()) najdluzsze = slowo;
        System.out.println(najdluzsze);

        // 3.3
        System.out.println("3.3");
        for (var slowo : slowa) {
            for (char litera = 'a'; litera <= 'z'; litera++) {
                final char l = litera;
                long ileLiter = slowo.chars().filter(c -> c == l).count();
                if (2 * ileLiter >= slowo.length()) {
                    System.out.println(slowo);
                    break;
                }
            }
        }
    }
}
```

**Odpowiedź:** 3.1: 26. 3.2: 5 słów, najdłuższe: rhszzohhubwbojohuubmmfue. 3.3: vzwzwgszezvzzlzzzzzzouz, azaaasfakaaaxbaaaaau, ppppppnoppnoclpop, zggggggpegpnovzgg, nyrpvqycpaylffffffffffffff, kkkkkkkkkkwpijccdbl, tstevttebttktnetitbttti, gvsvjvvvvvqppvuvcvvvi.

## 4.1

> **Treść zadania:** W sieci jest n > 1 komputerów; każdy ma ustalonego odbiorcę. W rundzie 0 każdy komputer ma jeden pakiet o swoim numerze. Na początku każdej rundy każdy komputer wysyła swojemu odbiorcy wszystkie pakiety, które miał po poprzedniej rundzie.
>
> Dla n = 6 komputerów o odbiorcach (kolejno dla komputerów 1–6): 3, 1, 6, 5, 4, 5 (po 1. rundzie pakiety 1–6 są w komputerach 3, 1, 6, 5, 4, 5) uzupełnij tabelę: podaj, w których komputerach znajdą się pakiety 1–6 po rundach 2, 3 i 4.

```py
odbiorca = [0, 3, 1, 6, 5, 4, 5]   # odbiorca[i] - odbiorca komputera i (indeks 0 pomijamy)
n = 6
pozycja = list(range(n + 1))       # pozycja[p] - komputer z pakietem p
for runda in range(1, 5):
    pozycja = [odbiorca[pozycja[p]] if p > 0 else 0 for p in range(n + 1)]
    print(runda, *pozycja[1:])
```
```cpp
// C++23
#include <print>
#include <vector>

int main() {
    std::vector<int> odbiorca = {0, 3, 1, 6, 5, 4, 5};  // odbiorca[i] - odbiorca komputera i (indeks 0 pomijamy)
    int n = 6;
    std::vector<int> pozycja(n + 1);  // pozycja[p] - komputer z pakietem p
    for (int p = 0; p <= n; p++) pozycja[p] = p;
    for (int runda = 1; runda < 5; runda++) {
        for (int p = 1; p <= n; p++) pozycja[p] = odbiorca[pozycja[p]];
        std::print("{}", runda);
        for (int p = 1; p <= n; p++) std::print(" {}", pozycja[p]);
        std::println();
    }
}
```
```java
// Java 25
public class Zadanie {
    public static void main(String[] args) throws Exception {
        int[] odbiorca = {0, 3, 1, 6, 5, 4, 5};  // odbiorca[i] - odbiorca komputera i (indeks 0 pomijamy)
        int n = 6;
        int[] pozycja = new int[n + 1];  // pozycja[p] - komputer z pakietem p
        for (int p = 0; p <= n; p++) pozycja[p] = p;
        for (int runda = 1; runda < 5; runda++) {
            for (int p = 1; p <= n; p++) pozycja[p] = odbiorca[pozycja[p]];
            var wiersz = new StringBuilder(String.valueOf(runda));
            for (int p = 1; p <= n; p++) wiersz.append(" ").append(pozycja[p]);
            System.out.println(wiersz);
        }
    }
}
```

**Odpowiedź:** po 2. rundzie: 6 3 5 4 5 4; po 3. rundzie: 5 6 4 5 4 5; po 4. rundzie: 4 5 5 4 5 4 (kolejno pakiety 1–6).

## 4.2, 4.3 i 4.4

> **Treść zadania:** Plik `odbiorcy.txt` zawiera numery odbiorców dla n = 1024 komputerów (wiersz i — odbiorca komputera i); zasady przesyłania pakietów jak w zadaniu 4.1. Odpowiedzi zapisz w `wyniki4.txt` z numerami zadań (przykład: `odbiorcy_przyklad.txt`, 16 wierszy).
>
> - 4.2 — Podaj liczbę komputerów, które nie są odbiorcami żadnych pakietów (przykład: 3).
> - 4.3 — Wyznacz najmniejszy numer rundy, w której jakikolwiek pakiet wraca do komputera, z którego wyruszył, i podaj najmniejszy numer takiego pakietu w tej rundzie (przykład: `3 7`).
> - 4.4 — Podaj największą liczbę pakietów znajdujących się w jednym komputerze po rundach 1, 2, 4 i 8 — cztery liczby w jednym wierszu, oddzielone spacjami (przykład: `2 2 3 4`).

```py
with open("odbiorcy.txt") as file:
    odbiorca = [0] + [int(wiersz) for wiersz in file]   # numeracja od 1
n = len(odbiorca) - 1

# 4.2
czy_odbiorca = [False] * (n + 1)
for i in range(1, n + 1):
    czy_odbiorca[odbiorca[i]] = True
print("4.2", czy_odbiorca[1:].count(False))

# 4.3
pozycja = list(range(n + 1))   # pozycja[p] - komputer, w którym jest pakiet p
runda = 0
znaleziony = 0
while znaleziony == 0:
    runda += 1
    for p in range(1, n + 1):
        pozycja[p] = odbiorca[pozycja[p]]
    for p in range(1, n + 1):
        if pozycja[p] == p:
            znaleziony = p
            break
print("4.3", runda, znaleziony)

# 4.4
pozycja = list(range(n + 1))
wyniki = []
for runda in range(1, 9):
    for p in range(1, n + 1):
        pozycja[p] = odbiorca[pozycja[p]]
    if runda in [1, 2, 4, 8]:
        ile = [0] * (n + 1)
        for p in range(1, n + 1):
            ile[pozycja[p]] += 1
        wyniki.append(max(ile))
print("4.4", *wyniki)
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <vector>

int main() {
    std::vector<int> odbiorca = {0};  // numeracja od 1
    std::ifstream plik("odbiorcy.txt");
    int x;
    while (plik >> x) odbiorca.push_back(x);
    int n = odbiorca.size() - 1;

    // 4.2
    std::vector<bool> czy_odbiorca(n + 1, false);
    for (int i = 1; i <= n; i++) czy_odbiorca[odbiorca[i]] = true;
    int nieodbierajace = 0;
    for (int i = 1; i <= n; i++)
        if (!czy_odbiorca[i]) nieodbierajace++;
    std::println("4.2 {}", nieodbierajace);

    // 4.3
    std::vector<int> pozycja(n + 1);  // pozycja[p] - komputer, w którym jest pakiet p
    for (int p = 0; p <= n; p++) pozycja[p] = p;
    int runda = 0;
    int znaleziony = 0;
    while (znaleziony == 0) {
        runda++;
        for (int p = 1; p <= n; p++) pozycja[p] = odbiorca[pozycja[p]];
        for (int p = 1; p <= n; p++) {
            if (pozycja[p] == p) {
                znaleziony = p;
                break;
            }
        }
    }
    std::println("4.3 {} {}", runda, znaleziony);

    // 4.4
    for (int p = 0; p <= n; p++) pozycja[p] = p;
    std::vector<int> wyniki;
    for (int runda = 1; runda < 9; runda++) {
        for (int p = 1; p <= n; p++) pozycja[p] = odbiorca[pozycja[p]];
        if (runda == 1 || runda == 2 || runda == 4 || runda == 8) {
            std::vector<int> ile(n + 1, 0);
            for (int p = 1; p <= n; p++) ile[pozycja[p]]++;
            wyniki.push_back(std::ranges::max(ile));
        }
    }
    std::print("4.4");
    for (int w : wyniki) std::print(" {}", w);
    std::println();
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var odbiorca = new ArrayList<Integer>();
        odbiorca.add(0);  // numeracja od 1
        for (var linia : Files.readAllLines(Path.of("odbiorcy.txt")))
            if (!linia.isBlank()) odbiorca.add(Integer.parseInt(linia.trim()));
        int n = odbiorca.size() - 1;

        // 4.2
        boolean[] czyOdbiorca = new boolean[n + 1];
        for (int i = 1; i <= n; i++) czyOdbiorca[odbiorca.get(i)] = true;
        int nieodbierajace = 0;
        for (int i = 1; i <= n; i++)
            if (!czyOdbiorca[i]) nieodbierajace++;
        System.out.println("4.2 " + nieodbierajace);

        // 4.3
        int[] pozycja = new int[n + 1];  // pozycja[p] - komputer, w którym jest pakiet p
        for (int p = 0; p <= n; p++) pozycja[p] = p;
        int runda = 0;
        int znaleziony = 0;
        while (znaleziony == 0) {
            runda++;
            for (int p = 1; p <= n; p++) pozycja[p] = odbiorca.get(pozycja[p]);
            for (int p = 1; p <= n; p++) {
                if (pozycja[p] == p) {
                    znaleziony = p;
                    break;
                }
            }
        }
        System.out.println("4.3 " + runda + " " + znaleziony);

        // 4.4
        for (int p = 0; p <= n; p++) pozycja[p] = p;
        var wyniki = new StringBuilder("4.4");
        for (int r = 1; r < 9; r++) {
            for (int p = 1; p <= n; p++) pozycja[p] = odbiorca.get(pozycja[p]);
            if (r == 1 || r == 2 || r == 4 || r == 8) {
                int[] ile = new int[n + 1];
                for (int p = 1; p <= n; p++) ile[pozycja[p]]++;
                wyniki.append(" ").append(Arrays.stream(ile).max().getAsInt());
            }
        }
        System.out.println(wyniki);
    }
}
```

**Odpowiedź:** 4.2: 395. 4.3: runda 3, pakiet 436. 4.4: 6 8 15 20.
