class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head is None

  def insert(self, node):
    if self.head == None:
      self.head = node
    else:
      lastNode = self.head

      while lastNode.next is not None:
        lastNode = lastNode.next

      lastNode.next = node

  def print(self):
    currentNode = self.head
    while currentNode is not None:
      print(currentNode.data)
      currentNode = currentNode.next

  def insert_new_head(self, newHeadNode):
    currentHeadNode = self.head
    if currentHeadNode != None and newHeadNode != None:
      newHeadNode.next = currentHeadNode
      self.head = newHeadNode
    else:
      raise NullReferenceException('Null object encountered')

  def insertAt(self, node, pos):
    if pos == 0:
      self.insert_new_head(node)
    else:
      currentNode = self.head
      currentPosition = 0

      while currentPosition != pos:
        previousNode = currentNode
        currentNode = currentNode.next
        currentPosition += 1

      node.next = currentNode
      previousNode.next = node

  def delete_last_node(self):
    currentNode = self.head

    while currentNode.next is not None:
      previousNode = currentNode
      currentNode = currentNode.next

    previousNode.next = None

  def delete_head(self):
    if self.is_empty() is False:
      currentHead = self.head
      self.head = currentHead.next
    else:
      print('Linked list is empty')

  def deleteAt(self, pos):
    if pos == 0:
      self.delete_head()
    else:
      currentNode = self.head
      position = 0
      while True:
        if position == pos:
          previousNode.next = currentNode.next
          currentNode = None
          break

        previousNode = currentNode
        currentNode = currentNode.next
        position += 1

  def __len__(self):
    length = 0
    currentNode = self.head
    while currentNode is not None:
      length += 1
      currentNode = currentNode.next

    return length


node1 = Node('John')
node2 = Node('Kai')
node3 = Node('Halsey')

sll = SinglyLinkedList()
sll.insert(node1)
sll.insert(node2)
sll.insert(node3)
sll.print()
print(f'---^^^----Insert 3 Nodes------Length: {len(sll)}')

node4 = Node('Tom')
sll.insertAt(node4, 0)
sll.print()
print(f'---^^^----Insert new Node at Head------Length: {len(sll)}')

node5 = Node('Cortana')
sll.insertAt(node5, 2)
sll.print()
print(f'---^^^----Insert new Node at index 2------Length: {len(sll)}')

sll.delete_last_node()
sll.print()
print(f'---^^^----Delete last node------Length: {len(sll)}')

sll.delete_head()
sll.print()
print(f'---^^^----Delete Head------Length: {len(sll)}')

sll.deleteAt(1)
sll.print()
print(f'---^^^----Delete node at index 1------Length: {len(sll)}')
