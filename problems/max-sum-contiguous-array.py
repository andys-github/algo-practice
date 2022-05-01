def max_sum_contiguous_array(nums):
  max_sum = nums[0]
  current_sum = nums[0]

  for n in nums[1:]:
    current_sum = max(n, current_sum + n)
    max_sum = max(max_sum, current_sum)

  return max_sum


print(max_sum_contiguous_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sum_contiguous_array([-1]))
print(max_sum_contiguous_array([-1, -2, -3, 0]))
