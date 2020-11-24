""" Write a program that asks the user for a number of seconds and prints out
how many minutes and seconds that is. For instance, 200 seconds and 20 seconds """

s = eval(input('Enter seconds: '))
m = s//60
s = s%60
print(m,'minutes',s,'seconds')