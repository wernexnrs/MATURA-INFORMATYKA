with open("sygnaly.txt") as file:
    slowa = file.read().split()

for slowo in slowa:
    # każde dwie litery są oddalone co najwyżej o 10 <=> największa i najmniejsza litera są oddalone co najwyżej o 10
    if ord(max(slowo)) - ord(min(slowo)) <= 10:
        print(slowo)
