""" Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise. """

a = eval(input())
b = eval(input())
if abs(a - b) <= 0.001:
	print('Close')
else:
	print('Not Close')