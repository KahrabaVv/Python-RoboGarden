def calculate_average(numbers):
    # Calculate the sum of the numbers in the list
    total_sum = sum(numbers)
    
    # Calculate the length of the list
    count = len(numbers)
    
    # Calculate the average by dividing the sum by the length
    if count == 0:
        return 0  # Avoid division by zero if the list is empty
    average = total_sum / count
    
    return average

# Example usage
numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("The average is:", result)
