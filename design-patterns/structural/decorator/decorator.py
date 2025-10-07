# decorators in Python ==================================================
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


# Decorator Design Pattern ==================================================
class Emperor:
    def __init__(self):
        self.clothes = []
    
    def declare_clothes(self):
        return f"The emperor is wearing: {', '.join(self.clothes) if self.clothes else 'nothing!'}"


class BaseDecorator:
    def __init__(self, emperor):
        self.emperor = emperor
    
    @property
    def clothes(self):
        return self.emperor.clothes
    
    def declare_clothes(self):
        return self.emperor.declare_clothes()

class ShirtDecorator(BaseDecorator):
    def __init__(self, emperor):
        super().__init__(emperor)
        self.emperor.clothes.append("a shirt")

class PantsDecorator(BaseDecorator):
    def __init__(self, emperor):
        super().__init__(emperor)
        self.emperor.clothes.append("pants")

class HatDecorator(BaseDecorator):
    def __init__(self, emperor):
        super().__init__(emperor)
        self.emperor.clothes.append("a hat")

## driver code
emperor = Emperor()
print(emperor.declare_clothes())
shirted_emperor = ShirtDecorator(emperor)
print(shirted_emperor.declare_clothes())
pants_emperor = PantsDecorator(shirted_emperor)
print(pants_emperor.declare_clothes())
hatted_emperor = HatDecorator(pants_emperor)
print(hatted_emperor.declare_clothes())