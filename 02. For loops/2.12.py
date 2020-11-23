""" Use a for loop to print a triangle. Allow the user to specify how high the
triangle should be. """

height = eval(input('Height of the triangle: '))
for i in range(height):
	print('*'*(i+1))