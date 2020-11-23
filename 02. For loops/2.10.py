""" Use a for loop to print a box. Allow the user to specify how wide and how
high the box should be """

high = eval(input('How much high: '))
wide = eval(input('How much wide: '))
for i in range(high):
	print('*'*wide)