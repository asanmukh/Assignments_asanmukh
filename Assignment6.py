# write a decorator which will take a function and execute it twice. Function is

# def smart_multiply(func):
#     def inner(a,b):
#         print("I am going to multiply", a, "and", b)
#         return func(a,b)
#     return inner
#
# @smart_multiply
# def multiply(a,b):
#     print(a*b)
# multiply(2,4)


# Create a generator to return the fibonnaci sequence starting from the first element
# up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
# 89, . . .

# def fin(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a+b #adding the number first and then swap it
#
# inp = int(input("Enter the number you want to generate fibonnaci series upto : "))
# print(list(fin(inp)))