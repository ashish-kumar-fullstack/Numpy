import numpy as np

# ==========================================
# 1. ACCESSING ARRAY ELEMENTS
# ==========================================
print("\n--- 1. Accessing Array Elements ---")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Element at index 0:", arr[0])
print("Element at index 2:", arr[2])


# ==========================================
# 2. POSITIVE INDEXING
# ==========================================
print("\n--- 2. Positive Indexing ---")

arr = np.array([100, 200, 300, 400, 500])

print("Array:", arr)
print("First element:", arr[0])
print("Second element:", arr[1])
print("Third element:", arr[2])
print("Last element using positive index:", arr[4])


# ==========================================
# 3. NEGATIVE INDEXING
# ==========================================
print("\n--- 3. Negative Indexing ---")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Last element:", arr[-1])
print("Second last element:", arr[-2])
print("Third last element:", arr[-3])


# ==========================================
# 4. SLICING 1D ARRAYS
# ==========================================
print("\n--- 4. Slicing 1D Arrays ---")

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original Array:", arr)

print("arr[1:5]:", arr[1:5])
print("arr[:4]:", arr[:4])
print("arr[3:]:", arr[3:])
print("arr[::2]:", arr[::2])
print("arr[1::2]:", arr[1::2])
print("arr[::-1]:", arr[::-1])


# ==========================================
# 5. SLICING 2D ARRAYS
# ==========================================
print("\n--- 5. Slicing 2D Arrays ---")

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:\n", arr)

print("First two rows:\n", arr[:2, :])
print("First two columns:\n", arr[:, :2])
print("Rows 1 to 2, columns 1 to 2:\n", arr[1:3, 1:3])
print("Every second column:\n", arr[:, ::2])


# ==========================================
# 6. ACCESSING ROWS AND COLUMNS
# ==========================================
print("\n--- 6. Accessing Rows and Columns ---")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original Array:\n", arr)

# Access rows
print("First row:", arr[0])
print("Second row:", arr[1])
print("Last row:", arr[-1])

# Access columns
print("First column:", arr[:, 0])
print("Second column:", arr[:, 1])
print("Last column:", arr[:, -1])

# Access specific element
print("Element at row 2, column 3:", arr[1, 2])


# ==========================================
# 7. SLICING 3D ARRAYS
# ==========================================
print("\n--- 7. Slicing 3D Arrays ---")

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("Original 3D Array:\n", arr)

# Access first 2D block
print("First block:\n", arr[0])

# Access second 2D block
print("Second block:\n", arr[1])

# Access one element
print("Element:", arr[1, 0, 2])

# Slice rows and columns from first block
print("First block, first row:\n", arr[0, 0, :])

# Get all blocks, first row, all columns
print("First row from all blocks:\n", arr[:, 0, :])


# ==========================================
# 8. FANCY INDEXING
# ==========================================
print("\n--- 8. Fancy Indexing ---")

arr = np.array([10, 20, 30, 40, 50, 60])

# Select multiple indexes
print("Selected elements:", arr[[0, 2, 4]])

# Select elements in custom order
print("Custom order:", arr[[4, 1, 3]])

# Fancy indexing in 2D arrays
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original 2D Array:\n", arr2)

# Select rows 0 and 2
print("Selected rows:\n", arr2[[0, 2]])

# Select specific elements using row and column indexes
print("Selected elements:", arr2[[0, 1, 2], [2, 0, 1]])


# ==========================================
# 9. BOOLEAN INDEXING
# ==========================================
print("\n--- 9. Boolean Indexing ---")

arr = np.array([10, 20, 30, 40, 50, 60])

# Boolean mask
mask = arr > 30

print("Original Array:", arr)
print("Boolean Mask:", mask)
print("Filtered Elements:", arr[mask])

# Boolean indexing in 2D
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original 2D Array:\n", arr2)
print("Elements greater than 50:", arr2[arr2 > 50])


# ==========================================
# 10. CONDITIONAL FILTERING
# ==========================================
print("\n--- 10. Conditional Filtering ---")

arr = np.array([10, 15, 20, 25, 30, 35, 40, 45])

# Greater than 25
print("Greater than 25:", arr[arr > 25])

# Less than 30
print("Less than 30:", arr[arr < 30])

# Equal to 30
print("Equal to 30:", arr[arr == 30])

# Even numbers
print("Even numbers:", arr[arr % 2 == 0])

# Odd numbers
print("Odd numbers:", arr[arr % 2 != 0])

# Numbers between 20 and 40
print("Between 20 and 40:", arr[(arr >= 20) & (arr <= 40)])

# Numbers greater than 20 OR less than 15
print("Using OR:", arr[(arr > 20) | (arr < 15)])

# 2D conditional filtering
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("2D Array:\n", arr2)

# Filter numbers greater than 40
print("Greater than 40:", arr2[arr2 > 40])

# Replace values conditionally
arr3 = arr2.copy()
arr3[arr3 < 50] = 0

print("Replace values less than 50 with 0:\n", arr3)