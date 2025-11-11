# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(x):
    return x * x

# Apply the square function to each number using map()
squared_numbers_map = map(square, numbers)

# Convert the map object to a list for printing
squared_numbers_list = list(squared_numbers_map)

print(f"Original numbers: {numbers}")
print(f"Squared numbers (using map and a named function): {squared_numbers_list}")

# Using a lambda function with map()
cubed_numbers_map = map(lambda x: x**3, numbers)
cubed_numbers_list = list(cubed_numbers_map)

print(f"Cubed numbers (using map and a lambda function): {cubed_numbers_list}")