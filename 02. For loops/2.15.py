num = eval(input('Enter height: '))
res = (num//2)
k = 1
j = num - 1
for i in range(num):
	if(i == res):
		print(' '*j,'*'*(num+1))
		j = j - 1
	if(i == 0):
		print(' '*j,'*')
		j = j - 1
	else:
		print(' '*j,'*',' '*k,'*')
		j = j - 1
		k = k + 2