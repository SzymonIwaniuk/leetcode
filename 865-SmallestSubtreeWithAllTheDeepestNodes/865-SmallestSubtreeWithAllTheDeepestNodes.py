
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxdepth = 1
        stack = [(1, root)]

        while stack:
            i, node = stack.pop()
            if node:
                maxdepth = max(maxdepth, i)
                stack.append((i + 1, node.left))
                stack.append((i + 1, node.right))
        
        stack = [(1, root, None)]
        nodes = set()
        parents = {}

        while stack:
            i, node, prev = stack.pop()

            if node:
                if i == maxdepth:
                    nodes.add(node)
                parents[node] = prev
                stack.append((i + 1, node.left, node))
                stack.append((i + 1, node.right, node))

        while len(nodes) != 1:
            nodes = set(parents[node] for node in nodes)

        result, = nodes
        return result

