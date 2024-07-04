import numpy as np

def one_hot_encoding(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError(f"The function can work for 1D matrices, not {arr.ndim}D")

    unique_vals = np.sort(np.unique(arr))

    unique_idx = {}

    for idx, val in enumerate(unique_vals):
        unique_idx[val] = idx
    
    one_hot = np.zeros((arr.shape[0], unique_vals.shape[0]))

    for i in range(arr.shape[0]):
        one_hot[i][unique_idx[arr[i]]] = 1
    
    return one_hot

# if __name__ == "__main__":
#     a = np.array(["a", "a", "b", "c"])
#     print(one_hot_encoding(a))
#     a = np.array([10, 5, 15, 20])
#     print(one_hot_encoding(a))

#     a = np.array([[1, 2], [3, 4]])
#     try:
#         print(one_hot_encoding(a))
#     except ValueError as e:
#         print(f"ValueError: {e}")

