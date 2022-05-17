# n: length of string
# time: O(n)
# space: O(n)

def befitting_brackets(string):
  stack = []

  brackets = {
    '(': ')',
    '{': '}',
    '[': ']'
  }

  for c in string:
    if c in brackets:
      stack.append(brackets[c])
    else:
      if stack and stack[-1] == c:
        stack.pop()
      else:
        return False

  return len(stack) == 0

