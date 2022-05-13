# a: amount
# n: length of numbers array
# time: O(a * n)
# space: O(a)

def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})


def _sum_possible(amount, numbers, memo):
  if amount < 0:
    return False

  if amount == 0:
    return True

  if amount in memo:
    return memo[amount]

  for number in numbers:
    if _sum_possible(amount - number, numbers, memo):
      memo[amount] = True
      return True

  memo[amount] = False
  return False
