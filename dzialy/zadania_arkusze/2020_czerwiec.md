 <a name="main"/> 
 
 <h1 align="center">2020 czerwiec</h1>
 
  - [1.2](#1.2)
  - [1.3](#1.3)
  - [4.1](#4.1)
  - [4.2](#4.2)
  - [4.3](#4.3)

<a name="1.2"/> 

## 1.2 [⬆️](#main)

Niech n będzie dodatnią liczbą całkowitą, a A[1..n] i B[1..n] będą n-elementowymi tablicami liczb całkowitych.Dla nieujemnej liczby całkowitej k, gdzie k < n, powiemy, że tablice A i B są k-podobne, gdy

A[1..k] = B[n-k+1..n] oraz A[k+1..n] = B[1..n-k]

Liczbę k nazywamy świadectwem podobieństwa.

Uwaga: dla k = 0 przyjmujemy, że prawdziwe jest A[1..0] = B[n+1..n]. 

Zapisz w wybranej przez siebie notacji (w postaci pseudokodu, listy kroków lub w wybranym języku programowania) funkcję czy_k_podobne(n, A, B, k), gdzie A i B są n-elementowymi tablicami liczb całkowitych. Wynikiem funkcji jest PRAWDA, jeśli tablice A i B są k-podobne dla zadanego parametru k, natomiast FAŁSZ – w przeciwnym przypadku. 

```python
n = 3
k = 0

A = [5, 7, 9]
B = [5, 7, 9]


def czy_k_podobne(n, A, B, k):
    for i in range(k):

        if A[i] != B[n - k + i]:
            return False
    for i in range(n - k):

        if B[i] != A[k + i]:
            return False
    return True

print(czy_k_podobne(n, A, B, k))
```

<a name="1.3"/> 

## 1.3 [⬆️](#main)

Zapisz w wybranej przez siebie notacji funkcję czy_podobne(n, A, B), która dla danych tablic A i B daje odpowiedź PRAWDA, jeśli istnieje takie k, dla którego tablice A i B są k-podobne, natomiast FAŁSZ – w przeciwnym przypadku. 

```python
def czy_podobne(n, A, B):
    for k in range(n):
        if czy_k_podobne(n, A, B, k):
            return True
        else:
            return False
```

<a name="4.1"/> 
  
W pliku pary.txt znajduje się 100 wierszy. Każdy wiersz zawiera parę danych składającą się z liczby całkowitej z przedziału od 3 do 100 i słowa (ciągu znaków) złożonego z małych liter alfabetu angielskiego o długości od 1 do 50 znaków. Liczba i słowo są oddzielone znakiem spacji. 

## 4.1 [⬆️](#main)

Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą  dwóch nieparzystych liczb pierwszych, np. liczba 20 jest równa sumie 3 + 17 lub sumie 7 + 13. Każdą liczbę parzystą z pliku pary.txt przedstaw w postaci sumy dwóch liczb pierwszych. Wypisz tę liczbę oraz dwa składniki sumy w kolejności niemalejącej. Jeżeli istnieje więcej rozwiązań (tak jak dla liczby 20) należy wypisać składniki sumy o największej różnicy. Wyniki podaj w oddzielnych wierszach, w kolejności zgodnej z kolejnością danych w pliku pary.txt. Liczby w każdym wierszu rozdziel znakiem spacji, np. dla liczby 20 należy wypisać 20 3 17. 

  ```python
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    else:
        return False


with open('Dane_PR2\pary.txt') as file:
    for line in file:
        num, word = line.strip().split()
        num = int(num)
        if num > 4 and num % 2 == 0:
            for j in range(3, num + 1):
                if is_prime(j) and is_prime(num - j):
                    print(num, j, num - j)
                    break

  ```
  
<a name="4.2"/> 

## 4.2 [⬆️](#main)

Dla każdego słowa z pliku pary.txt znajdź długość najdłuższego spójnego fragmentu tego słowa złożonego z identycznych liter. Wypisz znalezione fragmenty słów i ich długości oddzielone spacją, po jednej parze w każdym wierszu. Jeżeli istnieją dwa fragmenty o takiej samej największej długości, podaj pierwszy z nich. Wyniki podaj w kolejności zgodnej z kolejnością danych w pliku pary.txt. 

  ```python
with open("Dane_PR2\pary.txt") as file:
    for line in file:
        num, word = line.strip().split()

        seq = word[0]
        longest_seq = word[0]
        for char in word[1:]:
            if char == seq[-1]:
                seq += char
            else:
                seq = char
            if len(seq) > len(longest_seq):
                longest_seq = seq
        print(longest_seq, len(longest_seq))

  ```
  
<a name="4.3"/>

## 4.3 [⬆️](#main)

Para (liczba1, słowo1) jest mniejsza od pary (liczba2, słowo2), gdy:

 – liczba1 < liczba2,

albo

 – liczba1 = liczba2 
 
oraz słowo1 jest leksykograficznie (w porządku alfabetycznym) mniejsze od słowo2.

Przykład:

para (1, bbbb) jest mniejsza od pary (2, aaa), natomiast para (3, aaa) jest mniejsza od pary (3, ab).

Rozważ wszystkie pary (liczba, słowo) zapisane w wierszach pliku pary.txt, dla których liczba jest równa długości słowa, i wypisz spośród nich taką parę, która jest mniejsza od wszystkich pozostałych. W pliku pary.txt jest jedna taka para. 
   
  ```python
arr = []
with open("Dane_PR2\pary.txt") as file:
    for line in file:
        num, word = line.strip().split()
        num = int(num)
        if num == len(word):
            arr.append((num, word))
print(sorted(arr)[0])

  ```