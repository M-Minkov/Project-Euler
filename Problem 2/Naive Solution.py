"""

Runs a iterative fibonacci function, calculating every fibonacci value
It keeps calculating until it gets to the final value above 4000000, or for the general solution, "n"

The particular solution we calculate is where n = 4000000

As the growth of the fibonacci function acts similarly to an exponential function
We can say that the time complexity of our solution is Big-O(log(n))
As we're trying to calculate the largest fibonacci value that is less than n.

Note that this is not the same as calculating the nth fibonacci value, which would have
a time complexity of Big-O(n)

The memory complexity is Big-O(1).

"""



def fib(n):
    n_1 = 1
    n_2 = 2

    sum = 0


    while n_2 < n:
        if n_2 % 2 == 0:
            sum += n_2
        n_1, n_2 = n_2, n_1+n_2
        

    return sum

if __name__ == "__main__":
    print(fib(4000000))