import math  # Import math module for mathematical constants and functions

# Take the input from the user for the radius ,Ensure the radius is positive by taking its absolute value
radius = abs(float(input("Enter the radius of the circle: ")))

# Calculate the circumference and area
circumference = 2 * math.pi * radius
area = math.pi * radius**2

# Print the results
print("\nResults:")
print(f"Circumference: {circumference}")
print(f"Area: {area}")
