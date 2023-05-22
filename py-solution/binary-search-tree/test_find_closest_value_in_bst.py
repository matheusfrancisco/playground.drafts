

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def make_bst():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    return root


def find_closest_value_in_bst(bst, value):
    return find(bst, value, bst.value)


def find(root, target, closest):
    if root is None:
        return closest
    if abs(target - closest) > abs(target - root.value):
        closest = root.value
    if target < root.value:
        return find(root.left, target, closest)
    elif target > root.value:
        return find(root.right, target, closest)
    else:
        return closest


def test_find_closest():
    expected = 13
    assert expected == find_closest_value_in_bst(make_bst(), 12)
