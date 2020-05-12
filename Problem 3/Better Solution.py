"""

This time, similarly to the naive solution, we'll iterate over each number from 2 to sqrt(n)
Whenever we find a new prime number, this time we'll check to see if it divides n.
We'll keep dividing n by the prime number we found as many times as possible.
If it's no longer divisible, then we continue to search for the next prime number
This all stops once our number n, has been divided all the way down to the number 1.
Allowing us to end the loop (in most cases) early.

In the worst case, sqrt(n) is the largest prime number itself.
But this is very rare to happen for large values of n.

The solution technically has a time-complexity of Big-O((a^1.5)/log(a)), and a memory complexity of
Big-O(a/log(a)). Where "a" is the largest prime factor of n.

In the worst case a = sqrt(n), meaning our time complexity is also
Big-O(n^0.75/log(n)), and a memory complexity of Big-O(n^0.5/log(n)).

Which is not the best, but much better than our naive solution.
This is also very good for a lot of large numbers.
As an example for our particular case, the number 600851475143.
It's largest prime factor is 6857. Meaning we'll find our solution very quickly.

The number 10^100 also has a largest prime factor of 5. Meaning our method would take very few iterations.
However, our code would have to include much better support for numbers as large as 10^100, as the division process is quite cost effective.

We generally look at division to be an O(1) operation, as it takes a negligible amount of time. 

However without proper support for very large numbers, it takes much longer.

This method is still better than linear however.

If you see this method is almost the exact same as the naive solution.

Only this time we divide our number n, by whatever prime numbers we find.

And we have a checker that will end the process, once our number is divided down to 1.


"""

def find_largest_pfactor(n):
    primes = [2]

    while n % 2 == 0:
        n = n/2

    for i in range(3, int(n)+1):
        prime = True
        for a in primes:
            if i % a == 0:
                prime = False
                break
        
        if prime:
            primes.append(i)
            while n % i == 0:
                n = n/i
            if n == 1:
                break
        
        prime = True

    return primes[::-1][0]


if __name__ == "__main__":
    print(find_largest_pfactor(600851475143))