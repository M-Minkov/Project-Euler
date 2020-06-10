
def hexagonal(n: int) -> int:
    return (n*(2*n - 1))

def is_pentagonal(n: int) -> bool:
    temp = 1+((1+24*n)**0.5)

    if temp % 6 == 0:
        return True
    
    else:
        return False

def is_triangle(n: int):
    temp = -1 + ((1+8*n)**0.5)
    temp = temp/2

    if temp == int(temp):
        return temp
    else:
        return False

def triangle(n: int) -> int:
    return (n*(n+1)) << 1





n = 144

while True:
    hex_n = hexagonal(n)

    if is_pentagonal(hex_n) and type(is_triangle(hex_n)) is int:
        print(n)
        break
    n = n + 1

print(is_triangle(n))