prime_table = []
odd_composite = []


# Simple Big-O(n log(log(n))) Sieve of Eratosthenes used to compute the prime numbers, and all odd composite numbers
def sieve(n):
    A = []

    for i in range(n+1):
        A.append(True)

    for i in range(2, (int(n**0.5))+1):
        if A[i]:
            j = i**2
            while j <= n:
                A[j] = False
                j = j + i

    for i in range(len(A)):
        if A[i]:
            prime_table.append(i)
        elif i % 2 == 1:
                odd_composite.append(i)

# Function checking if the a number (n), meets the conjecture
def meets_conjecture(n) -> bool:
    temp = 0
    for i in prime_table:
        temp = n
        # Division by 2, and square root
        if i > ((n << 1)**0.5):
            break

        temp = temp - i

        # Division by 2, and square root
        temp = (temp << 1)**0.5

        if temp == int(temp):
            return True
    return False

# Compute all prime numbers under 100,000
sieve(10000)


# Check all odd composite numbers under 100,000 to see if any of them don't meet the conjecture
for i in odd_composite:
    if not meets_conjecture(i):
        print(i)
        break



"""
For this discussion we'll begin by assigning the smallest odd composite number that does not meet the conjecture,
to the variable A.

Measuring our time-complexity, it's noted that we start off with a simple implementation of a sieve of Eratosthenes.
We only require all of the prime numbers between 1, and square_root(A/2).
But we cannot stop there, as we first must find all of the odd composite numbers from 2 upto and including A.

So our sieve must run through all numbers from 2 to A.
Forcing our sieve to have a time-complexity of Big-O(A log(log(A)))
Note that we do not know how to estimate the value of A, so in implementation
we simply run the sieve with a very large value, that we believe must be bigger than A.

Our sieve's memory complexity is Big-O(A), due to the prime and odd-composite numbers recorded.

With a good estimation of A, our programme would run faster, and take less memory, however,
values under 1 million would still generally compute the answer within 0.1 Seconds.

A good estimation is therefore not required; lest the target changes to finding the 100th odd composite number which does not meet the conjecture.


Then we run our meets_conjecture checker function.
As an approximation, let us assume that the amount of prime-numbers under a number N, grows linearly with the number N.

Our checker operates by taking an odd composite number, removing a prime number from it, and then checking if the new number
is a square multiplied by 2. By reversing the process, and seeing if the outcome is an integer.

It checks the given number (B), against all prime numbers between 0 and square_root(B/2)


If we approximate the amount of prime numbers, and odd composite numbers under the number A,
to grow linearly with A, then the time-complexity for our checker function is A squared.
A**2

Our memory-complexity is already set by the sieve function,
our checker function does not use any additional memory.
Therfore our memory-complexity remains to be Big-O(A)

Our time-complexities add, to form Big-O(A log(log(A)) + A**2)

Note that this is a very approximate complexity, in reality there are variable conditions that I have implemented as great optimizations.

This explanation is meant to be kept simple, and not to go further in-depth in order to not strain the reader.
In reality our checker function is not A**2, as our checker function does not check a given number B against all the prime numbers between 0 and A.
It only checks them between 0 and square_root(B/2), which has far lower growth than what I had approximated.

A**2 is for simplicity, as we assumed that the amount of prime numbers under the number N, grows lineraly with N.
But in reality it does not, as the growth rate of amount of primes under a given number N, decreases exponentially.

I could have roughly approxmiated the amount of prime numbers under A through the well known pi function, pi(A) = A/log(A).

There are also some minor optimizations in the code, which give a much lower time constant.
Such as how I removed all division operations within the code.
Only a bit-shift operation is used, which will emulate division by 2.

However, again, the analysis has been simplified, as the problem is straight-forward, and the values for A are very low.

Even if our solution had endorsed an exponential time-complexity, we would see that such low values of A would still allow our programme
to find an answer within a small time-frame, with a similar amount of memory used.
"""