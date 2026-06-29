# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, level):
            if not root:
                return ([True, level])
            left = dfs(root.left, level + 1)
            right = dfs(root.right, level + 1)

            if abs(left[1] - right[1]) > 1 :
                return ([False, level])
            elif left[0] and right[0]:
                return ([True, max(left[1], right[1])])
            return ([False, level])
        ans = dfs(root, 0)[0]
        return ans

