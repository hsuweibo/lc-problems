# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # my first solution
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = None

        # Return the path sum of a maximal-sum path that ends at the root
        def maxRootSum(root):

            if not root:
                return 0

            # We call maxRootSum on the left and right subtree recursively
            right = maxRootSum(root.right)
            left = maxRootSum(root.left)

            # The maximal-sum path that ends at root can either be the root itself, 
            # the root + a path from left subtree, or + a path from right subtree
            max_root_sum = max(root.val, root.val + left, root.val + right)

            # The maximal-sum path that goes through root
            max_path_sum_through_root = max(max_root_sum, root.val + right + left)

            # The maximal-sum path of the entire tree must go through a root.
            # We update this as we traverse the tree
            nonlocal max_path_sum
            if max_path_sum is None:
                max_path_sum = max_path_sum_through_root
            else:
                max_path_sum = max(max_path_sum_through_root, max_path_sum)

            return max_root_sum

        maxRootSum(root)
        return max_path_sum