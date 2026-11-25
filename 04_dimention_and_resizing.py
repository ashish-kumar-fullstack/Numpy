
# Array Dimensions and Reshaping .........................................

# 0D arrays
# 1D arrays
# 2D arrays
# 3D arrays
# Higher-dimensional arrays
# reshape()
# flatten()
# ravel()
# transpose()
# T attribute
# expand_dims()
# squeeze()
# resize()
# newaxis

import numpy as np

# ==========================================
# 1. 0D ARRAY (SCALAR)
# ==========================================
print("\n--- 0D Array ---")

arr0 = np.array(10)

print(arr0)
print("Dimensions:", arr0.ndim)
print("Shape:", arr0.shape)


# ==========================================
# 2. 1D ARRAY
# ==========================================
print("\n--- 1D Array ---")

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1)
print("Dimensions:", arr1.ndim)
print("Shape:", arr1.shape)


# ==========================================
# 3. 2D ARRAY
# ==========================================
print("\n--- 2D Array ---")

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr2)
print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)


# ==========================================
# 4. 3D ARRAY
# ==========================================
print("\n--- 3D Array ---")

arr3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr3)
print("Dimensions:", arr3.ndim)
print("Shape:", arr3.shape)


# ==========================================
# 5. HIGHER DIMENSIONAL ARRAY
# ==========================================
print("\n--- Higher Dimensional Array ---")

arr_high = np.array([1, 2, 3, 4, 5, 6], ndmin=5)

print(arr_high)
print("Dimensions:", arr_high.ndim)
print("Shape:", arr_high.shape)


# ==========================================
# 6. RESHAPE()
# ==========================================
print("\n--- Reshape ---")

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2, 3)

print("Original Array:", arr)
print("Reshaped Array:\n", reshaped)


# ==========================================
# 7. FLATTEN()
# ==========================================
print("\n--- Flatten ---")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flattened = arr.flatten()

print("Original Array:\n", arr)
print("Flattened Array:", flattened)


# ==========================================
# 8. RAVEL()
# ==========================================
print("\n--- Ravel ---")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

raveled = arr.ravel()

print("Original Array:\n", arr)
print("Raveled Array:", raveled)


# ==========================================
# 9. TRANSPOSE()
# ==========================================
print("\n--- Transpose ---")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

transposed = np.transpose(arr)

print("Original Array:\n", arr)
print("Transposed Array:\n", transposed)


# ==========================================
# 10. T ATTRIBUTE
# ==========================================
print("\n--- T Attribute ---")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

transposed = arr.T

print("Original Array:\n", arr)
print("Transpose using T:\n", transposed)


# ==========================================
# 11. EXPAND_DIMS()
# ==========================================
print("\n--- Expand Dims ---")

arr = np.array([10, 20, 30])

expanded_axis0 = np.expand_dims(arr, axis=0)
expanded_axis1 = np.expand_dims(arr, axis=1)

print("Original Array:", arr)
print("Axis 0:\n", expanded_axis0)
print("Axis 0 Shape:", expanded_axis0.shape)

print("Axis 1:\n", expanded_axis1)
print("Axis 1 Shape:", expanded_axis1.shape)


# ==========================================
# 12. SQUEEZE()
# ==========================================
print("\n--- Squeeze ---")

arr = np.array([[[10, 20, 30]]])

squeezed = np.squeeze(arr)

print("Original Array:\n", arr)
print("Original Shape:", arr.shape)

print("Squeezed Array:", squeezed)
print("Squeezed Shape:", squeezed.shape)


# ==========================================
# 13. RESIZE()
# ==========================================
print("\n--- Resize ---")

arr = np.array([1, 2, 3, 4])

resized = np.resize(arr, (2, 3))

print("Original Array:", arr)
print("Resized Array:\n", resized)
print("Resized Shape:", resized.shape)


# ==========================================
# 14. NEWAXIS
# ==========================================
print("\n--- Newaxis ---")

arr = np.array([10, 20, 30])

row_array = arr[np.newaxis, :]
column_array = arr[:, np.newaxis]

print("Original Array:", arr)
print("Row Array:\n", row_array)
print("Row Shape:", row_array.shape)

print("Column Array:\n", column_array)
print("Column Shape:", column_array.shape)


