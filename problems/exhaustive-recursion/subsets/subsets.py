# n: size of elements array
# time: O(2 ^ n)
# space: O(2 ^ n)

def subsets(elements):
  if len(elements) == 0:
    return [[]]

  first = elements[0]
  without_first = subsets(elements[1:])
  with_first = []
  for sub in without_first:
    with_first.append([first, *sub])

  return without_first + with_first
