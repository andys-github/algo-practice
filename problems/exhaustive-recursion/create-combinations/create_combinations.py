# n: number of items
# k: size of each combination
# time: O(n choose k) --> Binomial co-efficient
# space: O(n choose k)

def create_combinations(items, k):
  if len(items) < k:
    return []

  if k == 0:
    return [[]]

  full_combinations = []
  first = items[0]

  partial_combos = create_combinations(items[1:], k - 1)
  for partial_combo in partial_combos:
    full_combinations.append([first, *partial_combo])

  combos_without_first = create_combinations(items[1:], k)

  return full_combinations + combos_without_first
