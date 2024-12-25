# Take the first input from the user
first_number = float(input("Enter the first number: "))

# Take the second input from the user
second_number = float(input("Enter the second number: "))

# Perform operations
sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
if second_number != 0:
    division_result = first_number / second_number
else:
    division_result = "Undefined (cannot divide by zero)"
# Print the results
print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")
