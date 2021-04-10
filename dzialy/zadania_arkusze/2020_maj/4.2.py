with open("Dane_PR2\pary.txt") as file:
    for line in file:
        line, slowo = line.strip().split()
        res = slowo[0]
        longest = slowo[0]
        for i in range(1, len(slowo)):
            if slowo[i - 1] == slowo[i]:
                res += slowo[i - 1]
            else:
                res = slowo[i]
            if len(res) > len(longest):
                longest = res
        print(longest, len(longest))