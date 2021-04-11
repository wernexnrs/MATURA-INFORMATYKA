## 4
```py
parzyste = 0
lista = []
with open("dane/cyfry.txt") as file:
    for line in file:
        line = line.strip()

        if int(line) % 2 == 0:  # a
            parzyste += 1

        lista.append((line, sum(int(i) for i in line)))

        if all(int(line[i - 1]) < int(line[i]) for i in range(1, len(line))):
            print(line)

    print("min:", sorted(lista, key=lambda x: x[1])[0][0])
    print("max:", sorted(lista, key=lambda x: x[1], reverse=True)[0][0])

    print(parzyste)

```
