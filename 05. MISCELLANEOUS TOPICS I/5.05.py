a = int(input('Enter an integer: '))
divisor_sum = 0
for i in range(1, a+1):
    if(a%i == 0):
        divisor_sum += i
print('The sum of divisor:',str(divisor_sum))
