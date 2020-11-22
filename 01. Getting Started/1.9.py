""" A lot of cell phones have tip calculators. Write one. Ask the user
for the price of the meal and the percent tip they want to leave. Then
print both the tip amount and the total bill with the tip included. """

price = eval(input('Price of the meal: '))
tip = eval(input('Percent tip you want to leave: '))
print('Tip amount:',(price*tip)/100)
print('Total bill:',price+((price*tip)/100))