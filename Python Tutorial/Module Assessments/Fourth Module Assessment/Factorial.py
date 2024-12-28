# Take the required input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Initialize the factorial variable
factorial = 1

# Apply the algorithm using a loop
for i in range(1, num + 1):
    factorial *= i  # Multiply each number from 1 to num

# Print the factorial
print(f"The factorial of {num} is {factorial}.")
