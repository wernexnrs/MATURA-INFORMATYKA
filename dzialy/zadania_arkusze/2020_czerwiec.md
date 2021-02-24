<h1 align="center">2020 czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

## 1.2 i 1.3

```py
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


def czy_podobne(n, A, B):
    for k in range(n):
        if czy_k_podobne(n, A, B, k):
            return True
        return False


print(czy_k_podobne(n, A, B, k))

```

## 4.1

```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
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

## 4.2

```py
with open("Dane_PR2\pary.txt") as file:
    for line in file:
        line, slowo = line.strip().split()
        res = slowo[0]
        longest = slowo[0]
        for i in range(1, len(slowo)):
            if slowo[i - 1] == slowo[i]:
                res += slowo[i - 1]
            else:
                res = slowo[i]
            if len(res) > len(longest):
                longest = res
        print(longest, len(longest))

```

## 4.3

```py
lista = []

with open("Dane_PR2\pary.txt") as file:
    for line in file:
        line, slowo = line.strip().split()
        line = int(line)

        if line == len(slowo):
            lista.append((line, slowo))

print(sorted(lista)[0])

```
