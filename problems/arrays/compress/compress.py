def compress(s):
  s += '!'
  result = []
  i = 0
  j = 0

  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      count = j - i
      if count == 1:
        result.append(s[i])
      else:
        result.append(f'{count}{s[i]}')
      i = j
      j += 1

  return ''.join(result)
