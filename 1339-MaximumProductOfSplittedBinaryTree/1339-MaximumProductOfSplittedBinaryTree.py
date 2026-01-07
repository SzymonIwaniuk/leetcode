
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def sum_trees(node):
            if node:
                node.sum_subtree = sum_trees(node.left) + sum_trees(node.right) + node.val
                return node.sum_subtree
            return 0

        total = sum_trees(root)
        MOD = 10**9 + 7

        def split_trees(node):
            if node:
                return max(
                        split_trees(node.left),
                        split_trees(node.right),
                        (total - node.sum_subtree) * node.sum_subtree,
                        )    
            return 0

        return split_trees(root) % MOD


