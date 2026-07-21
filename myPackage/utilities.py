def greet_user(name):
	"""Return a greeting for the given user name."""
	return "Hello, {}!".format(name)


if __name__ == '__main__':
	# simple CLI greeting when run as a script
	try:
		import sys
		#name = sys.argv[1] if len(sys.argv) > 1 else 'User'
		name = input(str("Enter your name: "))
		
	except Exception:
		#name = 'User'
		print("No name provided. Using default name 'User'.")
	print(greet_user(name))

#Using factorial function from math module
import math

def calculate_factorial(n):
	"""Calculate the factorial of a given number n."""
	return math.factorial(n)
n = int(input("Enter a number to calculate its factorial: "))
return_value = calculate_factorial(n)
print(f"The factorial of {n} is: {return_value}")




