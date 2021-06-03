# BRUTE FORCE METHOD
def return_divisors(int_number):
    divisors = list(filter(lambda i: (int_number % i == 0), list(range(2, int_number))))
    return divisors

with open("liczby.txt", "r") as file:
    # PREPARE DATA
    numbers = file.read().splitlines()
    numbers = list(map(int, numbers))

    # SET "GLOBAL" CONTAINERS
    max_length_of_numeric_string = 0
    start_number = None
    max_divisor = None

    # FIND ALL DIVISORS
    all_divisors = list()
    for number in numbers:
        number = int(number)
        all_divisors.extend(return_divisors(number))

    # DELETE ALL REPETITIONS AND REVERSE
    all_divisors = list(set(all_divisors))
    all_divisors.reverse()

    # TRY TO DEVISE EVERY NUMBER BY ALL POSIBLE DIVISORS
    for divisor in all_divisors:
        local_length_of_numeric_string = 1
        local_start_number = None
        for i in range(len(numbers)):
            if numbers[i] % divisor == 0:
                local_length_of_numeric_string += 1
            else:
                # FIND STRING START NUMBER
                try:
                    local_start_number = numbers[i - local_length_of_numeric_string]
                except IndexError:
                    local_start_number = numbers[i - local_length_of_numeric_string - 1]

                # CHECK IF THIS NUMBER STRING IS LONGER THAT PREVIOUS
                if local_length_of_numeric_string > max_length_of_numeric_string:
                    start_number = local_start_number
                    max_length_of_numeric_string = local_length_of_numeric_string
                    max_divisor = divisor

                # RESET VARIABLE STORING NUMBER STRING LENGTHH
                local_length_of_numeric_string = 1

    print(start_number, max_length_of_numeric_string, max_divisor)
