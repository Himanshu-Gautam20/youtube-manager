year = 1992

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True
else:
    is_leap_year = False

print(is_leap_year)