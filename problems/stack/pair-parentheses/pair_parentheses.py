# n: lenght of string
# time: O(n)
# space: O(1)

def paired_parentheses(string):
  count = 0

  for s in string:
    if count < 0:
      return False

    if s == '(':
      count += 1
    elif s == ')':
      count -= 1

  return count == 0
