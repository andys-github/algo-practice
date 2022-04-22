# ---------------------------
# SELECTION SORT
# ---------------------------
#
# Best Case:   O(n^2)
# Avg Case:    O(n^2)
# Worst Case:  O(n^2)
#
# Space Complexity: O(1)
# ---------------------------

def selection_sort(arr):
  for i in range(0, len(arr)):
    smallest_index = i
    smallest = arr[i]

    for j in range(i + 1, len(arr)):
      if arr[j] < smallest:
        smallest = arr[j]
        smallest_index = j

    if smallest != arr[i]:
       arr[smallest_index] = arr[i]
       arr[i] = smallest

  return arr

input_arr = [2, 4, 1, 0, 13, 5]
print("Input Array: ", input_arr)
print("Selection Sorted Array: ", selection_sort(input_arr))
