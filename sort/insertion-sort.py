# ---------------------------------------------
# I N S E R T I O N   S O R T
# ---------------------------------------------
# Time Complexity:
#   Best case:   O(n)
#   Avg Case:    O(n^2)
#   Worst Case:  O(n^2)
#
# Space Complexity: O(1)
# ---------------------------------------------

def insertion_sort(input_arr):
  for i in range(len(input_arr)):
    current_item = input_arr[i]
    j = i - 1

    while current_item < input_arr[j] and j >= 0:
      input_arr[j+1] = input_arr[j]
      j -= 1

    input_arr[j+1] = current_item

  return input_arr


input_array = [4, 5, 1, 2, 3, 20]
print(input_array)
print(insertion_sort(input_array))
