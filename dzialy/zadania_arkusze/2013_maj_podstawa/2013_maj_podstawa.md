## 5abcd
```py
parzyste = 0
dl_b = 0
zera = 0
jedynki = 0

lista = []

with open("dane/napisy.txt") as file:
    for line in file:
        line = line.strip()

        if len(line) % 2 == 0:  # a
            parzyste += 1

        if line.count("1") == line.count("0"):  # b
            dl_b += 1

        if "".join(set(list(line))) == "0":  # c
            zera += 1
        elif "".join(set(list(line))) == "1":
            jedynki += 1

        lista.append(line)
print(parzyste, dl_b, zera, jedynki)
print("-----------------")
for i in range(2, 17):
    count = 0
    for line in lista:
        if len(line) == i:
            count += 1
    print(i, count)

```
