# Array Operations ............................................

import numpy as np

# ==========================================
# 1. ADDITION
# ==========================================
print("\n--- 1. Addition ---")

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Using np.add():", np.add(arr1, arr2))

# Addition with a scalar
print("Scalar Addition:", arr1 + 5)


# ==========================================
# 2. SUBTRACTION
# ==========================================
print("\n--- 2. Subtraction ---")

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("Subtraction:", arr1 - arr2)
print("Using np.subtract():", np.subtract(arr1, arr2))

# Subtract scalar
print("Scalar Subtraction:", arr1 - 5)


# ==========================================
# 3. MULTIPLICATION
# ==========================================
print("\n--- 3. Multiplication ---")

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 3, 4, 5])

print("Multiplication:", arr1 * arr2)
print("Using np.multiply():", np.multiply(arr1, arr2))

# Scalar multiplication
print("Scalar Multiplication:", arr1 * 2)


# ==========================================
# 4. DIVISION
# ==========================================
print("\n--- 4. Division ---")

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 5, 8])

print("Division:", arr1 / arr2)
print("Using np.divide():", np.divide(arr1, arr2))

# Scalar division
print("Scalar Division:", arr1 / 2)


# ==========================================
# 5. MODULUS
# ==========================================
print("\n--- 5. Modulus ---")

arr1 = np.array([10, 15, 20, 25, 30])

print("Modulus by 3:", arr1 % 3)
print("Using np.mod():", np.mod(arr1, 3))

# Even numbers
print("Even numbers:", arr1[arr1 % 2 == 0])


# ==========================================
# 6. POWER
# ==========================================
print("\n--- 6. Power ---")

arr1 = np.array([2, 3, 4, 5])

print("Power of 2:", arr1 ** 2)
print("Using np.power():", np.power(arr1, 2))

# Different powers for different elements
arr2 = np.array([2, 3, 4])
powers = np.array([2, 3, 2])

print("Different Powers:", np.power(arr2, powers))


# ==========================================
# 7. FLOOR DIVISION
# ==========================================
print("\n--- 7. Floor Division ---")

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([3, 6, 7, 9])

print("Floor Division:", arr1 // arr2)
print("Using np.floor_divide():", np.floor_divide(arr1, arr2))

# Scalar floor division
print("Scalar Floor Division:", arr1 // 3)


# ==========================================
# 8. COMPARISON OPERATORS
# ==========================================
print("\n--- 8. Comparison Operators ---")

arr1 = np.array([10, 20, 30, 40, 50])

print("Array:", arr1)

print("Greater than 25:", arr1 > 25)
print("Less than 25:", arr1 < 25)
print("Greater than or equal to 30:", arr1 >= 30)
print("Less than or equal to 30:", arr1 <= 30)
print("Equal to 30:", arr1 == 30)
print("Not equal to 30:", arr1 != 30)

# Comparison between two arrays
arr2 = np.array([10, 25, 30, 35, 60])

print("Array comparison (arr1 == arr2):", arr1 == arr2)
print("Array comparison (arr1 > arr2):", arr1 > arr2)


# ==========================================
# 9. LOGICAL OPERATORS
# ==========================================
print("\n--- 9. Logical Operators ---")

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([5, 25, 30, 45, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Logical AND
print("Logical AND:", np.logical_and(arr1 > 20, arr1 < 50))

# Logical OR
print("Logical OR:", np.logical_or(arr1 < 20, arr1 > 40))

# Logical NOT
print("Logical NOT:", np.logical_not(arr1 > 30))

# Logical XOR
print("Logical XOR:", np.logical_xor(arr1 > 20, arr2 > 20))

# Using & and |
print("Using &:", (arr1 > 20) & (arr1 < 50))
print("Using |:", (arr1 < 20) | (arr1 > 40))


# ==========================================
# 10. MATHEMATICAL OPERATIONS
# ==========================================
print("\n--- 10. Mathematical Operations ---")

arr = np.array([1, 4, 9, 16, 25, 36])

print("Original Array:", arr)

# Square Root
print("Square Root:", np.sqrt(arr))

# Absolute Value
arr2 = np.array([-10, -20, 15, -25])
print("Absolute Value:", np.abs(arr2))

# Exponential
print("Exponential:", np.exp(np.array([1, 2, 3])))

# Natural Logarithm
print("Natural Log:", np.log(np.array([1, 2, 3])))

# Logarithm base 10
print("Log Base 10:", np.log10(np.array([10, 100, 1000])))

# Sin
print("Sine:", np.sin(np.array([0, np.pi/2, np.pi])))

# Cos
print("Cosine:", np.cos(np.array([0, np.pi/2, np.pi])))

# Tan
print("Tangent:", np.tan(np.array([0, np.pi/4])))

# Rounding
arr3 = np.array([2.456, 3.789, 4.123])

print("Round:", np.round(arr3, 2))

# Floor
print("Floor:", np.floor(arr3))

# Ceiling
print("Ceiling:", np.ceil(arr3))