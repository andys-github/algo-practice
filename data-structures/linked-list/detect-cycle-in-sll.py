from SinglyLinkedList import Node, SinglyLinkedList

def detectCycle(linkedList):
  currentNode = linkedList.head
  previousNode = currentNode

  while currentNode is not None:
    if currentNode.next == previousNode:
      currentNode.next = None
      break
    previousNode = currentNode
    currentNode = currentNode.next



# ------------------------------------------
node1 = Node('John')
node2 = Node('Kai')
node3 = Node('Cortana')

sll = SinglyLinkedList()

sll.insert(node1)
sll.insert(node2)
sll.insert(node3)

node3.next = node2

# sll.print_all()
detectCycle(sll)
print(sll)

