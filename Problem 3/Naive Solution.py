"""

For this problem we'll simply iterate over the numbers from 3 up until the square root of 600851475143.
We'll keep a list of prime numbers, which will start off with 2. Any number that is not divisible by any of the primes we have in our list,
is a prime number itself. Once we iterate over all of the numbers, we'll iterate over the prime list going from largest to smallest,
checking if 600851475143 is divisible by it. The first number we find that divides it cleanly, will be our answer.

For a more general solution, we replace 600851475143 with the number "n".
Our time-complexity would be Big-O((n^1.5)/log(n)), and our memory complexity is Big-O(n/log(n)), as there are aproximately n/log(n) prime numbers below n.

For n = 600851475143, however, you can see that this would take a lot of time.
Making this a very non-optimal solution

"""

def find_largest_prime(n):
    primes = [2]

    for i in range(3, int(n**0.5)+1):
        prime = True

        for a in primes:
            if i % a == 0:
                prime = False
                break
        
        if prime:
            primes.append(i)
        
        prime = True

    for i in range(len(primes)-1, -1, -1):
        if n % primes[i] == 0:
            return primes[i]