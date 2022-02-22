#1.Python program to find roots of quadratic equation
# import math
#
# # function for finding roots
# def equationroots(a, b, c):
#     # calculating discriminant using formula
#     dis = b * b - 4 * a * c
#     sqrt_val = math.sqrt(abs(dis))
#
#     # checking condition for discriminant
#     if dis > 0:
#         print(" real and different roots ")
#         print((-b + sqrt_val) / (2 * a))
#         print((-b - sqrt_val) / (2 * a))
#
#     elif dis == 0:
#         print(" real and same roots")
#         print(-b / (2 * a))
#
#         # when discriminant is less than 0
#     else:
#         print("Complex Roots")
#         print(- b / (2 * a), " + i", sqrt_val)
#         print(- b / (2 * a), " - i", sqrt_val)
#
#     # Driver Program
# a = 1
# b = 5
# c = 1
#
# # If a is 0, then incorrect equation
# if a == 0:
#     print("Input correct quadratic equation")
#
# else:
#     equationroots(a, b, c)


#2.Using map() function and lambda and count() function
#create a list consisted of the number of occurence of both letters: A and a.

# lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
# lst2 = list(map(lambda x: x.count("a") + x.count("A"), lst1))
# print(lst2)


