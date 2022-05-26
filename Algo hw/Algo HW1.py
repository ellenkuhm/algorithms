#Compute the sum of digits in all numbers from 1 to n.
#When a user enters a number n, find the sum of digits in all numbers from 1 to n.
import math
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
'''n = int(input("Please enter a random number :"))

def sum_digits(n):
    return (n*(n+1)/2)

print(sum_digits(n))

#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.
list_2 = []
for i in range(3):
    number = int(input("Please enter a number: "))
    list_2.append(number)

def maximum (a, b, c):
    list_2 = [a, b, c]
    return max(list_2)

print("Max number :", maximum (list_2[0], list_2[1], list_2[2]))'''

#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5)
list1 = []
for i in range (5):
    number = int(input("Please enter a number: "))
    list1.append(number)

even_count, odd_count = 0, 0

for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list:", odd_count)











