# K11720457
# Aral Cimcim

# Write a function clip(*values, min_=0, max_=1) -> list that returns a list of clipped values based on arbitrary many input values *values (integers or floats)

def clip(*values, min_=0, max_=1) -> list:
    if values == None:
        return []

    result = []
    for value in values:
        if value < min_:
            result.append(min_)
        elif value > max_:
            result.append(max_)
        else:
            result.append(value)
    return result

