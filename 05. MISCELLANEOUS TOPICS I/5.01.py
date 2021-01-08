""" Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1. """

e = []
for x in range(1, 101):
    if x%10 == 1 or x%10 == 9:
        y = x**2
        if y%10 == 1:
            e.append(y)
print(len(e))
