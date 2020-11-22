# Print a hollow box

for i in range(4):
	for j in range(20):
		if(i==0 or i==(3) or j==0 or j==(19)):
			print('*',end='')
		else:
			print(' ',end='')
	print()