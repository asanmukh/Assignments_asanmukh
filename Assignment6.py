# write a decorator which will take a function and execute it twice. Function is

def smart_multiply(func):
    def inner(a,b):
        print("I am going to multiply", a, "and", b)
        return func(a,b)
    return inner

@smart_multiply
def multiply(a,b):
    print(a*b)
