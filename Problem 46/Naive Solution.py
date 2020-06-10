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
        else:
            if i % 2 == 1:
                odd_composite.append(i)

# Function checking if the a number (n), meets the conjecture
def meets_conjecture(n) -> bool:
    temp = 0
    for i in prime_table:
        temp = n
        if i > ((n << 1)**0.5):
            break

        temp = temp - i

        # Division by 2, by shifting all of the bits to the left 1 space.
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

Measuring our time-complexity, it's noted that we start off wit ha simple implementation of a sieve of Eratosthenes.
We only require all of the prime numbers between 1, and square_root(A/2).
But we cannot stop there, as we first must find all of the odd composite numbers, including A.

So our sieve must run through all numbers from 2 to A.
Forcing our sieve to have a time-complexity of Big-O(A log(log(A)))
Note that we do not know how to estimate the value of A, so in implementation
we simply run the sieve with a very large value, that we believe must be bigger than A.

Our sieve's memory complexity is Big-O(A)

With a good estimation of A, our programme would run faster, and take less memory, however,
values under 1 million would still generally compute the answer within 0.1 Seconds.

A good estimation is therefore not required, unless if the target had changed to finding the 100th odd composite number, which does not meet the conjecture.
Rather than the 1st.

