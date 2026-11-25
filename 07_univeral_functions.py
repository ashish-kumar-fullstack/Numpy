# UNIVERSAL FUNCTIONS (ufuncs) .....................................................
import numpy as np


# ==========================================
# 1. np.sqrt() - SQUARE ROOT
# ==========================================
print("\n--- 1. Square Root ---")

arr = np.array([4, 9, 16, 25, 36])

print("Original Array:", arr)
print("Square Root:", np.sqrt(arr))


# ==========================================
# 2. np.square() - SQUARE
# ==========================================
print("\n--- 2. Square ---")

arr = np.array([2, 3, 4, 5, 6])

print("Original Array:", arr)
print("Square:", np.square(arr))


# ==========================================
# 3. np.exp() - EXPONENTIAL
# ==========================================
print("\n--- 3. Exponential ---")

arr = np.array([1, 2, 3, 4])

print("Original Array:", arr)
print("Exponential:", np.exp(arr))


# ==========================================
# 4. np.log() - NATURAL LOGARITHM
# ==========================================
print("\n--- 4. Natural Logarithm ---")

arr = np.array([1, 2, 10, 100])

print("Original Array:", arr)
print("Natural Log:", np.log(arr))


# ==========================================
# 5. np.log10() - LOG BASE 10
# ==========================================
print("\n--- 5. Log Base 10 ---")

arr = np.array([10, 100, 1000, 10000])

print("Original Array:", arr)
print("Log Base 10:", np.log10(arr))


# ==========================================
# 6. np.sin() - SINE
# ==========================================
print("\n--- 6. Sine ---")

arr = np.array([0, 30, 45, 60, 90])

# Convert degrees to radians
radians = np.deg2rad(arr)

print("Angles in Degrees:", arr)
print("Angles in Radians:", radians)
print("Sine:", np.sin(radians))


# ==========================================
# 7. np.cos() - COSINE
# ==========================================
print("\n--- 7. Cosine ---")

arr = np.array([0, 30, 45, 60, 90])

radians = np.deg2rad(arr)

print("Cosine:", np.cos(radians))


# ==========================================
# 8. np.tan() - TANGENT
# ==========================================
print("\n--- 8. Tangent ---")

arr = np.array([0, 30, 45, 60])

radians = np.deg2rad(arr)

print("Tangent:", np.tan(radians))


# ==========================================
# 9. np.abs() - ABSOLUTE VALUE
# ==========================================
print("\n--- 9. Absolute Value ---")

arr = np.array([-10, -20, 30, -40, 50])

print("Original Array:", arr)
print("Absolute Value:", np.abs(arr))


# ==========================================
# 10. np.round() - ROUNDING
# ==========================================
print("\n--- 10. Rounding ---")

arr = np.array([2.4567, 3.7891, 4.1234, 5.6789])

print("Original Array:", arr)
print("Round to 2 decimal places:", np.round(arr, 2))
print("Round to 1 decimal place:", np.round(arr, 1))
print("Round to nearest integer:", np.round(arr))


# ==========================================
# 11. np.floor() - FLOOR
# ==========================================
print("\n--- 11. Floor ---")

arr = np.array([2.7, 3.9, 4.1, 5.8, -2.3])

print("Original Array:", arr)
print("Floor:", np.floor(arr))


# ==========================================
# 12. np.ceil() - CEILING
# ==========================================
print("\n--- 12. Ceiling ---")

arr = np.array([2.1, 3.4, 4.8, 5.2, -2.3])

print("Original Array:", arr)
print("Ceiling:", np.ceil(arr))


# ==========================================
# 13. COMBINING MULTIPLE UFUNCS
# ==========================================
print("\n--- 13. Combining Multiple Functions ---")

arr = np.array([4, 9, 16, 25, 36])

# Square root
sqrt_values = np.sqrt(arr)

# Square the square root values
square_values = np.square(sqrt_values)

# Round values
rounded_values = np.round(square_values, 2)

print("Original Array:", arr)
print("Square Root:", sqrt_values)
print("Square of Square Root:", square_values)
print("Rounded Result:", rounded_values)