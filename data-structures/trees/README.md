# Trees

A tree is an undirected graph G(V, E) in which any two vertices are connected by exactly one path.

Equivalantly, a tree is a connected, acyclic and undirected graph.

- Height of a tree is the number of edges on 

# Binary Search Trees

- Every node in the tree can have at most 2 children (left and right)
- Left child is smaller than parent
- Right child is greater than parent
- We can excess **root node** exclusively, and other nodes can be accessed via root node

**Complete Binary Tree** - When all the left and right children of the BST is filled
- Height of complete BST is: h = &Omicron;(log N), N = number of nodes at height 'h'
  - If the tree is not balanced, h = &Omicron;(log N) does not hold
- Minimum item in a BST is the leftmost item, and the maximum item is at the rightmost.
