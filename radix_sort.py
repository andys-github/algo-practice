# -----------------------------
# Radix Sort
# -----------------------------
# Best Case:  O(nk)
# Avg Case:   O(nk)
# Worst Case: O(nk)
#
# Space Complexity: O(n + k)

# -----------------------------
# Helper methods
# -----------------------------

from math import log10, floor
def digit_count(num):
  '''
  returns the number of digits in a given number
  '''
  return floor(log10(abs(num))) + 1

# print('No of digits in 123: ', digit_count(123))
# print('No of digits in 12345: ', digit_count(12345))

def get_digit(num, place):
  '''
  returns the nth place digit of a number from the right
  '''
  return floor(abs(num) / (10**place)) % 10

# print('The 0th digit from right in 123 is: ', get_digit(123, 0))
# print('The 2nd digit from right in 123 is: ', get_digit(123, 2))
# print('The 4th digit from right in 123 is: ', get_digit(123, 4))

def most_digit(nums):
  '''
  returns the max number of digits from an array of numbers
  '''
  max_digits = 0
  for num in nums:
    current_digits = digit_count(num)
    max_digits = max_digits if max_digits > current_digits else current_digits
  return max_digits

# print('Max no. of digits in [123, 2, 32] is: ', most_digit([123, 2, 32]))

def radix_sort(arr): # O(k (2n)) --> O(nk)
  max_digit_count = most_digit(arr)
  for k in range(max_digit_count): # O(k)
    sub_arr = [[] for i in range(10)]
    for i in arr:  # O(n)
      digit = get_digit(i, k)
      sub_arr[digit].append(i)
    temp_arr = []
    list(map(temp_arr.extend, sub_arr)) # O(n)
    arr = temp_arr

  return arr

input_arr = [123, 4, 2398, 111, 99, 3, 100, 6789, 3456]

print(f'Input Array: {input_arr}')
print(f'Radix Sorted: {radix_sort(input_arr)}')
