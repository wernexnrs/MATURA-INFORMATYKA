<h1 align="center">Matura 2016 — maj, poziom rozszerzony (stara formuła)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/MIN-R1_1P-162.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/MIN-R2_1P-162.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/Dane_PR2.zip) --- [ODPOWIEDZI](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_do_2014/zasady_oceniania/MIN-R1-S.pdf)

## 2.1, 2.2 i 2.3

> **Treść zadania:** Zadanie 2. Popularność. Dane: liczba całkowita `n > 1` oraz tablica liczb całkowitych `A[1..n]`. Rozważamy algorytm:
>
> ```
> max ← 1; nr ← 1
> dla i = 1, 2, ..., n wykonuj:
>     k ← 0
>     dla j = i, i+1, ..., n wykonuj:
>         jeżeli A[i] = A[j], to            (wiersz 5)
>             k ← k + 1                     (wiersz 6)
>     jeżeli k > max, to
>         max ← k; nr ← i                   (wiersz 8)
> wynikiem jest A[nr]
> ```
>
> - 2.1 — Podaj wynik algorytmu dla danych: `n=5: 1, 2, 1, 2, 1`; `n=6: 2, 4, 4, 2, 4, 2`; `n=9: 2, 3, 3, 4, 4, 3, 2, 2, 3`.
> - 2.2 — Podaj, ile razy zostanie wykonane porównanie `A[i] = A[j]` (wiersz 5) dla `n` = 2 (odpowiedź: 3), 3, 7, 10, 15 i 1000.
> - 2.3 — Podaj, ile razy wykona się instrukcja z wiersza 6, a ile z wiersza 8, gdy wszystkie elementy tablicy są równe.

```py
def popularnosc(A):
    n = len(A)
    maks = 1
    nr = 0
    porownania = 0      # wiersz 5.
    wiersz6 = 0
    wiersz8 = 0
    for i in range(n):
        k = 0
        for j in range(i, n):
            porownania += 1
            if A[i] == A[j]:
                k += 1
                wiersz6 += 1
        if k > maks:
            maks = k
            nr = i
            wiersz8 += 1
    return A[nr], porownania, wiersz6, wiersz8


# 2.1
for A in [[1, 2, 1, 2, 1], [2, 4, 4, 2, 4, 2], [2, 3, 3, 4, 4, 3, 2, 2, 3]]:
    print(popularnosc(A)[0])

# 2.2 - liczba porownan w wierszu 5.
for n in [2, 3, 7, 10, 15, 1000]:
    print(n, popularnosc([0] * n)[1])

# 2.3 - wszystkie elementy rowne
n = 10
wynik, porownania, wiersz6, wiersz8 = popularnosc([5] * n)
print(wiersz6, n * (n + 1) // 2, wiersz8)
```

```cpp
// C++23
#include <print>
#include <vector>

struct Wynik {
    int najpopularniejszy;
    long long porownania, wiersz6, wiersz8;
};

Wynik popularnosc(const std::vector<int>& A) {
    int n = A.size();
    int maks = 1;
    int nr = 0;
    long long porownania = 0;  // wiersz 5.
    long long wiersz6 = 0;
    long long wiersz8 = 0;
    for (int i = 0; i < n; i++) {
        int k = 0;
        for (int j = i; j < n; j++) {
            porownania++;
            if (A[i] == A[j]) {
                k++;
                wiersz6++;
            }
        }
        if (k > maks) {
            maks = k;
            nr = i;
            wiersz8++;
        }
    }
    return {A[nr], porownania, wiersz6, wiersz8};
}

int main() {
    // 2.1
    std::vector<std::vector<int>> ciagi = {{1, 2, 1, 2, 1}, {2, 4, 4, 2, 4, 2}, {2, 3, 3, 4, 4, 3, 2, 2, 3}};
    for (const auto& A : ciagi)
        std::println("{}", popularnosc(A).najpopularniejszy);

    // 2.2 - liczba porownan w wierszu 5.
    for (int n : {2, 3, 7, 10, 15, 1000})
        std::println("{} {}", n, popularnosc(std::vector<int>(n, 0)).porownania);

    // 2.3 - wszystkie elementy rowne
    int n = 10;
    Wynik w = popularnosc(std::vector<int>(n, 5));
    std::println("{} {} {}", w.wiersz6, n * (n + 1) / 2, w.wiersz8);
}
```

