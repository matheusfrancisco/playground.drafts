
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def make_bst_false():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.left.left = BST(-5)
    root.left.left.left.left.left = BST(-15)
    root.left.left.left.left.right = BST(-2)
    root.left.left.left.left.left.left = BST(-22)
    root.left.left.left.left.left.left.left = BST(11)
    root.right = BST(15)
    root.right.right = BST(22)
    return root


def make_bst_true():
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


def validate_bst_helper(root, min_value, max_value):
    """Time: O(n) | Space: O(d) """
    if root is None:
        return True
    if root.value >= max_value or root.value < min_value:
        return False
    left_is_valid = validate_bst_helper(root.left, min_value, root.value)
    right_is_valid = validate_bst_helper(root.right, root.value, max_value)
    return left_is_valid and right_is_valid


def validate_bst(root):
    if root is None:
        return True
    return validate_bst_helper(root, float('-inf'), float('inf'))


def test_validate_bst():
    bst = make_bst_true()
    bst_false = make_bst_false()
    true = validate_bst(bst)
    assert true is True
    false = validate_bst(bst_false)
    assert false is False
