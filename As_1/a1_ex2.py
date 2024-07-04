# Aral Cimcim K11720457
# Read four numbers a, b, c and d from the console and convert them to integers

# take 4 user inputs
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

# sum of a, b and d
print(f"Sum of a, b and d: {a + b + d}")

# product of all four numbers
print(f"Product of all numbers: {a * b * c * d}")

# sum of a and b times the sum of c and d
print(f"The sum of a and b times the sum of c and d: {(a + b) * (c + d)}")

# result of an integer division when dividing a by d
print(f"a divided by d (int): {a // d}")

# result of a regular division when dividing a by d
print(f"a divided by d (float): {a / d}")

# remainder of a division (modulo) when dividing a by b
print(f"Remainder of a divided by b: {a % b}")

# power operator
print(f"c to the power of -a: {c ** -a}")

# square root
print(f"b to the power of 1/2 (square root): {b ** (1/2)}")

# complex equation
print(f"Complex equation: {(b / 3) * (b ** ((a + d / 2)) - 1) + c}")

