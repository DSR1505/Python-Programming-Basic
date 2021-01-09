""" Write a program that asks the user for an integer and tells them if it is squarefree or not """

import math
num = int(input('Enter the number: '))
root = math.sqrt(num)
if int(root + 0.5)**2 == num:
    print(num,'is a perfect square')
else:
    print(num,'is not a perfect sqare')
