# r = rows
# c = cols
# time: O(r * c)
# space: O(r * c)

def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
  if not is_in_bounds(grid, r, c) or grid[r][c] == 'X':
    return 0

  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1

  if (r, c) in memo:
    return memo[(r, c)]

  memo[(r, c)] = _count_paths(grid, r + 1, c, memo) + _count_paths(grid, r, c + 1, memo)
  return memo[(r, c)]


def is_in_bounds(grid, r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])
