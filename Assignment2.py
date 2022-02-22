#problem1
# rows = int(input("Enter the number of rows : "))
# for i in range(0, rows):
#     coff = 1
#     for j in range(1, rows - i):
#         print("  ", end="")
#
#     for k in range(0, i + 1):
#         print("  ", coff, end="")
#         coff = int(coff * (i - k) / (k + 1))
#     print()


# problem2_pattern1

#Python Program to Print Diamond Star Pattern

# rows = int(input("Enter Diamond Pattern Rows = "))
#
# print("Diamond Star Pattern")
# k = 0
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(end=' ')
#     while k != 2 * i - 1:
#         print('*', end='')
#         k = k + 1
#     k = 0
#     print()
#
# k = 2
# l = 1
# for i in range(1, rows):
#     for j in range(1, k):
#         print(end=' ')
#     k = k + 1
#     while l <= (2 * (rows - i) - 1):
#         print('*', end='')
#         l = l + 1
#     l = 1
#     print()

#problem2_pattern2

# Generating Hollow Pyramid Pattern Using Stars

# row = int(input('Enter number of rows required: '))
#
# for i in range(row):
#     for j in range(row - i):
#         print(' ', end='')  # printing space required and staying in same line
#
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == row - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()  # printing new line

#problem2_pattern3

# N = int(input("enter the number of rows: "))
# for row in range(0,N):
#     for col in range(0,N):
#         if col == N-1 or row == 0 or col == row:
#            print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()