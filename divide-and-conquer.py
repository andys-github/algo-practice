# Divide and Conquer
# using Recursion

# 1. Recursively find out sum of an integer array
def recur_sum(arr):
  if len(arr) == 0:
    return 0
  else:
    return arr.pop() + sum(arr)

input_arr_1 = [1, 2, 3, 4]
print("Input Array: ", input_arr_1)
print("Recursive Sum: ", recur_sum([1, 2, 3, 4]))
print("-------------------")

# 2. Recursively count the number of items in an array
def recur_count(arr):
  if arr == []:
    return 0
  else:
    arr.pop()
    return 1 + recur_count(arr)

input_arr_2 = [2, 1, 4, 6, 1]
print("Input Array: ", input_arr_2)
print("Recursive Count: ", recur_count(input_arr_2))
print("-------------------")

# 3. Recursively find the max item in an array
def recur_max(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  elif len(arr) == 2:
    return arr[0] if arr[0] > arr[1] else arr[1]
  else:
    sub_max = recur_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

input_arr_3 = [4, 2, 1, 10, 6, 9]
print("Input Array: ", input_arr_3)
print("Recursive Max: ", recur_max(input_arr_3))
print("-------------------")
