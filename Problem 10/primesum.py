
prime_numbers = [False, False] + [True] * 2000000

total = 0

for number in range(2, 2000000):

    if prime_numbers[number]:
        total += number

        change = number * 2
        while change < 2000000:
            prime_numbers[change] = False
            change += number
    


print(total)