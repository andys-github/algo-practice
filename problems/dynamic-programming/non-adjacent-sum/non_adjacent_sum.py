# n: lenght of nums array
# time: O(n)
# space: O(n)

def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, {})

def _non_adjacent_sum(nums, memo):
  if len(nums) == 0:
    return 0

  nums_tuple = tuple(nums)
  if nums_tuple in memo:
    return memo[nums_tuple]

  with_first = nums[0] + _non_adjacent_sum(nums[2:], memo)
  without_first = _non_adjacent_sum(nums[1:], memo)

  memo[nums_tuple] = max(with_first, without_first)
  return memo[nums_tuple]
