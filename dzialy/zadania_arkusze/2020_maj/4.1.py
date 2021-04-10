def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


with open('Dane_PR2\pary.txt') as file:
    for line in file:
        num, word = line.strip().split()
        num = int(num)
        if num > 4 and num % 2 == 0:
            for j in range(3, num + 1):
                if is_prime(j) and is_prime(num - j):
                    print(num, j, num - j)
                    break