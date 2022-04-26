class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def __str__(self):
    currentNode = self.head
    if currentNode is None:
      return 'Empty linked list'

    nodeData = []
    while currentNode is not None:
      nodeData.append(currentNode.data)
      currentNode = currentNode.next

    return ' --> '.join(map(str, nodeData))

  def __len__(self):
    length = 0
    currentNode = self.head
    while currentNode is not None:
      length += 1
      currentNode = currentNode.next
    return length

  def isEmpty(self):
    return len(self) == 0

  def insert(self, node):
    if self.head is None:
      self.head = node
    else:
      currentNode = self.head
      while currentNode.next is not None:
        currentNode = currentNode.next
      currentNode.next = node

  def insertAt(self, node, pos):
    if not (0 <= pos < len(self)):
      print(f'Error: Invalid position {pos} for insert operation!')

    if pos == 0:
      currentHead = self.head
      self.head = node
      node.next = currentHead
      return

    position = 0
    currentNode = self.head

    while currentNode is not None:
      if position == pos:
        previousNode.next = node
        node.next = currentNode
        break

      previousNode = currentNode
      currentNode = currentNode.next
      position += 1

  def deleteAt(self, pos):
    if self.isEmpty():
      print('Error: Can not delete element of an empty linked list')
      return

    if not (0 <= pos < len(self)):
      print(f'Error: Invalid position {pos} for delete operation!')
      return

    if pos == 0:
      currentHead = self.head
      self.head = currentHead.next
      return

    position = 0
    currentNode = self.head

    while currentNode is not None:
      if position == pos:
        previousNode.next = currentNode.next
        currentNode = None
        break
      previousNode = currentNode
      currentNode = currentNode.next
      position += 1

  def print_all(self):
    currentNode = self.head
    while currentNode is not None:
      print(currentNode.data)
      currentNode = currentNode.next




# ------------------------------------------
if __name__ == '__main__':
  node1 = Node('John')
  node2 = Node('Kai')
  node3 = Node('Cortana')

  sll = SinglyLinkedList()
  sll.insert(node1)
  sll.insert(node2)
  sll.insert(node3)

  print(sll)
  print('Length:', len(sll))

  sll.deleteAt(1)
  print(sll)
  print('Length:', len(sll))

  sll.insertAt(node2, 1)
  print(sll)
  print('Length:', len(sll))

