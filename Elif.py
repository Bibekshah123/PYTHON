#Using Elif ex 3.1

def is_leap_year_elif(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year_elif(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
