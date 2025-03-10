def is_leap_year(year):
    visokostn_year= (year % 400 == 0) or year % 4 == 0 and year % 100 != 0
    return visokostn_year
print(is_leap_year(2020))
