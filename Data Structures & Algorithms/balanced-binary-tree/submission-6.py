# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # resursion
        def dfs(root, level):
            if not root:
                return ([True, level])
            # call function on root.left and root.right
            left = dfs(root.left, level + 1)
            right = dfs(root.right, level + 1)

            # if the difference of height is larger than 1, 
            # return False with current level
            if abs(left[1] - right[1]) > 1 :
                return ([False, level])
            # if both passed the condition (True),
            # return True and its level
            elif left[0] and right[0]:
                return ([True, max(left[1], right[1])])
            # if only one of them/ none of them is True,
            #return False and its level
            return ([False, level])

        ans = dfs(root, 0)[0]
        return ans