```java
// Java 25
public class Zadanie {
    record Wynik(int najpopularniejszy, long porownania, long wiersz6, long wiersz8) {}

    static Wynik popularnosc(int[] A) {
        int n = A.length;
        int maks = 1;
        int nr = 0;
        long porownania = 0;  // wiersz 5.
        long wiersz6 = 0;
        long wiersz8 = 0;
        for (int i = 0; i < n; i++) {
            int k = 0;
            for (int j = i; j < n; j++) {
                porownania++;
                if (A[i] == A[j]) {
                    k++;
                    wiersz6++;
                }
            }
            if (k > maks) {
                maks = k;
                nr = i;
                wiersz8++;
            }
        }
        return new Wynik(A[nr], porownania, wiersz6, wiersz8);
    }

    public static void main(String[] args) {
        // 2.1
        int[][] ciagi = {{1, 2, 1, 2, 1}, {2, 4, 4, 2, 4, 2}, {2, 3, 3, 4, 4, 3, 2, 2, 3}};
        for (int[] A : ciagi)
            System.out.println(popularnosc(A).najpopularniejszy());

        // 2.2 - liczba porownan w wierszu 5.
        for (int n : new int[]{2, 3, 7, 10, 15, 1000})
            System.out.println(n + " " + popularnosc(new int[n]).porownania());

        // 2.3 - wszystkie elementy rowne
        int n = 10;
        int[] piatki = new int[n];
        java.util.Arrays.fill(piatki, 5);
        Wynik w = popularnosc(piatki);
        System.out.println(w.wiersz6() + " " + n * (n + 1) / 2 + " " + w.wiersz8());
    }
}
```

**Odpowiedź:** 2.1: 1; 2; 3. 2.2: 3; 6; 28; 55; 120; 500500 (czyli n(n+1)/2). 2.3: wiersz 6. — n(n+1)/2 razy, wiersz 8. — 1 raz

## 3.1 i 3.3

> **Treść zadania:** Zadanie 3. Przekątne w tabliczce mnożenia. W tabliczce mnożenia rozważamy przekątne biegnące „w lewo w dół”: n-ta przekątna zawiera iloczyny `i·j`, dla których `i + j = n + 1`. Suma liczb na 1. przekątnej wynosi 1, a na 6. przekątnej — 56 (na 4. przekątnej: 4+3+3+2+2+2+1+1+1+1 = 20).
>
> - 3.1 — Podaj sumę liczb na 8. przekątnej.
> - 3.3 — Zapisz algorytm, który dla danej dodatniej liczby całkowitej `n` obliczy sumę `w` liczb na n-tej przekątnej tabliczki mnożenia.

```py
def suma_przekatnej(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i * (n - i + 1)
    return suma


print(suma_przekatnej(1), suma_przekatnej(6), suma_przekatnej(8))
```

```cpp
// C++23
#include <print>

long long suma_przekatnej(int n) {
    long long suma = 0;
    for (int i = 1; i <= n; i++)
        suma += i * (n - i + 1);
    return suma;
}

int main() {
    std::println("{} {} {}", suma_przekatnej(1), suma_przekatnej(6), suma_przekatnej(8));
}
```

```java
// Java 25
public class Zadanie {
    static long sumaPrzekatnej(int n) {
        long suma = 0;
        for (int i = 1; i <= n; i++)
            suma += i * (n - i + 1);
        return suma;
    }

    public static void main(String[] args) {
        System.out.println(sumaPrzekatnej(1) + " " + sumaPrzekatnej(6) + " " + sumaPrzekatnej(8));
    }
}
```

**Odpowiedź:** 3.1: 120 (3.2: liczba piątek na n-tej przekątnej to n − 4)

## 4.1, 4.2 i 4.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Zadanie 4. Doświadczenie. Doświadczenie trwa 1500 minut. Na początku (minuta 0) w naczyniu jest 5 l roztworu o stężeniu 80% (4000 ml substancji X i 1000 ml wody). Pod koniec każdej parzystej minuty dozownik pobiera z naczynia 20 ml roztworu (pierwszy raz w 2. minucie). Co 50 minut, począwszy od 51. minuty, robot dolewa wodę, uzupełniając roztwór do 5 l (np. w 51. minucie przed dolaniem jest 4,5 l roztworu o stężeniu 80%, a po dolaniu 5 l o stężeniu 72%). Odpowiedzi zaokrąglone do dwóch miejsc po przecinku (zaokrąglaj dopiero wynik końcowy) zapisz w pliku `wyniki_4.txt`, poprzedzając każdą numerem zadania.
>
> - 4.1 — Podaj poziom roztworu w naczyniu w 191. minucie: ilość roztworu, ilość wody i ilość substancji X.
> - 4.2 — Podaj stężenie roztworu po 1500 minutach oraz łączną objętość wody dolanej w czasie doświadczenia.
> - 4.4 — Podaj maksymalną objętość porcji pobieranej przez dozownik (z dokładnością do 0,01 ml, przy niezmienionej pracy robota), przy której stężenie roztworu w trakcie doświadczenia nigdy nie spadnie poniżej 1%.

