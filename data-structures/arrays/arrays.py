# Dynamic Arrays
# - Arrays that grow in size dynamically
#
# In Python, the list datatype creates
# an array with an initial size.
# And later, as we keep on appending elements
# to the array (list), python increases the
# size of the array dynamically

import sys # to calculate the size of something (array) in bytes

def dynamic_array_size():
  arr = []
  n = 10
  for i in range(n):
    print(f'No of elements in array: {len(arr)} - Size of array: {sys.getsizeof(arr)}')
    arr.append(i)

dynamic_array_size()
# OUTPUT
#
# No of elements in array: 0 - Size of array: 56
# No of elements in array: 1 - Size of array: 88
# No of elements in array: 2 - Size of array: 88
# No of elements in array: 3 - Size of array: 88
# No of elements in array: 4 - Size of array: 88
# No of elements in array: 5 - Size of array: 120
# No of elements in array: 6 - Size of array: 120
# No of elements in array: 7 - Size of array: 120
# No of elements in array: 8 - Size of array: 120
# No of elements in array: 9 - Size of array: 184
