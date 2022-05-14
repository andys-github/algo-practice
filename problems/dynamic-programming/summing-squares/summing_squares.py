# n: input number
# time: O(n * sqrt(n))
# space: O(n)

from math import sqrt, floor

def summing_squares(n):
  return _summing_squares(n, {})


def _summing_squares(n, memo):
  if n == 0:
    return 0

  if n in memo:
    return memo[n]

  min_sum = float('inf')
  for i in range(1, floor(sqrt(n)) + 1):
    square = i * i
    _sum = 1 + _summing_squares(n - square, memo)
    min_sum = min(min_sum, _sum)

  memo[n] = min_sum
  return min_sum
