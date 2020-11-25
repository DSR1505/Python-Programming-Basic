""" Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over. """

credit = eval(input('How many credits you have: '))
if(credit <= 23):
	print('Student is a freshman')
elif(24 <= credit <= 53):
	print('Student is a sophomore')
elif(54 <= credit <= 83):
	print('Student is a junior')
else:
	print('Student is a senior')