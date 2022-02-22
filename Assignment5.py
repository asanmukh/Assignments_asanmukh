# 3. Convert a number to positive if
# it's negative in the list. Only pass those that are converted from negative to positive to the new list.

# list1=[-1000, 500, -600, 700, 5000, -90000, -17500]
# list2 = list(filter(map(list1,-list1 )))
# print(list2)

#5.Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.

# list1 = ["Netflix", "Hulu", "Sling", "Hbo"]
# list2 = [198, 166, 237, 125]
# d = dict(zip(list1, list2))
# print(d)

# 4. Take the first two values, run the function on them. Then take the result and the
# next value and have a multiplication between them. etc. When no more values are left, return the last result.

# from functools import reduce
# num_list = [1,2,3,4,5]
# def prod(x, y):
#     return x * y
# product = reduce(prod, num_list)
# print(product)