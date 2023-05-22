"""Problem Statement
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum
of all the node values of each path equals ‘S’.

Complexity Time O(N)
Space O(N)
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path_recursive(curr, sum, current_path, all_paths):
    if curr is None:
        return

    current_path.append(curr.val)
    if curr.val == sum and curr.left is None and curr.right is None:
        all_paths.append(list(current_path))
    else:
        find_path_recursive(curr.left, sum - curr.val, current_path, all_paths)
        find_path_recursive(curr.right, sum - curr.val, current_path, all_paths)

    del current_path[-1]

def find_paths(root, sum):
    all_paths = []
    find_path_recursive(root, sum, [], all_paths)
    return all_paths


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
