# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        max_depth = 0
        while stack:
            node = stack.pop()
            elem, depth = node[0], node[1]
            if elem.left:
                stack.append([elem.left, depth + 1])
            if elem.right:
                stack.append([elem.right, depth + 1])
            max_depth = max(max_depth, depth)
        return max_depth

   