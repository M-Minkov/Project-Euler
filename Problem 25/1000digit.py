from math import log10

fibonacci_numbers = [1, 1]

i = 2

while len(fibonacci_numbers) < 5000:
    fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
    i += 1

for i in range(4700, 5000):
    if len(str(fibonacci_numbers[i])) == 1000:
        print(i+1)
        break