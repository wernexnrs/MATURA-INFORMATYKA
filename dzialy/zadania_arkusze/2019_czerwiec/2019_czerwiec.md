<h1 align="center">7 czerwca 2019 r.</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md) --- [PLIKI](https://github.com/wernexnrs/MATURA-INFORMATYKA/tree/master/dzialy/zadania_arkusze/2019_czerwiec)

## 4.1

```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


with open("MIN-R2A1P-193_dane/liczby.txt") as file:
    for line in file:
        line = int(line)
        if is_prime(line) and line in range(100, 5001):
            print(line)
```

## 4.2

```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


with open("MIN-R2A1P-193_dane/pierwsze.txt") as file:
    for line in file:
        line = line.strip()
        liczba = int(line[::-1])
        if is_prime(liczba):
            print(line)
```

## 4.3

```py
def waga(n=''):
    wynik = 0
    while len(str(n)) > 1:
        for char in n:
            char = int(char)
            wynik += char
        n = str(wynik)
        wynik = 0
    return n


count = 0

with open("MIN-R2A1P-193_dane/pierwsze_przyklad.txt") as file:
    for line in file:
        line = line.strip()
        if waga(line) == '1':
            count += 1
print(count)
```

## 5 [[EXCEL] POBIERZ]() - brak 

### 5.*
- [Wyjaśnienie]() - brak

## 6 [[ACCESS] POBIERZ]()

### 6.1
- [Wyjaśnienie]() - brak

#### Kwarenda o nazwie 6_1(wynik)
```sql
SELECT TOP 1 Agenci.Imie, Agenci.Nazwisko, Zainteresowanie.Id_oferty
FROM Agenci INNER JOIN (Oferty INNER JOIN Zainteresowanie ON Oferty.Id_oferty = Zainteresowanie.Id_oferty) ON Agenci.Id_agenta = Oferty.Id_agenta
GROUP BY Agenci.Imie, Agenci.Nazwisko, Zainteresowanie.Id_oferty, Oferty.Id_agenta
ORDER BY Count(Zainteresowanie.Id_klienta) DESC;
```

### 6.2
- [Wyjaśnienie]() - brak

#### Kwarenda o nazwie 6_2(wynik)
```sql
SELECT Oferty.Woj, Avg(Oferty.Cena) AS ŚredniaOfCena
FROM Oferty
GROUP BY Oferty.Woj
ORDER BY Oferty.Woj;
```

### 6.3
- [Wyjaśnienie]() - brak

#### Kwarenda o nazwie 6_3(wynik)
```sql
SELECT Oferty.Id_oferty, Agenci.Imie, Agenci.Nazwisko, Oferty.Woj, Oferty.Pow, Oferty.Cena
FROM Agenci INNER JOIN Oferty ON Agenci.Id_agenta = Oferty.Id_agenta
WHERE (((Oferty.Id_oferty) Like "*MT") AND ((Oferty.Status) Like "A"));
```

### 6.4
- [Wyjaśnienie]() - brak

#### Kwarenda o nazwie 6_4(wynik)
```sql
SELECT Agenci.imie, Agenci.nazwisko
FROM Agenci
WHERE (((Agenci.Id_agenta) Not In (SELECT id_agenta FROM oferty WHERE status="S" AND data_zglosz LIKE "2017*")));
```

### 6.5
- [Wyjaśnienie]() - brak

#### Kwarenda o nazwie 6_5(wynik)
```sql
SELECT Oferty.Id_oferty, Oferty.Pow, Oferty.L_pokoi, Oferty.L_laz, Oferty.Cena, Agenci.Imie, Agenci.Nazwisko, Oferty.Status
FROM Agenci INNER JOIN Oferty ON Agenci.Id_agenta = Oferty.Id_agenta
WHERE (((Oferty.Pow)>180) AND ((Oferty.L_laz)>1) AND ((Oferty.Status) Like "A"));
```
