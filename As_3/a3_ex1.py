# K11720457
# Aral Cimcim

# Write a program that reads in a matrix specified by the number of rows and columns, and then prints this matrix.

num_rows = int(input("Number of rows: "))
num_cols = int(input("Number of cols: "))

# create the matrix as an empty list
matrix = []

# iterate through the rows and columns
for i in range(num_rows):
    rows = []
    for j in range(num_cols):
        # if i == j add 1, else add 0
        if i == j:
            rows.append(1)
        else:
            rows.append(0)
    # add the rows to the matrix
    matrix.append(rows)

# print the header (column index and the double hyphens)
col_index = ""
for j in range(num_cols):
    col_index += str(j) + " "

print("   " + col_index[:-1])
print("  " + "-" * num_cols * 2)

# print the rows with a vertical separator
for i in range(len(matrix)):
    row = matrix[i]
    sub_row = ""
    for j in row:
        sub_row += str(j) + " "

    # print the rows and remove the last empty space
    print(str(i) + "| " + sub_row[:-1])

