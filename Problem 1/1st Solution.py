"""

The easiest method that I can think off the top of my head
is to find every number that is divisible by 3 or 5

Because we only need to find the sum of all the numbers, and we
don't need to memorize them, we'll simple run a loop that goes from
1 to 1000, adding all the numbers that are divisible by the 2 along the way.

The solution has a time complexity of Big-O(n), and a memory complexity of O(1)
If you ignore how big the sum can go, the only number we keep track of is the sum.

"""


def find_sum(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    
    return sum


if __name__ == "__main__":
    print(find_sum(1000))