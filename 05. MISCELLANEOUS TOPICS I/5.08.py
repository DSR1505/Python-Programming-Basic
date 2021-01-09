x = eval(input('Enter x: '))
y = eval(input('Enter y: '))
z = eval(input('Enter z: '))
x = x + y + z
z = x - (y + z)
y = x - (y + z)
x = x - (y + z)
print('New x:',x,'New y:',y,'New z:',z)
