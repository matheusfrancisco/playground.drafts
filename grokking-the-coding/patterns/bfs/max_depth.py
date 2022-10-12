"""
Problem 1: Given a binary tree, find its maximum depth (or height).

Solution: We will follow a similar approach. Instead of returning as soon as we
find a leaf node, we will keep traversing for all the levels, incrementing
maximumDepth each time we complete a level. Here is what the code will look like:
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_max_depth(root):
    """
        The time complexity of the above algorithm is O(N)
        , where ‘N’ is the total number of nodes in the tree.
        This is due to the fact that we traverse each node once.
    """
    if root is None:
        return 0

    q = deque()
    q.append(root)
    _max = 0
    while q:
        _max += 1
        level_size = len(q)
        for _ in range(level_size):
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return _max


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Max Depth: " + str(find_max_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Max Depth: " + str(find_max_depth(root)))


main()
