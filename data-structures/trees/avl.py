class Node:
  def __init__(self, data, parent = None):
    self.data = data
    self.left = None
    self.right = None
    self.parent = parent
    self.height = 0


class AvlTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root:
      currentNode = self.root

      while currentNode:
        currentNode.height = self.calc_height(currentNode)
        if data < currentNode.data:
          if currentNode.left:
            currentNode = currentNode.left
          else:
            currentNode.left = Node(data, currentNode)
            break
        else:
          if currentNode.right:
            currentNode.height += 1
            currentNode = currentNode.right
          else:
            currentNode.right = Node(data, currentNode)
            break
    else:
      self.root = Node(data)

  def remove(self):


  def get_height(self, node):
    if not node:
      return -1
    else:
      return node.height

  def calc_height(self, node):
    height = max(self.get_height(node.left), self.get_height(node.right)) + 1
    print(f'Node {node.data} has a height of {height}')
    return height

  def print_in_order(self, node):
    if node.left:
      self.print_in_order(node.left)

    print(node.data, node.height, sep=' --- ')

    if node.right:
      self.print_in_order(node.right)

  def print_tree(self):
    if self.root:
      self.print_in_order(self.root)
    else:
      print('Empty Tree')





# -------------------------------------------------------
avl = AvlTree()

#      12 (2)
#     /      \
#    4(1)     15(1)
#   /   \     /    \
#  1(0) 6(0) 13(0) 19(0)


tree_data = [12, 4, 15, 1, 6, 13, 19]

for d in tree_data:
  avl.insert(d)

# avl.print_tree()
