# -------------------------------------------------------------
# Problem Statement:
# -------------------------------------------------------------
# Reverse an array T[] in O(n) linear time complexity.
# The algorithm should be in-place as well, so no additional
# space, in other words, O(1) space complexity
#
# For example:
# Input: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]
# -------------------------------------------------------------

def reverse_array(arr):
  start_index = 0
  end_index = len(arr) - 1
  loop_count = 0

  while start_index < end_index:
    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    start_index += 1
    end_index -= 1
    loop_count += 1

  print("Loop Count: ", loop_count)

  return arr

input_array = [1, 2, 3, 4, 5]
print("\nInput array: ", input_array)
print("Reversed array: ", reverse_array(input_array))

input_array2 = [11, 12, 13, 14, 15, 16]
print("\nInput array: ", input_array2)
print("Reversed array: ", reverse_array(input_array2))

input_array3 = [-1, 0, 1]
print("\nInput array: ", input_array3)
print("Reversed array: ", reverse_array(input_array3))
