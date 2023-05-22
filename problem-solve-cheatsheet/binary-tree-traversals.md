## Binary Tree Traversals
A binary search tree is a binary tree where the left child is smaller and the right child is greater than its parent. 
Traverse a BST using Inorder to:

· visit the tree in sorted order
· validate whether a binary tree is a binary search tree
```python
## DFS

def preorder(root: TreeNode) -> None:
"""
"""
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root: TreeNode) -> None:
"""

Visits nodes in ascending order

            5
           / \
          3   7
         / \   \
        1   4   9 
# prints 1,3,4,5,7,9
"""
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root: TreeNode) -> None:
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

## BFS

def levelorder(root: TreeNode) -> None:
    if not root: return
    q = deque([root])
    
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            print(str(node.val), end = " ")
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)

        print()
```




