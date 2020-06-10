
def hexagonal(n: int) -> int:
    return (n*(2*n - 1))

def is_pentagonal(n: int) -> bool:
    temp = (1/6) + (((2*n/3) + (1/36))**0.5)

    if temp == int(temp):
        return True
    else:
        return False

def is_triangle(n: int) -> bool:
    temp = (-1 + ((1+8*n)**0.5))/2
    
    if temp == int(temp):
        return True
    else:
        return False





n = 144

while True:
    hex_n = hexagonal(n)

    if is_pentagonal(hex_n) and is_triangle(hex_n):
        print(n)
        break

