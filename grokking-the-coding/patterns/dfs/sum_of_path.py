"""

Given a binary tree where each node can only have a digit (0-9) value,
each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path_recursive(curr, path_sum):
    if curr is None:
        return 0

    path_sum = 10 * path_sum + curr.val

    if curr.left is None and curr.right is None:
        return path_sum

    left = find_path_recursive(curr.left, path_sum)
    right = find_path_recursive(curr.right, path_sum)
    return left + right


def find_sum_of_path_numbers(root):
    return find_path_recursive(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
