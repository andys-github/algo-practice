def find_smallest(arr):
  smallest = arr[0]
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i

  return smallest, smallest_index


# print(find_smallest([1, 3, 4, 1, 0]))

def selection_sort(arr):
  output_arr = []
  counter = len(arr)

  for i in range(counter):
    _, sm_index = find_smallest(arr)
    output_arr.append(arr.pop(sm_index))

  return output_arr

input_arr = [2, 4, 1, 0, 13]
print("Input Array: ", input_arr)
print("Selection Sorted Array: ", selection_sort(input_arr))
