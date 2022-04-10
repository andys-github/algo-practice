# -------------------------
# Q U I C K   S O R T
# -------------------------
# Worst-case: O(n^2)
# Avg-case:   O(n log n)

def quick_sort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    lh_arr = [i for i in arr if i < pivot]
    pivot_elements = [i for i in arr if i == pivot]
    rh_arr = [i for i in arr if i > pivot]
    return quick_sort(lh_arr) + pivot_elements + quick_sort(rh_arr)

print("Quick Sort Algorithm")
input_arr = [12, 3, 4, 3, 15, 4]
print("Input Array: ", input_arr)
print("Sorted Array: ", quick_sort(input_arr))
