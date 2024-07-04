import numpy as np
# import numbers

def moving_average_2D(arr: np.ndarray, size: int) -> np.ndarray:
    if arr.ndim != 2:
        raise ValueError(f"apply for 2D array, not {arr.dim}D")
    
    # for element in arr:
    #     if not isinstance(element, numbers.Number):
    #         raise TypeError("Invalid data type")
    
    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("Invalid data type")

    if size < 1 or (size, size) > (arr.shape[0], arr.shape[1]):
        raise ValueError("Invalid window size")
    
    rows = arr.shape[0]
    cols = arr.shape[1]

    result = np.zeros((rows - size + 1, cols - size + 1))

    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            result[i, j] = np.mean(arr[i:i + size, j:j + size])

    return result

# if __name__ == "__main__":
#     arr = np.arange(4*5).reshape(4, -1)
#     print(arr)
#     result = moving_average_2D(arr, 3)
#     print(result)
#     try:
#         moving_average_2D(arr, 5)
#     except ValueError as e:
#         print(f"ValueError: {e}")
#     try:
#         moving_average_2D(np.array([["a", "b"], ["c", "d"]]), 2)
#     except TypeError as e:
#         print(f"TypeError: {e}")

