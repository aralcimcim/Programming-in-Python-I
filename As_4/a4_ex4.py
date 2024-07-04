# K11720457
# Aral Cimcim

# Write a function round_(number, ndigits: int) that rounds a given number (integer or float) to ndigits precision

def round_(number, ndigits: int):
    if ndigits is None:
        return int(number + 0.5)
    else:
        factor = 10 ** ndigits
        temp = number * factor
        if temp - int(temp) < 0.5:
            return int(temp) / factor
        else:
            return (int(temp) + 1) / factor