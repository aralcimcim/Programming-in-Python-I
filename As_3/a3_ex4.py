# K11720457
# Aral Cimcim

# Write a program where the user can enter a string that contains comma-separated elements. variant: 2

# take comma-separated user inputs as strings and split them
strings = input("Enter comma-separated elements: ").split(",")

# create 2 empty lists for numbers, non-numbers, and a dictionary for counts
non_nums = []
nums = []
counts = {}

# iterate through the user input
for string in strings:
    # if the string is an integer, convert the string to integer
    if string.isdecimal():
        num = int(string)
        # store the number to the nums list
        nums.append(num)

        # if the num is already in the counts dict, increment the count by 1
        if num in counts:
            counts[num] += 1
        # otherwise this is the first encounter, count = 1
        else:
            counts[num] = 1
    # if not num, then append to the non_nums list
    else:
        non_nums.append(string)

# print the found nums, non_nums, and counts in the dict
print(f"integers: {nums}\ncounts: {counts}\nrest: {non_nums}")

