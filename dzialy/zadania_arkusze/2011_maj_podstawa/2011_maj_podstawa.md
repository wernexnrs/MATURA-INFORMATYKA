## 4abc

```py
parzyste = 0
nieparzyste = 0

with open("dane/hasla.txt") as file:
    with open("dane/wynik4b.txt", "w") as file2:
        with open("dane/wynik4c.txt", "w") as file3:
            for line in file:
                line = line.strip()
                if len(line) % 2 == 0:
                    parzyste += 1
                else:
                    nieparzyste += 1
                if line == line[::-1]:
                    file2.write(line + "\n")
                if any((ord(line[i - 1]) + ord(line[i])) == 220 for i in range(1, len(line))):
                    file3.write(line + "\n")

print(parzyste, nieparzyste)

```
