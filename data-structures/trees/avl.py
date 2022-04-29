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
        currentNode.height = max(self.calc_height(currentNode.left), self.calc_height(currentNode.right)) + 1
        if data < currentNode.data:
          if currentNode.left:
            currentNode = currentNode.left
          else:
            currentNode.left = Node(data, currentNode)
            break
        else:
          if currentNode.right:
            currentNode = currentNode.right
          else:
            currentNode.right = Node(data, currentNode)
            break
    else:
      self.root = Node(data)

    self.handle_violation(self.root)

  def remove(self, data, node):
    if data < node.data:
      self.remove(data, node.left)
    elif data > node.dat:
      self.remove(data, node.right)
    else:
      # Case 1: Node is leaf
      # Case 2: Node has one child
      # Case 3: Node has two children
      parent = node.parent
      if node.left is None:
        if node.right is None: # Case 1
          if parent is not None:
            if parent.left == node: # 'node' is left leaf
              parent.left = None
            if parent.right == node: # 'node' is right leaf
              parent.right = None
          else: # 'node' is root
            self.root = None
        else: # Case 2 ('node' has a right child)
          child = node.right
          if parent is not None:
            if parent.left == node: # 'node' is left child
              parent.left = child
              child.parent = parent
            if parent.right == node: # 'node' is right child
              parent.right = child
              child.parent = parent
          else: # 'node' is root
            self.root = child
        del node
        # after every insertion/deletion, check for any AVL violation
        self.handle_violation(self.root)
      else:
        if node.right is None: # Case 2 ('node' has a left child)
          child = node.left
          if parent is not None:
            if parent.left == node: # 'node' is left child
              parent.left = child
              child.parent = parent
            if parent.right == node: # 'node' is right child
              parent.right = child
              child.parent = parent
          else: # 'node' is root
            self.root = child
          del node
          # after every insertion/deletion, check for any AVL violation
          self.handle_violation(self.root)
        else: # Case 3
          predecessor = self.get_predecessor(node.left)
          temp = predecessor.data
          predecessor.data = node.data
          node.data = temp
          self.remove(data, predecessor)




  def handle_violation(self, node):
    pass

  def get_predecessor(self, node):
    if node.right:
      return self.getpredecessor(node.right)

    return node


  def calc_height(self, node):
    if not node:
      return -1
    else:
      return node.height

  def calc_balance_factor(self, node):
    if node is not None:
       return 0

    return self.calc_height(node.left) - self.calc_height(node.right)

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

print('In-order Traversal:')
avl.print_tree()
