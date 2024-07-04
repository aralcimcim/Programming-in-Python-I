# K11720457
# Aral Cimcim

# Write a program where the user can enter a string that contains comma-separated elements. variant: 1

# take comma-separated user inputs and split them 
string_parts = input("Enter comma-separated elements: ").split(",")

# create an empty dict as 'strings'
strings = {}

# set previous string to None
prev_string = None

# iterate through the user inputs
for curr_string in string_parts:
    # reset sum to 0
    sum = 0
    # compute the sum of the hash vals
    for char in curr_string:
        sum += ord(char)
    
    # if the user input is the same as the previous one, use assert to check if the hash_vals match (for the input 'test,test,test' assert is checked 2 times)
    if prev_string == curr_string:
        assert strings[curr_string] == sum

    # enter the hash vals for the curr string to the strings dict 
    strings[curr_string] = sum

    # update the string element
    prev_string = curr_string

# print the found results
for part in strings:
    print(f"'{part}' -> {strings[part]}")

