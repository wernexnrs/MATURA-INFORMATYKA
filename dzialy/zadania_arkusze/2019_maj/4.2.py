import math

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        line = line.strip()
        suma = 0
        for num in line:
            num = int(num)
            suma += math.factorial(num)
        if int(line) == suma:
            print(line)