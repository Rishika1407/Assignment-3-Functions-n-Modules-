#Task 1

def factorial(n): 
 if n < 2: 
     return 1 
 else:
    return n * factorial(n - 1)

#Call the function with a sample number
sample = 5 
print("Factorial of", sample, "is:", factorial(sample))

#Task 2

import math

num = float(input("Enter a number: "))

sine_result = math.sin(num)  # Always calculate sine

if num > 0:
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    print("Square root:", sqrt_result)
    print("Natural logarithm (ln):", log_result)
else:
    print("Please enter a number greater than 0 for square root and log calculations.")

print("Sine (in radians):", sine_result)

