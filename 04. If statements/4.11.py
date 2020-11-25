""" Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. """

# Take the user's input which is in hour and date in am pm format.
hour = eval(input('Enter hour: '))
day = eval(input('Enter am(1) or pm(2)? '))
future = eval(input('How many hours ahead? '))

# Transform it to 24 format. Ex: 1pm becomes 13, 12 am becomes 0, etc.
if day == 1 and hour == 12:
	hour = 0
elif day == 2 and hour != 12:
	hour += 12

new_hour = hour + future				# add the transformed date (in 24 format) to the number of hours the user wants and store that value in new_hour
new_hour = new_hour % 24				# Now new_hour holds the result in 24 format. We need to transform back to am pm format. So Divide new_hour by 24 and take the reminder. Ex: if new_hour = 27 --> new_hour % 24 = 3

""" Remember that new_hour is still in 24 hour format. So:
If : 0 <= new_hour < 12 --> the new date to print is AM
Else --> the new date to print is PM """
if new_hour >= 0 and new_hour < 12:
	new_hour = new_hour % 12
	if new_hour == 0:
		new_hour = 12
	print('New Hour:',new_hour,'am')
else:
	new_hour = new_hour % 12
	if new_hour == 0:
		new_hour = 12
	print('New Hour:',new_hour,'pm')