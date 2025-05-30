# create a decorater to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_values = '. '.join(str(arg) for arg in args)
        kwargs_values = '. '.join(f"{k}={v}"for k, v in kwargs.items())
        print(f"function is {func.__name__} with arguments {args_values} ans kwargs value {kwargs_values}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Hello")

@debug
def greet(name, greeting = "Hello"):
    print(f"{name}, {greeting} !")

hello()
greet("Himanshu", "Namaste")