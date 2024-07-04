import numpy as np
import numbers

def extend(arr: np.ndarray, rows: int, cols: int, fill=None) -> np.ndarray:

    arr_dim = arr.ndim
    if arr_dim == 2:
        arr_rows, arr_cols = arr.shape #arr.shape[0], arr.shape[1]
    
    else:
        raise ValueError(f"can only extend 2D arrays, not {arr_dim}D")
 
    if rows < arr_rows:
        raise ValueError("invalid rows")
    
    if cols < arr_cols:
        raise ValueError("invalid cols")
    
    if fill is not None and not isinstance(fill, numbers.Number):
        raise ValueError("invalid fill") 
    
    extended_arr = np.empty_like(arr, shape=(rows, cols))
    
    if fill is None:
    
        arr_row_mean = np.mean(arr, axis=1)
        arr_col_mean = np.mean(arr, axis=0)
        arr_mean = np.mean(arr)

    for row in range(rows):
        for col in range(cols):
            if row < arr_rows and col < arr_cols:
                extended_arr[row][col] = arr[row][col]
            else:
                if fill is None:
                    if row < arr_rows:
                        extended_arr[row][col] = arr_row_mean[row]
                    elif col < arr_cols:
                        extended_arr[row][col] = arr_col_mean[col]
                    else:
                        extended_arr[row][col] = arr_mean
                else:
                    extended_arr[row][col] = fill

    return extended_arr


# if __name__ == '__main__':
#     m1 = np.arange(2*3).reshape(2,-1)
#     print(m1)
#     print(extend(m1, 2, 3))
#     print(extend(m1, 4, 5))

#     try:
#         print(extend(m1, 2, 1))
#     except ValueError as e:
#         print(f"ValueError: {e}")
#     try:
#         print(extend(m1, 1, 2))
#     except ValueError as e:
#         print(f"ValueError: {e}")

#     m2 = np.arange(2*3,dtype=float).reshape(2,-1)
#     print(m2)
#     print(extend(m2, 4, 5))
#     print(extend(m1, 4, 5, fill=10))

#     try:
#         print(extend(m2, 4,4, fill="foo"))
#     except ValueError as e:
#         print(f"ValueError: {e}")

#     m3 = np.ones(1)
#     print(m3)

#     try:
#         print(extend(m3, 2, 3))
#     except ValueError as e:
#         print(f"ValueError: {e}")