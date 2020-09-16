def branchs(tree, current_sum, sums):
    if tree is None:
        return sums
    current_sum = current_sum + tree.value
    if tree.left is None and tree.right is None:
        sums.append(current_sum)
        return

    branchs(tree.left, current_sum, sums)
    branchs(tree.right, current_sum, sums)


def branch_sums(tree):
    sums = []
    branchs(tree, 0, sums)
    return sums


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def test_case_1():
    # tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    tree = BinaryTreeNode(1)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(4)
    tree.left.left.left = BinaryTreeNode(8)
    tree.left.left.right = BinaryTreeNode(9)
    tree.left.right = BinaryTreeNode(5)
    tree.left.right.left = BinaryTreeNode(10)
    tree.right = BinaryTreeNode(3)
    tree.right.left = BinaryTreeNode(6)
    tree.right.right = BinaryTreeNode(7)
    assert branch_sums(tree) == [15, 16, 18, 10, 11]
