""" Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the
temperature is in. Your program should convert the temperature to the other unit. The
conversions are F = (C * 9/5) + 32 and C = (F - 32) * 5/9. """

temp = eval(input('Enter temperature: '))
unit = input('Enter Unit: ')
if(unit == "C"):
	f = (temp * 9/5) + 32
	print('Temperature in Fahrenheit:',f)
elif(unit == "F"):
	c = (temp - 32) * 5/9
	print('Temperature in Celsius:',c)
else:
	print('Invalid Unit')