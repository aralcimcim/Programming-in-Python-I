# K11720457
# Aral Cimcim

# Write a program that calculates and outputs the subscription price of the fictional magazine Python – The Programmer’s Magazine.

# take user inputs for the subscription duration
duration_val = int(input("Please enter the duration of your subscription (in months): "))

# if duration_val is negative or 0, duration is invalid
if duration_val < 0 or duration_val == 0:
    print("Invalid subscription duration")
    exit(0)

# for a duration less than 6 months, the price is 6.50 per month
if duration_val < 6:
    price_per_month = 6.50
    full_price = price_per_month * duration_val

    # print the results
    print(f"The price per month is {price_per_month:.2f}\nThe full price for {duration_val} months is {full_price:.2f}")

# for a duration of at least 6 months but less than 12 months, the price is 5.90 per month
if 6 < duration_val < 12:
    price_per_month = 5.90
    full_price = price_per_month * duration_val

    # print the results
    print(f"The price per month is {price_per_month:.2f}\nThe full price for {duration_val} months is {full_price:.2f}")

# for subscription periods of one year or more, read the customer’s postal code, which should be 4 digits
if duration_val >= 12:
    postal_code = input("Please enter your postal code: ")

    # for a postal code < 1000 or > 9999 (i.e., for numbers that do not have exactly 4 digits), print an error message ("Invalid postal code")
    if len(postal_code) < 4 or len(postal_code) > 4:
        print("Invalid postal code")
        exit(0)

    # compute the middle digits
    mid_digits = ""
    for i in range(1, 3):
        mid_digits += postal_code[i]

    # for valid postal codes, the monthly price is 4.xx, where xx is the middle two digits (hundreds and tens places) of the postal code
    price_per_month = float(f"{len(postal_code)}.{mid_digits}")
    full_price = price_per_month * duration_val

    # print the results
    print(f"The price per month is {price_per_month:.2f}\nThe full price for {duration_val} months {full_price:.2f}")

