# decorators in Python
## decorator example
def print_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments for {func.__name__} were: {args}")
        print(f"Keyword arguments for {func.__name__} were: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

## decorator applied to function
@print_arguments
def add(x, y):
    return x + y

## driver code
add(3, 5)



