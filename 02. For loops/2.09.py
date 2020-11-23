# Write a program that asks the user how many Fibonacci numbers to print and then prints that many.

num = eval(input('How many: '))
t1 = 1
t2 = 1
print(t1,t2,end=",")
for i in range(2,num):
	res = t1 + t2
	print(res,end=",")
	t1 = t2
	t2 = res