num = 5

def factorial_calculator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factorial = factorial_calculator(num)

result_msg = f"Factorial of {num} is {factorial}"

print(result_msg)

#Variant..
import math

python_easy_factorial = math.factorial(5)