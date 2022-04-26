# -------------------------
# Q U I C K   S O R T
# -------------------------
# Time Complexity:
#   Best-case:  O(n log n)
#   Avg-case:   O(n log n)
#   Worst-case: O(n^2)
#
# Space Complexity: O(log n)
# -------------------------

def quick_sort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    lesser_elements = []
    pivot_elements = []
    greater_elements = []

    for i in arr:
      if i < pivot:
        lesser_elements.append(i)
      elif i > pivot:
        greater_elements.append(i)
      else:
        pivot_elements.append(i)

    return quick_sort(lesser_elements) + pivot_elements + quick_sort(greater_elements)

print("Quick Sort Algorithm")
input_arr = [12, 3, 4, 3, 15, 4]
print("Input Array: ", input_arr)
print("Sorted Array: ", quick_sort(input_arr))
