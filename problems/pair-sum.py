def pair_sum(numbers, target_sum):
  tracker = {}
  result = []

  for i, num in enumerate(numbers):
    if tracker.get(target_sum - num) is None:
      tracker[num] = i
    else:
      result.append((tracker[target_sum - num], i))

  return result


print(pair_sum([2, 2, 1, 3], 4))
print(pair_sum([1, 2, 3, 4], 3))
print(pair_sum([1, 1, 1], 5))