```py
def doswiadczenie(porcja):
    substancja = 4000.0
    woda = 1000.0
    dolana_woda = 0
    stan_191 = None
    najmniejsze_stezenie = 1
    for minuta in range(1, 1501):
        if minuta == 191:
            stan_191 = (substancja + woda, woda, substancja)
        # koniec parzystej minuty - dozownik pobiera porcje roztworu
        if minuta % 2 == 0:
            objetosc = substancja + woda
            substancja -= porcja * substancja / objetosc
            woda -= porcja * woda / objetosc
        # co 50 minut (51., 101., ...) robot dolewa wode do 5 litrow
        if minuta % 50 == 1 and minuta > 1:
            dolewka = 5000 - (substancja + woda)
            woda += dolewka
            dolana_woda += dolewka
        najmniejsze_stezenie = min(najmniejsze_stezenie, substancja / (substancja + woda))
    stezenie = substancja / (substancja + woda)
    return stan_191, stezenie, dolana_woda, najmniejsze_stezenie


stan_191, stezenie, dolana_woda, _ = doswiadczenie(20)
print("4.1", [round(x, 2) for x in stan_191])
print("4.2", round(stezenie * 100, 2), round(dolana_woda, 2))

# 4.4 - zwiekszamy porcje co 0,01 ml, dopoki stezenie nie spadnie ponizej 1%
setne = 2000
while doswiadczenie((setne + 1) / 100)[3] >= 0.01:
    setne += 1
print("4.4", setne / 100)
```

```cpp
// C++23
#include <algorithm>
#include <format>
#include <print>
#include <string>

// zaokraglenie do 2 miejsc jak round(x, 2) w Pythonie
double zaokraglij(double x) {
    return std::stod(std::format("{:.2f}", x));
}

// liczba zmiennoprzecinkowa wypisana tak jak w Pythonie (np. 14500.0, 1917.28)
std::string jak_python(double x) {
    std::string s = std::format("{}", x);
    if (s.find_first_of(".e") == std::string::npos)
        s += ".0";
    return s;
}

struct Wynik {
    double roztwor_191, woda_191, substancja_191;
    double stezenie, dolana_woda, najmniejsze_stezenie;
};

Wynik doswiadczenie(double porcja) {
    double substancja = 4000.0;
    double woda = 1000.0;
    double dolana_woda = 0;
    Wynik w{};
    double najmniejsze_stezenie = 1;
    for (int minuta = 1; minuta <= 1500; minuta++) {
        if (minuta == 191) {
            w.roztwor_191 = substancja + woda;
            w.woda_191 = woda;
            w.substancja_191 = substancja;
        }
        // koniec parzystej minuty - dozownik pobiera porcje roztworu
        if (minuta % 2 == 0) {
            double objetosc = substancja + woda;
            substancja -= porcja * substancja / objetosc;
            woda -= porcja * woda / objetosc;
        }
        // co 50 minut (51., 101., ...) robot dolewa wode do 5 litrow
        if (minuta % 50 == 1 && minuta > 1) {
            double dolewka = 5000 - (substancja + woda);
            woda += dolewka;
            dolana_woda += dolewka;
        }
        najmniejsze_stezenie = std::min(najmniejsze_stezenie, substancja / (substancja + woda));
    }
    w.stezenie = substancja / (substancja + woda);
    w.dolana_woda = dolana_woda;
    w.najmniejsze_stezenie = najmniejsze_stezenie;
    return w;
}

int main() {
    Wynik w = doswiadczenie(20);
    std::println("4.1 [{}, {}, {}]", jak_python(zaokraglij(w.roztwor_191)),
                 jak_python(zaokraglij(w.woda_191)), jak_python(zaokraglij(w.substancja_191)));
    std::println("4.2 {} {}", jak_python(zaokraglij(w.stezenie * 100)), jak_python(zaokraglij(w.dolana_woda)));

    // 4.4 - zwiekszamy porcje co 0,01 ml, dopoki stezenie nie spadnie ponizej 1%
    int setne = 2000;
    while (doswiadczenie((setne + 1) / 100.0).najmniejsze_stezenie >= 0.01)
        setne++;
    std::println("4.4 {}", jak_python(setne / 100.0));
}
```

