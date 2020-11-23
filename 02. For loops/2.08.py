""" Write a program that asks the user for their name and how many times
to print it. """

name = input('Enter your name: ')
num = eval(input('How many times to print: '))
for i in range(num):
	print(name)