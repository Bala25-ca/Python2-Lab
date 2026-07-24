#Generate Fibonacci numbers using a generator function
def gen_fibonacci(n):
    x = 0
    y = 1
    print(x)
    print(y)
    for i in range(n):
        
        z = x + y
        x = y
        y = z
        print(z)

n = int(input("Enter the number of Fibonacci numbers to generate: "))
gen_fibonacci(n)
    
