# s: length of string
# w: size of words array
# time: O(s * w)
# space: O(s)

def quickest_concat(s, words):
  quickest = _quickest_concat(s, words, {})
  return -1 if quickest == float('inf') else quickest

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]

  if s == '':
    return 0

  min_count = float('inf')
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      count = 1 + _quickest_concat(suffix, words, memo)
      min_count = min(min_count, count)

  memo[s] = min_count
  return memo[s]
