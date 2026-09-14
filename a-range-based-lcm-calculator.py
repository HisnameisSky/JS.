import math

def smallest_commons(arr):
    min_val = min(arr)
    max_val = max(arr)
    def gcd(a,b):
        return a if b == 0 else gcd(b,a%b)

    def lcm(a,b):
        return (a*b) // gcd(a,b)

    multiple = min_val
    for i in range(min_val +1, max_val +1):
        multiple = lcm(multiple,i)
    return multiple

#

def smallest_commons_pythonic(arr):
    return math.lcm(*range(min(arr),max(arr)+1))

#

import math

print(math.lcm(12,18))
print(math.lcm(2,3,4,5,6))

numbers=[12,18,24,30]
print(math.lcm(*numbers))

print(math.lcm(*range(1,14)))

#

import math
print(math.gcd(24,36,60,84))
data = [100, 150,200,250]
print(math.gcd(*data))

#

import math 
factors = [2,3,5,7]
print(math.prod(factors))