```java
// Java 25
import java.math.BigDecimal;
import java.math.RoundingMode;

public class Zadanie {
    // zaokraglenie do 2 miejsc jak round(x, 2) w Pythonie
    static double zaokraglij(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).doubleValue();
    }

    record Wynik(double roztwor191, double woda191, double substancja191,
                 double stezenie, double dolanaWoda, double najmniejszeStezenie) {}

    static Wynik doswiadczenie(double porcja) {
        double substancja = 4000.0;
        double woda = 1000.0;
        double dolanaWoda = 0;
        double roztwor191 = 0, woda191 = 0, substancja191 = 0;
        double najmniejszeStezenie = 1;
        for (int minuta = 1; minuta <= 1500; minuta++) {
            if (minuta == 191) {
                roztwor191 = substancja + woda;
                woda191 = woda;
                substancja191 = substancja;
            }
            // koniec parzystej minuty - dozownik pobiera porcje roztworu
            if (minuta % 2 == 0) {
                double objetosc = substancja + woda;
                substancja -= porcja * substancja / objetosc;
                woda -= porcja * woda / objetosc;
            }
            // co 50 minut (51., 101., ...) robot dolewa wode do 5 litrow
            if (minuta % 50 == 1 && minuta > 1) {
                double dolewka = 5000 - (substancja + woda);
                woda += dolewka;
                dolanaWoda += dolewka;
            }
            najmniejszeStezenie = Math.min(najmniejszeStezenie, substancja / (substancja + woda));
        }
        double stezenie = substancja / (substancja + woda);
        return new Wynik(roztwor191, woda191, substancja191, stezenie, dolanaWoda, najmniejszeStezenie);
    }

    public static void main(String[] args) {
        Wynik w = doswiadczenie(20);
        System.out.println("4.1 [" + zaokraglij(w.roztwor191()) + ", " + zaokraglij(w.woda191()) + ", "
                + zaokraglij(w.substancja191()) + "]");
        System.out.println("4.2 " + zaokraglij(w.stezenie() * 100) + " " + zaokraglij(w.dolanaWoda()));

        // 4.4 - zwiekszamy porcje co 0,01 ml, dopoki stezenie nie spadnie ponizej 1%
        int setne = 2000;
        while (doswiadczenie((setne + 1) / 100.0).najmniejszeStezenie() >= 0.01)
            setne++;
        System.out.println("4.4 " + setne / 100.0);
    }
}
```

**Odpowiedź:** 4.1: roztwór 4600,00 ml, woda 1917,28 ml, substancja X 2682,72 ml (w kluczu CKE wartości wody i substancji są zamienione miejscami — stężenie 0,8·0,9³ = 58,32% daje 2682,72 ml substancji); 4.2: 3,77%, 14 500 ml; 4.4: 28,04 ml

## 4.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** W doświadczeniu z zadania 4 (naczynie 5 l, początkowo 4000 ml substancji X i 1000 ml wody; co parzystą minutę dozownik pobiera 20 ml roztworu, od 51. minuty co 50 minut robot dolewa wodę do 5 l) przedstaw na jednym wykresie liniowym, jak przez cały czas doświadczenia (od minuty 0 do 1500) zmieniały się ilość wody i ilość substancji X w naczyniu. Zadbaj o czytelność wykresu.

```py
# dane do wykresu liniowego: minuta, woda, substancja X
substancja = 4000.0
woda = 1000.0

with open("wykres_4_3.txt", "w") as wynik:
    wynik.write("minuta;woda;substancja\n")
    for minuta in range(0, 1501):
        wynik.write(f"{minuta};{woda:.2f};{substancja:.2f}\n")
        if minuta % 2 == 0 and minuta > 0:
            objetosc = substancja + woda
            substancja -= 20 * substancja / objetosc
            woda -= 20 * woda / objetosc
        if minuta % 50 == 1 and minuta > 1:
            woda += 5000 - (substancja + woda)
```

