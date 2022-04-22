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
# NOTE:
# Best case can be optimized for
# almost sorted array to O(n)
# ---------------------------------------------

def bubble_sort(arr):
  arr_size = len(arr)
  _counter = 0
  for i in range(arr_size):
    for j in range(arr_size - 1):
      _counter += 1
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr, _counter

def bubble_sort_optimized(arr):
  arr_size = len(arr)
  _counter = 0

  for i in range(arr_size):
    # to keep track of any swaps
    # that happended in the previous run
    no_swaps = True

    for j in range(arr_size - 1):
      _counter += 1
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        no_swaps = False  # Swap happened
    # print(arr)
    if no_swaps: break # If no swap happened in the previous loop, break
  return arr, _counter

input_arr = [8, 1, 2, 3, 4, 5, 6, 7]
print('Input Array: ', input_arr)
sorted_arr, counter = bubble_sort(input_arr)
print('Bubble Sorted Array: ', sorted_arr, 'Loops: ', counter)

input_arr2 = [8, 1, 2, 3, 4, 5, 6, 7]
print('Input Array: ', input_arr2)
sorted_arr2, counter2 = bubble_sort_optimized(input_arr2)
print('Optimized Bubble Sorted Array: ', sorted_arr2, 'Loops: ', counter2)
