year = int(input())
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(1 if is_leap else 0)
