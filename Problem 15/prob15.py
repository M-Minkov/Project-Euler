cache = []

for i in range(21):
    cache.append([])
    for j in range(21):
        cache[i].append(0)


for i in range(21):
    cache[0][i] = 1
    cache[i][0] = 1


def F(x, y):
    
    if cache[x][y] != 0:
        return cache[x][y]
    
    cache[x][y] = F(x - 1, y) + F(x, y - 1)
    return cache[x][y]

print(F(20, 20))