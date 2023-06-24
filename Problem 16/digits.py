
number = 2 << 999

digits = [int(digit) for digit in str(number)]
print(sum(digits))