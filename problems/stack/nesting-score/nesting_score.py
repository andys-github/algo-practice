# n: length of string
# time: O(n)
# space: O(n)

def nesting_score(string):
  stack = [0]

  for char in string:
    if char == '[':
      stack.append(0)
    else:
      ch = stack.pop()
      if ch == 0:
        stack[-1] += 1
      else:
        stack[-1] += ch * 2

  return stack.pop()
