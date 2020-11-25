""" Write a program that asks the user to enter a number and prints out all the divisors of that number. """

n = eval(input('Enter a integer: '))
for i in range(1, n+1):
	if(n % i == 0):
		print(i)