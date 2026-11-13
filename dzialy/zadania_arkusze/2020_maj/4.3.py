pary = []

with open("pary.txt") as file:
    for line in file:
        liczba, slowo = line.split()
        liczba = int(liczba)
        if liczba == len(slowo):
            pary.append((liczba, slowo))

# krotki porównują się najpierw po liczbie, a przy równości - po słowie
liczba, slowo = min(pary)
print(liczba, slowo)
