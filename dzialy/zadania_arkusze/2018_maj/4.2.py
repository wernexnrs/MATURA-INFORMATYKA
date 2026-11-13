with open("sygnaly.txt") as file:
    slowa = file.read().split()

maks = 0
najlepsze = ""

for slowo in slowa:
    rozne = len(set(slowo))
    if rozne > maks:
        maks = rozne
        najlepsze = slowo

print(najlepsze, maks)
