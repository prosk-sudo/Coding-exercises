def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # do something
    pass

print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))   # True
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))   # False

