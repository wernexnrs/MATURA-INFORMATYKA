## 5
```py
import math


def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


with open("Dane/liczby.txt") as file:
    for line in file:
        line = int(line.strip())
        square = math.sqrt(line)
        if int(square + 0.5) ** 2 == line and is_prime(int(square)):
            print(line)
```
