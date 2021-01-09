""" Write a program that finds all four of the perfect numbers that are less than 10000. """

n = 1
while n <= 10000:
    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n)
    n = n + 1
