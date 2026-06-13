#decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.



def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator
def greeter(name):
    print(f"Hello, {name}!")


greeter("Alice")