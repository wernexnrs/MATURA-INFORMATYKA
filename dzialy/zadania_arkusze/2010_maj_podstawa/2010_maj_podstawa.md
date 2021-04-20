## 4

```py
with open("Dane/dane.txt") as file:
    for line in file:
        line = line.strip()
        if line == line[::-1]:
            print(line)
```
