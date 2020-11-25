""" Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not """

from random import randint
x = randint(1,10)
y = eval(input('Enter a number between 1 and 10: '))
if(x == y):
	print('You get it right')
else:
	print('Try again')