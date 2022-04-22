# ---------------------------------------------
# B U B B L E   S O R T
# ---------------------------------------------
# Time Complexity:
#   Best Case:   O(n^2)
#   Avg Case:    O(n^2)
#   Worst Case:  O(n^2)
#
# Space Complexity: O(1)
# ---------------------------------------------

def bubble_sort(arr):
  arr_size = len(arr)
  for i in range(arr_size):
    for j in range(arr_size - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

input_arr = [6, 4, 15, 10, 13]
print('Input Array: ', input_arr)
print('Sorted Array: ', bubble_sort(input_arr))
