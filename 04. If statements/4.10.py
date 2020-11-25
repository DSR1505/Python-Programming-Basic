""" Write a multiplication game program for kids. The program should give the player ten
randomly generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is. """

from random import randint
for i in range(10):
	a = randint(1, 9)
	b = randint(1, 9)
	print('Question',i,':',a,'x',b,'=',end=' ')
	c = a * b
	submit = eval(input())
	if submit == c:
		print('Right!')
	else:
		print('Wrong! The answer is',c)