class Node:
  def __init__(self, data, parent = None):
    self.data = data
    self.left = None
    self.right = None
    self.parent = parent

  def __repr__(self):
    return 'None' if self is None else str(self.data)

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
            node.parent = currentNode
            currentNode.right = node
            break
          else:
            currentNode = currentNode.right

  def printTree(self):
    currentNode = self.root
    if currentNode is not None:
      print(currentNode.data)
      while currentNode:
        print(currentNode.left, currentNode.right, sep=' --- ')
        if currentNode.left is not None:
          currentNode = currentNode.left
        elif currentNode.right is not None:
          currentNode = currentNode.right
        else:
         currentNode = None
    else:
      print('Empty Binary Search Tree')


node1 = Node(12)
node2 = Node(4)
node3 = Node(15)
node4 = Node(2)

bst = BinarySearchTree()
bst.insert(node1)
bst.insert(node2)
bst.insert(node3)
bst.insert(node4)

bst.printTree()
