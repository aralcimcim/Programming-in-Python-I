# K11720457
# Aral Cimcim

# Write a program that prints a big 0 (zero) over a user-specified number of rows/lines (integer). If this number is less than 3, then print "Invalid number of lines". Otherwise print a 0 over the entered number of lines consisting of the characters | and -

# take user inputs
num_lines = int(input("Enter number of lines: "))

# if input is < 3, invalid input
if num_lines < 3:
    print("Invalid number of lines")

# construct the big 0
else:
    print((num_lines * "-") + ("\n|" + (num_lines - 2) * " " + "|") * (num_lines - 2) + ("\n" + num_lines * "-"))

