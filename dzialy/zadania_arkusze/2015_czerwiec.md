<h1 align="center">2015 czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

## 6.1

```py
suma = suma_2 = 0
with open("MIN-R2A1P-153_dane\kody.txt") as file:
    with open("kody1.txt", "w") as result:
        for line in file:
            line = line.strip()

            for i in range(1, len(line), 2):
                suma += int(line[i])
                suma_2 += int(line[i - 1])
            result.write(f"{suma} {suma_2}\n")
            suma = suma_2 = 0

```

## 6.2

```py
suma = suma_2 = 0

slow = {
    "0": "10101110111010",
    "1": "11101010101110",
    "2": "10111010101110",
    "3": "11101110101010",
    "4": "10101110101110",
    "5": "11101011101010",
    "6": "10111011101010",
    "7": "10101011101110",
    "8": "11101010111010",
    "9": "10111010111010"
}
with open("MIN-R2A1P-153_dane\kody.txt") as file:
    with open("kody2.txt", "w") as result:
        for line in file:
            line = line.strip()

            for i in range(1, len(line), 2):
                suma += int(line[i])
                suma_2 += int(line[i - 1])
            wynik = suma + suma_2

            suma = suma_2 = 0

            wynik %= 10
            wynik = 10 - wynik
            wynik %= 10
            result.write(f"{wynik} {slow[str(wynik)]}\n")

```

## 6.3

```py
suma = suma_2 = 0

slow = {
    "0": "10101110111010",
    "1": "11101010101110",
    "2": "10111010101110",
    "3": "11101110101010",
    "4": "10101110101110",
    "5": "11101011101010",
    "6": "10111011101010",
    "7": "10101011101110",
    "8": "11101010111010",
    "9": "10111010111010"
}
with open("MIN-R2A1P-153_dane\kody.txt") as file:
    with open("kody3.txt", "w") as result:
        for line in file:
            line = line.strip()

            for i in range(1, len(line), 2):
                suma += int(line[i])
                suma_2 += int(line[i - 1])
            wynik = suma + suma_2

            suma = suma_2 = 0

            wynik %= 10
            wynik = 10 - wynik
            wynik %= 10

            end = f"11011010"

            for i in line:
                end += slow[i]
            end += f"{slow[str(wynik)]}11010110\n"
            result.write(end)

```
