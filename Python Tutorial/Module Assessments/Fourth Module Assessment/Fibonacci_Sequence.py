# Define required variables
n = int(input("Enter the number of Fibonacci terms you want: "))  # Input from the user
a, b = 0, 1  # Initializing the first two Fibonacci numbers

# Start the loop to calculate Fibonacci numbers
for i in range(n):
    print(f"Term {i + 1}: {a}")  # Print the current Fibonacci number
    a, b = b, a + b  # Update Fibonacci numbers
