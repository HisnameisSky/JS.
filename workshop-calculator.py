import math


def calculate_sum(num1, num2):
    return num1 + num2


print(calculate_sum(2, 5))
print(calculate_sum(10, 10))
print(calculate_sum(5, 5))


def calculate_difference(num1, num2):
    return num1 - num2


print(calculate_difference(22, 5))
print(calculate_difference(12, 1))
print(calculate_difference(17, 9))


def calculate_product(num1, num2):
    return num1 * num2


print(calculate_product(13, 5))


def calculate_quotient(num1, num2):
    return "Error: Division by zero" if num2 == 0 else num1 / num2


print(calculate_quotient(7, 11))
print(calculate_quotient(3, 0))


def calculate_square(num):
    return num**2


print(calculate_square(2))
print(calculate_square(9))


def calculate_square_root(num):
    return math.sqrt(num)


print(calculate_square_root(25))
print(calculate_square_root(100))