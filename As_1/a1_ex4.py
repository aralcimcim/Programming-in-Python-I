# Aral Cimcim K11720457
# Write a program that can print a small order form for a store that sells PC parts

# order form outline
print("=" * 50 + "\nPC Parts Store - Order\n" + "=" * 50)

# take inputs from the user
num_cables = int(input("Number of cables: "))
num_monitors = int(input("Number of monitors: "))
num_keyboards = int(input("Number of keyboards: "))

# compute the costs
cable_cost = num_cables * 9.90
monitor_cost = num_monitors * 249.99
keyboard_cost = num_keyboards * 27.50
total = cable_cost + monitor_cost + keyboard_cost

# return the results
print(f"{num_cables:3d} cables (9.90 EUR each) = {cable_cost:.2f} EUR")
print(f"{num_monitors:3d} monitors (249.99 EUR each) = {monitor_cost:.2f} EUR")
print(f"{num_keyboards:3d} keyboards (27.50 EUR each) = {keyboard_cost:.2f} EUR")
print("-" * 50 + f"\nTotal: {total:.2f} EUR\n" + "=" * 50)

