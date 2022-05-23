#Compute the sum of digits in all numbers from 1 to n.
#When a user enters a number n, find the sum of digits in all numbers from 1 to n.
import math
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
def sum_digits(n):
    return (n*(n+1)/2)

print(sum_digits(5))

#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.
def maximum (a, b, c):
    list = [a, b, c]
    return max(list)

#print(maximum (124, 21, 32))

#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5)
list1 = [3, 4, 5, 6, 0]

even_count, odd_count = 0, 0

for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count +=1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list:", odd_count)











