# Prompts user to enter year and month
import calendar
import datetime
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Displays the calendar for the specified month and year
print(calendar.month(year, month))

#Displays the current date and time
now = datetime.datetime.now()

if (month == now.month and year == now.year):
    print("The specified month and year is the current month.")

# Display month and year if it is the current month
    print("Today's date is:", now.strftime("%B"), now.day, year)
    
else:
    print("The specified month and year is not the current month.")
print("Today's date and time is:", now.strftime("%Y-%m-%d %H:%M:%S"))
