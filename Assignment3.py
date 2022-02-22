#7.Convert Dictionary to list

# dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# output = []
# for key, value in dict.items():
#     tmp = []
#     tmp.append(key)
#     tmp.extend(value)
#     output.append(tmp)
# print(output)


#6.Rename key city to location in the following dictionary

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)

#1.Return all the duplicate values from list of arraylist

# k = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
# new_k = []
# for elem in k:
#     if elem not in new_k:
#         new_k.append(elem)
# k = new_k
# print(k)

#2.Merge two lists as shown below

# list1 = ["Hello ", "take"]
# list2 = ["Dear", "Sir"]
# list1.extend(list2)
# print(list1)

#6.Merge following two Python dictionaries into one

# dict_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict_2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict_1.update(dict_2)
# print('Updated dictionary:')
# print(dict_1)

#5.Merge following two Python dictionaries into one

# Keys = ["Ten", "Twenty", "Thirty"]
# Value = [10,20,30]
# dict_from_list = dict(zip(Keys, Value))
# print(dict_from_list)