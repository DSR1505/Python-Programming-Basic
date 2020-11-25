""" A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost. """

item = eval(input('How many items are you buying: '))
if(1 <= item <10):
	total = item * 12
	print('Total amount is $',total,sep='')
elif(10 <= item <= 99):
	total = item * 10
	print('Total amount is $',total,sep='')
else:
	total = item * 7
	print('Total amount is $',total,sep='')