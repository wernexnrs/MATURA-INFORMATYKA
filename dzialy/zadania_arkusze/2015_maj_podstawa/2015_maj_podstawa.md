## 5.1
```py
slowa = []

with open("slowa.txt") as file:
    for line in file:
        slowa.append(line.strip())

for i in range(1, 13):
    count = 0
    for line in slowa:
        if len(line) == i:
            count += 1
    print(i, count)

```

## 5.2
```py
slowa = []
nowe = []

with open("slowa.txt") as file:
    for line in file:
        slowa.append(line.strip())

with open("nowe.txt") as file2:
    for line in file2:
        nowe.append(line.strip())

for line in nowe:
    print(line, slowa.count(line), slowa.count(line[::-1]))
```
