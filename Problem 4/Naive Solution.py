"""

Off the top of my head a way of doing this problem would be to have two numbers x, and y.

Set both numbers to 999, and then multiply them together.
I'd check if it's a palindrome, return the number, otherwise subtract 1 from x.
Multiply the two numbers again, if it's a palindrome, return it, otherwise subtract 1 from y this time.

This process would keep repeating until a palindrome is found.

If we wanted this for a general case, we would set the amount of digits in the numbers to be "n".

In our particular case we're looking at n=3.

Our time complexity for this method is Big-O(10^n), as there are
(10^n - 10^(n-1))^2 different pairs of x and y. Simplifying the formula down it becomes
0.81*10^(2n). But the constants are not counted for in complexity analysis.

Our memory complexity is O(1), as we only keep track of 2 different numbers.

Generally, although this time complexity may seem very high, we are using very low values of n.
Our particular case is where n = 3, allowing for a naive solution to be good enough.

"""

x = 999
y = 999

palindrome = False
number = 0

while not palindrome:
    number = str(x*y)
    if number == number[::-1]:
        print(number)
        break

    x = x - 1

    number = str(x*y)
    if number == number[::-1]:
        print(number)
        break

    y = y - 1