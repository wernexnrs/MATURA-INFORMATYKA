## 6
```py
count = 0
count2 = 0
count3 = 0
count4 = 0
suma = 0
lista_liczb = []

with open("liczby.txt") as file:
    for line in file:
        line = line.strip()
        if line[-1] == "6":  # 6.1
            count += 1

        if line[-1] == "7" and "6" not in line:  # 6.2
            count2 += 1

        if line[-1] == "2":
            if int(line[:-1], 2) % 2 != 0:  # 6.3
                count3 += 1

        if line[-1] == "4":  # 6.4
            suma += int(line[:-1], 4)

        lista_liczb.append((line, int(line[:-1], int(line[-1]))))

print(count, count2, count3, suma)

print(sorted(lista_liczb, key=lambda x: x[1], reverse=True)[0])
print(sorted(lista_liczb, key=lambda x: x[1])[0])

```
