def maxProductContiguousArray(nums):
  current_max = nums[0]
  current_min = nums[0]
  max_prod = nums[0]

  for n in nums[1:]:
    if n == 0:
      current_max = 1
      current_min = 0

    temp = current_max * n
    current_max = max(n, current_max * n, current_min * n)
    current_min = min(n, temp, current_min * n)

    max_prod = max(n, max_prod, current_max)

  return max_prod


print(maxProductContiguousArray([-1, 0, -2]))
print(maxProductContiguousArray([-1, 0, -2, -3]))
print(maxProductContiguousArray([-1, 0]))
print(maxProductContiguousArray([-1, -2, -3, -4]))
print(maxProductContiguousArray([-1, 2, -3, 4, -5]))
