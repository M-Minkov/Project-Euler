"""

As an approximation I'm going to assume that if both numbers must have "n" digits each.
Then the palindrome will an amount of digits of 2n.

So in our particular case, our n = 3. We want two numbers, both 3 digits long,
that multiply against one another to form a palindrome number. Which we will assume to have 6 digits.

For our naive solution, I believe an easy way would be to find every 6 digit palindrome number.
And check each number if they can be written as the multiple, of two 3 digit numbers.

We do this by taking the palindrome number, and attempting to divide it by all the numbers from 999 to 100.
If the ending division gives us another number of 3 digits, then we've found our palindrome.

Because it's a palindrome it's symmetrical down the middle, we can just consider the first 3 digits.

For a general case it would be the same, we would find all the palindromes of length 2n.
Only using the first n digits to make each unique palindrome.
And then checking it against all of the numbers between 10^n and 10^(n+1)

This would mean there are 10^n different palindrome numbers of length n, and we start counting from the largest palindrome.

In the worst case, our biggest palindrome number is one of the smallest 2n digit numbers.

Our time complexity is therfore Big-O(10^2n), we'll only keep track of the largest palindrome we've found,
and the two multiples. We'll consider having only 3 numbers to be saved insignificant and therfore Big-Theta(1)

The time complexity is exponential, however it's not that bad, especially considering our low value of n.
The answer still came out instantly after I had run the code.

However, this might be just because the 6 digit palindrome that met the condition, was greater than 900000, which is one of the best cases.
if we write n = 4, we still get a pretty low run time. But once we get upto 5, it slows down quite a significant amount. At 6 we're left waiting for about a minute

"""


def large_palindrome(n):
    a = (10**n)-1

    found = False

    while not found:
        if a == 10**(n-1):
            break
        b = str(a)
        num = int(b + b[::-1])

        for i in range((10**n)-1, 10**(n-1), -1):
            res = str(num//i)
            if num % i == 0 and len(res) == n:
                print(num)
                print(i)
                print(res)
                found = True
                break
        
        a -= 1
    return num


if __name__ == "__main__":
    print(large_palindrome(5))