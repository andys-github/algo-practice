# Trees

A tree is an undirected graph G(V, E) in which any two vertices are connected by exactly one path.

Equivalantly, a tree is a connected, acyclic and undirected graph.

- Height of a tree is the number of edges on 

## Binary Search Trees

- Every node in the tree can have at most 2 children (left and right)
- Left child is smaller than parent
- Right child is greater than parent
- We can excess **root node** exclusively, and other nodes can be accessed via root node

**Complete Binary Tree**
- A BST where all the left and right children of the BST is filled
- Height of complete BST is: h = &Omicron;(log N), N = number of nodes at height 'h'
  - If the tree is not balanced, h = &Omicron;(log N) does not hold
- Minimum item in a BST is the leftmost item, and the maximum item is at the rightmost.

**Deleting a node in BST**
- Deleting a node with one child - just change the parent-child relation with the updated values
- Deleteing a node with two children (e.g, root)
  - Replace it with **successor** node (The smallest node on the right of the node)
  - Replace it with **predecessor** node (The largest node on the left)

**Tree Traversal**
- Pre-order: **root** --> left sub-tree --> right sub-tree
- Post-order: left subtree --> right sub-tree --> **root**
- In-order: left sub-tree --> **root** --> right sub-tree
  - **This results in a sorted order**

#### Big-O Complexities of BST
<table>
  <thead>
    <tr>
      <th rowspan="2">Case</th>
      <th colspan="3">Time Complexity</th>
      <th rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Insertion</th>
      <th>Deletion</th>
      <th>Search</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Average Case</td>
      <td>&Omicron;(log N)</td>
      <td>&Omicron;(log N)</td>
      <td>&Omicron;(log N)</td>
      <td>&Omicron;(N)</td>
    </tr>
    <tr>
      <td>Worst Case</td>
      <td>&Omicron;(N)</td>
      <td>&Omicron;(N)</td>
      <td>&Omicron;(N)</td>
      <td>&Omicron;(N)</td>
    </tr>
  </tbody>
</table>

<br />

> **Cons:** BST can become imbalanced, which is when we would need balanced trees like AVL, Red-black trees, etc

## AVL Trees
- named after Adelson - Velsky - Landis
- This data structure has a guaranteed O(log N) running time complexity
- The running time of BST depends on the height (h) of the tree
- In AVL trees, the heights of two sub-trees of any node can differ by at most one
- AVL trees are faster than Red-Black tree because they are more rigidly balanced and hence need more work	
- Windows OS heavily relies on AVL, whereas Linux leans on Red-Black
- AVL trees are exactly same as BST except that we track height (h) of each nodes in the tree:
> all subtree height parameters can not exceed by 1 (otherwise the tree is considered imbalanced)
> | h<sub>left</sub> - h<sub>right</sub> | <= 1
> This difference (h<sub>left</sub> - h<sub>right</sub>) in heights is called as **balance factor**
> If the balance factor is positive, then it is a left-heavy case, otherwise right-heavy case

