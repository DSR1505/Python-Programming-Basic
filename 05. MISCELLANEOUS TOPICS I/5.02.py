a = []
b = []
for x in range(1, 101):
    if x%10 == 2 or x%10 == 8:
        y = x**2
        if y%10 == 4:
            a.append(y)
    if x%10 == 3 or x%10 == 7:
        z = x**2
        if z%10 == 9:
            b.append(z)
print('Square of number ending with 4:',len(a))
print('Square of number ending with 9:',len(b))