```cpp
// C++23
#include <fstream>
#include <print>

int main() {
    // dane do wykresu liniowego: minuta, woda, substancja X
    double substancja = 4000.0;
    double woda = 1000.0;

    std::ofstream wynik("wykres_4_3.txt");
    std::println(wynik, "minuta;woda;substancja");
    for (int minuta = 0; minuta <= 1500; minuta++) {
        std::println(wynik, "{};{:.2f};{:.2f}", minuta, woda, substancja);
        if (minuta % 2 == 0 && minuta > 0) {
            double objetosc = substancja + woda;
            substancja -= 20 * substancja / objetosc;
            woda -= 20 * woda / objetosc;
        }
        if (minuta % 50 == 1 && minuta > 1)
            woda += 5000 - (substancja + woda);
    }
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class Zadanie {
    // liczba z 2 miejscami po kropce, jak f"{x:.2f}" w Pythonie
    static String dwaMiejsca(double x) {
        return new BigDecimal(x).setScale(2, RoundingMode.HALF_EVEN).toPlainString();
    }

    public static void main(String[] args) throws Exception {
        // dane do wykresu liniowego: minuta, woda, substancja X
        double substancja = 4000.0;
        double woda = 1000.0;

        try (var wynik = new PrintWriter("wykres_4_3.txt")) {
            wynik.println("minuta;woda;substancja");
            for (int minuta = 0; minuta <= 1500; minuta++) {
                wynik.println(minuta + ";" + dwaMiejsca(woda) + ";" + dwaMiejsca(substancja));
                if (minuta % 2 == 0 && minuta > 0) {
                    double objetosc = substancja + woda;
                    substancja -= 20 * substancja / objetosc;
                    woda -= 20 * woda / objetosc;
                }
                if (minuta % 50 == 1 && minuta > 1)
                    woda += 5000 - (substancja + woda);
            }
        }
    }
}
```

**Odpowiedź:** wykres liniowy dwóch serii (woda — rośnie „ząbkami”, substancja X — maleje) tworzymy z pliku `wykres_4_3.txt`

## 5.1, 5.2 i 5.3

> **Treść zadania:** Zadanie 5. Gra w życie. Plansza ma 12 wierszy i 20 kolumn (plik `gra.txt`, każdy wiersz planszy w osobnym wierszu; `X` — komórka żywa, `.` — martwa). Plansza jest „zawinięta”: prawa krawędź sąsiaduje z lewą, a górny wiersz z dolnym; każda komórka ma 8 sąsiadów (bokiem lub wierzchołkiem). W następnym pokoleniu żywe są tylko komórki, które: są żywe i mają 2 lub 3 żywych sąsiadów albo są martwe i mają dokładnie 3 żywych sąsiadów. Plik zawiera pierwsze pokolenie. Odpowiedzi zapisz w pliku `wyniki_5.txt`, poprzedzając każdą numerem zadania.
>
> - 5.1 — Podaj liczbę żywych sąsiadów komórki w 2. wierszu i 19. kolumnie w 37. pokoleniu.
> - 5.2 — Podaj liczbę żywych komórek w drugim pokoleniu.
> - 5.3 — W którym pokoleniu (sprawdzając najwyżej do 100.) układ się ustali, tzn. będzie identyczny jak w poprzednim? Podaj numer tego pokolenia i liczbę żywych komórek w nim.

```py
def sasiedzi(plansza, w, k):
    n, m = len(plansza), len(plansza[0])
    licznik = 0
    for dw in (-1, 0, 1):
        for dk in (-1, 0, 1):
            if (dw != 0 or dk != 0) and plansza[(w + dw) % n][(k + dk) % m] == "X":
                licznik += 1
    return licznik


def nastepne_pokolenie(plansza):
    nowa = []
    for w in range(len(plansza)):
        wiersz = ""
        for k in range(len(plansza[0])):
            s = sasiedzi(plansza, w, k)
            if s == 3 or (plansza[w][k] == "X" and s == 2):
                wiersz += "X"
            else:
                wiersz += "."
        nowa.append(wiersz)
    return nowa


def zywe(plansza):
    return sum(wiersz.count("X") for wiersz in plansza)


plansza = []
with open("gra.txt") as file:
    for line in file:
        if line.strip():
            plansza.append(line.strip())

pokolenia = {1: plansza}
for p in range(2, 101):
    pokolenia[p] = nastepne_pokolenie(pokolenia[p - 1])

print("5.1", sasiedzi(pokolenia[37], 1, 18))
print("5.2", zywe(pokolenia[2]))
for p in range(2, 101):
    if pokolenia[p] == pokolenia[p - 1]:
        print("5.3", p, zywe(pokolenia[p]))
        break
```

