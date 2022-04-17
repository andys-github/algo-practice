# Radix Sort

# Helper methods
# ------------------------------
# digit_count: returns the number of digits in a given number
# get_digit: returns the nth place digit from a number

from math import log10, floor
def digit_count(num):
  return floor(log10(abs(num))) + 1

# print('No of digits in 123: ', digit_count(123))
# print('No of digits in 12345: ', digit_count(12345))

def get_digit(num, place):
  return floor(abs(num) / (10**place)) % 10

print('The 0th digit from right in 123 is: ', get_digit(123, 0))
print('The 2nd digit from right in 123 is: ', get_digit(123, 2))
print('The 4th digit from right in 123 is: ', get_digit(123, 4))

