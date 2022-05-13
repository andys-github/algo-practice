# r: no. of rows
# c: no. of cols
# time: O(r * c)
# space: O(r * c)

def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})


def _max_path_sum(grid, r, c, memo):
  if not in_bounds(grid, r, c):
    return 0

  if (r, c) in memo:
    return memo[(r, c)]

  memo[(r, c)] = grid[r][c] + max(_max_path_sum(grid, r + 1, c, memo), _max_path_sum(grid, r, c + 1, memo))
  return memo[(r, c)]


def in_bounds(grid, r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])
