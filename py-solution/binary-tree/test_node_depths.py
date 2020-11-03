"""
The distance between a node in a BTree and the tree's root is
called the node's depth

Write a function that takes in a Binary tree and returns the sum of its
nodes' depths.

"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def make_btree():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    return root


def test_node_depths():
    root = make_btree()
    assert node_depths(root) == 16


def test_iterative_node_depths():
    root = make_btree()
    assert node_depths_iterative(root) == 16


def node_depths(root):
    """
    Time: O(n)
    Space: O(h)

    """
    depth = 0
    return sum_depth(root, depth)


def sum_depth(root, depth):
    if root is None:
        return 0
    return depth + sum_depth(root.left, depth + 1) + sum_depth(root.right, depth + 1) # noqa


def node_depths_iterative(root):
    """
    Time: O(n)
    Space: O(h)

    """
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sum_of_depths

