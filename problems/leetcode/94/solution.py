from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        inorder(root, out)
        return out


def inorder(root: TreeNode, out: list) -> None:
    if not root:
        return
    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)
