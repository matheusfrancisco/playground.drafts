
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result

    q = deque()
    q.append(root)

    while q:
        leve_size = len(q)
        current_level_avg = 0
        for _ in range(leve_size):
            current_node = q.popleft()
            current_level_avg += current_node.val
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

        result.append(current_level_avg/leve_size)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
