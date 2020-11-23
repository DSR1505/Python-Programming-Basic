""" Use for loops to print a diamond. Allow the user to specify how high the
diamond should be. """

num = eval(input('Enter the height: '))
j = (num//2)
for i in range(1,num+1,2):
	print(' '*j,'*'*i)
	j = j - 1
j = 1
for i in range(num-2,0,-2):
	print(' '*j,'*'*i)
	j = j + 1