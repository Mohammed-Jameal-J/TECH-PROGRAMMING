import math_helper

math_helper.add(5, 3)        # Output: 8
math_helper.subtract(5, 3)   # Output: 2
math_helper.multiply(5, 3)   # Output: 15
math_helper.divide(5, 3)     # Output: 1.666666666

print(math_helper.PI)        # Output: 3.14159

from math_helper import add, subtract

print(add(10, 5))           # Output: 15
print(subtract(10, 5))      # Output: 5

from math_helper import add as addition