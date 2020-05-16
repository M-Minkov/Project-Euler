"""

We can use a "sieve of Eratosthenes," to solve this problem.
An algorithm used by having a sorted list of all of the numbers from 2 to some number "k".
You mark all multiples of any prime number found in the sieve, starting from the lowest prime number found (usually 2 as the first number)

Once this is complete, we look for the first number that is not marked in the list and is greater than the prime we held onto.
If we started with 2 as our first prime number, the first number we find that is not marked will be 3.
This non-marked number will also be prime.
We repeat the process with our new prime number.

Our time-complexity for this problem is Big-O(klog(log(k))), and our memory-complexity is Big-O(k).

Although this solution is very similar to solutions used in previous problems, the way we go about the algorithm makes the set-up easier.
Also the amounts we increment optimizes the algorithm, to the new time-complexity we have, rather than for it to be linear.

By using this "sieve," it makes the programme very quick and easy to implement. Absolutely perfect for a naive solution.

If we want to find the nth prime number, it would be good to aproximate how large the nth prime number is.
And set this value to k.

A good aproximation we have is the prime pi function.
Pi(k) = k/log(k)

It states that under the number k, there are aproximately k/log(k) different prime numbers.
To aproximate what our value for k will be, we solve the equation:
n = k/log(k)

This form of equation is one that appears regularly in mathematics, and can be solved using the "product log function."
Also known as the "Lambert W function." Saving the math for later, the answer if n = 10001, rounded up is 46698.

This function is much more accurate for numbers above a million, but generally for lower numbers it only underestimates

We can also simple guess, by setting k to a very large value.
Generally if it's not too big, we can still find the nth prime number, without much delay.

A good aproximation for k will make the programme faster, but likely not by a whole lot.

"""



def nth_prime_number(n, k):

    sieve = [True for i in range(k+1)]

    counter = 0

    for i in range(2, k+1):
        if sieve[i]:
            counter = counter + 1
            if counter == n:
                return i

            for j in range(i**2, k+1, i):
                sieve[j] = False



if __name__ == "__main__":
    n = 10001
    k = 1000000
    
    print(nth_prime_number(n, k))