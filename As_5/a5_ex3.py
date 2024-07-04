# K11720457
# Aral Cimcim

# Write a generator function gen_fibonacci(upper_bound) that yields Fibonacci numbers which are not greater than upper_bound (can be included)

def gen_fibonacci(upper_bound):
    # TypeError for wrong bound type.
    if not isinstance(upper_bound, (int, float)):
        raise TypeError("The upper bound must be either int or float")
    
    # ValueError for negative upper_bound.
    if upper_bound < 0:
        raise ValueError("The upper bound can not be negative")
    
    a = 0 # F(0)
    b = 1 # F(1)

    # Yield "a" until upper bound.
    while a <= upper_bound:
        yield a
        a, b = b, a + b

# list(gen_fibonacci("3"))
list(gen_fibonacci(-1))
# list(gen_fibonacci(0)) -> [0]
# list(gen_fibonacci(1)) -> [0, 1, 1]
# list(gen_fibonacci(3)) -> [0, 1, 1, 2, 3]
# list(gen_fibonacci(9.2)) -> [0, 1, 1, 2, 3, 5, 8]