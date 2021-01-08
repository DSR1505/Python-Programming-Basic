""" Write a program that asks the user to enter a number and prints the sum of the divisors of
that number. The sum of the divisors of a number is an important function in number theory. """

a = int(input('Enter an integer: '))
divisor_sum = 0
for i in range(1, a+1):
    if(a%i == 0):
        divisor_sum += i
print('The sum of divisor:',str(divisor_sum))
