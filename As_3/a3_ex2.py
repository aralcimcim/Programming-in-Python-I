# K11720457
# Aral Cimcim

# Write a program that repeatedly reads in elements/strings from the user until "x" is entered.

# create an empty list to store all elements
all = []
while True:
    # take inputs from the user and break the loop if the input is 'x'
    curr_string = input("Enter element or 'x' when done: ")
    if curr_string == 'x':
        break
    # otherwise add the current string to the 'all list'
    else:
        all.append(curr_string)

# sort the elements in the all list and name them as 'unique'
unique = sorted(set(all))

# print the all and unique lists
print(f"all: {all}\nunique (sorted): {unique}")

