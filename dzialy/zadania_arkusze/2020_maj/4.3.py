lista = []

with open("Dane_PR2\pary.txt") as file:
    for line in file:
        line, slowo = line.strip().split()
        line = int(line)

        if line == len(slowo):
            lista.append((line, slowo))

print(sorted(lista)[0])
