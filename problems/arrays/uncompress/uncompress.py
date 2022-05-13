# n: number of groups
# m: max num found in any group
# time: O(n * m)
# space: O(n * m)

def uncompress(s):
  result_array = []
  i = 0
  j = 0

  while j < len(s):
    if s[j].isdigit():
      j += 1
    else:
      number = int(s[i:j])
      character = s[j]
      result_array.append(character * number)
      j += 1
      i = j

  return ''.join(result_array)

