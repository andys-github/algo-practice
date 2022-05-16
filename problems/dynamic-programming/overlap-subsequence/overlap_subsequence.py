# n: length of string 1
# m: length of string 2
# time: O(n * m)
# space: O(n * m)

def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, s1, s2, memo):
  key = (s1, s2)

  if key in memo:
    return memo[key]

  if s1 == len(string_1) or s2 == len(string_2):
    return 0

  if string_1[s1] == string_2[s2]:
    memo[key] = 1 + _overlap_subsequence(string_1, string_2, s1 + 1, s2 + 1, memo)
    return memo[key]

  memo[key] = max(
    _overlap_subsequence(string_1, string_2, s1 + 1, s2, memo),
    _overlap_subsequence(string_1, string_2, s1, s2 + 1, memo)
  )

  return memo[key]
