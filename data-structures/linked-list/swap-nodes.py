from SinglyLinkedList import Node, SinglyLinkedList

def swapNodes(linkedList, dataOne, dataTwo):
  previousOne = None
  previousTwo = None

  currentNode = linkedList.head
  while currentNode is not None:
    if dataOne == currentNode.data:
      firstNode = currentNode
      break
    previousOne = currentNode
    currentNode = currentNode.next

  currentNode = linkedList.head
  while currentNode is not None:
    if dataTwo == currentNode.data:
      secondNode = currentNode
      break
    previousTwo = currentNode
    currentNode = currentNode.next

  previousOne.next = secondNode
  nextSecond = secondNode.next
  secondNode.next = firstNode.next
  previousTwo.next = firstNode
  firstNode.next = nextSecond



# --------------------------------------
node1 = Node('John')
node2 = Node('Kai')
node3 = Node('Halsey')
node4 = Node('Cortana')
node5 = Node('Keane')

sll = SinglyLinkedList()
sll.insert(node1)
sll.insert(node2)
sll.insert(node3)
sll.insert(node4)
sll.insert(node5)

print(sll)

swapNodes(sll, 'Kai', 'Cortana')
print(sll)
