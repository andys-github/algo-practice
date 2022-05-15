# s: lenght of string
# time: O(s^2)
# space: O(s^2)

def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, start, end, memo):
  if start > end:
    return 0

  if start == end:
    return 1

  pos = (start, end)
  if pos in memo:
    return memo[pos]

  if string[start] == string[end]:
    memo[pos] = 2 + _max_palin_subsequence(string, start + 1, end - 1, memo)
    return memo[pos]

  memo[pos] = max(_max_palin_subsequence(string, start + 1, end, memo), _max_palin_subsequence(string, start, end - 1, memo))
  return memo[pos]
