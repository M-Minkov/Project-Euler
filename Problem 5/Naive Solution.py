"""

The easiest solution I can think of, would be to start with the number 1.

Check if the number is divisible by every number between 1 to 20.
Once we find a number that it's not divisible by, we add 20 to that number.
And check again.
We repeat this until we find a number that is divisible all of the numbers between 1 to 20.

If this problem were generalized to the number "n"
Find a number that is divisible by all of the numbers between 1 to n, we would notice this solution has an exponential time-complexity

It likely depends on the amount of prime factors each number from 1 to n has.
And can therfore be seen as a factorial time-complexity problem.

The time complexity is Big-O(n!)

The memory complexity is Big-O(1), as we only keep track of two numbers at any given moment.


"""


def smallest_multiple(n):
    
    found = False
    
    answer = 0

    while not found:
        answer += 20


        found = True
        for i in range(2, n+1):
            if answer % i != 0:
                found = False
                break
    
    return answer


if __name__ == "__main__":
    print(smallest_multiple(20))