# a: amount
# c: number of coins
# time: O(a * c)
# space: O(a)


def min_change(amount, coins):
  res = _min_change(amount, coins, {})
  return -1 if res == float('inf') else res

def _min_change(amount, coins, memo):
  if amount < 0:
    return float('inf')

  if amount == 0:
    return 0

  if amount in memo:
    return memo[amount]

  min_coins = float('inf')

  for coin in coins:
    num_coins = 1 + _min_change(amount - coin, coins, memo)
    min_coins = min(min_coins, num_coins)

  memo[amount] = min_coins
  return min_coins
