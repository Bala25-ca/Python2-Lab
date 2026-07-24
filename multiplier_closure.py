# make_multiplier(factor) is a closure that takes a factor and returns
#  a function that multiplies its input by that factor.

def make_multiplier(factor):
    """Returns a function that multiplies its input by the given factor."""
    def multiplier(x):
        return x * factor
    return multiplier   
#Demonstrate the use of the closure
times3 = make_multiplier(3)
times10 = make_multiplier(10)

#calling these functions with an argument to see the result
print(times3(7))  # Output: 21
print(times10(7))  # Output: 70
