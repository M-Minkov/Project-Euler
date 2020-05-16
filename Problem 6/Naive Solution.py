"""

For this solution, we'll do a for loop from the numbers 1 to n, whilst maintaining 2 counters.

The first counter squares the current iteration number, and adds it to itself.
The second counter just adds the number to itself

Once the loop has finished, the 2nd counter will be squared, and the result that's outputted is the 2nd counter minus the 1st

As it loops from 1 to n, the time complexity is Big-O(n)

The memory complexity is Big-O(1)

"""


def sum_square_difference(n):
    
    counter_1 = 0
    counter_2 = 0

    for i in range(1, n+1):
        counter_1 += i**2
        counter_2 += i
    
    counter_2 = counter_2**2

    return counter_2-counter_1



if __name__ == "__main__":
    print(sum_square_difference(100))