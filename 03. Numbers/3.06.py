""" Write a program that asks the user to enter two numbers, x and y,
and computes (|x-y|)/(x+y). """

x = eval(input())
y = eval(input())
if (x-y < 0):
	print(-(x-y)/(x+y))
else:
	print((x-y)/(x+y))