"""

The equation states that a + b + c = 1000

And that a^2 + b^2 = c^2

Where a, b, and c are all natural numbers, and, a < b < c.

We can do some rearranging to form a new equation, which will allow for a nice brute-force solution.

We know that a + b + c = 1000
Therfore a + b = 1000 - c

(a+b)^2 = (1000 - c)^2

a^2 + 2ab + b^2 = 1000^2 - 2000c + c^2

a^2 + b^2 = c^2

a^2 + 2ab + b^2 = 1000^2 - 2000c + a^2 + b^2

2ab = 1000^2 - 2000c
ab = 500*1000 - 1000c
ab - 500,000 = -1000c
500 - (ab/1000) = c

By using this final equation, we can iterate through numbers from 1 to 1000, setting b to each value.
Then have an inner loop where "a" iterates through numbers 1 to b.
We then plug in both numbers into the equation to see what our value for c is.
If c is an integer, and a + b + c = 1000, and a < b < c.
Then we have found our answer for the numbers.

We output the product a*b*c.

if we generalized the problem and stated that a + b + c = n
And we simply had to just find one pythogrean triplet, that met the same previous conditions.
Using the same method, our time-complexity is only Big-O(n^2)

Our memory-complexity is Big-O(1).


"""


def pythagorean_triplet():
    for b in range(2, 1000):
        for a in range(1, b):
            c = 500 - (a*b/1000)

            if c == int(c) and a+b+c==1000 and a < b < c:
                return a*b*c


if __name__ == "__main__":
    print(pythagorean_triplet())