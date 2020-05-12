n_0 = 1
n_1 = 1
n_2 = 2

sum = 0


while n_2 < 4000000:
    if n_2 % 2 == 0:
        sum += n_2
    n_1, n_2 = n_2, n_1+n_2
    

print(sum)