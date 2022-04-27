class Node:
  def __init__(self, data, parent = None):
    self.data = data
    self.left = None
    self.right = None
    self.parent = parent

  def __str__(self):
    return None if self is None else str(self.data)

  def __repr__(self):
    return None if self is None else str(self.data)

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, node):
    if self.root is None:
      self.root = node
    else:
      currentNode = self.root
      while currentNode is not None:
        if node.data <= currentNode.data:
          if currentNode.left is None:
            node.parent = currentNode
            currentNode.left = node
            break
          else:
            currentNode = currentNode.left
        else:
          if currentNode.right is None:
            # print(node)
            node.parent = currentNode
            currentNode.right = node
            break
          else:
            currentNode = currentNode.right

  def print_tree(self):
    currentNode = self.root
    if currentNode is not None:
      print(currentNode.data)
      while currentNode:
        print(currentNode)
        # print(currentNode.left, currentNode.right, sep=' --- ')
        if currentNode.left is not None:
          currentNode = currentNode.left
        elif currentNode.right is not None:
          currentNode = currentNode.right
        else:
         currentNode = None
    else:
      print('Empty Binary Search Tree')

  def get_min(self):
    if self.root is None:
      return None
    return self.get_min_value(self.root)

  def get_min_value(self, node):
    if node.left:
      return self.get_min_value(node.left)
    return node.data

  def get_max(self):
    if self.root is None:
      return None
    return self.get_max_value(self.root)

  def get_max_value(self, node):
    if node.right:
      return self.get_max_value(node.right)
    return node.data

  def traverse(self, order='in'):
    if self.root:
      if order == 'pre':
        return self.traverse_pre_order(self.root)
      elif order == 'post':
        return self.traverse_post_order(self.root)
      else:
        return self.traverse_in_order(self.root)

  def traverse_in_order(self, node):
    if node.left:
      self.traverse_in_order(node.left)

    print(node)

    if node.right:
      self.traverse_in_order(node.right)

  def traverse_pre_order(self, node):
    print(node)

    if node.left:
       self.traverse_pre_order(node.left)

    if node.right:
       self.traverse_pre_order(node.right)

  def traverse_post_order(self, node):
    if node.left:
       self.traverse_post_order(node.left)

    if node.right:
       self.traverse_post_order(node.right)

    print(node)





# ------------------------------

if __name__ == '__main__':
  bst = BinarySearchTree()
  tree_data = [12, 4, 15, 2, 26, 7, 13]

  for d in tree_data:
    node = Node(d)
    bst.insert(node)

  #        12
  #
  #    4        15
  #
  #  2    7   13   26

  print('In-order Traversal')
  bst.traverse()

  print('Pre-order Traversal')
  bst.traverse(order='pre')

  print('Post-order Traversal')
  bst.traverse(order='post')
