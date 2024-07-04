# K11720457
# Aral Cimcim

# Write a program that repeatedly reads positive integers from the console using a while loop, store only the current number and the previous number

# set the previous number as an empty string
prev_num = ""

# start the loop
while True:
    # take user inputs as the current number
    curr_num = input("Enter number or 'x': ")

    # if the first input is x, break
    if curr_num == 'x':
        if prev_num == "":
            print("Empty sequence")
        
        # keep taking inputs and break iff user enters x
        else:
            print("All numbers had the same digit in the ones place")
        # exit 1
        exit(0)

    # set the first number as the previous number
    if prev_num == "":
        prev_num = curr_num

    # convert strings to integers, check with modulo: if the digits in the ones place do not match, break
    if int(curr_num) % 10 != int(prev_num) % 10:
        print(f"{prev_num} and {curr_num} differ in the ones place")
        # exit 2
        exit(0)

    # move to the next number in the loop
    prev_num = curr_num

