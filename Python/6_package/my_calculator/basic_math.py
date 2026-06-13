'''
A simple math helper module that provides 
basic arithmetic functions.
'''
#module math_helper
def add(a, b):
    '''Returns the sum of a and b.'''
    return a + b

def subtract(a, b):
    '''Returns the difference of a and b.'''
    return a - b

def multiply(a, b):
    '''Returns the product of a and b.'''
    return a * b

def divide(a, b):
    '''Returns the quotient of a and b.'''
    return a / b

PI = 3.14159


if __name__ == "__main__":
    # Test the functions
    print(add(5, 3))        # Output: 8
    print(subtract(5, 3))   # Output: 2
    print(multiply(5, 3))   # Output: 15
    print(divide(5, 3))     # Output: 1.666666666

    print(PI)              # Output: 3.14159