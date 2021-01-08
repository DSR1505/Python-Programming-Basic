""" Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000. """

def solve_sum(n):
    if(n%2 == 1):
        return (n+1)/2
    return -n/2
n = 2000
print(int(solve_sum(n)))
