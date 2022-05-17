# n: length of string
# m: number of groups
# time: O(9^m * n)
# space: O(9^m * n)

from collections import deque

def decompress_braces(string):
  stack = []

  for char in string:
    if char == '{':
      continue
    elif char == '}':
      res = decompress(stack)
      stack.append(res)
    elif char.isdigit():
      stack.append(int(char))
    else:
      stack.append(char)

  return ''.join(stack)

def decompress(stack):
  queue = deque([])

  while stack and not isinstance(stack[-1], int):
    queue.appendleft(stack.pop())

  times = stack.pop()

  return ''.join(queue) * times
