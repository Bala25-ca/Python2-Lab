import math
import random
import platform

# Generate a random number between 1 and 100 using the random module
random_number = random.randint(1, 100)
print(f"Random number generated: {random_number}")

# Calculate the square root of the random number using the math module
square_root = math.sqrt(random_number)
print(f"Square root of {random_number}: {square_root}")

# Get the current operating system using the platform module
current_os = platform.system()
print(f"Current operating system: {current_os}")
