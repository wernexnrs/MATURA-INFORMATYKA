with open("pary.txt") as file:
    for line in file:
        slowo = line.split()[1]
        najdluzszy = slowo[0]
        fragment = slowo[0]
        for i in range(1, len(slowo)):
            if slowo[i] == slowo[i - 1]:
                fragment += slowo[i]
            else:
                fragment = slowo[i]
            if len(fragment) > len(najdluzszy):
                najdluzszy = fragment
        print(najdluzszy, len(najdluzszy))
