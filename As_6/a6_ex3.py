# K11720457
# Aral Cimcim

# Write a function that merges .csv files
# headers: name;id;grade id;name;age name;id;email

import os

def merge_csv_files(*paths: str, delimiter = ';', only_shared_columns = False):

    csv_data = []

    headers_all = []

    for path in paths:
        with open(path, "r") as file:

            headers = file.readline().strip().split(delimiter)

            for header in headers:
                if header not in headers_all:
                    headers_all.append(header)
            
            for line in file:
                row = {}

                vals = line.strip().split(delimiter)

                for i in range(len(headers)):
                    row[headers[i]] = vals[i]

                csv_data.append(row)

    if only_shared_columns:
        file_name = "merged_shared.csv"

        shared_headers = []
        for header in headers_all:
            headers_all_rows = True
            for row in csv_data:
                if header not in row:
                    headers_all_rows = False
                    break
            
            if headers_all_rows:
                shared_headers.append(header)
        headers_all = shared_headers

    else:
        file_name = "merged_all.csv"

    output = os.path.join(os.path.dirname(paths[0]), file_name)

    with open(output, "w") as file:

        file.write(delimiter.join(headers_all) + "\n")

        for row in csv_data:
            rows_list = []
            for header in headers_all:
                if header in row:
                    rows_list.append(row[header])
                else:
                    rows_list.append("NaN")

            file.write(delimiter.join(rows_list) + "\n")

