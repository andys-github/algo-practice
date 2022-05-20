# n: size of items array
# time: O(n!)
# space: O(n!)

def permutations(items):
  if len(items) == 0:
    return [[]]

  first = items[0]
  full_permutations = []

  for p in permutations(items[1:]):
    for i in range(len(p) + 1):
      full_permutations.append(p[:i] + [first] + p[i:])

  return full_permutations
