# K11720457
# Aral Cimcim

# Using the built-in range(start, stop, step), write a program that reads these three integer numbers and iterates through the value range

# take user inputs for start, stop, step
start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

# set counters for sum of odds and count of evens
even_count = 0
sum_odd_nums = 0

# start the loop
for i, num in enumerate(range(start, stop, step)):
    # stop printing after 5 iterations
    if i < 5:
        print(f"Number in iteration: {i} = {num}")
    # count the even numbers
    if num % 2 == 0:
        even_count += 1
    
    else:
        # sum the odd numbers
        sum_odd_nums += num

# print the even counts and odd sums
print(f"Even number count: {even_count} \nSum of odd numbers: {sum_odd_nums}")

