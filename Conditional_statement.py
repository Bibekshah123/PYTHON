#Using Conditional Statement ex 3.1

def is_leap_year_conditional(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

year = int(input("Enter a year: "))
if is_leap_year_conditional(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