```cpp
// C++23
#include <fstream>
#include <map>
#include <print>
#include <string>
#include <vector>

using Plansza = std::vector<std::string>;

int sasiedzi(const Plansza& plansza, int w, int k) {
    int n = plansza.size(), m = plansza[0].size();
    int licznik = 0;
    for (int dw = -1; dw <= 1; dw++)
        for (int dk = -1; dk <= 1; dk++)
            // (x % n + n) % n - reszta zawsze nieujemna, jak % w Pythonie
            if ((dw != 0 || dk != 0) && plansza[((w + dw) % n + n) % n][((k + dk) % m + m) % m] == 'X')
                licznik++;
    return licznik;
}

Plansza nastepne_pokolenie(const Plansza& plansza) {
    Plansza nowa;
    for (int w = 0; w < (int)plansza.size(); w++) {
        std::string wiersz;
        for (int k = 0; k < (int)plansza[0].size(); k++) {
            int s = sasiedzi(plansza, w, k);
            if (s == 3 || (plansza[w][k] == 'X' && s == 2))
                wiersz += 'X';
            else
                wiersz += '.';
        }
        nowa.push_back(wiersz);
    }
    return nowa;
}

int zywe(const Plansza& plansza) {
    int suma = 0;
    for (const auto& wiersz : plansza)
        for (char c : wiersz)
            if (c == 'X')
                suma++;
    return suma;
}

int main() {
    Plansza plansza;
    std::ifstream plik("gra.txt");
    std::string linia;
    while (std::getline(plik, linia)) {
        while (!linia.empty() && (linia.back() == '\r' || linia.back() == ' '))
            linia.pop_back();
        if (!linia.empty())
            plansza.push_back(linia);
    }

    std::map<int, Plansza> pokolenia;
    pokolenia[1] = plansza;
    for (int p = 2; p <= 100; p++)
        pokolenia[p] = nastepne_pokolenie(pokolenia[p - 1]);

    std::println("5.1 {}", sasiedzi(pokolenia[37], 1, 18));
    std::println("5.2 {}", zywe(pokolenia[2]));
    for (int p = 2; p <= 100; p++) {
        if (pokolenia[p] == pokolenia[p - 1]) {
            std::println("5.3 {} {}", p, zywe(pokolenia[p]));
            break;
        }
    }
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Zadanie {
    static int sasiedzi(List<String> plansza, int w, int k) {
        int n = plansza.size(), m = plansza.get(0).length();
        int licznik = 0;
        for (int dw = -1; dw <= 1; dw++)
            for (int dk = -1; dk <= 1; dk++)
                // Math.floorMod - reszta zawsze nieujemna, jak % w Pythonie
                if ((dw != 0 || dk != 0) && plansza.get(Math.floorMod(w + dw, n)).charAt(Math.floorMod(k + dk, m)) == 'X')
                    licznik++;
        return licznik;
    }

    static List<String> nastepnePokolenie(List<String> plansza) {
        List<String> nowa = new ArrayList<>();
        for (int w = 0; w < plansza.size(); w++) {
            var wiersz = new StringBuilder();
            for (int k = 0; k < plansza.get(0).length(); k++) {
                int s = sasiedzi(plansza, w, k);
                if (s == 3 || (plansza.get(w).charAt(k) == 'X' && s == 2))
                    wiersz.append('X');
                else
                    wiersz.append('.');
            }
            nowa.add(wiersz.toString());
        }
        return nowa;
    }

    static int zywe(List<String> plansza) {
        int suma = 0;
        for (String wiersz : plansza)
            for (char c : wiersz.toCharArray())
                if (c == 'X')
                    suma++;
        return suma;
    }

    public static void main(String[] args) throws Exception {
        List<String> plansza = new ArrayList<>();
        for (String linia : Files.readAllLines(Path.of("gra.txt")))
            if (!linia.strip().isEmpty())
                plansza.add(linia.strip());

        Map<Integer, List<String>> pokolenia = new HashMap<>();
        pokolenia.put(1, plansza);
        for (int p = 2; p <= 100; p++)
            pokolenia.put(p, nastepnePokolenie(pokolenia.get(p - 1)));

        System.out.println("5.1 " + sasiedzi(pokolenia.get(37), 1, 18));
        System.out.println("5.2 " + zywe(pokolenia.get(2)));
        for (int p = 2; p <= 100; p++) {
            if (pokolenia.get(p).equals(pokolenia.get(p - 1))) {
                System.out.println("5.3 " + p + " " + zywe(pokolenia.get(p)));
                break;
            }
        }
    }
}
```

**Odpowiedź:** 5.1: 4; 5.2: 8; 5.3: w 51. pokoleniu, 8 żywych komórek
