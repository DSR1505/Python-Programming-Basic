""" Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an inch. """

cm = eval(input('Enter length in centimeters: '))
if(cm < 0):
	print('Invalid length')
else:
	inch = cm/2.54
	print('Length in inches:',inch)