# Aral Cimcim K11720457
# Write a program that computes and prints several metrics of a room given a user-specified length, width and height

# take user inputs for length, width, height
length = float(input("Length (meters): "))
width = float(input("Width (meters): "))
height = float(input("Height (meters): "))

# compute the metrics
circumference = (length + width) * 2
volume = length * width * height
wall_area = (length * height * 2) + (width * height * 2)
num_windows = int(wall_area // 12)
paint_needed = (wall_area - (num_windows * 2)) * 0.75

# print the results
print(f"Circumference: {circumference:.2f} meters")
print(f"Volume: {volume:.2f} cubic meters")
print(f"Wall area: {wall_area:.2f} square meters")
print(f"Number of windows: {num_windows}")
print(f"Needed paint: {paint_needed:.2f} liters")

