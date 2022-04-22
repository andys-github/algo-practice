# ------------------------------------
# MERGE SORT
# ------------------------------------
# Time Complexity:
# For all cases: O(n log n)
#
# Space Complexity: O(n)
# ------------------------------------

def merge_array(arr1, arr2):
  result = []

  arr1_ptr = 0
  arr2_ptr = 0

  while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
    if arr1[arr1_ptr] <= arr2[arr2_ptr]:
      result.append(arr1[arr1_ptr])
      arr1_ptr += 1
    else:
      result.append(arr2[arr2_ptr])
      arr2_ptr += 1

  while arr1_ptr < len(arr1):
    result.append(arr1[arr1_ptr])
    arr1_ptr += 1

  while arr2_ptr < len(arr2):
    result.append(arr2[arr2_ptr])
    arr2_ptr += 1

  return result



def merge_sort(input_arr):
  if len(input_arr) <= 1:
    return input_arr
  mid = len(input_arr) // 2
  left = merge_sort(input_arr[:mid])
  right = merge_sort(input_arr[mid:])

  return merge_array(left, right)

input_array = [5, 10, 23, 0, 1, 8, 3, 100, 99, 98, 97]

print(input_array)
print(merge_sort(input_array))
