#Use a for loop to print a hollow box. Allow the user to specify how wide and how high the box should be

hori = eval(input('Horizontal limit: '))
verti = eval(input('Vertical limit: '))
for i in range(hori):
	for j in range(verti):
		if(i==0 or i==(hori-1) or j==0 or j==(verti-1)):
			print('*',end='')
		else:
			print(' ',end='')
	print()