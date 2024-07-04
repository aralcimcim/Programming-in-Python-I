# K11720457
# Aral Cimcim

# Write a function sub_summarize(nested: list, sub_sums: list) -> int that calculates the sum of the input list nested and sums of sub lists arbitrarily nested in the input list.

def sub_summarize(nested: list, sub_sums: list) -> int:
    # Set num_total to 0.
    num_total = 0

    # Iterate through the list.
    for i in nested:
        # If the item is a list find the sub_total.
        if isinstance(i, list):
            sub_total = sub_summarize(i, sub_sums)

            num_total += sub_total
        # Otherwise add the non sublist items.
        else:
            num_total += i

    # Append the num_total.
    sub_sums.append(num_total)

    return num_total

