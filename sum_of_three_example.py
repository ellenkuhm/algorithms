# Our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.


import random

random_number = random.randint(1, 5)

print(f'The random number is: {random_number}')
#
# result = 0
# # for digit in str(random_number):  # 349 -> [3, 4, 9] string
# #     result = result + int(digit)
#
# # O(n)  # n = length of random_number
# while random_number != 0:
#     result = result + (random_number % 10)
#     random_number = random_number // 10
#
# print(f'Result: {result}')