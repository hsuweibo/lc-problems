import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        # If the node has a right child, the successor is the left-most leaf of the right child
        if p.right:
            curr = p.right
            while (curr.left is not None):
                curr = curr.left
            return curr

        # If the node has no right child, the sucessor is the parent of last node that is a left child in the bst search path
        curr = root
        parent_of_last_left_child = None

        while (curr is not None and curr.val != p.val):
            if p.val > curr.val:
                curr = curr.right
            else:
                parent_of_last_left_child = curr
                curr = curr.left

        if curr is None:
            print("not found")
            return

        return parent_of_last_left_child

class TestInorder(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_input1(self):
        root = TreeNode(6)
        n2 = TreeNode(2)
        n8 = TreeNode(8)
        n0 = TreeNode(0)
        n4 = TreeNode(4)
        n7 = TreeNode(7)
        n9 = TreeNode(9)
        n3 = TreeNode(3)
        n5 = TreeNode(5)
        root.left = n2
        root.right = n8
        n2.left = n0
        n2.right = n4
        n8.left = n7
        n8.right = n9
        n4.left = n3
        n4.right = n5
        self.assertEqual(self.solution.inorderSuccessor(root, n2), n3)

if __name__ == '__main__':
    unittest.main()