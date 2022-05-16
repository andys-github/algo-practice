# n: length of numbers array
# time: O(n^2)
# space: O(n)

def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]

  if i == len(numbers):
    return False

  if i == len(numbers) - 1:
    return True

  steps = numbers[i]
  for s in range(1, steps + 1):
    if _array_stepper(numbers, i + s, memo):
      memo[i] = True
      return True

  memo[i] = False
  return False
