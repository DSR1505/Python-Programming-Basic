""" Use a for loop to print an upside down triangle. Allow the user to specify
how high the triangle should be """

height = eval(input('Height of the triangle: '))
for i in range(height,0,-1):
	print('*'*i)