def max_value(nums):
  max_num = float('-inf') # nums[0]

  # for i in range(1, len(nums)):
  #   if nums[i] > max_num:
  #     max_num = nums[i]

  for num in nums:
    if num > max_num:
      max_num = num

  return max_num

